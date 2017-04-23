import requests
import json
import re

#This python script will perform 3 text related functions in Azure Cognitive Services.
#  1) Language Translation for a string of text
#  2) Sentiment Analysis for a string of text
#  3) Key Word identification from a string of text


def sentiment():
    # This function will call the azure services API to determine a sentiment analysis score for a string of text
    # The API will assign a score from 0 to 1.   The lower the number, the more negative the sentiment.  The higher the number the more positive the sentiment score.
    # Get your Text Analysis API Key from the Azure portal and assign to the 'key' variable below.

    key = 'enter your azure key for Text Analysis'
    serviceurl = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

    while True:
        text = input("Enter a phrase to test sentiment, or type 'Q' to quit: ")

        if text == 'Q' or text == 'q':
            quit()
        elif len(text) > 0:
            jsontext = '{"documents":[{"id":"1","text":"' + text + '"},]}'
            req = requests.post(serviceurl, jsontext, headers = {'Ocp-Apim-Subscription-Key': key, 'Content-Type':'application/json'}, params = {'numberOfLanguagesToDetect':'1'})
            jinfo = req.json()
            score = jinfo['documents'][0]['score']
            print ("")
            print ('Sentiment Score: ', score, '    Phrase: ', text)
            print ("")
        else:
            continue



def text_translate():

    # This function will translate a string of text from one language to another language.
    # you must get a token from Azure to use the text translate API.   You can run 10 translations per token.  This script will get a new token for each string of text.
    # Get your Text Translate API Key from the Azure portal and assign to the 'key' variable below.

    tokenurl = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'

    serviceurl ='https://api.microsofttranslator.com/v2/http.svc/Translate'

    key = 'enter your key from Azure Portal for the Text Translate API'

    while True:
        print ("1) Chinese Simplified")
        print ("2) Chinese Traditional")
        print ("3) French")
        print ("4) German")
        print ("5) Hindi")
        print ("6) Korean")
        print ("7) Spanish")
        print ("8) English")
        print ("7) Quit")

        selection = input("Enter the Number code above of the language you want to translate into: ")
        language = int(selection)
  
        if language == 1:
            to_language = 'zh-CHS'
        elif language == 2:
            to_language = 'zh-CHS'
        elif language == 3:
            to_language = 'fr'
        elif language == 4:
            to_language = 'de'
        elif language == 5:
            to_language = 'hi'
        elif language == 6:
            to_language = 'ko'
        elif language == 7:
            to_language = 'es'
        elif language == 8:
            to_language = 'en'
        elif language =='Q' or language == 'q':
            quit()
        else:
            print("Enter a valid number of a language: ")
            continue

        while True:
            print ("")
            print ("")
            text = input("Enter a phrase you want translated or type 'Q' to quit: ")
    
            if text == 'Q' or text == 'q':
                quit()
            elif len(text) > 0:
                #Get Token, good for 10 min of translations
                req = requests.post(tokenurl, headers = {'Ocp-Apim-Subscription-Key': key})
                resp = req.text
                token = "Bearer" + " " + resp
                #print (token)
  
                #Call the Azure service for tranlation
                req = requests.get(serviceurl, headers = {'Ocp-Apim-Subscription-Key': key, 'Authorization':token}, params = {'text':text, 'to':to_language, 'Content-Type':'text/plain'})
                resp = req.text
                string = 'Serialization/">(.+?)<'
                results = re.findall(string, resp) 
                print ("Translation: ", results[0])
                print ("Text Provided:", text)

            else:
                continue

def key_word():
    # This function will identify the key words in a string of text.
    # Get your key from the azure portal for Text Analysis API. 

    serviceurl = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases' 
    key = 'enter your azure key for Text Analysis'
    language = 'en'
    textfilelocation = input("Type directory location of text file:  ")
    textfile = open(textfilelocation, 'r').read()
    text = ''
    counter = 0
    
    for letter in textfile:
        lettertest = str(letter)
        if lettertest.isalpha() or lettertest == " ": 
            counter = counter + 1
            text = text + lettertest
        if counter > 4999:
            break

    jsontext = '{"documents": [{"language":"'  + language + '","id": "1" ,"text":"' + text + '"}]}'

    req = requests.post(serviceurl, jsontext, headers = {'Ocp-Apim-Subscription-Key': key, 'Content-Type':'application/json'})
    jinfo = req.json()
#    print (jinfo)
    print ("")
    print ("Key words for the first ", counter, " letters of text:")
    for item in jinfo['documents'][0]['keyPhrases']:
        print (item)
    print ("")
    print ("")

while True:
    # Select which API you want to use.
    print ("1) Language Translation")
    print ("2) Sentiment Analysis")
    print ("3) Key word identification")
    print ("4) Quit")

    selection = input("Enter the Number code above of the language you want to translate into: ")
    choice = int(selection)
  
    if choice == 1:
        text_translate()
    elif choice == 2:
        sentiment() 
    elif choice == 3:
        key_word()
    elif choice == 4:
        quit()


