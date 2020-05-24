usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "damaya" and passwordInput == "5555" :
    print("!Welcome come!")
    print("--Born to Eat CAFE--")
    print("Plese Select Menu set")
    print("Mene Set 1")
    print("แกงส้มดอกแค กับ ข้าวไข่เจียว เสริฟพร้อมไอศกรีม 89 บาท")
    print("Mene Set 2")
    print("ผัดไทยกุ้งสด เสริฟพร้อมไอศกรีม 109 บาท")
    print("Mene Set 3")
    print("ข้าวเหนียวไก่ย่างและส้มตำ เสริฟพร้อมไอศกรีม 129 บาท")
    userSelectMenu = int(input("Select Menu Set >>"))
    if userSelectMenu == 1:
        MS1_Value = 89
        MS1_Number = int(input("คุณต้องการอาหารชุดกี่ที่? :"))
        price = MS1_Value*MS1_Number
        print("รวมทั้งหมด",price,"บาท")
    elif userSelectMenu == 2:
        MS2_Value = 109
        MS2_Number = int(input("คุณต้องการอาหารชุดกี่ที่? :"))
        price = MS2_Value * MS2_Number
        print("รวมทั้งหมด", price, "บาท")
    elif userSelectMenu == 3:
        MS3_Value = 129
        MS3_Number = int(input("คุณต้องการอาหารชุดกี่ที่? :"))
        price = MS3_Value * MS3_Number
        print("รวมทั้งหมด", price, "บาท")
else:
    print("Login Failed")

