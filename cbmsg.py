#!/usr/bin/env python3
print (" BY CHRIST BOWEL ")
print ("github.com/christbowel")


import requests
import json
import datetime 
   
#debut 

num = input("Entrer le numero avec le code du pays : ")
msg = input(" Entrez votre message : ")

#envoi du message 

resp = requests.post('https://textbelt.com/text',{
      'phone' : num ,
      'message' : msg ,
      'key' : 'textbelt'
})

print(resp.json())

print ("heure d'envoi : ", datetime.datetime.now())

print ("thanks for using | by christ bowel ")


