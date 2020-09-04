def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string length of 1.')
    if (width < 2) or (height < 2):
        raise Exception('"Width and Height" must be greater than or equal to 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


boxPrint('#', 2,9)