import rent
import view
import returnn
def funct():
    # welcome message is generated
    print("*************************************")
    print("Welcome to costume rental Application")
    print("*************************************")
    
    while(True):
        
        print("\nSelect your desirable option")
        print("(1) || Press 1 for viewing a costume.")
        print("(2) || Press 2 for renting a costume.")
        print("(3) || Press 3 for returning a costume.")
        print("(4) || Press 4 to exit from the application.")
        #try except for selecting the option
        while(True):
            try:
                choose=int(input("\nEnter your option: "))
                break
            except:
                print("\nEnter valid option.")
        if choose==1:
            print("\nLet's view the costume")
            view.view() 
        elif choose==2:
            print("\nLet's rent the costume")
            view.view()
            rent.validate() # validate funtion is called from the rent module
        elif choose== 3:
            print("\nLet's hand back the costume.")
            view.view()
            returnn.validate() # validate funtion is called from the module returnn
        elif choose== 4:
            print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n \tThank you for using our Application || Have a good Day:) \n")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            break
        else:
            print("\n\tInvalid input!!!!")
            print("\n\tPlease Select the value as per the provided option.")
            
funct()

