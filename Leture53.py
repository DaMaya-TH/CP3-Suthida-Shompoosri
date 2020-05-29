def vatCaculator(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print("Exclude VAT:",vatCaculator(float(input("Total Price :"))))
