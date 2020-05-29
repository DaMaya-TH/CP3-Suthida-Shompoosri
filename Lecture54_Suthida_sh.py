def login():
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("User Name or Password is Wrong")
        return login()
def showMenu():
    print("Done!")
    print("--i'M cOLD--")
    print("1. Vat Caculator")
    print("2. Price Caculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        vatCaculation()
    elif userSelected == 2:
        priceCaculation()
def vatCaculation(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    print("Exclude VAT",result, "THB")
def priceCaculation():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCaculation(price1 + price2)

login()
print("Finish!!")
