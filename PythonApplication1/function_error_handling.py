#def main():
#    printnames(getnames())
#    return

#def getnames():
#    names = ['a','b','c']
#    newletter = input('enter new letter')
#    names.append(newletter)
#    return names

#def printnames(names):
#    for name in names:
#        print(name)
#    return

#main()

import sys
fno  = input('Enter first no: ')
sno = input('enter the second no: ')
fno = float(fno)
sno = float(sno)
try :
    result = fno / sno
    print(result)
except ZeroDivisionError :
    print("The answer is infinity")
    sys.exit()
except :
    error = sys.exc_info()[0]
    print(" something went wrong ")
    print(error)
finally:
    print('i will always run')