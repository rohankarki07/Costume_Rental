def view():
    count=0
    print("-----------------------------------------------------------------------------------")
    print("ID \t Custome Name\t\tBrand Name\t\tprice\t\tQuantity")
    print("-----------------------------------------------------------------------------------")
    file=open("stock.txt","r") # open the stock text file in the read mode
    counter = 0
    for line in file:
        counter += 1 # increase the counter value by 1
        line = line.replace(",","\t\t")
        print(counter,"\t" ,line)
    file.close() # close the file
    print("-----------------------------------------------------------------------------------")
