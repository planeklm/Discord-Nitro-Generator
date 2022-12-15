#import necessary libraries
import random
import time
import winsound

#try to import colorama
try:
  import colorama
  from colorama import Fore
#if it fails, install it
except:
  print("Installing colorama...")
  import subprocess
  subprocess.call(["pip", "install", "colorama"])
  import colorama
  from colorama import Fore

#print the intro
print("NITRO GENERATOR")
time.sleep(2) #add a 2 second delay

#get the user input
num_codes = int(input("How many codes would you like to generate? "))

#define the function
def generate_nitro_code():
  
  #create a list of characters to make up the code
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
  
  #create an empty string to store the nitro code
  nitro_code = ''
  
  #loop through the characters and randomly select one for each iteration
  for i in range(16):
    nitro_code += random.choice(characters)
  
  #return the nitro code
  return nitro_code

#create a file to store the codes
f = open("nitro_codes.txt", "w+")

#call the function
for i in range(num_codes):
  code = generate_nitro_code()
  print(Fore.BLUE + "discord.gift/" + code) #print the code in blue
  f.write("discord.gift/" + code + "\n") #write the code to the file
  time.sleep(1) #add a 1 second delay

#play the sound
winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

#wait for user input
input(Fore.GREEN + "Press enter to finish...")

#close the file
f.close()