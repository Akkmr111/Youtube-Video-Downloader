from tkinter import*
from tkinter import filedialog
from pytube import YouTube

def Videolist(videoURL):
    videoURL =str(videoURL)
    video = YouTube(videoURL)
    fileList = video.title
    streamList = video.streams
    for stream in streamList:
        item = "\n"
        item += str(streamList.index(stream)+1)+') '
        item += str(stream)
        fileList += item
    return fileList

def downloader(videoURL, itemNum, location):
    videoURL = str(videoURL)
    video = YouTube(videoURL)
    item = video.streams[int(itemNum)-1]
    item.download(str(location))

def directoryLocation():
    filename = filedialog.askdirectory()
    return filename

def insertPath(entry):
    entry.delete(0, END)
    entry.insert(0, directoryLocation())

def insertList(searchEntry, textEntry):
    url = searchEntry.get()
    videolist = Videolist(url)
    textEntry.delete('1.0',END)
    textEntry.insert('1.0',videolist)
root = Tk()
root.title("YouTube Downloader")
root.geometry("640x750")
logo = PhotoImage(file="YouTube.png")
Label(root, image=logo).grid(row=0,column=0,columnspan=3)
VideoLink = Label(root,text="Video Link: ",font=20)
VideoLink.grid(row=1,column=0, pady=30, padx=20)
LinkEntry = Entry(root,borderwidth=0,width=50)
LinkEntry.grid(row=1,column=1, pady=30, padx=20)
SearchButton = Button(root,text="Search", width=10,command=lambda :insertList(LinkEntry,videotext))
SearchButton.grid(row=1, column=2, pady=30, padx=20)
videoLabel = Label(root,text="Available Audio/Video: ", font=20)
videoLabel.grid(row=2, column=0,columnspan=3)
videotext = Text(root,height=20, width=80)
videotext.grid(row=3,column=0,columnspan=3)
selectlabel = Label(root,text="Select File: ", font=20)
selectlabel.grid(row=4,column=0, pady=30, padx=20)
selectEntry = Entry(root, borderwidth=0, width=3)
selectEntry.grid(row=4, column=1, pady=30, padx=20)
locationLabel = Label(root, text="Location: ",font=20)
locationLabel.grid(row=5,column=0, pady=30, padx=20)
locationEntry = Entry(root,borderwidth=0,width=50)
locationEntry.grid(row=5, column=1, pady=30, padx=20)
locationButton = Button(root, text="Choose", width=10, command=lambda:insertPath(locationEntry))
locationButton.grid(row=5, column=2, pady=30, padx=20)
DownloadButton = Button(root, text="Download", width=20, bg="green", fg="white",command=lambda:downloader(LinkEntry.get(),selectEntry.get(),locationEntry.get()))
DownloadButton.grid(row=6, column=0,columnspan=3)

root.mainloop()