import os
import shutil

path = os.getcwd()

print (os.walk(path))
daysdone=[]
listdays = 100
listing = [x[0] for x in os.walk(path)]
for paths in listing:
    currentday= 0
    for days in range(listdays):
        if days < 10:
            
            theday = "day-0"+str(days+1)
        else:
            theday = "day-"+str(days+1)
        if theday in paths and theday not in daysdone:
            
            print (paths)
            readme = paths+"\\README.md"
            newfolder= path+"\\"+theday
              
            os.mkdir(path+"\\"+theday)
            shutil.copy(readme, newfolder)
            os.mkdir(path+"\\"+theday+"\\louis")
            os.mkdir(path+"\\"+theday+"\\blaize")
            
            print (path)
            daysdone.append(theday)
            
            


#print (listing)

#os.mkdir(path, dayXX)

