"""Practice with conditionals."""

def less_than_ten(num:int)-> None:
    """tell me if num is less than 10"""
    dub: int=num*2
    dub = dub -1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")
    

less_than_ten(num=3)


