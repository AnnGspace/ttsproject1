import tkinter as tk
from googletrans import Translator
import pyttsx3

# Create an instance of Translator and Pyttsx3
translator = Translator()
engine = pyttsx3.init()

# Define a function to translate the text and speak it
def translate_and_speak():
    # Get the text from the entry widget
    original_text = entry.get()
    
    # Translate the text to the language of your choice (in this example, Spanish)
    translated_text = translator.translate(original_text, dest='es').text
    
    # Speak the translated text
    engine.say(translated_text)
    engine.runAndWait()

# Create a Tkinter window
root = tk.Tk()
root.title('Translator')

# Create a label widget
label = tk.Label(root, text='Enter text to translate:')
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button widget to trigger the translation and speech
button = tk.Button(root, text='Translate and Speak', command=translate_and_speak)
button.pack()

# Start the Tkinter mainloop
root.mainloop()




........



from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyttsx3
import os
from googletrans import Translator,LANGUAGES
root = Tk()

language_options = ttk.Combobox(root, values=['en', 'es', 'fr', 'ja'])
language_options.set("en")
language_options.place(x=750,y=400)

output_text=StringVar()

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

def speaknow():
    translate_text()
    textog=output_text
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voice=engine.getProperty('voices')



    def setvoice():
        if(gender == 'Female'):
            engine.setProperty('voice',voice[1].id)
            engine.say(textog)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voice[0].id)
            engine.say(textog)
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
            

def download():
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

root.mainloop()
