from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.title("Youtube video downloader")

label_1=Label(root, text="Youtube video downloader", font="arial 20 bold").pack()
link=StringVar()
label_2=Label(root,text="Paste link here:",font="arial 15 bold").place(x=160, y=50)
Entry(root,width=70,textvariable=link).place(x=30,y=90)

def downloader():
    url=YouTube(str(link.get()))
    video=url.streams.first()
    video.download('Enter Download path') #Please provide the download path
    label_3=Label(root,text="Downloaded",font='arial 15').place(x=180,y=210)

btn=Button(root,text="Download",font='arial 15 bold',bg='pale violet red',padx=2,command=downloader).place(x=180,y=150)
root.mainloop()