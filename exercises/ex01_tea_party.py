"""Tea Party!"""
 
__author__: str = "730769845"


def main_planner(guests:int) -> None: #doesnt need return statement in body because return value is None. also the : after the return type if very important... 
    """calls each function and produces printed output"""
    print("A Cozy Tea Party for " + str(guests) + " People!") #must turn everything in print statement into strings to match eachother. also, have to use + to combine strings. also, have to take into account spaces by adding them into the "".
    print("Tea Bags: " + str(tea_bags(people=guests))) #in tea_bags, people comes first because it is a parameter of tea_bags. it cant be guests=people
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))))  #when calling a function, must define all parameters of that function with the parameter of that function=smth. can get complicated when calling a function within a funciton within a function


def tea_bags(people: int) -> int:
    """to computre the number of tea bags needed based on number of guests"""
    return people*2


def treats(people:int) -> int:
    """to compute the number of treats needed based on the number of teas guests are expecting to drink"""
    return int(tea_bags(people=people)*1.5) #turn into int bc return type is int. 


def cost(tea_count:int,treat_count:int) -> float:
    """to compute the cost of the tea bags and the treats combined"""
    return tea_count*0.50 + treat_count*0.75 #doesnt need to call any other functions, went through a couple tries to understand that one. 


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
