print('''
* TABLE GENERATOR *
''')

#outer while loop
while True:

#user's' input  

#float for avoiding error with decimals
    num = float(input("Which Number's table do you want? :   "))

#range formula    
    for i in range(1,11):
        print(f"{num:g} × {i} = {num * i:g}")
       #removes unnecessory decimal points

#inner while loop
    while True:
        again = input("Want any other number's table? [YES/NO]:                     ").upper()

        if again == "YES" or again == "Y":
            break
        elif again == "NO" or again == "N":
            exit()
        else:
             print( "**Type a Valid Answer**") #prevents error from invalid input
             
   