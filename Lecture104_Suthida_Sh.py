class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Add product to ",self.name,self.lastName,"'s cart")
customer1 = Customer()
customer1.name = "Suthida"
customer1.lastName = "Shompoosri"
customer1.addCart()

customer2 = Customer()
customer2.name = "จี้"
customer2.lastName = "แมวที่บ้าน"
customer2.addCart()

customer3 = Customer()
customer3.name = "ฮิตเลอร์"
customer3.lastName = "แมวตัวเก่า"
customer3.addCart()

customer4 = Customer()
customer4.name = "สกอตติสโฟล์"
customer4.lastName = "แมวที่อยากเลี้ยง แต่ไม่มีตังจะซื้อ"
customer4.addCart()
