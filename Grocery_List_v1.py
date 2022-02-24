import csv
from twilio.rest import Client
#   To begin the program with a main menu we start
#   with a list of choices
def File_write(File,food):
    outputFile = open(File,'a',newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(food)
    outputFile.close()



    
while(True):
    print('Welcome to the grocery list.')
    print("Please select an option by entering ")
    print('a number corresponding to your choice')
    print('')
    print('1. Add a list to your menu')#choice 1 will be creating a new string
    print('2. Send a grocery list')#choice 2 will be making a grocery list and sending it
    print('3. Exit the program')

    choice = input()
    templist = ['placeholder']#reset the list
    n=0#set the counter to 0 so user can add more than one recipe per program 
    if choice == str(1)or choice =='one':#create function to add food
      print('Write in the title of your recipe')  
      templist[0] = input()
      print('Now please write in each ingredient once at a time and press enter')
      print("When you are finished, write 'done'")
      n=0#set the counter to 0 so user can add more than one recipe per program run
      while(True):
          ch = input()
          if ch=='done' or ch=='Done' or ch=='DONE':
              
              File_write('grocery_list.csv',templist)
              print(templist)
              break
          elif ch!='done' or ch!='Done' or ch!='DONE':
              print(ch)
              n=n+1
              templist.append(ch)
          else:
              print('something went wrong')
              break
              
          
          
    elif choice == str(2)or choice =='two':
        message_string = ''
        while(True):
            exampleFile = open('grocery_list.csv')
            exampleReader = csv.reader(exampleFile)
            print('Enter the number corresponding to the recipe you want to add')
            for row in exampleReader:
                print('#'+str(exampleReader.line_num)+' '+str(row))
            print('Enter the number corresponding to the recipe you want to add')
            choice = input()
            if choice == 'exit':
                break
            elif choice == 'send' or choice == 'Send':
                print('set up twilio to get your code to text you the list')
                #Once you set up a twilio accout(free version works)
                #you can uncomment the following 
               # accountSID = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
                #authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
                #twilioCli = Client(accountSID,authToken)
                #my_twilio_number = 'xxxxxxxx'
                #my_cell_phone = 'xxxxxxxxxx'
                #message = twilioCli.messages.create(body=message_string,from_= my_twilio_number,to=my_cell_phone)

                break
            exampleFile = open('grocery_list.csv')
            exampleReader = csv.reader(exampleFile)
            for row in exampleReader:
                if choice ==str(exampleReader.line_num):
                    print(row)
                    for i in range(len(row)):
                        message_string = message_string+str(row[i])+'\n'
                        print('')
                    print(message_string)
            print('')
            print('One more meal has been added to your grocery list.')
            print('When you are finished, type Send.')
            print("If you'd like to cancel the list, type cancel.")
            print('')
            print('')
    elif choice == str(3)or choice =='three':
        print('Have a nice day! Goodbye!')
        break
    else:
        for i in range(30):
            print('')
        print('You did not choose an option')
        print('')


