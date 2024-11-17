import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

from backend import download_music, download_video

user_url = ""
save_music_or_video= ""

first_screen = tk.Tk()
first_screen.title("Download Video and Music")
first_screen.geometry("450x200")
first_screen.configure(bg="#000000")

def def_load_screen_downlad():
    download_screen = tk.Toplevel(first_screen)
    download_screen.title("Download")
    download_screen.geometry("300x100")
    download_screen.transient(first_screen)
    
    label_title = tk.Label(first_screen, text= "Downloading...", font=("Arial", 16, "bold"), bg="#000000", fg="#FFFFFF")
    label_title.place(x=125, y=20)

def def_select_directory():
    global save_music_or_video
    try:
        save_music_or_video = filedialog.askdirectory(title="Selecione uma pasta para salvar o arquivo")

        if save_music_or_video == "" or save_music_or_video == None:
            messagebox.showinfo("Attention", "add a folder")
            return False
        else:
            print("Caminho:" + save_music_or_video)

    except Exception as ex:
        messagebox.showerror("Error", f"Type error: {ex}")
        return False

def def_start_download_music():
    global user_url, save_music_or_video

    if user_url == None or user_url == "":
        messagebox.showinfo("Attention", "Insert a URL")
        return False
    elif save_music_or_video == None or save_music_or_video == "":
        messagebox.showinfo("Attention", "Insert a folder")
        return False
    
    user_url = user_url.get("1.0", "end-1c")
    if download_music(user_url, save_music_or_video) == False:
        messagebox.showinfo("Attention", "Folder or URL invalid")
        return False
    
    messagebox.showinfo("Information", "download completed")

def def_start_download_video():
    global user_url, save_music_or_video

    if user_url == None or user_url == "":
        messagebox.showinfo("Attention", "Insert a URL")
        return False
    elif save_music_or_video == None or save_music_or_video == "":
        messagebox.showinfo("Attention", "Insert a folder")
        return False

    user_url = user_url.get("1.0", "end-1c")

    if download_video(user_url, save_music_or_video) == False:
       messagebox.showinfo("Attention", "Folder or URL invalid")

    messagebox.showinfo("Information", "download completed")

label_title = tk.Label(first_screen, text= "Download Video & Music", font=("Arial", 16, "bold"), bg="#000000", fg="#FFFFFF")
label_title.place(x=100, y=20)

label_url = tk.Label(first_screen, text= "URL:", font=("Arial", 12, "bold"), bg="#000000", fg="#FFFFFF")
label_url.place(x=10, y=76)

label_directory = tk.Label(first_screen, text= "Directory:", font=("Arial", 12, "bold"), bg="#000000", fg="#FFFFFF")
label_directory.place(x=10, y=120)

label_audio = tk.Label(first_screen, text= "Music", font=("Arial", 12, "bold"), bg="#000000", fg="#FFFFFF")
label_audio.place(x=320, y=120)

label_video = tk.Label(first_screen, text= "Video", font=("Arial", 12, "bold"), bg="#000000", fg="#FFFFFF")
label_video.place(x=320, y=155)

label_author = tk.Label(first_screen, text= "Creator: Gustavo Alfredo", font=("Arial", 8, "bold"), bg="#000000", fg="#FFFFFF")
label_author.place(x=10, y=175)

#URL MUSIC
user_url = tk.Text(first_screen, width=41, height=1.45)
user_url.place(x=100, y=80)
user_url.pack

img_download = Image.open("icons/download.png") 
img_download = img_download.resize((20, 20)) 
img_download_tk = ImageTk.PhotoImage(img_download)

img_search = Image.open("icons/search.png") 
img_search = img_search.resize((20, 20)) 
img_search_tk = ImageTk.PhotoImage(img_search)

btn_buscar_arquivo = tk.Button(first_screen,
                                text="D", 
                                command=def_select_directory, 
                                bg="#ffffff", 
                                fg="#000000",
                                width=30,
                                image=img_search_tk,
                                cursor="hand2"
                               )

btn_buscar_arquivo.place(x=100, y=120)  

btn_download_music = tk.Button(first_screen,
                                text="D", 
                                command=def_start_download_music, 
                                bg="#20d464", 
                                fg="#000000",
                                width=40,
                                image=img_download_tk,
                                cursor="hand2"
                                )

btn_download_music.place(x=387, y=120)

btn_download_video = tk.Button(first_screen,
                               text="D", 
                               command=def_start_download_video, 
                               bg="#20d464", 
                               fg="#000000",
                               width=40,
                               image=img_download_tk,
                               cursor="hand2"
                              )

btn_download_video.place(x=387, y=155) 

first_screen.mainloop()