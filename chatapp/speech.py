from gtts import gTTS
import os


def speak_text(text):
    tts = gTTS(text, lang='en', tld='com', slow=False)
    tts.save("response.mp3")
    os.system("mpg123 response.mp3")
