import pyttsx3,PyPDF2
from datetime import date

# #pyttsx3 documentation: https://pyttsx3.readthedocs.io/en/latest/

# Function to extract the pdf-file
def extract_text(file):

    pdfreader = PyPDF2.PdfReader(open(file,'rb'))

    full_text = ""

    for page in range(len(pdfreader.pages)):

        text = pdfreader.pages[page].extract_text()
        legible_text = text.strip().replace('\n', ' ')
        full_text += legible_text

    return full_text

#takes the extraxted text from the function extract_text() and turns it into an audio-file
#to let the audio-file get stored on the local pwd, the text has to run completely throug

def make_audio(file, language, output_name):

    today = str(date.today())
    path = "../../00_docs/pdf_readins/" + file
    engine = pyttsx3.init()

    if language == "german":
        i = 0
    elif language == "english":
        i = 1
    else:
        print('please choose the language "english" or "german"!')

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[i].id)

    text = extract_text(path)

    print(text)

    engine.say(text)

    engine.save_to_file(text, today + "_" + output_name + '.mp3')

    engine.runAndWait()

    engine.stop()

make_audio('Exercise01.pdf', "english", "test")