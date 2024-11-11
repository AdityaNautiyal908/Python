from tkinter import *
from speedtest import Speedtest

def speedcheck():
    sp = Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
    up = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Tester")
sp.geometry("500x600")
sp.config(bg="#ADD8E6")

title_label = Label(sp, text="Internet Speed Tester", font=("Times New Roman", 20, "bold"), bg="#ADD8E6", fg="#000000")
title_label.place(x=60, y=50, height=50, width=380)

download_label = Label(sp, text="Download Speed", font=("Times New Roman", 20, "bold"))
download_label.place(x=60, y=120, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times New Roman", 20, "bold"))
lab_down.place(x=60, y=180, height=50, width=380)

upload_label = Label(sp, text="Upload Speed", font=("Times New Roman", 20, "bold"))
upload_label.place(x=60, y=240, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times New Roman", 20, "bold"))
lab_up.place(x=60, y=300, height=50, width=380)

button = Button(sp, text="CHECK SPEED", font=("Times New Roman", 20, "bold"), relief="raised", bg="Red", command=speedcheck)
button.place(x=60, y=380, height=50, width=380)

sp.mainloop()
