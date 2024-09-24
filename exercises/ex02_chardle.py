"""EX02 - Chardle - A cute step toward Wordle."""
 
__author__: str = "730769845"



def input_word()-> str:
    word: str=str(input("Enter a 5-character word: ")) #defining a word variable so user can input the word of their choice. 
    if len(word)==5: #making it so only if the length of the word is 5 that it will continue running. 
        # print("'"+word+"'")
        return word
    else:
        print("Error: Word must contain 5 characters.") #if the word doesnt equal 5, it will send you and error message and stop running. 
        # print("'"+word+"'")
        exit() #special built-in function called exit() that will send a signal to your system and tell the program to quit at that point, not continuing on further in the program
    


def input_letter()-> str:
    letter: str=str(input("Enter a single character: ")) #defining a letter variable so user can input the letter of their choice
    if len(letter)==1: #making it so only if they enter a single letter the code will continue running
        # print("'"+letter+"'")
        return letter
    else:
        print("Error: Character must be a single character.") #if the letter is not a single letter, it will print an error and stop running
        # print("'"+letter+"'")
        exit() #special built-in function called exit() that will send a signal to your system and tell the program to quit at that point, not continuing on further in the program. 
    


def contains_char(w:str,l:str)->None:
    count: int = 0 #making a count variable that will be added for each time the inputed letter is found in the inputed word
    if len(l) == 1:
        print("Searching for "+l+" in "+w) #printing searching letter in word if letter is a single character. 
    if l==w[0]:
            print(l+" found at index 0") #printing if character matches first letter of the word
            count += 1 #adding to count to be used later 
    if l==w[1]:
            print(l+" found at index 1") #printing if character matches second letter of the word
            count += 1 #adding to count to be used later 
    if l==w[2]:
            print(l+" found at index 2") #printing if character matches third letter of the word
            count += 1 #adding to count to be used later 
    if l==w[3]:
            print(l+" found at index 3") #printing if character matches fourth letter of the word
            count += 1 #adding to count to be used later 
    if l==w[4]:
            print(l+" found at index 4") #printing if character matches fifth letter of the word
            count += 1 #adding to count to be used later 

    if count == 0: #using count variable, if there is no value added that means the word does not contain that letter.
          print("No instances of " + l + " found in " + w) #printing statement above
    else:
        if count == 1: #if there is only one time the letter is in the word, it will print "instance" instead of "instances"
            print(str(count) + " instance of " + l + " found in " + w) #printing statement above
        else:
            print(str(count) +  " instances of " + l + " found in " + w) #if there are multiple times the letter is found in the word, it will use plural grammer:instances


def main()-> None: #function to call all other functions
    contains_char(w=input_word(),l=input_letter())

if __name__ == "__main__": #making it possible to run Python program as a module and making it possible for other modules to import functions and reuse them. 
    main()