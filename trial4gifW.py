from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from itertools import count
from tkinter.ttk import Combobox
from tkinter import filedialog
import pyttsx3
import os
from googletrans import Translator,LANGUAGES
root = Tk()


#main frame
main_frame=Frame(root,bg="light blue",highlightbackground='black',highlightthickness=2)
main_frame.place(x=0,y=40,height=950,width=2000)

image_list=[]
gif_duration= 0

def extract_gif(path):
    global gif_duration
    image=Image.open(path)
    for r in count(1):
        try:
            image_list.append(ImageTk.PhotoImage(image.copy()))
            image.seek(r)
            
        except Exception as error:
            print(error)
            break
    gif_duration=int(image.info['duration'])


x=0
def play_gif():
    global x
    try:
        x+=1
        cur_image=image_list[x]
        gif_lb.config(image=cur_image)

        main_frame.after(gif_duration,play_gif)
        
    except Exception as error:
        x=0
        main_frame.after(gif_duration,play_gif)
        print(error)
    

gif_lb=Label(main_frame)
gif_lb.pack()

extract_gif("projectGIF.gif")
play_gif()


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



def delete_page():
    for frame in main_frame.winfo_children():
        frame.destroy()
    

def home_page():
    home_frame=Frame(main_frame)

    #statusbar function
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
    
    #language options in main frame
    list_lang= list(LANGUAGES.values())

    language_options = ttk.Combobox(main_frame, value=list_lang)
    language_options.set("en")
    language_options.place(x=660,y=400)

    #input text area
    text_area=Text(main_frame,font="Helvetica 30",bg="white",relief=GROOVE,wrap=WORD)
    text_area.place(x=10,y=150,width=500,height=250)

    #voice and speed label
    Label(main_frame,text="VOICE",font="Helvetica 30 bold",bg="light blue", fg="white").place(x=530,y=140)
    Label(main_frame,text="SPEED",font="Helvetica 30 bold",bg="light blue", fg="white").place(x=750,y=140)

    #gender combobox
    gender_combobox=Combobox(main_frame,values=['Female','Male'],font="Helvetica 20 bold",state='r',width=10)
    gender_combobox.place(x=530,y=200)
    gender_combobox.set('Female')

    #speed combobox
    speed_combobox=Combobox(main_frame,values=['Fast','Normal','Slow'],font="Helvetica 20 bold",state='r',width=10)
    speed_combobox.place(x=750,y=200)
    speed_combobox.set('Normal')

    global imageicon
    global imageicon2
    imageicon=Image.open("affiliate-marketing-icon.png")
    imageicon=imageicon.resize((50,50))
    imageicon2=ImageTk.PhotoImage(imageicon)
    btn=Button(main_frame,text="Speak",image=imageicon2,width=170,compound=LEFT,bg="green",font="Helvetica 15 bold",relief=GROOVE,command=speaknow)
    btn.place(x=540,y=260)

    #download button image
    global imageicon3
    global imageicon4
    imageicon3=Image.open("download-install-line-icon.png")
    imageicon3=imageicon3.resize((50,50))
    imageicon4=ImageTk.PhotoImage(imageicon3)
    btnsavee=Button(main_frame,text="Download",image=imageicon4,width=170,compound=LEFT,bg="blue",font="Helvetica 15 bold",relief=GROOVE,command=download)
    btnsavee.place(x=765,y=260)

    #status bar
    statusbar=StringVar()
    statusbar.set("Ready")
    sbar=Label(main_frame,textvariable=statusbar,relief=RIDGE,anchor="w")
    sbar.pack(side=BOTTOM,fill=X)
    Button(main_frame,text="Upload",command=statusbr)

    #language options label
    Label(main_frame,text="Choose prefered language",font="Helvetica 21 bold",bg="light blue", fg="white").place(x=530,y=345)

    '''# bind functions to buttons
    imageicon=Image.open("affiliate-marketing-icon.png")
    imageicon=imageicon.resize((50,50))
    imageicon2=ImageTk.PhotoImage(imageicon)
    btn=Button(main_frame,text="Speak",compound=LEFT,bg="light yellow",fg="black",font="Helvetica 20 bold",relief=GROOVE,command=speaknow)
    btn.place(x=540,y=260,width=150,height=50)

    imageicon3=Image.open("download-install-line-icon.png")
    imageicon3=imageicon3.resize((50,50))
    imageicon4=ImageTk.PhotoImage(imageicon3)
    download_btn=Button(main_frame,text="Download",font="Helvetica 20 bold",bg="light yellow",fg="black",relief=GROOVE,command=download)
    download_btn.place(x=765,y=260,width=150,height=50)'''


    home_frame.pack(pady=20)


def handwritten_page():
    handwritten_frame=Frame(main_frame)
    lb=Label(handwritten_frame,text="Convert into speech from handwritten text",font="Helvetica 25 bold")
    lb.pack()
    handwritten_frame.pack(pady=20)

def login_page():
    login_frame=Frame(main_frame)
    lb=Label(login_frame,text="Login to contact the owners",font="Helvetica 25 bold")
    lb.pack()
    login_frame.pack(pady=20)

def contact_page():
    contact_frame=Frame(main_frame)
    lb=Label(contact_frame,text="Contact the developpers",font="Helvetica 25 bold")
    lb.pack()
    contact_frame.pack(pady=20)

def about_page():
    about_frame=Frame(main_frame)
    lb=Label(about_frame,text="Anupama, Dipanjali, Tahseen",font="Helvetica 25 bold")
    lb.pack()
    about_frame.pack(pady=20)
 

def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_frame.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)
        
    toggle_menu_frame=Frame(root,bg='grey')

    def hide_indicator():
        home_indicate.config(bg='grey')
        handwritten_indicate.config(bg='grey')
        login_indicate.config(bg='grey')
        contact_indicate.config(bg='grey')
        about_indicate.config(bg='grey')

    def indicate(lb,page):
        hide_indicator()
        lb.config(bg='blue')
        delete_page()
        page()

    global home_icon
    global home_icon1
    home_icon=Image.open("icons8-home-50.png")
    home_icon1=ImageTk.PhotoImage(home_icon)
    home_btn=Button(toggle_menu_frame,image=home_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(home_indicate,home_page))
    home_btn.place(x=70,y=20)
    hombtn_frm=Frame(toggle_menu_frame)
    hombtn_frm.pack()
    home_indicate=Label(toggle_menu_frame,text='',bg='grey')
    home_indicate.place(x=10,y=25,width=5,height=40)

    global handwritten_icon
    global handwritten_icon1
    handwritten_icon=Image.open("handwriting.png")
    handwritten_icon=handwritten_icon.resize((50,50))
    handwritten_icon1=ImageTk.PhotoImage(handwritten_icon)
    handwritten_btn=Button(toggle_menu_frame,image=handwritten_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(handwritten_indicate,handwritten_page))
    handwritten_btn.place(x=70,y=100)
    handwritten_indicate=Label(toggle_menu_frame,text='',bg='grey')
    handwritten_indicate.place(x=10,y=105,width=5,height=40)

    global login_icon
    global login_icon1
    login_icon=Image.open("login.png")
    login_icon=login_icon.resize((50,50))
    login_icon1=ImageTk.PhotoImage(login_icon)
    login_btn=Button(toggle_menu_frame,image=login_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(login_indicate,login_page))
    login_btn.place(x=70,y=180)
    login_indicate=Label(toggle_menu_frame,text='',bg='grey')
    login_indicate.place(x=10,y=185,width=5,height=40)

    global contact_icon
    global contact_icon1
    contact_icon=Image.open("communicate.png")
    contact_icon=contact_icon.resize((50,50))
    contact_icon1=ImageTk.PhotoImage(contact_icon)
    contact_btn=Button(toggle_menu_frame,image=contact_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(contact_indicate,contact_page))
    contact_btn.place(x=70,y=260)
    contact_indicate=Label(toggle_menu_frame,text='',bg='grey')
    contact_indicate.place(x=10,y=265,width=5,height=40)

    global about_icon
    global about_icon1
    about_icon=Image.open("information.png")
    about_icon=about_icon.resize((50,50))
    about_icon1=ImageTk.PhotoImage(about_icon)
    about_btn=Button(toggle_menu_frame,image=about_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(about_indicate,about_page))
    about_btn.place(x=70,y=340)
    about_indicate=Label(toggle_menu_frame,text='',bg='grey')
    about_indicate.place(x=10,y=345,width=5,height=40)
    
    window_height=root.winfo_height()
    toggle_menu_frame.place(x=0,y=50,height=window_height,width=200)
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


def confirm_exit():
    result=messagebox.askokcancel(title="Exit",message="Do you want to exit ?")
    if result:
        root.destroy()


root.protocol("WM_DELETE_WINDOW", confirm_exit)



    

root.mainloop()
