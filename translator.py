from tkinter import *
from googletrans import Translator

def translate_text():
    # Get the text to be translated and the destination language from the user interface
    text_to_translate = text_input.get(1.0, END).strip()
    destination_language = language_options.get()

    # Translate the text using Googletrans
    translator = Translator()
    translated = translator.translate(text_to_translate, dest=destination_language)

    # Set the translated text in the output area
    translated_output.delete(1.0, END)
    translated_output.insert(END, translated.text)

# Set up the main window and UI widgets
root = Tk()
root.title("Googletrans Translator")

text_input = Text(root, height=10, width=50)
text_input.grid(row=0, column=0, padx=10, pady=10)

language_options = ttk.Combobox(root, values=['en', 'es', 'fr', 'ja'])
language_options.current(0)
language_options.grid(row=0, column=1, padx=10, pady=10)

translate_button = Button(root, text="Translate", command=translate_text)
translate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

translated_output = Text(root, height=10, width=50)
translated_output.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
