import convert
def update_stock():
    f=open("stock.txt","w") #open the stock text file in write mode
    for key,values in convert.dic_costume.items():
        f.write(",".join(values))
        f.write("\n")
    f.close() # close the file
