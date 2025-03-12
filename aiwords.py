#an application to define any word.
import time
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet
import os


#The clear screen module
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    return "Your word not here...."

word=""
while word!="end":
    print("WELCOME TO AN APP THAT CAN DEFINE ANY WORD")
    print("=========================================")
    print()
    print()
    word=input("Enter a word to define below -> ")
    time.sleep(2)
    print("The word is you just entered is ->",word)
    time.sleep(2)
    print(f"The Word means: {get_word_meaning(word)}")
    time.sleep(3)
    print("To stop enter the word end")
    time.sleep(2)
    clear_screen()
