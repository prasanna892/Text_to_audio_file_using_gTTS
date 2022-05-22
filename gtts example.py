from gtts import gTTS
import os

outfile = input("enter_file_name.extinsion: ")
text = input("Enter your text here: ")
language = input("Enter your language (eg -> 'en-US'): ")

obj = gTTS(text=text, lang=language, slow=False)

obj.save(outfile) # saving file

os.system(outfile) # playing audio file