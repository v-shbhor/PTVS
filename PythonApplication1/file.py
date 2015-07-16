#filename = 'demo1.csv'
#write = 'w'
#append = 'a'
#readwrite = 'w+'
#file = open(filename,write)
#file.write("Susan, 29 \n")
#file.writelines("Shailesh, 34")
#file.close()

#READ FILE
#animalFile = open("abc.txt","r")
#allfileCOntents = animalFile.read()
#print(allfileCOntents)

#READ CSV file , the below method "with" -- "as"  helps u to close the file even in  worst condition.
#similar to using in .net
import csv
with open("abc.txt","r") as animalFile:
    allrowlist = csv.reader(animalFile)
    
    #for currentrow in allrowlist:
    #    print(currentrow)
    #    for currentword in currentrow:
    #        print(currentword)

    for currentrow in allrowlist:
        print(','.join(currentrow))



