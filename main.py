#!/usr/bin/env python3
## revox's youtube downloader (v0.2)
## https://github.com/revoxhere/youtube-downloader
from __future__ import unicode_literals
from tkinter import *
import youtube_dl, time
preset = ""

def webm():
    global ydl_opts, preset
    preset = "WEBM Video (max quality)"
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'true',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm',
        }],
    }
    download()

def mkv():
    global ydl_opts, preset
    preset = "MKV Video (max quality)"
    ydl_opts = {
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
    }
    download()

def mp4():
    global ydl_opts, preset
    preset = "MP4 Video (max quality)"
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'true',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    download()

def wav():
    global ydl_opts, preset
    preset = "WAV (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }
    download()

def aac():
    global ydl_opts, preset
    preset = "AAC (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
        }],
    }
    download()

def flac():
    global ydl_opts, preset
    preset = "FLAC (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
        }],
    }
    download()

def mp3low():
    global ydl_opts, preset
    preset = "MP3 Low (64kbps)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '64',
        }],
    }
    download()

def mp3medium():
    global ydl_opts, preset
    preset = "MP3 Medium (192kbps)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    download()

def mp3high():
    global ydl_opts, preset
    preset = "MP3 High (328kbps)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '328',
        }],
    }
    download()


def download():
    url = urlbutton.get()
    print(url)
    if url:
        try:
            label = Label(roots, text = "                                                                                                                                    ", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
            roots.update_idletasks()
            label = Label(roots, text = "Downloading using "+preset+" preset.", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
            roots.update_idletasks()

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([str(url)])
                    
            label = Label(roots, text = "                                                                                                             ", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
            roots.update_idletasks()
            label = Label(roots, text = "Done!", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
            roots.update_idletasks()
        except:
            label = Label(roots, text = "                                                                                                           ", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
            roots.update_idletasks()
            label = Label(roots, text = "Error! Check the URL!", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
            roots.update_idletasks()
    else:
        label = Label(roots, text = "                                                                                                                        ", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
        roots.update_idletasks()
        label = Label(roots, text = "Error! URL box is empty!", bg="white", font=("Arial", 9)).place(relx = 0.5, rely = 0.8, anchor = CENTER)
        roots.update_idletasks()
    urlbutton.delete(0, END)
    roots.update_idletasks()


def paste():
    urlbutton.delete(0, END)
    global ClipBoard
    AnnoyingWindow = Tk()
    try:
        ClipBoard = AnnoyingWindow.clipboard_get()
    except:
        pass
    AnnoyingWindow.destroy()
    try:
        urlbutton.insert(0, ClipBoard)
    except:
        pass
    
def roots():
        global urlbutton, roots, paste, mp3low, mp3medium, mp3high, flac, aac, wav, mp4, mkv, webm

        roots = Tk() #register window
        roots.title('revox\'s youtube downloader')
        roots.configure(background='white')
        roots.geometry("500x200")

        label = Label(roots, text="URL:", bg="white", fg="#7f8fa6", font = 'Arial',).place(relx = 0.1, rely = 0.1, anchor = CENTER)

        urlbutton = Entry(roots, width = 47)
        urlbutton.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        grab = Button(roots, text='Paste!', command=paste, bg="white", font = 'Arial', fg="#44bd32", height = 1, width = 3).place(relx = 0.91, rely = 0.1, anchor = CENTER)

        mp3low = Button(roots, text='MP3 Low', command=mp3low, bg="#c0392b", font = 'Arial', fg="white", width=15).place(relx = 0.2, rely = 0.3, anchor = CENTER)
        mp3medium = Button(roots, text='MP3 Medium', command=mp3medium, bg="#f39c12", font = 'Arial', fg="white", width=15).place(relx = 0.5, rely = 0.3, anchor = CENTER)
        mp3high = Button(roots, text='MP3 High', command=mp3high, bg="#6ab04c", font = 'Arial', fg="white", width=15).place(relx = 0.8, rely = 0.3, anchor = CENTER)

        flac = Button(roots, text='Flac Max', command=flac, bg="#00b894", font = 'Arial', fg="white", width=15).place(relx = 0.2, rely = 0.47, anchor = CENTER)
        aac = Button(roots, text='AAC Max', command=aac, bg="#00b894", font = 'Arial', fg="white", width=15).place(relx = 0.5, rely = 0.47, anchor = CENTER)
        wav = Button(roots, text='WAV Max', command=wav, bg="#00b894", font = 'Arial', fg="white", width=15).place(relx = 0.8, rely = 0.47, anchor = CENTER)

        mp4 = Button(roots, text='MP4 Video', command=mp4, bg="#0097e6", font = 'Arial', fg="white", width=15).place(relx = 0.2, rely = 0.64, anchor = CENTER)
        mkv = Button(roots, text='MKV Video', command=mkv, bg="#0097e6", font = 'Arial', fg="white", width=15).place(relx = 0.5, rely = 0.64, anchor = CENTER)
        webm = Button(roots, text='WEBM Video', command=webm, bg="#0097e6", font = 'Arial', fg="white", width=15).place(relx = 0.8, rely = 0.64, anchor = CENTER)
        
        roots.mainloop()

roots()
 
