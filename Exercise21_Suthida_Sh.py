from tkinter import *
import math


def calculateBMI(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))#โชว์ในโปรแกรมPcCharm
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))#ให้โชว์บนหน้าต่าง

def resultBMI(event):

    BMI = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    #print(BMI)
    if BMI < 18.5:
        print('น้ำหนักน้อย/ผอม')
        labelResult2.configure(text="น้ำหนักน้อย/ผอม")
    elif BMI < 22.9 and BMI >= 18.5:
        print('ปกติ/สุขภาพดี')
        labelResult2.configure(text="ปกติ/สุขภาพดี")
    elif BMI < 24.9 and BMI >= 23:
        print('ท้วม/โรคอ้วนระดับ 1')
        labelResult2.configure(text="ท้วม/โรคอ้วนระดับ 1")
    elif BMI < 29.9 and BMI >= 25:
        print('อ้วน/โรคอ้วนระดับ 2')
        labelResult2.configure(text="อ้วน/โรคอ้วนระดับ 2")
    elif BMI > 30:
        print('อ้วนมาก/โรคอ้วนระดับ 3')
        labelResult2.configure(text="อ้วนมาก/โรคอ้วนระดับ 3")

mainWindow = Tk()
    #ส่วนสูง
labelHeight = Label(mainWindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
    #น้ำหนัก
labelWeight = Label(mainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow)
textBoxWeight.grid(row=1,column=1)
    #คำนวณ
calculateButton = Button(mainWindow,text = "คำนวณ BMI",width=10,height=2)
calculateButton.grid(row=2,column=0)
calculateButton.bind('<Button-1>',calculateBMI)#กดปุ่มไปยังฟังชั่น calclulateBMI
calculateButton = Button(mainWindow,text = "ผลลัพธ์ BMI",width=10,height=2)
calculateButton.grid(row=3,column=0)
calculateButton.bind('<Button-1>',resultBMI)#กดปุ่มไปยังฟังชั่น calclulateBMI

    #ช่องโชว์ค่าBMIที่คำนวณไว้
labelResult = Label(mainWindow)
labelResult.grid(row=2,column=1)

labelResult2 = Label(mainWindow)
labelResult2.grid(row=3,column=1)


    #ผลลัพธ์


mainWindow.mainloop()
