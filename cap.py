#Cap.py game file
import time
import os
print("You walk out of the theatre ,and feel like there is nothing to do, and you start walking down the road.")
time.sleep(4)
print ("As you start walking down the road you see someone get mugged and beaten up. you know what to do! Do you... ")
print ("""
1. run over and help?
2. finish the rest of the pop corn and enjoy the show?
3. go and get a coffee?
""")
choice = input("What do you do? ")
if choice == "3":
    print("You think that you should help, but you realy like coffee so you leave.")
    time.sleep(2)
    print("You make you way throught the hood untill you reach a cross road.")
    time.sleep(4)
    print("The pearson that you probably should have helped is probably dead by now due to the fact that you where the only one there to stop it but maybe you can still help them")
    print("""
1.GO back and help the person.
2.go left.
3.go right.
4.cotiune go forwards.
""")
    choice1=input("What to do")
    if choice==("1"):
        print("You sprint down the road back to the theatre but you are to late")
        print("#fail")
    print("YOU ARE DEAD, DEAD, DEAD! YOU ARE DEAD, DEAD, DEAD!  ")
if choice == "2":
    print("You just stand there and grab some  more popcorn and wait for it to end. ")
    time.sleep(4)
    print("Out of the corrner of his eyes he sees you standing there. You know what you've got your self into, As the look he gives you....")
    time.sleep(6)
    print("With a burning rage he punch you face and then kick you were it hurts. ")
    print("He contiues to beat you up and finily thorw you over to the bins. Out of the courner of your eyes you see a bin lid.What do you do...")
if choice == "1":
    print("You run towards the guy and shout stop.")
    time.sleep(2)
    print("He turns around a gives you the LOOK....")
    time.sleep(6)
    print("With a burning rage he punch you face and then kick you were it hurts. ")
    print("He contiues to beat you up and finily thorw you over to the bins. Out of the courner of your eyes you see a bin lid.What do you do...")
    time.sleep(2)
    choice1 = input("you know what to do")
    
    
