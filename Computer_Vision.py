import requests
import json
from PIL import Image

#URL to access Azure Computer Vision
serviceurlanalyze = 'https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze' 


# Subscription Key for Computer Vision
key = 'Enter your subscription key for Computer Vision API'


def analyze_print(jinfo):
    #Decode the JSON from the API call        
    categories = jinfo['categories']
    tags = jinfo['description']['tags']
    caption = jinfo['description']['captions'][0]['text']
    captionconfidence = jinfo['description']['captions'][0]['confidence']
    faces = jinfo['faces']
    
    print ("")
    print ("")

    print('Inferred Caption: ', caption, '      Confidence: ', captionconfidence)

    for item in categories:
        print (item)

    for item in tags:
        print (item)

    for item in jinfo['faces']:
        print ('Age: ', item['age'], '      Gender: ', item['gender'],  'Left position: ', item['faceRectangle']['left'])

    for item in jinfo['faces']:
        print (item)


while True:
    #call the Azure computer vision API by sending a URL of a picture image, or by sending an image file to the API
    print ("")
    print ("")
    print ("1) Send URL")
    print ("2) Send image file")
    print ("3) Quit")
    selection = input ("Type the number of your selection: ")

    if selection == str(1):
        urlImage = input("Enter URL for picture: ")
        payload = {'url': urlImage}
        req = requests.post(serviceurlanalyze, data = json.dumps(payload), headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key': key}, params = {'visualFeatures' : 'Description, Tags, Faces, Categories, Color'})
        jinfo = req.json()
        analyze_print(jinfo)
 
    elif selection == str(2):
        fname = input("Enter file location and name: ")
        picturefile = open(fname, 'rb')
        data = picturefile
        req = requests.post(serviceurlanalyze, data, headers = {'Content-Type':'application/octet-stream', 'Ocp-Apim-Subscription-Key': key}, params = { 'visualFeatures' : 'Description, Tags, Faces, Categories, Color'})
        jinfo = req.json()
        analyze_print(jinfo)
        image = Image.open(fname)
        image.show()


    elif selection == str(3):
        quit()
    else:
        continue   

   

