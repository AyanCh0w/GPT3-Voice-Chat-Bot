import speech_recognition as sr
import openai
import pyttsx3
import os

openai.api_key = ""

engine = pyttsx3.init()

r = sr.Recognizer()

if openai.api_key == "":
    engine.say("You don't have your api key entered")
    engine.runAndWait()
    os._exit()


engine.say("Welcome to your virtual assistant")
engine.runAndWait()
engine.say("If you would like to exit the program, say exit")
engine.runAndWait()
engine.say("You may begin talking now")
engine.runAndWait()

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)

    prompt = r.recognize_google(audio, language="en-EN", show_all=False)

    print(prompt)

    if prompt == "exit":
        engine.say("exiting program")
        engine.runAndWait()
        break
    
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        responce = str(response["choices"][0]["text"])
        print(responce)

        engine.say(responce)
        engine.runAndWait()
    except:
        engine.say("Welcome to your virtual assistant")
        engine.runAndWait()
