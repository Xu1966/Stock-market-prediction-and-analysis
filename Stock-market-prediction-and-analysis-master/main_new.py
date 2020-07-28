
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import csv

import time
from threading import Timer

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import agriculture
import siddhartha
import machapuchre
import nabil
import arun


import openpyxl
import predict

import agriculture_predict
import siddhartha_predict
import machapuchre_predict
import nabil_predict
import arun_predict



def animate():

    lines = graph_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)





class login(Tk):

    def login_screen():
        global login_screen
        login_screen = Toplevel(root)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        Label(login_screen, text="Username * ").pack()
        username_login_entry = ttk.Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = ttk.Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        btn=ttk.Button(login_screen, text="Login", command = login.login_verify)
        btn.pack()




    def register_screen():
        global register_screen
        register_screen = Toplevel(root)
        register_screen.title("Register")
        register_screen.geometry("500x300")

        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()

        lbl=ttk.Label(register_screen, text="Please enter details below")
        lbl.pack()
        Label(register_screen, text="").pack()
        username_lable = ttk.Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = ttk.Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = ttk.Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        btn1=ttk.Button(register_screen, text="Register", command = login.register_user)
        btn1.pack(side=LEFT, padx=20)
        btn2=ttk.Button(register_screen, text="Exit", command = login.exit)
        btn2.pack(side=RIGHT, padx=20)

    def des1():
        global lbl1
        lbl1.destroy()
    def des2():
        global lbl2
        lbl2.destroy()
    def des3():
        global lbl3
        lbl3.destroy()
        register_screen.destroy()
    def register_user():
        global register_user
        global lbl1
        global lbl2
        global lbl3

        username_info = username.get()
        password_info = password.get()

        if username_info == "" or password_info == "":
            lbl1=ttk.Label(register_screen, text="Please complete the required field", font=("calibri", 11))
            lbl1.pack(side=TOP)

            t = Timer(2.0, login.des1)
            t.start()

        elif len(password_info) < 8:
            lbl2=ttk.Label(register_screen, text="the password is too short", font=("calibri", 11))
            lbl2.pack(side=TOP)

            t = Timer(2.0, login.des2)
            t.start()

        else:
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0, END)
            password_entry.delete(0, END)
            lbl3=ttk.Label(register_screen, text="Success", font=("calibri", 11))
            lbl3.pack(side=TOP)

            t = Timer(2.0, login.des3)
            t.start()


    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login.login_sucess()

            else:
                login.password_not_recognised()

        else:
            login.user_not_found()


    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        label=ttk.Label(login_success_screen, text="Login Success")
        label.pack()
        btn=ttk.Button(login_success_screen, text="OK", command=login.delete_login_success)
        btn.pack()

    # Designing popup for login invalid password

    def password_not_recognised():
        global password_not_recog_screen
        password_not_recog_screen = Toplevel(login_screen)
        password_not_recog_screen.title("Success")
        password_not_recog_screen.geometry("150x100")
        Label(password_not_recog_screen, text="Invalid Password ").pack()
        btn=ttk.Button(password_not_recog_screen, text="OK", command=login.delete_password_not_recognised)
        btn.pack()

    # Designing popup for user not found

    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        btn=ttk.Button(user_not_found_screen, text="OK", command=login.delete_user_not_found_screen)
        btn.pack()

    def delete_login_success():
        login_success_screen.destroy()
        login_screen.destroy()
        stockmarket.window()
        root.destroy()



    def delete_password_not_recognised():
        password_not_recog_screen.destroy()


    def delete_user_not_found_screen():
        user_not_found_screen.destroy()

    def exit():
        register_screen.destroy()


    def main_window():
        global root
        root = Tk()
        root.geometry("300x250")
        root.title("Account Login")

        root.iconbitmap(default="stock_market_qgq_icon.ico")


        Label(text="Select Your Choice", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        btn1=ttk.Button(text="Login", command = login.login_screen)
        btn1.pack()
        Label(text="").pack()
        btn2=ttk.Button(text="Register", command= login.register_screen)
        btn2.pack()
        status = Label(text="Login/Register", bd=1,relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        root.mainloop()

class stockmarket(Tk):
    def window():
        global window
        global x
        window = Tk()
        window.geometry("1100x200")
        window.title("Stock Market Prediction")
        frame_1=Frame(window)
        frame_2=Frame(window)
        Label(frame_1, text="Please choose the company from the following" , font=("Calibri", 10)).grid(row=0, column=0)

        l1=Label(frame_2, text="S.N.")
        l1.grid(row=1,column=0)
        l1=Label(frame_2, text="Traded Companies")
        l1.grid(row=1,column=1)
        l1=Label(frame_2, text="No. of Transactions")
        l1.grid(row=1,column=3)
        l1=Label(frame_2, text="Max Price")
        l1.grid(row=1,column=4)
        l1=Label(frame_2, text="Min price")
        l1.grid(row=1,column=5)
        l1=Label(frame_2, text="Closing Price")
        l1.grid(row=1,column=6)
        l1=Label(frame_2, text="Traded Shares")
        l1.grid(row=1,column=7)
        l1=Label(frame_2,text="Amount")
        l1.grid(row=1,column=8)
        l1=Label(frame_2,text="Previous Closing")
        l1.grid(row=1,column=9)
        l1=Label(frame_2,text="Difference Rs.")
        l1.grid(row=1,column=10)

        #l1=Label(frame_2,text="1" , cursor="hand2")
        #l1.grid(row=2,column=0)
        #l1.bind("<Button-1>", agriculture.load)
        #l1=ttk.Button(frame_2, text="Agriculture Development Bank Limited",command=agriculture.load)
        #l1.grid(row=2,column=1)
        #with open ('agriculture.csv') as file:
        #    csv.reader(file)
        book=openpyxl.load_workbook("main_page.xlsx")
        sheet=book.active
        
       

        # yo serial number ko lagi ho
        y=1
        for x in range(2,7):
            l1=Label(frame_2, text=y)
            l1.grid(row=x,column=0)
            y=y+1


        l1=ttk.Button(frame_2, text="Agriculture Development Bank Limited",command=agriculture.load)
        l1.grid(row=2,column=1)
        l1 = ttk.Button(frame_2, text="Arun Valley Hydropower Development Co. Ltd. (AHPC) ", command=arun.load)
        l1.grid(row=3, column=1)
        l1=ttk.Button(frame_2, text="Machhapuchre Bank Ltd.",command=machapuchre.load)
        l1.grid(row=4,column=1)
        l1=ttk.Button(frame_2, text="Nabil Bank Limited",command=nabil.load)
        l1.grid(row=5,column=1)
        l1 = ttk.Button(frame_2, text="Siddhartha Bank Ltd", command=siddhartha.load)
        l1.grid(row=6, column=1)
      


        #for predict button
        l1=ttk.Button(frame_2, text="Predict",command=agriculture_predict.load)
        l1.grid(row=2,column=2)
        l1 = ttk.Button(frame_2, text="Predict", command=arun_predict.load)
        l1.grid(row=3, column=2)
        l1=ttk.Button(frame_2, text="Predict",command=machapuchre_predict.load)
        l1.grid(row=4,column=2)
        l1=ttk.Button(frame_2, text="Predict",command=nabil_predict.load)
        l1.grid(row=5,column=2)
        l1 = ttk.Button(frame_2, text="Predict", command=siddhartha_predict.load)
        l1.grid(row=6, column=2)
    
        
        
        #for loop lagaune khojeko sabai lai ekaichoti

        #y=5
        #i=67
        #for x in range(2,12):
        #    for z in range(2,9):
        #        l1=Label(frame_2, text=sheet[chr(i)+str(y)].value)
        #        l1.grid(row=x,column=z)
        #        i=i+1
        #    y=y+1


        #y=5
        #for x in range(2,12):
        #    l1=ttk.Button(frame_2, text=sheet['B'+str(y)].value,command=arun.load)
        #    l1.grid(row=x,column=1)
        #    y=y+1

        x=67
        for y in range(3,11):
            l1=Label(frame_2, text=sheet[chr(x)+str(5)].value)
            l1.grid(row=2,column=y)
            x=x+1

        x = 67
        for y in range(3, 11):
            l1 = Label(frame_2, text=sheet[chr(x) + str(9)].value)
            l1.grid(row=3, column=y)
            x = x + 1

        x = 67
        for y in range(3, 11):
            l1 = Label(frame_2, text=sheet[chr(x) + str(75)].value)
            l1.grid(row=4, column=y)
            x = x + 1

        x = 67
        for y in range(3, 11):
            l1 = Label(frame_2, text=sheet[chr(x) + str(87)].value)
            l1.grid(row=5, column=y)
            x = x + 1

        x = 67
        for y in range(3, 11):
            l1 = Label(frame_2, text=sheet[chr(x) + str(152)].value)
            l1.grid(row=6, column=y)
            x = x + 1


        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['D'+str(y)].value)
        #     l1.grid(row=x,column=3)
        #     y=y+1
        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['E'+str(y)].value)
        #     l1.grid(row=x,column=4)
        #     y=y+1
        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['F'+str(y)].value)
        #     l1.grid(row=x,column=5)
        #     y=y+1
        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['G'+str(y)].value)
        #     l1.grid(row=x,column=6)
        #     y=y+1
        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['H'+str(y)].value)
        #     l1.grid(row=x,column=7)
        #     y=y+1
        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['I'+str(y)].value)
        #     l1.grid(row=x,column=8)
        #     y=y+1
        # y=5
        # for x in range(2,7):
        #     l1=Label(frame_2, text=sheet['J'+str(y)].value)
        #     l1.grid(row=x,column=9)
        #     y=y+1
        
        frame_1.grid(row=0 , column= 2)
        frame_2.grid(row=1 , column= 0)
        frame_2.grid(row=1 , column= 1)
        frame_2.grid(row=1 , column= 2)


#def app1():
#    global graph_data

#    global ax1
#    graph_data = open('stockData1.txt','r').read()

#    style.use('ggplot')
#    fig = plt.figure()
#    ax1=fig.add_subplot(1,1,1)
#    animate()

#    ani = animation.FuncAnimation(fig, animate, interval=1000)

#    plt.title('Agriculture Development Bank Limited')
#    plt.xlabel('Days')
#    plt.ylabel('Stock')
#    plt.show()

#def app2():
#    global graph_data
#    global ax1

#    graph_data = open('stockData2.txt','r').read()
#    style.use('ggplot')
#    fig = plt.figure()
#    ax1=fig.add_subplot(1,1,1)
#    animate()
#    ani = animation.FuncAnimation(fig, animate, interval=1000)
#    plt.title('Ankhu Khola Jalvidhyut Company Limited')
#    plt.xlabel('Days')
#    plt.ylabel('Stock')
#    plt.show()

#def app3():
#    global graph_data
#    global ax1
#    graph_data = open('stockData3.txt','r').read()
#    style.use('ggplot')
#    fig = plt.figure()
#    ax1=fig.add_subplot(1,1,1)
#    animate()
#    ani = animation.FuncAnimation(fig, animate, interval=1000)
#    plt.title('Api Power Company Ltd.')
#    plt.xlabel('Days')
#    plt.ylabel('Stock')
#    plt.show()



        window.mainloop()


login.main_window()