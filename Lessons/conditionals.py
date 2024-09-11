"""Practice with conditionals."""

def less_than_ten(num:int)-> None:
    """tell me if num is less than 10"""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")
    

less_than_ten(num=3)



def check_first_letter(word:str, letter:str)-> str:
    """tell me if first letter of word matches with letter"""
    if word[0]==letter:
        return "match!"
    else:
        return "no match!" 

print(check_first_letter(word=”happy”, letter=”h”))
print(check_first_letter(word=”happy”, letter=”s”)) 