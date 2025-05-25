import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio_text = r.listen(source)

        try:
            result = r.recognize_google(audio_text).strip()
            print(f"You said: {result}")
            return result
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google.")
            return ""


   

# Reading Microphone as source


    
    

