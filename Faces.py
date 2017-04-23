from PIL import Image
import requests
import json
import cognitive_face as CF
import os



#Subscription key for Face API.  Get from the Azure Face API in the Azure Portal.
key = 'Enter your key'


def create_person_group():
    #A Person Group is a logical group of people that you would want to detect in pictures, e.g., familiy members
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}'

    #Assign the name of the person group and give it a description
    persongroupid = 'enter the group id'
    userdata = 'enter a desciption for the person group'

    payload = {'name': persongroupid, 'userData':userdata}
    req = requests.put(serviceurlpersongroup, data = json.dumps(payload), headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key': key}, params = {'personGroupId':persongroupid})
    jinfo = req.json()
    print (jinfo)

  
def get_person_group():
    #Retrieve the elements in a Person Group.  
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}'
    persongroupid = 'enter the group id'
    req = requests.get(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'personGroupId' : persongroupid})
    jinfo = req.json()
    print (jinfo)

def create_person():
    #Create a person within the Person Group
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/persons'

    persongroupid = 'enter the group id'
    person = 'enter the persons name'
    description = 'enter a desciption of te person'

    payload = {'name':person,'userData':description}

    req = requests.post(serviceurlpersongroup, data = json.dumps(payload), headers = {'Content-Type':'application/json','Ocp-Apim-Subscription-Key': key}, params = {'personGroupId' : persongroupid})
    jinfo = req.json()
    print (jinfo)


def get_person_info():
    #Retrieve information on a person within a Person Group
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/persons/{personId}'
    persongroupid = 'enter person group id name'
    personid = 'enter person id assigned by azure face API'

    req = requests.get(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'personGroupId' : persongroupid, 'personId': personid})
    jinfo = req.json()
    print (jinfo)

def add_persisted_face():
    #Add a face to a person within a Person Group.  Send a picture of the person's face by specifying a file name path.
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces'
    persongroupid = 'enter person group id'
    personid = 'enter person id'
    userdata = 'enter description of picture'
    targetface = ''

    fname = 'enter file directory location'
    data = open(fname, 'rb')

    req = requests.post(serviceurlpersongroup, data, headers = {'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key': key}, params = {'personGroupId':persongroupid, 'personId':personid})
    jinfo = req.json()
    print (jinfo)


def delete_persisted_face():
    #Delete a face for a Person within a Person Group
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/persons/{personId}/persistedFaces/{persistedFaceId}'
    persongroupid = 'enter a person group id'
    personid = 'enter a person id'
    faceid = 'enter a face id'

    req = requests.delete(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'personGroupId':persongroupid, 'personId':personid, 'persistedFaceId':faceid})
    print (req.content)

def create_face_list():
    #Create a Face List
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}'

    facelistid = 'enter a face list name you want to create'
    name = 'Give the face list id a name'
    userdata = 'provide a description of the face list'

    payload = {'name': name, 'userData':userdata}
    req = requests.put(serviceurlpersongroup, data = json.dumps(payload), headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key': key}, params = {'faceListId':facelistid})
    print (req.content)

def list_face_lists():
    #List the faces in the Face List
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/facelists'
    req = requests.get(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key})
    jinfo = req.json()
    print (jinfo)

def add_face_to_list():
    #Add a face to a Face List.   Send a picture from a file location by specifying the location directory and file name path.
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}/persistedFaces'
    facelistid = 'face list id'
    userdata = 'give name to the picture with the face you want added'
    targetface = ''

    fname = 'file location of the picture with the face'
    data = open(fname, 'rb')

    req = requests.post(serviceurlpersongroup, data, headers = {'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key': key}, params = {'faceListId':facelistid, 'userData':userdata})
    jinfo = req.json()
    print (jinfo)

def list_faces_on_face_list():
    #list faces in the Face List
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}'
    facelistid = 'face list id'
    req = requests.get(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'faceListId':facelistid})
    jinfo = req.json()
    print (jinfo)

def delete_face_from_face_list():
    #Delete faces from a face list
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/facelists/{faceListId}/persistedFaces/{persistedFaceId}'
    facelistid = 'face list id'
    faceid = 'enter the face id of the face to delete'

    req = requests.delete(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'facelistid':facelistid, 'persistedFaceId':faceid})
    print (req.content)

def train_person_group():
    #Train a Person Group, so that Azure can identify these people on any pictures sent to Azure.
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/train'
    persongroupid = 'person group to train'
    req = requests.post(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'personGroupId':persongroupid})
    print(req.content)

def train_status_person_group():
    #Check the training status of the Person Group.   Face detection of a person Group cannot be executed unless the Person Group has been successfully trained
    serviceurlpersongroup = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/{personGroupId}/training'
    persongroupid = 'person group'
    req = requests.get(serviceurlpersongroup, headers = {'Ocp-Apim-Subscription-Key': key}, params = {'personGroupId':persongroupid})
    jinfo = req.json()
    print (jinfo)


def analyze_picture(fname):
    #Use the Analyze API to detect the caption, categories, and tags for the picture
    # Subscription Key for Computer Vision
    keyanalyze = 'enter azure key for computer vision API'

    serviceurlanalyze = 'https://westus.api.cognitive.microsoft.com/vision/v1.0/analyze' 
 
    data = open(fname, 'rb')

    reqs = requests.post(serviceurlanalyze, data, headers = {'Content-Type':'application/octet-stream', 'Ocp-Apim-Subscription-Key': keyanalyze}, params = { 'visualFeatures' : 'Description, Tags, Faces, Categories, Color'})
    jinfoanalyze = reqs.json()
    try:
        categories = jinfoanalyze['categories']
        tags = jinfoanalyze['description']['tags']
        caption = jinfoanalyze['description']['captions'][0]['text']
        captionconfidence = jinfoanalyze['description']['captions'][0]['confidence']
        faces = jinfoanalyze['faces']
    
        print('Inferred Caption: ', caption, '      Confidence: ', captionconfidence)

        for cat in categories:
            print ("Category: ", cat['name'], "    Score:", cat['score'])

        for tag in tags:
            print (tag) 
    except:
        print ("Could not discern image")



serviceurldetect = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
serviceurlidentify = 'https://westus.api.cognitive.microsoft.com/face/v1.0/identify'
picturedirectory = 'enter the directory with all the pictures'
facelist = list()


#Check to see if people are detected in each picture located within a directory of many pictures.  Use the Detect API
directory = input("Enter directory path of pictures: ")
for file in os.listdir(path = directory):
    fname = directory + file
    
    data = open(fname, 'rb')

    image = Image.open(fname)
    image.show()

    analyze_picture(fname)

    facelist.clear()
    
   
    req = requests.post(serviceurldetect, data , headers = {'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key': key}, params = {'returnFaceId': 'True', 'returnFaceLandmarks':'False', 'returnFaceAttributes':'emotion,gender,smile,age,facialhair,glasses'})
    jinfo = req.json()

    nbrfacesdetected = 0
    
    for item in jinfo:
        nbrfacesdetected = nbrfacesdetected + 1
        faceid = item['faceId']
        facelist.append(faceid)

        smile = item['faceAttributes']['smile']
        gender = item['faceAttributes']['gender']
        age = item['faceAttributes']['age']
        glasses = item['faceAttributes']['glasses']
        emotion = item['faceAttributes']['emotion']  
        #Find the emotion with the highest score.  Maximium value in the dictionary of values.
        v=list(emotion.values())
        k=list(emotion.keys())
        maxemotion = k[v.index(max(v))]
        emotionvalue = emotion[maxemotion]

    
        facialhair = item['faceAttributes']['facialHair']
    
        print ("Gender: ", gender, "    Age: ", age, "    Smile: ", smile, "    Emotion: ", maxemotion, "    Glasses: ", glasses)

    print ("Number of faces detected: ", nbrfacesdetected)

    #Check if people match persons in the people group, using the Identify API
    persongroupid = 'enter the person group id'
    confidencethreshold = 0.55

    payload = {'faceIds':facelist,'personGroupId': persongroupid, 'maxNumOfCandidatesReturned':5,'confidenceThreshold': confidencethreshold}
    req = requests.post(serviceurlidentify, data = json.dumps(payload)  , headers = {'Content-Type':'application/json','Ocp-Apim-Subscription-Key': key})
    jinfo = req.json()
    
    nbrgroupmembers = 0
    for item in jinfo:
        try:
            facematch = (item['faceId'])
     
            if len(item['candidates'])>0:
                nbrgroupmembers = nbrgroupmembers + 1
                groupmember = item['candidates'][0]['personId']
                matchconfidence = item['candidates'][0]['confidence']
                print("Face Match for: ", facematch, "      Group Member: ", groupmember, "      Confidence: ", matchconfidence)
        except:
            print("No group  members detected") 
            nbrgroupmembers = 0
            
    print ("Number of people from group detected: ", nbrgroupmembers)





