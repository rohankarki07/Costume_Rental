import view
import update
import datetime
import convert
import amount

#creating dictionary and list ofr later for appending the values
Bill = {"Costume Name":[], "Brand Name":[], "Per Piece Price":[]}
tprice = []

def validate():
    while(True):
        #try except for the string value check in the costume renting.
        try: 
            cus_id=int(input("Enter Id of Costume you want to rent: "))
            break
        except:
            print("\n Enter the input as integer.")
            
    while(True):
        if cus_id > 0 and cus_id <= len(convert.dic_costume):
            print("The Costume ID you rented is: ", cus_id)
            print("++++++++++++++++++++")
            print("\nCostume is available in the stock.")
            print("\n++++++++++++++++++++++")

             # call the module convert for the quantity
            quantity = amount.quantity_val(convert.dic_costume,[cus_id])

                        
            select_book=convert.dic_costume[cus_id]
            
            if int(select_book[3]) >= quantity:
                print("\nQuantity is available")
                update_quantity=int(select_book[3])-quantity # subtracting the stock after renting 
                select_book[3]=str(update_quantity) # uodate the stock 
                
                print(convert.dic_costume)
                price= str(select_book[2])
                price1= str(float(select_book[2].strip("$")))
                Bill["Per Piece Price"].append(price)  #append the price in the dictionary
                pri=float(price.replace("$",""))*quantity # replacing $ with space 
                tprice.append(pri) # appending pri to list tprice
                Bill["Costume Name"].append(select_book[0])
                Bill["Brand Name"].append(select_book[1])
                
                print("\nThe pre piece price of the custome is: ",price) # per piece price of the costune is displayed
           
        else:
            print("\n \tInvalid input")

            # Asking if the customer wants to rent more costume or not
        print("+++++++++++++++++++++++++++++++++")
        print("\nHave the customer rented another custome as well???")
        ans=input("Please enter 'y' to rent other clothes else Enter any other variables: ").lower()
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
        if ans == "y":
            print("+++++++++++++++++++++++++++++++++++")
            print("\nLet's rent a costume")
            print("\n+++++++++++++++++++++++++++++++++")
            update.update_stock()
            view.view() # call the view function form module view
            validate()
            price2=str(float(price1)*quantity)

        else:
            #date and time latest
            cdt = datetime.datetime.now()

            y = str(cdt.year)
            m = str(cdt.month)
            d = str(cdt.day)
            h = str(cdt.hour)
            mi = str(cdt.minute)
            sec = str(cdt.second)
            nowtime = str(y + "-" + m + "-" + d + " " + h + ":" + mi + ":" + sec)

            name=input("\nEnter name of the customer: ") # asking name of the customer

            #generating bill in txt file of renting
            p=str(y+m+d+h+mi+sec)
            j = open(p+"_rent.text","w")
            j.write("\n--------------------------------------")
            j.write("\n \tBill Details\n")
            j.write("--------------------------------------")
            j.write("\n**************************************")
            j.write("\n"+"The name of customer is: "+name+"\n")
            j.write("\n"+"The Date and Time of rent is "+nowtime+"\n")
            j.write("\n"+"The Total Price of the Costume you rented is: "+str(float(price1)*quantity)+"\n"+"\n")
            for key,values in Bill.items():
                        j.write('%s:%s\n\n' % (key, ",".join(values)))
            j.write("\n**************************************")  
        break
