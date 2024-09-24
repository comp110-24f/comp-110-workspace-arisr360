"""CQ03 - While Loops"""

__author__ = "730769845" 



def num_instances(phrase: str, search_char: str) -> None: 
    count=0 #starting at count=0 bc we are starting at no searched characters in the phrase
    index=0 #index starts at 0 bc we want to start checking at the first letter
    while index < len(phrase): #condition is if the number of letters in the phrase is less than the index bc we want to check each character 
        if search_char == phrase[index]: #to check if the character we are looking for is in the phrase
            count += 1 # += is the same thing as saying count=count+1. if there is a charater we are looking for in the phrase, we need to increase the count
        index += 1 # += is the same thing as saying index=index+1. for the next loop, we want to change the index to check the the next letter so we can check one by one
    print(count) #print in the func body bc coubnt is a local variable

num_instances(phrase="HelloHeLloHEllo", search_char="e")
num_instances(phrase="HelloHelloHello", search_char="e")
num_instances(phrase="Happy Tuesday!", search_char="y")
num_instances(phrase="Happy Tuesday!", search_char="z")
