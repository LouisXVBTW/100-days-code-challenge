import os
import shutil

path = os.getcwd()

print (os.walk(path))
namedone=[]
listdays = 100
listing = [x[0] for x in os.walk(path)]
for paths in listing:
    currentday= 0
    for days in range(listdays):
        if days < 10:
            
            louisday = "day-0"+str(days+1)+"\\louis"
            blaizeday = "day-0"+str(days+1)+"\\blaize"
        else:
            louisday = "day-"+str(days+1)+"\\louis"
            blaizeday = "day-"+str(days+1)+"\\blaize"
        #print (louisday, blaizeday)
        if louisday in paths and louisday not in namedone:
            
            namedone.append(louisday)
            print (paths)
            gitkeep = paths+"\\.gitkeep"
            print (gitkeep)
            with open(gitkeep, 'w') as f:
                pass
            

            
        if blaizeday in paths and blaizeday not in namedone:
            
            namedone.append(blaizeday)
            print (paths)
            gitkeep = paths+"\\.gitkeep"
            print (gitkeep)
            with open(gitkeep, 'w') as f:
                pass
            
            
            
            #print (path)

            
            


#print (listing)

#os.mkdir(path, dayXX)

