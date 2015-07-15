#intend the print statement is imp. Also python is case sensitive hence if user 
#repies Yes it will not work
answer=input("Do you want express shipping")
if answer == "yes" :
    print("that will cost an extra 10$")
print("have a nice day")
    # if answer != "no" :

freeToaster=False
deposit = int(input("how much do you want to deposit"))
if deposit > 100 :
    print("Enjoy your day")
    freeToaster=True
else:
    print(" you need to deposit above 100")
print("have a nice day")
if freeToaster :
    print("you just recieved a free toaster")

#elif
team = input('enter your country team ').upper()
bestteam = input('enter your best team ').upper()
if team == 'INDIA' and \
    bestteam == 'AUSTRALIA' or bestteam == 'SRILANKA' :
    print("Best Team")
elif team == 'PAKISTAN' and bestteam == 'BANGLADESH' \
    or bestteam == 'INDIA' :
    print("Worst Team")
else:
    print("I have nothing to say here")

    