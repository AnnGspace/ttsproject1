from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyttsx3
import os
from googletrans import Translator,LANGUAGES
root = Tk()


list_lang= list(LANGUAGES.values())

language_options = ttk.Combobox(root, value=list_lang)
language_options.set("en")
language_options.place(x=660,y=400)

output_text=StringVar()

def popup():
    msg.showinfo("Download", "Want to save the audio?")

def translate_text():
    # Get the text to be translated and the destination language from the user interface
    text_to_translate = text_area.get(1.0,END).strip()
    destination_language = language_options.get()

    # Translate the text using Googletrans
    translator = Translator()
    translated = translator.translate(text_to_translate, dest=language_options.get())
    output_text=translated.text
    print(output_text)

    # Set the translated text in the output area
    #translated_output.delete(1.0, END)
    #translated_output.insert(END, translated.text)


engine=pyttsx3.init()

def statusbr():
    statusbar.set("Processing.....")
    sbar.update()
    import time
    time.sleep(0.5)
    statusbar.set("Ready")

def speaknow():
    text_to_translate = text_area.get(1.0,END).strip()
    destination_language = language_options.get()
    translator = Translator()
    translated = translator.translate(text_to_translate, dest=language_options.get()).text
    text=output_text
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voice=engine.getProperty('voices')



    def setvoice():
        if(gender == 'Female'):
            engine.setProperty('voice',voice[1].id)
            engine.say(translated)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voice[0].id)
            engine.say(translated)
            engine.runAndWait()
            
    if(text):
         if(speed =="Fast"):
             engine.setProperty('rate',250)
             setvoice()
         elif (speed == 'Normal'):
             engine.setProperty('rate',150)
             statusbr()
             setvoice()
         else:
             engine.setProperty('rate',60)
             statusbr()
             setvoice()
            

def download():
    popup()
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voice=engine.getProperty('voices')

    def setvoice():
        if(gender == 'Female'):
            engine.setProperty('voice',voice[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voice[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)            
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            
    if(text):
         if(speed =="Fast"):
             engine.setProperty('rate',250)
             setvoice()
         elif (speed == 'Normal'):
             engine.setProperty('rate',150)
             setvoice()
         else:
             engine.setProperty('rate',60)
             setvoice()

root.title("Text to Speech")
root.geometry("1000x500+500+200")
root.maxsize(1000,500)
root.minsize(1000,500)
root.configure(bg="light blue")

#icon
#root.wm_iconbitmap("online-ads-report-icon.png")
image_icon=PhotoImage(file="online-ads-report-icon.png")
root.iconphoto(False,image_icon)


#Top frame
Top_frame=Frame(root,bg="light yellow", width=1000, height=100)
Top_frame.place(x=0,y=0)

logo=Image.open("online-ads-report-icon.png")
logo=logo.resize((95,95))
imglogo=ImageTk.PhotoImage(logo)
Label(Top_frame,image=imglogo).place(x=10,y=5)

Label(Top_frame,text="Text To Speech",font="Helvetica 30 bold", bg="light yellow",fg="black").place(x=120,y=30)

text_area=Text(root,font="Helvetica 30",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="Helvetica 30 bold",bg="light blue", fg="white").place(x=530,y=140)
Label(root,text="SPEED",font="Helvetica 30 bold",bg="light blue", fg="white").place(x=750,y=140)

gender_combobox=Combobox(root,values=['Female','Male'],font="Helvetica 20 bold",state='r',width=10)
gender_combobox.place(x=530,y=200)
gender_combobox.set('Female')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="Helvetica 20 bold",state='r',width=10)
speed_combobox.place(x=750,y=200)
speed_combobox.set('Normal')

imageicon=Image.open("affiliate-marketing-icon.png")
imageicon=imageicon.resize((50,50))
imageicon2=ImageTk.PhotoImage(imageicon)
btn=Button(root,text="Speak",compound=LEFT,image=imageicon2,bg="green",width=170,font="Helvetica 15 bold",relief=GROOVE,command=speaknow)
btn.place(x=540,y=260)


imageicon3=Image.open("download-install-line-icon.png")
imageicon3=imageicon3.resize((50,50))
imageicon4=ImageTk.PhotoImage(imageicon3)
btnsavee=Button(root,text="Download",compound=LEFT,image=imageicon4,bg="blue",width=170,font="Helvetica 15 bold",relief=GROOVE,command=download)
btnsavee.place(x=765,y=260)

statusbar=StringVar()
statusbar.set("Ready")
sbar=Label(root,textvariable=statusbar,relief=RIDGE,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="Upload",command=statusbr)

Label(root,text="Choose prefered language",font="Helvetica 21 bold",bg="light blue", fg="white").place(x=530,y=345)



root.mainloop()


