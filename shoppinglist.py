import os,sys,time

sl = []
try:
	f = open("shopping2.txt","r")
	for line in f:
		sl.append(line.strip())
	f.close()
except:
	pass

def mainScreen():
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("     SHOPPING LIST    ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n\nYour list contains",len(sl),"items.\n")
	print("Please choose from the following options:\n")
	print("(1) Add to the list")
	print("(2) Delete from the list")
	print("(3) View the list")
	print("(4) Leave the program")
	choice = input("\nchoice: ")
	if len(choice) > 0:
		if choice.lower()[0] == "1":
			addScreen()
		elif choice.lower()[0] == "2":
			deleteScreen()
		elif choice.lower()[0] == "3":
			viewScreen()
		elif choice.lower()[0] == "4":
			sys.exit()
		else:
			mainScreen()
	else:
		mainScreen()
	

def addScreen():
    global sl
    os.system('cls')  # for Linux 'clear'
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("     ADD SCREEN    ")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("\n\n")
    print("Please enter the name of the item you want to add.")
    print("Press ENTER to return to the main menu.\n")
    item_name = input("\nItem name: ")
    if len(item_name) > 0:
        item_price = input("Item price: ")
        if len(item_price) > 0:
            item = f"{item_name} - ${item_price}"
            sl.append(item)
            print("Item added")
            saveList()
            time.sleep(1)
        else:
            print("Invalid input")
            time.sleep(1)
        addScreen()
    else:
        mainScreen()
	


def viewScreen():
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("     VIEW SCREEN    ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n\n")
	for item in sl:
		print(item)
	
	print("\n\n")
	print("Press enter to return to the main menu")
	input()
	mainScreen()
	

	
def deleteScreen():
	global sl
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("     DELETE SCREEN    ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	count = 0
	for item in sl:
		print(count, " - ", item)
		count = count + 1
	print("What number to delete?")
	choice = input("number: ")
	if len(choice) > 0:
		try:
			del sl[int(choice)]
			print("Item deleted...")
			saveList()
			time.sleep(1)
		except:
			print("Invalid number")
			time.sleep(1)
		deleteScreen()
	
	else:
		mainScreen()
		
def saveList():
		f = open("shopping2.txt", "w")
		for item in sl:
			f.write(item+"\n")
		f.close()
			
	
mainScreen()