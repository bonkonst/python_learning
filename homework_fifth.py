def insert_whitespace(text):
    list_of_symbol = []
    for char in text:
        if char.islower():
            list_of_symbol.append(char)
        else:
            if char.isupper():
                list_of_symbol.append(" " + char)
                continue
    return "".join(list_of_symbol)


print(insert_whitespace('SheWalksToTheBeach'))
