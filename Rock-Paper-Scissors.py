import random
Choices = ['rock','paper','scissors'] 

def rps():
        while True:
                Value_User = input('What would you wanna pick (rock/paper/scissors/quit): \n') # input 
                if Value_User in Choices: # Checking valid choice
                        sys_choice = Choices[random.randint(0,2)]
                        print('System choice is :', sys_choice)
                        while True:
                                if (Value_User == sys_choice):
                                        print('Draw!')
                                        break
                                else: 
                                        while True:
                                                if (Value_User in ['scissors']) and (sys_choice in ['paper']):
                                                        print('You won!') #User wins
                                                        return False
                                                elif (Value_User in ['scissors']) and (sys_choice in ['rock']):
                                                        print('You lost!')
                                                        return False
                                                elif (Value_User in ['rock']) and (sys_choice in ['paper']):
                                                        print('You lost!')
                                                        return False
                                                elif (Value_User in ['rock']) and (sys_choice in ['scissors']):
                                                        print('You won!')
                                                        return False
                                                elif (Value_User in ['paper']) and (sys_choice in ['rock']):
                                                        print('You won!')
                                                        return False
                                                elif (Value_User in ['paper']) and (sys_choice in ['scissors']):
                                                        print('You lost!')
                                                        return False

                elif Value_User in ['quit']:
                        print('Thanks For Playing')
                        return False
                else: 
                        print('Please enter reasonable input please.') #Asking for re-input 

def Run_Code():
        rps()
        retry = input('Want to play again?(y/n): \n') #Asking for retry 
        while retry in ['y']:
                rps()
        else:
                exit 

Run_Code()