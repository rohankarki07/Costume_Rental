def convert_dictionary():
    dictionary = {}
    file = open("stock.txt","r") # opening the stock.txt file in read mode
    costume_id = 0

    for line in file:
        costume_id += 1
        line = line.replace("\n","")
        line = line.split(",")
        dictionary[costume_id] = line
    return dictionary
dic_costume = convert_dictionary()
