"""Practice with Functions."""

from random import randint

print(randint(3,17))

#with hashtag, can write comments that dont effect anything

#function definition
def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num2."""
    return num1 + num2

#function call
print(sum(num1=2,num2=13)) #<- arguments

