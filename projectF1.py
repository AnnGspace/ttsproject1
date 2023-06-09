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
import PyPDF2
import pygame
from gtts import gTTS
import pytesseract as pt
import time
from mutagen.mp3 import MP3
import webbrowser

root = Tk()


#main frame
main_frame=Frame(root,bg="light blue",highlightbackground='black',highlightthickness=2)
main_frame.place(x=0,y=40,height=950,width=2000)

Label(main_frame,text="Text to Speech Converter",font="Helvetica 50 bold",bg="light blue", fg="cadetblue").place(x=470,y=705)

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


def delete_page():
    global main_frame
    main_frame.destroy()
    

def home_page():
    global main_frame
    global root
    main_frame=Frame(root,bg="light blue",highlightbackground='black',highlightthickness=2)
    main_frame.place(x=0,y=40,height=950,width=2000)
    toggle_menu_frame.lift()
   
    main_frame.propagate(False)

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
        print(text_to_translate)
        print(destination_language)
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

    def set_volume(volume):
    # Convert the volume value from the slider (0-100) to the range supported by the engine (0.0-1.0)
        volume = float(volume) / 100.0
        engine.setProperty('volume', volume)

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
    language_options.place(x=1190,y=460)

    #input text area
    text_area=Text(main_frame,font="Helvetica 30",bg="white",relief=GROOVE,wrap=WORD)
    text_area.place(x=10,y=150,width=940,height=500)

    #voice and speed label
    Label(main_frame,text="VOICE",font="Helvetica 30 bold",bg="light blue", fg="darkorchid").place(x=1015,y=160)
    Label(main_frame,text="SPEED",font="Helvetica 30 bold",bg="light blue", fg="darkorchid").place(x=1365,y=160)

    #gender combobox
    gender_combobox=Combobox(main_frame,values=['Female','Male'],font="Helvetica 20 bold",state='r',width=10)
    gender_combobox.place(x=1000,y=220)
    gender_combobox.set('Female')

    #speed combobox
    speed_combobox=Combobox(main_frame,values=['Fast','Normal','Slow'],font="Helvetica 20 bold",state='r',width=10)
    speed_combobox.place(x=1350,y=220)
    speed_combobox.set('Normal')

    #Create the volume slider
    volume_label = Label(main_frame,font="Helvetica 30 bold",bg="light blue", fg="darksalmon",text="Volume")
    volume_label.place(x=1190,y=530)

    volume_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
    volume_slider.set(50)  # Set the initial volume to 50%
    volume_slider.place(x=1235,y=595)


    global imageicon
    global imageicon2
    imageicon=Image.open("affiliate-marketing-icon.png")
    imageicon=imageicon.resize((50,50))
    imageicon2=ImageTk.PhotoImage(imageicon)
    btn=Button(main_frame,text="Speak",image=imageicon2,width=170,compound=LEFT,bg="rosy brown",font="Helvetica 15 bold",relief=GROOVE,command=speaknow)
    btn.place(x=1015,y=280)

    #download button image
    global imageicon3
    global imageicon4
    imageicon3=Image.open("download-install-line-icon.png")
    imageicon3=imageicon3.resize((50,50))
    imageicon4=ImageTk.PhotoImage(imageicon3)
    btnsavee=Button(main_frame,text="Download",image=imageicon4,width=170,compound=LEFT,bg="rosy brown",font="Helvetica 15 bold",relief=GROOVE,command=download)
    btnsavee.place(x=1365,y=280)

    #status bar
    statusbar=StringVar()
    statusbar.set("Ready")
    sbar=Label(main_frame,textvariable=statusbar,relief=RIDGE,anchor="w")
    sbar.pack(side=BOTTOM,fill=X)
    Button(main_frame,text="Upload",command=statusbr)

    #language options label
    Label(main_frame,text="Choose preferred language",font="Helvetica 30 bold",bg="light blue", fg="darkslateblue").place(x=970,y=385)

def audiobook_page():
    global main_frame
    global root
    global file_path
   # global pause variable
    global check
    check=False
    #initializing mixer 
    pygame.mixer.init()
    # making audio slider
    def slider(x):
       # slider_label.config(text=f'{int(slide.get())} of {int(audio_len)}')
        pygame.mixer.init()
        pygame.mixer.music.load("text.mp3")  # Replace "path_to_audio_file.mp3" with the actual path to your audio file
        pygame.mixer.music.play(loops=0,start=int(slide.get()))


    # take file path from user
    def open_pdf_file():
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    #
    
    #play the audio
    def play_audio():
        pygame.mixer.init()
        pygame.mixer.music.load("text.mp3")  # Replace "path_to_audio_file.mp3" with the actual path to your audio file
        pygame.mixer.music.play()
        # call the play time fuction
        play_time()
        # upadate slider lenth to from 100 to lenght of audio 
        #slider_position=int(audio_len)
        #slide.config(to=slider_position,value=0) 

    #
    
    # stop the audio
    def stop_audio():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        # clear status
        status.config(text='')
        # make slider go to 0 again
        slide.config(value=0)
    #

    
    #pause the audio
    def pause_audio():
        global check
        if not check:
            pygame.mixer.music.pause()
            check=True
        else:
            pygame.mixer.music.unpause()
            check=False
    #
    
    
    # song length
    def play_time():
        global status
        current_time=pygame.mixer.music.get_pos()/1000
        
        con_current_time=time.strftime('%M:%S',time.gmtime(current_time))
        #load audio
        audio_mut=MP3('text.mp3')
       
        # get the lenght
        global audio_len
        audio_len=audio_mut.info.length
        con_audio_len=time.strftime('%M:%S',time.gmtime(audio_len))
       
        if int(slide.get())==int(audio_len):
            status.config(text=f'Time Elapsed:{con_audio_len} of {con_audio_len}  ')
       #check if the slider has been moved or not and do this only if song is not ended
        elif check:
            pass

        elif int(slide.get())==int(current_time+1):
            # slider has not been moved

            # upadate slider lenth to from 100 to lenght of audio 
            slider_position=int(audio_len)
            slide.config(to=slider_position,value=int(current_time)+1)
           

            # update status
            status.config(text=f'Time Elapsed:{con_current_time} of {con_audio_len}  ')
        else:
            #slider has been moved

             # upadate slider lenth to from 100 to lenght of audio 
            slider_position=int(audio_len)
            slide.config(to=slider_position,value=int(slide.get()))
            
            # update status
            con_current_time=time.strftime('%M:%S',time.gmtime(slide.get()))
            status.config(text=f'Time Elapsed:{con_current_time} of {con_audio_len}  ')
            # move this thing one second further as this else part taking the  pos of slider not moving wth audio so we need to increase it one further
            next_time=int(slide.get())+1
            slide.config(value=next_time)

       
        # update silder with audio
       
        status.after(1000,play_time)

    #
   
    # read the pdf file
    def audioRead(pageTo):
        global file_path
        if file_path:
            print(file_path)
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_of_pages = len(pdf_reader.pages)
                pageF=int(pageTo)+1

                for page_number in range(int(pageTo),pageF):
                    page = pdf_reader.pages[page_number]
                    text = page.extract_text()
                    tts = gTTS(text,lang='hi')
                    if os.path.exists('text.mp3'):
                        os.remove('text.mp3')
                        tts.save('text.mp3')
                        file.close()
                    else:
                        tts.save('text.mp3')
                        file.close()
    #
                    
   
    # opening icon images
    global playicon
    playicon=Image.open("play.png")
    playicon=playicon.resize((50,50))
    playicon=ImageTk.PhotoImage(playicon)
    global pauseicon
    pauseicon=Image.open("pause.png")
    pauseicon=pauseicon.resize((50,50))
    pauseicon=ImageTk.PhotoImage(pauseicon)
    global stopicon
    stopicon=Image.open("stop-button.png")
    stopicon=stopicon.resize((50,50))
    stopicon=ImageTk.PhotoImage(stopicon)
    global converticon
    converticon=Image.open("convert.png")
    converticon=converticon.resize((50,50))
    converticon=ImageTk.PhotoImage(converticon)
    global openicon
    openicon=Image.open("folder.png")
    openicon=openicon.resize((50,50))
    openicon=ImageTk.PhotoImage(openicon)
    #
   
    # frame configuration
    main_frame=Frame(root,bg="light blue",highlightbackground='black',highlightthickness=2)
    main_frame.place(x=0,y=40,height=950,width=2000)
    toggle_menu_frame.lift()
    main_frame.propagate(False)
    lb=Label(main_frame,text="Listen to your pdf file as an audiobook",font="Helvetica 25 bold",fg='black',bg='peru',bd=2,relief='solid')
    lb.place(x=570,y=40)
    button =Button(main_frame, text="Open pdf file",image=openicon,compound=LEFT, command=open_pdf_file,bd=2,relief='solid',font='Helvetica 20',bg='papayawhip')
    button.place(x=610,y=199)
    read=Button(main_frame, text="Convert", image=converticon,compound=LEFT,command=lambda:audioRead(text_area.get(1.0,END).strip()),bd=2,relief='solid',font='Helvetica 20',bg='peachpuff')
    read.place(x=870,y=280)
    play=Button(main_frame,image=playicon,command=play_audio,bd=2,relief='solid',font='Helvetica 10',bg='green')
    play.place(x=825,y=400)
    pause=Button(main_frame,image=pauseicon,command=pause_audio,bd=2,relief='solid',font='Helvetica 20',bg='palevioletred')
    pause.place(x=920,y=400)
    stop=Button(main_frame,image=stopicon,command=stop_audio,bd=2,relief='solid',font='Helvetica 20',bg='red')
    stop.place(x=1015,y=400)
    lb=Label(main_frame,text='Enter page number',font='Helvetica 10',bg='peru')
    lb.place(x=875,y=210)
    text_area=Text(main_frame,font="Helvetica 30",bg="papayawhip",relief=GROOVE,wrap=WORD,)
    text_area.place(x=1050,y=200,width=200,height=50)
    global status
    status=Label(main_frame,text='',font='Helvetica 10',bg='white',relief=GROOVE)
    status.place(x=650,y=700,width=600)
    slide=ttk.Scale(main_frame, from_=0, to =100 , orient=HORIZONTAL,value=0,command=slider,length=360)
    slide.place(x=770 ,y=600)
   
    #

def ocr_page():
    global main_frames
    global root
    global file_path
   
    #initializing mixer
    pygame.mixer.init()
    
    # take file path from user
    def open_pdf_file():
        global file_path
        file_path = filedialog.askopenfilename()
    # 
    
    #play the audio
    def play_audio():
        pygame.mixer.init()
        pygame.mixer.music.load("text1.mp3")  # Replace "path_to_audio_file.mp3" with the actual path to your audio file
        pygame.mixer.music.play()
    #
    # stop the audio
    def stop_audio():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        text_area.delete('1.0','end')
    #
    # read the pdf file
    def audioRead(text_area):
        global file_path
        global imageText
        if file_path:
            imageText=Image.open(file_path)
            text=pt.image_to_string(imageText,lang='eng')
            text_area.delete('1.0','end')
            text_area.insert("1.0",text)
            tts = gTTS(text,lang='hi')
            if os.path.exists('text.mp3'):
                os.remove('text.mp3')
                tts.save('text1.mp3')
            else:
                tts.save('text1.mp3')
           
    #
                    
    # opening icon images
    global playicon
    playicon=Image.open("play.png")
    playicon=playicon.resize((50,50))
    playicon=ImageTk.PhotoImage(playicon)
    global pauseicon
    pauseicon=Image.open("stop-button.png")
    pauseicon=pauseicon.resize((50,50))
    pauseicon=ImageTk.PhotoImage(pauseicon)
    global converticon
    converticon=Image.open("convert.png")
    converticon=converticon.resize((50,50))
    converticon=ImageTk.PhotoImage(converticon)
    global openicon
    openicon=Image.open("folder.png")
    openicon=openicon.resize((50,50))
    openicon=ImageTk.PhotoImage(openicon)
    #
    
    main_frame=Frame(root,bg="light blue",highlightbackground='black',highlightthickness=2)
    main_frame.place(x=0,y=40,height=950,width=2000)
    toggle_menu_frame.lift()
    main_frame.propagate(False)
    lb=Label(main_frame,text="OCR to speech",font="Helvetica 25 bold",fg='black',bg='peru',bd=2,relief='solid')
    lb.place(x=800,y=40)
    button =Button(main_frame, text="Open pdf file",image=openicon,compound=LEFT, command=open_pdf_file,bd=2,relief='solid',font='Helvetica 20',bg='wheat')
    button.place(x=550,y=199)
    read=Button(main_frame, text="Convert", image=converticon,compound=LEFT,command=lambda:audioRead(text_area),bd=2,relief='solid',font='Helvetica 20',bg='thistle')
    read.place(x=1100,y=200)
    play=Button(main_frame,image=playicon,command=play_audio,bd=2,relief='solid',font='Helvetica 10',bg='green')
    play.place(x=970,y=300)
    stop=Button(main_frame,image=pauseicon,command=stop_audio,bd=2,relief='solid',font='Helvetica 20',bg='red')
    stop.place(x=860,y=300)
    text_area=Text(main_frame,font="Helvetica 10",bg="white",relief=GROOVE,wrap=WORD,)
    text_area.place(x=640,y=400,width=600,height=300)


def contact_page():
    global main_frame
    global root

    def open_link1(event):
        link1 = "mailto:ghoshanupama524@gmail.com"
        print("Opening link:", link1)
        webbrowser.open_new(link1)

    def open_link2(event):
        email2 = "mailto:tahseenyasmin284@gmail.com"
        print("Opening link:", email2)
        webbrowser.open_new(email2)

    def open_link3(event):
        link3 = "mailto:dipanjali9330@gmail.com"
        print("Opening link:", link3)
        webbrowser.open_new(link3)

    main_frame = Frame(root, bg="papayawhip", highlightbackground='black', highlightthickness=2)
    main_frame.place(x=0, y=40, height=950, width=2000)

    Label(main_frame,text="Contact the developers",font="Helvetica 30 bold",bg="bisque", fg="dark green").place(x=700,y=30)

    label1 = Label(main_frame, text="Click here to mail Anupama Ghosh", fg="blue", cursor="hand2")
    label1.place(x=850, y=120)

    label2 = Label(main_frame, text="Click here to mail Tahseen Yasmin", fg="blue", cursor="hand2")
    label2.place(x=850, y=220)

    label3 = Label(main_frame, text="Click here to mail Dipanjali Singh", fg="blue", cursor="hand2")
    label3.place(x=850, y=320)

    label1.bind("<Button-1>", open_link1)
    label2.bind("<Button-1>", open_link2)
    label3.bind("<Button-1>", open_link3)

    Label(main_frame,text="Get the github repository of this open sourse software",font="Helvetica 30 bold",bg="bisque", fg="dark green").place(x=300,y=410)

    def open_link4(event):
        # Open the link in a web browser or perform any desired action
        link4 = "https://github.com/AnnGspace/ttsproject1"
        print("Opening link:", link4)
        webbrowser.open_new(link4)

    label4 = Label(root, text="Click here to visit the website", fg="blue", cursor="hand2")
    label4.place(x=850, y=550)

    # Add a binding to the Label widget to handle hyperlink clicks
    label4.bind("<Button-1>", open_link4)

    def open_link5(event):
        # Open the link in a web browser or perform any desired action
        link5 = "https://github.com/SpaceOfCode/textTospeech/tree/master/TextTospeech"
        print("Opening link:", link5)
        webbrowser.open_new(link5)

    label5 = Label(root, text="Click here to visit the website", fg="blue", cursor="hand2")
    label5.place(x=850, y=650)

    # Add a binding to the Label widget to handle hyperlink clicks
    label5.bind("<Button-1>", open_link5)
    
    toggle_menu_frame.lift()
    main_frame.propagate(False)   


def about_page():
    global main_frame
    global root
    main_frame=Frame(root,bg="beige",highlightbackground='black',highlightthickness=2)
    main_frame.place(x=0,y=40,height=950,width=2000)
    toggle_menu_frame.lift()
    text_frame=Frame(main_frame,bg="aquamarine",highlightbackground='black',highlightthickness=2)
    text_frame.place(x=390,y=140,height=500,width=1000)

    # about image 
    global about
    global imgabout
    about=Image.open("About.png")
    about=about.resize((295,493))
    imgabout=ImageTk.PhotoImage(about)
    # text that need to be inserted
    text=" Anumpma Ghosh-:  Anumpma has developped the overall layout of the project, the designing of the front page and the toggle menubar.She has also developped the text to speech conversion.\n\n\nTahseen Yasmin-: Tahseen has contriubuted to the design part with her creative ideas .She has developed the OCR funtion and the contact function.\n\n\nDipanjali Singh-: Dipanjali has developped the audiobook part and the about page .She hascontribted to the design part with her ideas to the main developer to design the layout of the project."
   
   # puting the image in text-frame
    abouimg=Label(text_frame,image=imgabout,bd=2,relief='solid')
    abouimg.place(x=0,y=0)
    text_area=Text(text_frame,font="Helvetica 15",bg="white",relief=GROOVE,wrap=WORD)
    text_area.place(x=300,y=10,width=690,height=470)
    text_area.insert("1.0",text)
    text_area.configure(state=DISABLED)
   

def toggle_menu():
    global toggle_menu_frame
    def collapse_toggle_menu():
        global root
        toggle_menu_frame.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)
        
    toggle_menu_frame=Frame(root,bg='grey')
    

    def hide_indicator():
        home_indicate.config(bg='grey')
        audiobook_indicate.config(bg='grey')
        ocr_indicate.config(bg='grey')
        contact_indicate.config(bg='grey')
        about_indicate.config(bg='grey')

    def indicate(lb,page):
        hide_indicator() #hide previous indicators
        lb.config(bg='blue') #make indicator active
        delete_page()  #delete previou frame
        page()  #make new frame
    # home icon and button config
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
    #
    #hand icon and button config
    global audiobook_icon
    global audiobook_icon1
    audiobook_icon=Image.open("audiobook.png")
    audiobook_icon=audiobook_icon.resize((50,50))
    audiobook_icon1=ImageTk.PhotoImage(audiobook_icon)
    audiobook_btn=Button(toggle_menu_frame,image=audiobook_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(audiobook_indicate,audiobook_page))
    audiobook_btn.place(x=70,y=100)
    # indicator which is gray and would become blue
    audiobook_indicate=Label(toggle_menu_frame,text='',bg='grey')
    audiobook_indicate.place(x=10,y=105,width=5,height=40)
    #
    # login icon and button config
    global ocr_icon
    global ocr_icon1
    ocr_icon=Image.open("handwriting.png")
    ocr_icon=ocr_icon.resize((50,50))
    ocr_icon1=ImageTk.PhotoImage(ocr_icon)
    ocr_btn=Button(toggle_menu_frame,image=ocr_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(ocr_indicate,ocr_page))
    ocr_btn.place(x=70,y=180)
    ocr_indicate=Label(toggle_menu_frame,text='',bg='grey')
    ocr_indicate.place(x=10,y=185,width=5,height=40)
    #
    #contact icon and button config
    global contact_icon
    global contact_icon1
    contact_icon=Image.open("communicate.png")
    contact_icon=contact_icon.resize((50,50))
    contact_icon1=ImageTk.PhotoImage(contact_icon)
    contact_btn=Button(toggle_menu_frame,image=contact_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(contact_indicate,contact_page))
    contact_btn.place(x=70,y=260)
    contact_indicate=Label(toggle_menu_frame,text='',bg='grey')
    contact_indicate.place(x=10,y=265,width=5,height=40)
    #
    #about icon and button config
    global about_icon
    global about_icon1
    about_icon=Image.open("information.png")
    about_icon=about_icon.resize((50,50))
    about_icon1=ImageTk.PhotoImage(about_icon)
    about_btn=Button(toggle_menu_frame,image=about_icon1,font="Helvetica 25 bold",bd=0,bg='grey',fg='white',command=lambda:indicate(about_indicate,about_page))
    about_btn.place(x=70,y=340)
    about_indicate=Label(toggle_menu_frame,text='',bg='grey')
    about_indicate.place(x=10,y=345,width=5,height=40)
    #
    # window size increase config
    window_height=root.winfo_height()
    toggle_menu_frame.place(x=0,y=43,height=window_height,width=200)
    toggle_menu_frame.lift()
    #
    # = to x toggle menue sign
    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)
    #

#head frame
head_frame= Frame(root,bg='blue',highlightbackground='black',highlightthickness=2)

toggle_btn=Button(head_frame,text='≡', bg='blue',fg='white',font="Helvetica 30 bold",bd=0,activebackground='blue',activeforeground='white',command=toggle_menu)
toggle_btn.pack(side=LEFT)

title_lb=Label(head_frame,text='Menu',bg='blue',fg='white',font="Helvetica 30 bold")
title_lb.pack(side=LEFT)
head_frame.pack(side=TOP,fill=X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)
#


#taking window exit confermation
def confirm_exit():
    result=messagebox.askokcancel(title="Exit",message="Do you want to exit ?")
    if result:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", confirm_exit)
#
root.mainloop()
