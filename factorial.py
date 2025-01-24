def welcome (number):
    result = 1
    for i in range (number, 0, -1):
        result = result * i 
    print (result)
welcome (4)