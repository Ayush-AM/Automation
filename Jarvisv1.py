from Engine.STT import STT
from Engine.TTS import TTS
from Brain.Brain import get_answer
import webbrowser
try :
    import pywhatkit as kt
except ModuleNotFoundError :
    import subprocess
    subprocess.run('pip install pywhatkit')
    import pywhatkit as kt


print("please press the key 1 or 2 to start jarvis input")
x = int(input())
if x == 1 :
    while True :
        text = input()
        if  "jarvis" in text.lower():
            text = text.replace("jarvis", "")
            text = text.replace("who is ", "")
            text = text.replace("what is ", "")
            TTS(get_answer(text))    
        if  "search in youtube" in text:
            text = text.replace("jarvis", "")
            text = text.replace("search in youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
        if  "on google" in text:
            text = text.replace("jarvis", "")
            text = text.replace("search in google", "")
            TTS("Searching about your requests sir")
            webbrowser.open(f"https://www.google.com/search?q={text}")
            TTS(f"You can see the search results about {text} on your screen.")             
        if "on youtube" in text:
            text = text.replace("music", "")
            text = text.replace("on youtube", "")
            text = text.replace("play", "")
            TTS(f"playing youtube video {text}")
            kt.playonyt(text)
            TTS("enjoy sir")
            

if x == 2:
    while True :
        text = str(STT()).lower()
        if  "jarvis" in text:
            text = text.replace("jarvis", "")
            text = text.replace("who is ", "")
            text = text.replace("what is ", "")
            TTS(get_answer(text))
        if  "search in youtube" in text:
            text = text.replace("jarvis", "")
            text = text.replace("search in youtube", "")
            TTS("Searching about your requests sir")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
        if  "on google" in text:
            text = text.replace("jarvis", "")
            text = text.replace("search in google", "")
            TTS("Searching about your requests sir")
            webbrowser.open(f"https://www.google.com/search?q={text}")
            TTS(f"You can see the search results about {text} on your screen.")            
        if "on youtube" in text:
            text = text.replace("music", "")
            text = text.replace("on youtube", "")
            text = text.replace("play", "")
            TTS(f"playing youtube video {text}")
            kt.playonyt(text)
            TTS("enjoy sir")