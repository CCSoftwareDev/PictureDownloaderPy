from tkinter import *
import time
import requests
import webbrowser
import urllib.request
from io import BytesIO
from PIL import Image,ImageTk

window = Tk()

window.geometry("1920x1080")

window.title("Picture Downloader")

new = 2
taburl = "https://google.com/search?q="

topic = ""
size = ""

user_inputTopic = StringVar(window)
user_inputSize = StringVar(window)


inpbar1name = Entry(window, width=25, border=5, textvariable=user_inputTopic)
inpbar1name.insert(0, "Image Name Here")
inpbar2name = Entry(window, width=25, border=5, textvariable=user_inputSize)
inpbar2name.insert(0, "Image Size Here")

# photos
img1 = PhotoImage(file="")


# loops and functions


def downloadImage():
    response = requests.get("https://e-cdns-images.dzcdn.net/images/cover/f1b3d104a37df7a71ee22101f3b4bb91/500x500.jpg")

    file = open("downloadedImg.png", "wb")
    file.write(response.content)
    file.close()

    print("Downloading Image!")
    time.sleep(1)
    print("Downloaded Image!")


def searchImage():
    #newUrl = taburl + (str(user_inputTopic.get() + " ")) + (str(user_inputSize.get()))
    response = requests.get("https://e-cdns-images.dzcdn.net/images/cover/f1b3d104a37df7a71ee22101f3b4bb91/500x500.jpg")
    img = ImageTk.Image.open(BytesIO(response.content))
    img1 = ImageTk.PhotoImage(img)
    oasislab.configure(image=img1)
    oasislab.image = img1
    print("searching Image")
    time.sleep(1)
    print("Image Found!")




# Labels

txt1 = Label(window, text="Put a name of the image you want in the input bar.")
oasislab = Label(window, image=img1)
oasislab.image = img1
# buttons

btnimagename = Button(window, text="Search Image!", command=lambda:searchImage())
btndownloadimage = Button(window, text="download this Image!", command=lambda: downloadImage())

# pack
txt1.pack(anchor=N)
inpbar1name.pack(anchor=CENTER)
inpbar2name.pack()
btnimagename.pack()
oasislab.pack(expand="yes")
btndownloadimage.pack()

window.mainloop()
