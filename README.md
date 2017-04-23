Repository Name = AzureCognitiveServicesPython
Sample code for accessing Azure Cognitive Services
The python scripts in this repository can be used to call Microsoft's Azure Cogniive Services API's
The scripts assume the that the developer has setup an Azure account and has Keys to the API's, which can be created in the Azure portal

There are scripts for:
1)  Text Analysis and Translation API's.    This script will take a string of text and
  a) Translate it from one language to another language
  b) Determine the 'Sentiment' score, which ranges from 0 to 1. The lower the number, the more negative the score.  The higer the more positive
  c) Determine the 'Key Words' in a string of text, i.e., find the main subjects of in the text
 
2) Computer vision API.  This script will identify objects in a picture image.  The user can either send an image file to the API or send a URL.
3) Face API.  This script reads picture images from a file directory and sends to the Face API. 
   Azure will identify faces in the image and will assess whether any faces match a faces in a Face Group
   Azure will also provide information about the faces in the picture.
      Age:  Estimated age of the person
      Gender:  Male or Female
      Smile: This is a number score.  The higher, the more the person is smiling
      Emotion: This is the dominant emotion detected for the person based on a numeric score assigned to different emotion types
      Glasses:  Whether the person is wearing glasses or not
   This script will also determine how many faces are in the picture and whether any match faces in "Person Group ID". 
   A confidence level is provided on any face match.
   
   Azure Face API allows the developer to setup faces that Azure can be 'trained' to detect.  To do this
      1) Create a person id
      2) Add a 'persisted' face to the person by sending a picture of this person to the API.   
  
   Assign person id's to a Person Group.  This is a logical group of people, e.g., family members
   Once a person group is created and person's are assigned with persisted faces, you can 'Train' the Person Group.
   Training allows azure to identify known people in the Person Group if any pictue with these people is sent to Azure
   
   As an alternative to setting up a Person Group, the developer can create Face Lists.  This is similar to Person Groups, but does not need training.
    
   
