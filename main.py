import os, time, sys

def load_item_list():
	file_character = os.open('data/character.json', os.O_RDONLY)
	list_character = os.read(file_character, 9999999)
	print(list_character)
	file_itemlist = os.open('data/itemlist.json', os.O_RDONLY)
	list_itemlist = os.read(file_itemlist, 9999999)
	print(list_itemlist)

def clear():
	if sys.platform == "linux" or sys.platform == "Linux":
		os.system('clear')
	else:
		os.system('cls')	

if __name__ == "__main__":
	print('Welcome to: "A TALE OF FIRE AND FLAMES"\nAn text-based MMORPG game to engage in quests and collect items to achieve victory against mobs and other players! Will you be the best?')
	time.sleep(3)
	clear()
	time.sleep(1)
	load_item_list()