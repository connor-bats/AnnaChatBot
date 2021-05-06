from gtts import gTTS

import pyttsx3 as pt
import os
import datetime
from geopy.geocoders import Nominatim
import geocoder
import requests
import re
import wikipedia as wk
import requests
import urllib.response, urllib.parse
from bs4 import BeautifulSoup
import re
import subprocess
import webbrowser


api="1c7fb71632e2b9103f2f74babdb1aaed"








def speak(text):

    x = 1
    engine = pt.init()
    #text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."


    
    engine.setProperty('rate',135)

    voices = engine.getProperty('voices')
    if x == 1:
        engine.setProperty('voice', voices[3].id)
    else:
        engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()










def listen():
    import speech_recognition as sr
    r= sr.Recognizer()

    with sr.Microphone() as source:
        print("Speaking now ...")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print("You've Said this: {}".format(text))
            return text
        except:
            print("Sorry couldn't get you")
            return "Couldnot get you! Sorry!"
            
        










def getLocation():
    g = geocoder.ip('me')
    z = g.latlng
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(str(z[0]) + "," + str(z[1]))
    location = str(location)
    location = location.split(",")
    currentLocation = location[2]
    return currentLocation





def getWeather(sentence):


    api_key = api
    location=nounExtraction3(sentence)
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    if(len(location)==0):
        city_name = getLocation()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            z = x["weather"]
            weather_description = z[0]["description"]
            text = "The current weather is " + weather_description
            speak(text)
        else:
            speak("Not found")
    else:
        location=list(location)
        city_name = location[0]
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            z = x["weather"]
            weather_description = z[0]["description"]
            text = "The current weather is " + weather_description
            print(text)
            speak(text)
        else:
            speak("Not found")










def getTemprature(sentence):


    api_key = api
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    location=nounExtraction3(sentence)

    if(len(location)==0):
        city_name = getLocation()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"] - 273.15
            current_temperature = round(current_temperature, 2)

            text = "The temperature is " + str(current_temperature) + " " + "Degree Celsius "
            print(text)
            speak(text)
        else:
            speak("Not found")

    else:
        location=list(location)
        city_name = location[0]
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"] - 273.15
            current_temperature=round(current_temperature,2)
            text = "The temperature is " + str(current_temperature) + " " + "Degree Celsius "
            print(text)
            speak(text)
        else:
            speak("Not found")








def searchWikipedia(subject):
    try:
        result = wk.summary(subject, sentences = 2)
        speak(result)
    except:
        searchGoogle(subject)
        
        
        
        


def getDate(year, month, day):
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    text = "The date today is "+month_names[month-1]+" "+str(day)+", "+str(year)
    speak(text)











def getDatetime(flag):
    x = datetime.datetime.now()
    
    
    year = x.strftime("%Y")
   # print("year:", year)

    month = x.strftime("%m")
    #print("month:", month)

    day = x.strftime("%d")
    #print("day:", day)

    hr = x.strftime("%H")
    #print(type(hr))
    time = x.strftime("%M")
    #print("time:", time)
    hr = int(hr)
    
    if hr>12 and hr <=23:
        hr = hr - 12
        desg = "PM"
    elif hr == 0:
        hr = 12
        desg = 'AM'
    else:
        desg = "AM"
    
    if flag == 1:
        getDate(year, month, day)
    
    else:
        text = "The time is"+" "+str(hr)+" "+time+" "+desg
    
        speak(text)
    
    









def playYoutube(name):
    
    query_string = urllib.parse.urlencode({"search_query": name})
    url = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", url.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clipurl = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])


    print(clipurl)

    webbrowser.open_new_tab(clipurl)  
    
    




def searchGoogle(item):
    item=item.lower()
    string=item.replace('search ','')
    string = string.replace(' ', '+')
    print(string)
    url = 'https://google.com/search?q=' + string
    webbrowser.open_new_tab(url)











def searchAmazon(item):
    item=item.lower()
    string = item.replace('in amazon','')
    string=string.replace('amazon','')
    string=string.replace('search ','')
    string = string.replace(' ', '+')
    
    print(string)
    url = 'https://amazon.in/s?k=' + string
    webbrowser.open_new_tab(url)
    
    
    
    
    
    



def searchFlipkart(item):
    item=item.lower()
    string = item.replace('in flipkart','')
    string=string.replace('search','')
    string = string.replace(' ', '+')
    
    print(string)
    url = 'https://www.flipkart.com/search?q=' + string
    webbrowser.open_new_tab(url)
    








    




















import random

import json

import torch

from model import NeuralNet

from nltk_utils import bag_of_words, tokenize

import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')





def intentDetection(sentence):
    sentence = tokenize(sentence)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)
    
    
    output = model(x)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim = 1 )
    prob = probs[0][predicted.item()]
    
    #print(prob.item())
    
    return tag, prob.item()
    





with open('data/intents.json','r', encoding = 'mbcs') as f:
    intents = json.load(f)


FILE = 'chatter.pth'
data = torch.load(FILE)


input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']





model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()









import spacy
spacy_nlp = spacy.load("en_core_web_md")

spacy.load("en_core_web_md")

def nounExtraction(sentence):
    doc = spacy_nlp(sentence)
    
    
    
    return list(doc.noun_chunks)
    
    
   
    
from textblob import TextBlob

def nounExtraction2(sentence):
    blob = TextBlob(sentence)
    return blob.noun_phrases
    
    

def nounExtraction3(text):
    doc = spacy_nlp(text)
    named_entities = set()
    money_entities = set()
    organization_entities = set()
    location_entities = set()
    time_indicator_entities = set()
    
    for i in doc.ents:
        entry = str(i.lemma_).lower()
        text = text.replace(str(i).lower(), "")
        # Time indicator entities detection
        if i.label_ in ["TIM", "DATE"]:
            time_indicator_entities.add(entry)
        # money value entities detection
        elif i.label_ in ["MONEY"]:
            money_entities.add(entry)
        # organization entities detection
        elif i.label_ in ["ORG"]:
            organization_entities.add(entry)
        # Geographical and Geographical entities detection
        elif i.label_ in ["GPE", "GEO"]:
            location_entities.add(entry)
        # extract artifacts, events and natural phenomenon from text
        elif i.label_ in ["ART", "EVE", "NAT", "PERSON"]:
            named_entities.add(entry.title())
    
    
    return location_entities
    # print(f"named entities - {named_entities}")
    # print(f"money entities - {money_entities}")
    # print(f"location entities - {location_entities}")
    # print(f"time indicator entities - {time_indicator_entities}")
    # print(f"organization entities - {organization_entities}")





print("Let's chat. Say 'quit' to exit.")

while True:
    
    
    
    
    sentence = listen()
    if sentence == 'quit':
        break
    
    if sentence == 'Couldnot get you! Sorry!':
        continue
    
    
    tag, probItem = intentDetection(sentence) 
    
    
    if probItem > 0.75:
        if tag == 'weather':
            getWeather(sentence)
        
        
        
        
        
        
        
        
        
        
        elif tag == 'temperature':
            getTemprature(sentence)
        
        
        
        
        
        
        
        
        
        
        
        
        elif tag == 'music/video':
            print(tag)
            noun_set = nounExtraction(sentence)
            person = ['you', 'we', 'i', 'me', 'us', 'them']
            noun_set = [str(w) for w in noun_set]
            #print(type(noun_set[0]))
            noun_set = [w for w in noun_set if w not in person]
            
            try:
                query = noun_set[0]
                for w in range(1,len(noun_set)):
                    query = query + " " + noun_set[w]
                playYoutube(query)
            except:
                speak('Can you say the name clearly once again! ')
                
                
                
                
                
                
                
            
            
        elif tag == 'search':
            print(tag)
            noun_set = nounExtraction(sentence)
            person = ['you', 'we', 'i', 'me', 'us', 'them']
            noun_set = [str(w) for w in noun_set]
            #print(type(noun_set[0]))
            noun_set = [w for w in noun_set if w not in person]
            
            try:
                query = noun_set[0]
                for w in range(1,len(noun_set)):
                    query = query + " " + noun_set[w]
                searchWikipedia(query)
            except:
                speak('Can you say the name clearly once again! ')
                
                
                
                
                
                
                
                
        elif tag == 'search amazon':
            print(tag)
            noun_set = nounExtraction(sentence)
            person = ['you', 'we', 'i', 'me', 'us', 'them', 'amazon']
            noun_set = [str(w) for w in noun_set]
            #print(type(noun_set[0]))
            noun_set = [w for w in noun_set if w not in person]
            
            try:
                query = noun_set[0]
                for w in range(1,len(noun_set)):
                    query = query + " " + noun_set[w]
                searchAmazon(query)
            except:
                speak('Can you say the name clearly once again! ')
                
                
                
                
                
                
                
        elif tag == 'search flipkart':
            print(tag)
            noun_set = nounExtraction(sentence)
            person = ['you', 'we', 'i', 'me', 'us', 'them', 'flipkart']
            noun_set = [str(w) for w in noun_set]
            #print(type(noun_set[0]))
            noun_set = [w for w in noun_set if w not in person]
            
            try:
                query = noun_set[0]
                for w in range(1,len(noun_set)):
                    query = query + " " + noun_set[w]
                searchFlipkart(query)
            except:
                speak('Can you say the name clearly once again! ')
                
                
                
                
                
                
                
        elif tag == 'time':
            getDatetime(0)
            
            
            
            
            
            
            
        
        elif tag == 'goodbye':
            for intent in intents['intents']:
                if intent['tags'] == tag:
                    x=random.choice(intent['responses'])
            print(x)
            speak(x)
            break
        
        
        
        
        
        
        
        
        else:
            for intent in intents['intents']:
                if intent['tags'] == tag:
                    x=random.choice(intent['responses'])
                    print(x)
                    speak(x)
        
        
            
                
    
    
    
    
    
    
    else:
        print("Cannot understand")
        speak("Cannot understand")