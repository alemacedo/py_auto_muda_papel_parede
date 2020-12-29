from tkinter import *
from tkinter import filedialog
from os import walk
import ctypes
import random

directory = "G:/Imagens/Wallpaper"
files = []
number_files = 0

def on_get_directory():
    
    global directory, files, number_files
           
    files.clear()
    number_files = 0
    
    new_directory = filedialog.askdirectory()
    
    if ( new_directory
         and directory != new_directory ):
    
        directory = new_directory
    
        set_text_entry(en_directory, directory)
    
        count_files(directory)
    
def count_files(path):
    
    global files, number_files
    
    for (dirpath, dirnames, filenames) in walk(path):        
        for file in filenames:
            files.append({"path": dirpath,
                          "file": file})
        
        number_files = number_files + len(filenames)
                                
    set_text_entry(en_files, number_files)
    
    if number_files > 0:
        bt_start["state"] = NORMAL
    else:
        bt_start["state"] = DISABLED
    
def get_random_path():
    
    global files
    
    path = random.choice(files)
    
    return f'{path["path"]}/{path["file"]}'
    
def on_start():
    
    path = get_random_path()
    
    print(path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
    

def set_text_entry(entry, text):
    entry["state"] = NORMAL
    entry.delete(0, END)
    entry.insert(0, text)
    entry["state"] = "readonly"
    
    
window = Tk()

window.title("Auto Muda Papel de Parede (beta)")
window.geometry("350x350")
window.resizable(False, False)

container = Frame(window)
container.pack(fill=BOTH, expand=True)

frame_1 = Frame(container, pady=10)
frame_1.pack()
lb_directory = Label(frame_1, text="Diretório raiz:")
lb_directory.pack()
en_directory = Entry(frame_1, width=50, state="readonly")
en_directory.pack()
bt_directory = Button(frame_1, text="Procurar...", width=15, command =on_get_directory )
bt_directory.pack(pady=4)

frame_2 = Frame(container, pady=10)
frame_2.pack()
lb_qtt = Label(frame_2, text="Arquivos:")
lb_qtt.pack()
en_files = Entry(frame_2, state="readonly")
en_files.pack()
bt_start = Button(frame_2, text="Mudar", state=DISABLED, width=15, command=on_start)
bt_start.pack(pady=4)

frame_3 = Frame(container, pady=15)
frame_3.pack()
lb_wallpaper = Label(frame_3, text="Atual:")
lb_wallpaper.pack()
frame_pic = Frame(frame_3,
                  bg="black",
                  height=240,
                  width=200)
frame_pic.pack(fill=BOTH, expand=True)

set_text_entry(en_directory, directory)
count_files(directory)
                
# start the program
window.mainloop()

# ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)