from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyttsx3
import os
from googletrans import Translator,LANGUAGES
root = Tk()


main_frame=Frame(root,bg="light blue",highlightbackground='black',highlightthickness=2)
main_frame.place(x=0,y=40,height=950,width=2000)


engine=pyttsx3.init()


root.title("Text to Speech Converter")
root.geometry("1000x500+500+200")
#root.maxsize(1000,500)
#root.minsize(1000,500)
root.configure(bg="light blue")


#icon
#root.wm_iconbitmap("online-ads-report-icon.png")
image_icon=PhotoImage(file="online-ads-report-icon.png")
root.iconphoto(False,image_icon)


#Top frame
'''Top_frame=Frame(root,bg="light yellow", width=1000, height=100)
Top_frame.place(x=0,y=0)

logo=Image.open("online-ads-report-icon.png")
logo=logo.resize((95,95))
imglogo=ImageTk.PhotoImage(logo)
Label(Top_frame,image=imglogo).place(x=10,y=5)

Label(Top_frame,text="Text To Speech",font="Helvetica 30 bold", bg="light yellow",fg="black").place(x=120,y=30)'''


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
    text=translated
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
    result=messagebox.askyesno("Download", "Want to save the audio?")
    if result:
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
    else:
        exit()


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
    




def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()
    



list_lang= list(LANGUAGES.values())

language_options = ttk.Combobox(root, value=list_lang)
language_options.set("en")
language_options.place(x=660,y=400)
    

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

Label(root,text="Choose prefered language",font="Helvetica 21 bold",bg="light blue", fg="white").place(x=530,y=345)



def handwritten_page():
    handwritten_frame=Frame(main_frame)
    lb=Label(handwritten_frame,text="Convert into speech from handwritten text",font="Helvetica 25 bold")
    lb.pack()
    handwritten_frame.pack(pady=20)

def about_page():
    about_frame=Frame(main_frame)
    lb=Label(about_frame,text="Anupama, Dipanjali, Tahseen",font="Helvetica 25 bold")
    lb.pack()
    about_frame.pack(pady=20)

def feedback_page():
    feedback_frame=Frame(main_frame)
    lb=Label(feedback_frame,text="Leave your honest feedback",font="Helvetica 25 bold")
    lb.pack()
    feedback_frame.pack(pady=20)

def login_page():
    login_frame=Frame(main_frame)
    lb=Label(login_frame,text="Login to contact the owners",font="Helvetica 25 bold")
    lb.pack()
    login_frame.pack(pady=20)

def exit_page():
    exit_frame=Frame(main_frame)
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()
    login_frame.pack(pady=20)

 

def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_frame.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)
        
    toggle_menu_frame=Frame(root,bg='grey')

    def hide_indicator():
        handwritten_indicate.config(bg='grey')
        about_indicate.config(bg='grey')
        feedback_indicate.config(bg='grey')
        login_indicate.config(bg='grey')
        exit_indicate.config(bg='grey')


    def indicate(lb,page):
        hide_indicator()
        lb.config(bg='blue')
        delete_page()
        page()

    handwritten_btn=Button(toggle_menu_frame,text='Hand written text',font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(handwritten_indicate,handwritten_page))
    handwritten_btn.place(x=20,y=100)
    handwritten_indicate=Label(toggle_menu_frame,text='',bg='grey')
    handwritten_indicate.place(x=10,y=120,width=5,height=40)

    about_btn=Button(toggle_menu_frame,text='About',font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(about_indicate,about_page))
    about_btn.place(x=20,y=180)
    about_indicate=Label(toggle_menu_frame,text='',bg='grey')
    about_indicate.place(x=10,y=200,width=5,height=40)

    feedback_btn=Button(toggle_menu_frame,text='Feedback',font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(feedback_indicate,feedback_page))
    feedback_btn.place(x=20,y=260)
    feedback_indicate=Label(toggle_menu_frame,text='',bg='grey')
    feedback_indicate.place(x=10,y=280,width=5,height=40)

    login_btn=Button(toggle_menu_frame,text='Login',font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(login_indicate,login_page))
    login_btn.place(x=20,y=340)
    login_indicate=Label(toggle_menu_frame,text='',bg='grey')
    login_indicate.place(x=10,y=360,width=5,height=40)

    exit_btn=Button(toggle_menu_frame,text='Exit',font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(exit_indicate,exit_page))
    exit_btn.place(x=20,y=420)
    exit_indicate=Label(toggle_menu_frame,text='',bg='grey')
    exit_indicate.place(x=10,y=445,width=5,height=40)
    
    window_height=root.winfo_height()
    toggle_menu_frame.place(x=0,y=50,height=window_height,width=300)
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)

head_frame= Frame(root,bg='blue',highlightbackground='black',highlightthickness=2)

toggle_btn=Button(head_frame,text='≡', bg='blue',fg='white',font="Helvetica 30 bold",bd=0,activebackground='blue',activeforeground='white',command=toggle_menu)
toggle_btn.pack(side=LEFT)

title_lb=Label(head_frame,text='Menu',bg='blue',fg='white',font="Helvetica 30 bold")
title_lb.pack(side=LEFT)

head_frame.pack(side=TOP,fill=X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)




    

root.mainloop()
