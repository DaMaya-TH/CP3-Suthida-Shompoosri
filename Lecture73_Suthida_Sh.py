systemMenu = {'ข้าวหน้าเนื้อ':99,'ข้าวหน้าไก่':79,'ข้าวแกงกะหรี่':89,'ข้าวหมูทอด':159}
menuList = []

def showBill():
    print("-----My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],"THB")
        totalPrice +=  int(menuList[number][1])
    print("Total Price :", totalPrice,"THB")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()

