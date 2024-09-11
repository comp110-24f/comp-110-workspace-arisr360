"""My first Challenge Question in COMP110!"""
 
__author__ = "730769845"

def mimic(message:str) -> str:
   """should return message back to you!"""
   return message

def main() -> None:
    """pulls together my functions that implements the high-level logic of my program"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
  main()