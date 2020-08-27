import time #These import the modules I have used throughout the program.
import os
import csv

def menu():#Function that displays the menu with numbers for use in if statements.
    print("\n1. Enter Airport\n2. Enter Flight Details\n3. Enter Price Plan and Calculate Profit\n4. Clear Data\n5. Quit")

def quit():#Function to quit the program.(I wrote this first, that is why it's only used once later in the program)
    print('Thank you for your time, we hope you enjoyed your experience with us and will return to work with us again in the future\nThis program will now close in 5 seconds')
    time.sleep(5)#Pauses for 5 seconds before ending the program.
    os._exit(0)#Ends the program(Although leaves the shell open if run from the code reading shell, works correctly if executed directly.) 

def repeater():#Begins the definition for the program's main body of code, used as a repeating loop, that only ends when quit() is run.
    global oac#Makes variables available through all of the functions being run
    global oan
    global dflpl
    global dfboh
    choice = 0#Resets the choice variable each time the function is run
    print('\nWhat would you like to do now?\nYou should follow the list in order(Apart from the clear data and quit options)')
    menu()#Displays the menu each time the function is run
    choice = input('Please enter the number of the option you wish to complete:\n')

    if choice == '1':#If statements to act as branches for the menu decision.
        global uk_A_code#Makes variables available through all of the functions being run
        global int_A_code
        global int_index
        print('You have chosen to enter the airport details:')
        uk_A_code = input('What is the airport code for the UK airport?\n')
        int_A_code = input('What is the airport code for the international airport?\n')
        if uk_A_code == 'LPL':#Only continues the program if the variable is "LPL" or "BOH"
            if int_A_code in oac:#Presence check to make sure the international airport code is valid using a list and then continues the program, if not it stops the branch and resets back to the first decision. 
                int_index = oac.index(int_A_code)#Makes a variable for the position in the list so that the same position can be applied to other lists, so that only the relavent information will be used later.
                print('Airport code entered:\n',int_A_code,'\nName of airport:\n',oan[int_index])
                repeater()#Keeps all variables and begins from the menu
        if uk_A_code == 'BOH':#Same as above
            if int_A_code in oac:
                int_index = oac.index(int_A_code)
                print('Airport code entered:\n',int_A_code,'\nName of airport:\n',oan[int_index])
                repeater()
            
        else:#If either the uk or the international code is invalid the program clears the variables and begins from the beginning again
            print('That airport code is invalid, you will be returned to the menu in a moment')
            uk_A_code = None#Returns the variable to an empty, un-formatted state
            int_A_code = None
            time.sleep(2)#Pauses for 2 seconds to allow the user to read the error message
            repeater()#Begins from the first decision
        

    if choice == '2':
        global fcs#Makes variables available through all of the functions being run
        global hoas
        global scs
        global aircraft
        global km_rcps
        global this_mfr
        global all_s
        global min_first
        global ac_index

        print('You have chosen to enter the flight details:')
        ac_index = input('Please type the bracketed initials of the aircraft types you will be flying in:\n1. medium narrow body(mnb)\n2. large narrow body(lnb)\n3. medium wide body(mwb)\n')
        if ac_index in ac_ints:#Checks if the three initials entered are valid and if they are continues the program.
            index = ac_ints.index(ac_index)#Checks the position of the input and uses the index number to set all the relavent data as variable for later
            aircraft = ac_type[index]#The next lines set the data for the aircraft type as variables and displays them.
            print('These are the full deatails of your aircraft:')
            print('Aircraft:\n:',aircraft)
            km_rcps = rcps[index]
            print('This is the running cost for a 100km per seat:\n£',km_rcps)
            this_mfr = mfr[index]
            print('This is the maximum flight range in km:\n',this_mfr)
            this_mfr = int(this_mfr)
            all_s = max_s_capacity[index]
            print('This is the capacity of the aircraft if all the seats are standard class:\n',all_s)
            min_first = min_f_s[index]
            print('This is the mimimum number of first-class seats(If there are any):\n',min_first)
            fcs = int(input('How many first class seats are there on the flight?\n'))#Forces an integer input to fix problem that occurred later
            if fcs >= 0:#Only continues the first class seat calculations if the number is higher than 0
                if fcs >= min_first:#Makes sure the amount of first class seats is greater than the minimum number of first class seats on this specific aircraft.
                    hoas = all_s/2#Calculates half of all seats if they were all standard class
                    if fcs < hoas:#Checks that the number of first class seats is less than half of the total seats available
                        minus = fcs*2#Number for use in next equation.
                        scs = all_s - minus#Calculates the number of standard seats by taking out the number of first class seats from the total seats on the aircraft
                        scs = int(scs)#Makes number into an integer to avoid issues later
                        repeater()#Begins from menu
                    else:#The two else statements remove the inputed number of first class seats and begins from the menu
                        print('Number of first class seats you entered is invalid, you will be returned to the menu in a moment')
                        fcs = None
                        time.sleep(2)
                        repeater()
                else:
                    print('The number of first class seats you entered is invalid, you will be returned to the menu in a moment')
                    fcs = None
                    time.sleep(2)
                    repeater()
            minus = fcs*2#Calculates the number of standard seats if there are no first class seats
            scs = all_s - minus#//
            scs = int(scs)#//
            repeater()#//

        else:#Stops the program, empties the variable and resets to menu
            print('The initials you entered are invalid, you will be returned to the menu in a moment')
            ac_index = None#//
            time.sleep(2)#//
            repeater()#//

    if choice == '3':
        print('You have chosen to enter the price plan and calculate the profit:\n\nWe are checking to make sure all required fields are present:\n')
        if uk_A_code is None:#The next lines check the required variables and if they are missing informs the user of the error and begins from the menu
            print('You have not entered one of the airport codes, please complete this before continuing.')
            print('You will be returned to the menu in a moment:\n')
            time.sleep(5)
            repeater()
        if int_A_code is None:
            print('You have not entered one of the airport codes, please complete this before continuing.')
            print('You will be returned to the menu in a moment:\n')
            time.sleep(5)
            repeater()
        if ac_index is None:
            print('You have not entered the aircraft type, please complete this before continuing.')
            print('You will be returned to the menu in a moment:\n')
            time.sleep(5)
            repeater()
        if fcs is None:
            print("You have not entered the aircraft's number of first class seats, please complete this before continuing.")
            print('You will be returned to the menu in a moment:\n')
            time.sleep(5)
            repeater()
        if uk_A_code == 'LPL':#Code repeats itself here depending on the uk airport
            if this_mfr > dflpl[int_index]:#Makes sure the distance to travel is within the maximum flight range of the aircraft
                print('Check complete: You have entered all of the relavent data correctly, we may now contine:')
                posc = int(input('Please enter the price of a standard class seat:\n'))
                pofc = int(input('Please enter the price of a first class seat:\n'))
                fcps = km_rcps * dfboh[int_index] / 100#Calculates the Flight cost per seats and holds it for later
                all_seats = fcs + scs#Calculates all seats, so that the next equation is not confused buy the multiple actions.
                fc = fcps * all_seats#Calculates the flight cost in total, using the supplied formula
                fip1 = fcs * pofc#First half of the flight income equation
                fip2 = scs * posc#Second half of the flight income equation
                fi = fip1 + fip2#Completes the flght income equation
                fc = int(fc)#Makes both variables into integers, to negate the 'float' - 'int' type error I recieved during testing
                fi = int(fi)
                fp = fi - fc#Calculates the flight profit
                print('This is the flight cost per seat of the flight:\n£',fcps)#These display all of the flight details
                print('This is the total flight cost:\n£',fc)
                print('This is the expected income of the flight:\n£',fi)
                print('This is the expected profit from the flight:\n£',fp)
                time.sleep(5)
                print('You will now be taken back to the menu, thank you for using our service, we hope to see you again:')
                time.sleep(3)
                repeater()
                                

            else:#Closes this branch and begins from the start again
                print("The information you have provided has shown that the flight range of the airctaft is less than the distance to be traveled, please run the clear data option and start again.")
                print('You will be returned to the menu in a moment:\n')
                time.sleep(5)
                repeater()

        if uk_A_code == 'BOH':#Beginning of the repeat of the code above.
            if this_mfr > dfboh[int_index]:
                print('Check complete: You have entered all of the relavent data correctly, we may now contine:')
                posc = int(input('Please enter the price of a standard class seat:\n'))
                pofc = int(input('Please enter the price of a first class seat:\n'))
                fcps = km_rcps * dfboh[int_index] / 100
                all_seats = fcs + scs
                fc = fcps * all_seats
                fip1 = fcs * pofc
                fip2 = scs * posc
                fi = fip1 + fip2
                fc = int(fc)
                fi = int(fi)
                fp = fi - fc
                print('This is the flight cost per seat of the flight:\n£',fcps)
                print('This is the total flight cost:\n£',fc)
                print('This is the expected income of the flight:\n£',fi)
                print('This is the expected profit from the flight:\n£',fp)
                time.sleep(5)
                print('You will now be taken back to the menu, thank you for using our service, we hope to see you again:')
                time.sleep(3)
                

            else:
                print("The information you have provided has shown that the flight range of the airctaft is less than the distance to be traveled, please run the clear data option and start again.")
                print('You will be returned to the menu in a moment:\n')
                time.sleep(5)
                repeater()#End of the repeat of the code above.

                
    if choice == '4':
        uk_A_code = None#Resets all relavent, global variables to be their empty state.
        int_A_code = None
        int_index = None
        ac_index = None
        aircraft = None
        km_rcps = None
        this_mfr = None
        all_s = None
        fcs = None
        scs = None
        hoas = None
        posc = None
        pofc = None
        fcps = None
        fip1 = None
        fip2 = None
        fi = None
        fp = None
        print('All inputed data has been reset, you will be returned to the menu in a moment:')
        time.sleep(2)
        repeater()
        
    if choice == '5':
        quit()#Runs the quit function and is the only way to end the loop
                
        
global oac#Makes variables available through all of the functions being run
global oan
global dflpl
global dfboh
global ac_type
global rcps
global mfr
global max_s_capacity
global min_f_s
global ac_index
global ac_ints
oac = []#Sets these as lists for the file reader
oan = []
dflpl = []
dfboh = []
ac_ints = ['mnb','lnb','mwb']#Custom lists for the aircraft details
ac_type = ['medium narrow body','large narrow body','medium wide body']
rcps = [8,7,5]
mfr = [2650,5600,4050]
max_s_capacity = [180,220,406]
min_f_s = [8,10,14]

from csv import reader#Imports a specific tool from the csv module that helps to read the .txt file
fp = open('Airports.txt')#Opens the file as a variable for use in the reader tool
csv_reader = reader(fp)#Reads the variable using the reader tool and sets it as a variable
for row in csv_reader:#Loop for as long as there are lines in the file
    if len(row) > 1:#Only runs the list append commands if there is an unread line in the variable
        oac.append(row[0])#Sorts the information from the .txt into lists by column, rather than by row, leading to the lists being based on the separate list headers, rather than by line
        oan.append(row[1])
        dflpl.append(row[2])
        dfboh.append(row[3])

dflpl = list(map(int, dflpl))#These two make the string values in the list into integers all at once, as you can't change each item individualally
dfboh = list(map(int, dfboh))

print("Welcome to our airline's flight planner and calculator")
repeater()#This is the first run of the function and is the real beginning of the loop based-program
