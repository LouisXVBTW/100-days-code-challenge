import random

def main():
    makeSkewers([5,3])


def makeSkewers(types):
    skewers = []
    for i in range(types[0]):
        string = "--o"
        for i in range(5):
            string += random.choice(["-","o"])
        string += "--"
        skewers.append(string)
    string =""
    for i in range(types[1]):
   
        string = "--x"
        for i in range(5):
            string += random.choice(["-","x","o"])
        string += "--"
        skewers.append(string)
    print ("Skewers:\n")
    for i in skewers:
        print(i)


if __name__ == '__main__':
    main()