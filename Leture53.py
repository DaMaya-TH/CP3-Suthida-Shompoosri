def vatCaculator(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCaculator(float(input("Total Price :"))))
