## Very early work in progress.
from __future__ import unicode_literals
from tkinter import *
import youtube_dl
def download():
    label = Label(roots, text = "Downloading...", bg="white", font=("Arial", 9)).grid(row=2, column=2)
    url = urlbutton.get()
    urlbutton.delete(0, END)
    roots.update_idletasks()
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
##with youtube_dl.YoutubeDL(ydl_opts) as ydl:
##meta = ydl.extract_info(str(url), download=False)
##        print 'upload date : %s' %(meta['upload_date'])
##        print 'uploader    : %s' %(meta['uploader'])
##        print 'views       : %d' %(meta['view_count'])
##        print 'likes       : %d' %(meta['like_count'])
##        print 'dislikes    : %d' %(meta['dislike_count'])
##        print 'id          : %s' %(meta['id'])
##        print 'format      : %s' %(meta['format'])
##        print 'duration    : %s' %(meta['duration'])
##        print 'title       : %s' %(meta['title'])
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(url)])
    label = Label(roots, text = "                         ", bg="white", font=("Arial", 9)).grid(row=2, column=2)
    roots.update_idletasks()
    label = Label(roots, text = "Done!", bg="white", font=("Arial", 9)).grid(row=2, column=2)
    roots.update_idletasks()
def roots():
        global urlbutton, roots
        roots = Tk() #register window
        roots.title('revox\'s ytdl')
        roots.configure(background='white')
        label = Label(roots, text="URL:", bg="white").grid(row=1, column=1)
        urlbutton = Entry(roots) 
        urlbutton.grid(row=1, column=2)
        grab = Button(roots, text='Grab!', command=download, bg="white")
        grab.grid(row=1, column=3)
        label = Label(roots, bg="white").grid(row=2, column=1)
        roots.mainloop()
roots()
 
