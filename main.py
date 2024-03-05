print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

fist_quest = input('You are at a cross road, Where do you want to go? Type "left" or "right"\n')
fist_quest_lower = fist_quest.lower()

if fist_quest_lower == "left":
  second_quest = input('You come to a lake, There is an island in the middle of the lake, Typer "wait" to wait for a boat, Typer "swin" to swin across\n')
  second_quest_lower = second_quest.lower()

  if second_quest_lower == "wait":
    final_quest = input('You arrive at the island unharmed, There is a house with 3 doors, One red, one yellow and one blue, Which colour do you choose?\n')
    final_quest_lower = final_quest.lower()
    
    if final_quest_lower == "red":
      print("You open the red door, You see a red dragon, it put you on fire. Game Over")
    
    elif final_quest_lower == "yellow":
      bonus_quest = input("You open the yellow door, You see a room full of gold, it have a golden chest in the middle, Do you want to open the chest or take the gold?\n")
      bonus_quest_lower = bonus_quest.lower()
      
      if bonus_quest_lower == "chest":
        print("You decide to open the chest, When you touch the chest, it opened revealing to be a mimic, swallowing you. Game Over")
        
      elif bonus_quest_lower == "gold":
        print("You decide to take the gold, You take all and leave the room, teleporting you to the cross road, You exit the island alive. Fin")

      else:
        print("You decide to not take the Treasure, You turn around and leave the room, coming across a red dragon and a yeti, You get stabbed and burned by the two. Game Over")
    
    elif final_quest_lower == "blue":
      print("You open the blue door, You see a yeti, it throw a ice lance on you. Game Over")
    else:
      print("You decide to turn around and not enter any door, You exit the house and enconter a kraken, killing you on the spot. Game Over")
      
  else:
    print("You were killed by a shark")
    
else:
  print("You fell into a hole. Game Over ")