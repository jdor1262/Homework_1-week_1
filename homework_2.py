## 2. Course Score Calculation

on = True

while on: 
    
    nm = input('\nPlease put the name: ').upper()
    print("\n Welcome", nm)

    asgt_1 = float(input('\nPlease put the score of Assignment 1: '))
    asgt_2 = float(input('\nPlease put the score of Assignment 2: '))
    asgt_3 = float(input('\nPlease put the score of Assignment 3: '))
    asgt_4 = float(input('\nPlease put the score of Assignment 4: '))
    
    score = ((asgt_1+ asgt_2 + asgt_3 + asgt_4)/4)*(0.10)

    print('***'*10)
    tst_1 = float(input('\nPlease put the score of test 1: '))
    tst_2 = float(input('\nPlease put the score of test 2: '))

    score = (score + ((tst_1 + tst_2)/2)*(0.70)) 

    print('***'*10)
    lbw_1 = float(input('\nPlease put the score of Lab-Work 1: '))
    lbw_2 = float(input('\nPlease put the score of Lab-Work 2: '))

    score = round((score + ((lbw_1 + lbw_2)/2)*(.20)), 2 )

    print('***'*10)

  
    if score >= 90 :
        print(f"\nThe score:  {score} is 'A' ")
    elif score >= 80 : 
        print(f"\nThe score:  {score} is  'B' ")
    elif score >= 70 :
        print(f"\nThe score:  {score} is 'C' ")
    elif score >= 60 :
        print(f"\nThe score:  {score} is 'D' ")
    print('\n')

    std = ""
    
    std = [nm,score]

    print(std,'\n')
    
    cont = True
    while cont != "y" or cont != "n":
        cont = input ( "Do you want to continue ? ( 'y' / 'n' ): ").upper()
        if cont == "Y" or cont== "YES":
            print()
            break
        if cont == "N" or cont== "NOT":
            on = False
            break

print('\n bye')