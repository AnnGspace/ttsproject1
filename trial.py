from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pyttsx3
from googletrans import Translator

root = Tk()
root.title("Translator")
root.geometry("700x400")
root.resizable(width=False, height=False)

# Create language options for the Combobox
languages = LANGUAGES
language_options = ttk.Combobox(root, values=list(languages.values()))
language_options.grid(row=0, column=0, padx=5, pady=5)
language_options.set("English")

# Create a Text widget to get input text
input_text = Text(root, height=10, width=40, font=("Arial", 12))
input_text.grid(row=1, column=0, padx=5, pady=5)

# Create a Text widget to display the translated text
translated_text = Text(root, height=10, width=40, font=("Arial", 12))
translated_text.grid(row=1, column=1, padx=5, pady=5)

# Create a function to translate the text
def translate_text():
    text = input_text.get("1.0", "end-1c")
    destination_language = language_options.get()
    translator = Translator()
    translated = translator.translate(text, dest=destination_language)
    translated_text.insert("1.0", translated.text)

# Create a button to translate the text
translate_button = Button(root, text="Translate", command=translate_text)
translate_button.grid(row=0, column=1, padx=5, pady=5)

# Create a function to speak the translated text
def speak_text():
    engine = pyttsx3.init()
    text = translated_text.get("1.0", "end-1c")
    engine.say(text)
    engine.runAndWait()

# Create a button to speak the translated text
speak_button = Button(root, text="Speak", command=speak_text)
speak_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
