import random

nemo = "Nemo"
count = 0


#chose a sentence for testing
nemotext = ["I am finding Nemo !","Nemo is me","I Nemo am", \
             "I am finding Nemo!","neMo is me", "i Nemo am Nemo", \
             "look at Nemo's"]
summonNemo = (random.choice(nemotext))
print (summonNemo)

#split and append to list then measure list length
splicingNemo = summonNemo.split()
nemoLen = len(splitNemo)

#if it finds the word nemo in list return ots first position then end
for z in splicingNemo:
    if z == nemo:
        findingNemo = splicingNemo.index(nemo)
        print (f"I found Nemo at {findingNemo + 1}!")
        break

#count how many times the word in the list isnt nemo
    if z != nemo:
        count += 1

#if amount of not nemo == length of the list. Nemo cannot be found :/
if count == nemoLen:
    print ("I can't find Nemo :(")
