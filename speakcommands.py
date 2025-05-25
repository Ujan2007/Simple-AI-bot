#for speaking + taking questions and commands


import requests
import pyttsx3
import xml.etree.ElementTree as ET
import song
import automation

engine = pyttsx3.init()
app_id = '83Y88Y-XKUKXY598Q'  # Make sure this is in quotes!
url = 'http://api.wolframalpha.com/v2/query'

def get_answer_from_wolfram(query):
    params = {
        'input': query,
        'format': 'plaintext',
        'output': 'XML',
        'appid': app_id
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return "Error contacting WolframAlpha."

    root = ET.fromstring(response.content)

    for pod in root.findall('.//pod'):
        if 'primary' in pod.attrib and pod.attrib['primary'] == 'true':
            plaintext = pod.find('.//plaintext')
            if plaintext is not None:
                return plaintext.text.strip()

    # Fallback to any non-empty pod
    for pod in root.findall('.//pod'):
        plaintext = pod.find('.//plaintext')
        if plaintext is not None and plaintext.text:
            return plaintext.text.strip()

    return "Sorry, I couldn't find a proper answer."




    
def yes():
    print("If you have a question, ask and put a ? at the end of it")
    engine.say("If you have a question, ask and put a question mark at the end of it")
    engine.runAndWait()
    engine.say("So what can I do for you?")
    print("So what can I do for you?")
    engine.runAndWait()

    ques = input()
    return ques

def question(ques):
    if "youtube" in ques.lower():
        print("Please wait, playing your video..")
        engine.say("Please wait, playing your video")
        engine.runAndWait()
        automation.yt(ques)  
        return
    elif(ques.lower() == "exit"):
        no()
    elif "song" in ques:
        song.music(ques)    
    elif ques.strip().endswith("?"):
        answer = get_answer_from_wolfram(ques)  
        print(answer)
        engine.say(answer)
        engine.runAndWait()
        print("Do you want to use Jarvis again? Press S if yes")
        engine.say("Do you want to use Jarvis again? Press S if yes")
        engine.runAndWait()
        o = input()
        if o.upper() == "S":
            new_ques = yes()
            question(new_ques)
        else:
            no()
    else:
        print("That is not a question or a command try again. You may write exit and exit the program")
        engine.say("That is not a question or a command try again. You may write exit and exit the program")
        engine.runAndWait()
        new_ques = yes()
        question(new_ques)

def no():
    print("Goodbye, have a good day!")
    engine.say("Goodbye, have a good day!")
    engine.runAndWait()

# To start the interaction:
if __name__ == "__main__":
    ques = yes()
    question(ques)