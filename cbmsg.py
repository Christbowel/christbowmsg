#!/usr/bin/env python3
import pyfiglet
import requests
import json
import datetime
ascii_text = pyfiglet.figlet_format("christbowmsg", font="starwars")
ascii_text += "\n\033[38;2;255;153;51m\033[2mby christbowel\033[0m"
print(ascii_text)
 
   
#debut 

num = input("Entrer le numero avec le code du pays (exemple: +237671234567) : ")
msg = input(f"\033[34mVueillez Saisir Votre Message: ")


#envoi du message 

resp = requests.post('https://textbelt.com/text',{
			'phone' : num,
			'message' : msg ,
			'key' : 'textbelt'
		})
print(resp.json())

print ("heure d'envoi : ", datetime.datetime.now())

print ("thanks for using | by christ bowel ")

