import pyshorteners
import pyperclip
from tkinter import *

root=Tk()
root.title("URL Shortener")
root.geometry("900x350")

def shorten_url():
    url_entry=url.get()
    result= pyshorteners.Shortener().tinyurl.short(url_entry)
    urlEntry.insert(END, result)
root.configure(bg="lightblue")
Label(root, text="Generating Short URL ", font=("Helvetica", 23, "bold"), bg="lightblue",fg="blue").pack(pady=15)

frame1=Frame(root)
Label(frame1, text="Enter Long URL: ", font=("Georgia 17 bold"),bg="lightblue", fg="purple").pack(side=LEFT)
url=Entry(frame1, width="43", bg="white",font=("Georgia 15 bold"))
url.pack()
frame1.pack(pady=10)

Button(root, text="Generate Short URL", font=("Helvetica", 18, "bold"), fg="white", bg="green", command=shorten_url).pack(pady=14)


frame2=Frame(root)
Label(frame2, text="Shortened URL: ", font=("Georgia 17 bold"), bg="lightblue",fg="purple").pack(side=LEFT)
urlEntry=Entry(frame2, width="35", fg="blue",bg="white", font=("Georgia 15 bold"))
urlEntry.pack()
frame2.pack(pady=10)

root.mainloop()
