def second_index(string, symbol):
    if symbol in string:
        temp = str.replace(string, symbol, "", 1)
        index = temp.index(symbol) + 1
        return index
    else:return
string = input("Enter string :")
symbol = input("Enter the symbol :")
print(second_index(string, symbol))
