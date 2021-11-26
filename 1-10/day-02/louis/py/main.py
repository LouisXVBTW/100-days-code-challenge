import random
import time

def main():
    findNemo("I am finding Nemo !")


def findNemo(string):
    index = string.find("Nemo")
    print(("I found Neemo at " + str(index)) if index != -1 else "I can't find Nemo :(")




if __name__ == '__main__':
    main()
    