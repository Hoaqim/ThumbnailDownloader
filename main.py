from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk



def search():
    global image

    #Getting the url
    try:
        url = search_bar.get()
        request_url = urlopen(url)
        page_html = request_url.read()
        request_url.close()

        # Getting the image url
        soup_obj = BeautifulSoup(page_html, "html.parser")
        thumbnail_url = soup_obj.find('link', rel="image_src")['href']
    except:
        popup = Toplevel(window)
        popup.title("error")
        popup.geometry(f"200x200+{x+200}+{y+100}")
        popup.resizable(0,0)
        popup.configure(bg="red")
        label = Label(popup, text="Something went wrong! \n"
                      "Check if your link is correct!\n", pady="25",
                      font="Comic_sans", bg="red").pack()

    #Getting the image and putting the smaller image to the label
    image = Image.open(requests.get(thumbnail_url, stream=True).raw)
    image_sample = image.resize((480,250))
    photo = ImageTk.PhotoImage(image_sample)
    show_thumbnail.configure(image = photo)
    show_thumbnail.image = photo

    download_button.pack()


def download():
    file = filedialog.asksaveasfile(mode='w',defaultextension='.jpg')
    image.save(file)


window = Tk()

y = (window.winfo_screenheight()//2) - 200
x = (window.winfo_screenwidth()//2) - 300

window.geometry(f"600x400+{x}+{y}")
window.resizable(0,0)
window.title("Thumbnail Downloader")
window.iconbitmap("Beautiful_logo.ico")

instruction = Label(window, text="Put youtube link below")
instruction.pack()

container = Label(window)
container.pack()

search_bar = Entry(container)
search_bar.grid(row=0,column=0, padx=(0,10), ipady=4)

search_button = Button(container, text="Search", command=search, bg="lightblue")
search_button.grid(row=0,column=1)

show_thumbnail = Label(window)
show_thumbnail.pack()

download_button = Button(window, text="Download", command=download, bg="lightgreen")


window.mainloop()