def quantity_val(dic_costume,cus_id):
    while(True):
        #try except for the string check in the quantity.
        try:
            quantity=int(input("\nEnter the Quantity : "))
            while quantiy<=0 or quantity >int(dic_costume,[cus_id][3]):
                print("Invalid option")
                quantity=int(input("\nEnter the Quantity : "))
            break
        except:
            print("\nEnter integer as a quantity.")
    return quantity
