# Toggle Dev Modes
devmode = True

# Import Packages
import os, sys
import time
import firebase_admin
from firebase_admin import credentials
from firebase import firebase

# Firebase Realtime Database Setup
if devmode == False:
	cred = credentials.Certificate("a-tale-of-fire-and-flames-firebase-adminsdk-kjo2l-978f1902e7.json")
	firebase_admin.initialize_app(cred)
	firebase = firebase.FirebaseApplication("https://a-tale-of-fire-and-flames-default-rtdb.firebaseio.com/", None)

# Load Item Charts
def load_item_list():
	file_character = os.open('data/character.json', os.O_RDONLY)
	list_character = os.read(file_character, 9999999)
	print(list_character)
	file_itemlist = os.open('data/itemlist.json', os.O_RDONLY)
	list_itemlist = os.read(file_itemlist, 9999999)
	print(list_itemlist)

def dev_load_item_list():
	file_character = os.open('dev_data/dev_character.json', os.O_RDONLY)
	list_character = os.read(file_character, 9999999)
	print(list_character)

# Database Send
if devmode == False:
	data_send = firebase.post('/', data)

# Clear Command
def clear():
	if sys.platform == "linux" or sys.platform == "Linux":
		os.system('clear')
	else:
		os.system('cls')	

# Main Run Loop
if __name__ == "__main__":
	print('Welcome to: "A TALE OF FIRE AND FLAMES"\nAn text-based MMORPG game to engage in quests and collect items to achieve victory against mobs and other players! Will you be the best?')
	time.sleep(3)
	clear()
	time.sleep(1)
	if devmode == True:
		load_item_list()
		dev_load_item_list()