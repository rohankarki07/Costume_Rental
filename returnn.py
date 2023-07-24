import view
import update
import amount
import datetime
import convert
import math

ret = {"Costume Name":[], "Brand Name":[], "Per Piece Price":[]}
retprice = []
days = []


def validate():

    #id number of the costume
    while(True):
        try:
            cus_id=int(input("Enter Id of Costume you want to return: "))
            break
        except:
            print("\n Enter the input as integer.")
    while(True):

        if cus_id > 0 and cus_id <= len(convert.dic_costume):
            print("The Costume ID you returned is: ", cus_id)
            quantity = quantity = amount.quantity_val(convert.dic_costume,[cus_id])
            select_book=convert.dic_costume[cus_id]
            
            if int(select_book[3]) >= quantity:
                print("\n Amount of Returning Quantity is available. ")
                update_quantity=int(select_book[3])+quantity # adding costumes in the stock after returning
                select_book[3]=str(update_quantity) # uodate the stock
                
                print(convert.dic_costume) # print the dictionary
                price= str(select_book[2])
                price1= str(float(select_book[2].strip("$")))
                ret["Per Piece Price"].append(price)
                pri=float(price.replace("$",""))*quantity # replacing $ with empty space
                retprice.append(pri)
                ret["Costume Name"].append(select_book[0])
                ret["Brand Name"].append(select_book[1])
                take = int(input("Enter how much days ago u took the item: "))
                if take >= 5: # check weather the returning days is more than the date to return
                    totaldays = take-5
                    days.append(totaldays) # append the late days in the list created
                    
                
                print("\nThe pre piece price of the custome is: ",price)
           
        
        else:
            print("\n \tInvalid input")
            
        print("+++++++++++++++++++++++++++++++++")
        print("Do you want to return  another custome as well???")
        ans=input("Please enter 'y' to return other clothes else Enter any other variables: ").lower()        
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
        if ans == "y":
            # runs after the user input y 
            print("+++++++++++++++++++++++++++++++++++")
            print("\nLet's return a costume")
            print("\n+++++++++++++++++++++++++++++++++")
            update.update_stock() # call the function update_stock() from the module update
            view.view() # call the function validte view() form module view
            validate() # call the function validate()
            price2=str(float(price1)*quantity)

        else:
            abc = math.fsum(days) # sum all the late days appended to the list 
            #date and time latest
            cdt = datetime.datetime.now()

            y = str(cdt.year)
            m = str(cdt.month)
            d = str(cdt.day)
            h = str(cdt.hour)
            mi = str(cdt.minute)
            sec = str(cdt.second)
            nowtime = str(y + "-" + m + "-" + d + " " + h + ":" + mi + ":" + sec)

            name=input("\nEnter name of the customer: ") #asking name of the customer

            #making bill generate in txt file of returning
            p=str(y+m+d+h+mi+sec)
            j = open(p+"_return.text","w")
            j.write("\n--------------------------------------")
            j.write("\n \tBill Details")
            j.write("\n--------------------------------------")
            j.write("\n**************************************")
            j.write("\n"+"The name of customer is: "+name+"\n")
            j.write("\n"+"The Date and Time of return is "+nowtime+"\n\n")
            #j.write("\n"+"The Total Price of the Costume you returned is: "+str(float(price1)*quantity)+"\n"+"\n")
            for key,values in ret.items():
                        j.write('%s:%s\n\n' % (key, ",".join(values)))
            if take >= 5:
                    j.write("Fine amount is: $"+str(abc*10))
            else:
                j.write("Fine amount is $0.")
            j.write("\n**************************************")
            
            
        break

