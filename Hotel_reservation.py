from tkinter import *

from time import sleep

from mysql.connector import *

from tkinter import messagebox, scrolledtext, ttk

from tkinter import *
from PIL import ImageTk, Image

import time

from tkcalendar import Calendar

db = connect(host='localhost', username='root', password='313705', database="hotel_reservation")

# ============================== main window ========================
def main_screen():
    main_window = Tk()

    main_window.title("Hotel_reservation")

    #                                                           Main frame

    main_frame = LabelFrame(main_window, width=1200, height=800)

    main_frame.grid(row=0, column=0)

    top_frame = LabelFrame(main_frame, width=1200, height=200)

    top_frame.grid(row=0, column=0)

    inner_frame = LabelFrame(top_frame, text="Login", width=1200, height=200, font=("ariel", 30, "italic"))

    inner_frame.grid(row=0, column=0)

    x = "hotel1.jpg"
    img = Image.open(x)
    img = img.resize((1200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(inner_frame, image=img)
    panel.image = img
    panel.pack()

    Label(inner_frame, text="Username ", font=("ariel", 20, "italic")).place(x=15, y=105)

    entry_username = StringVar()

    entry_name = Entry(inner_frame, textvariable=entry_username, font=("ariel", 16, "italic"))

    entry_name.place(x=157, y=110)

    Label(inner_frame, text="Password ", font=("ariel", 20, "italic")).place(x=505, y=105)

    entry_username1 = StringVar()

    entry_password = Entry(inner_frame, textvariable=entry_username1, font=("ariel", 16, "italic"), show="*")
    entry_password.place(x=645, y=110)

    # ----------------------------Password visibility-------------------------------------------------
    def show_1():
        entry_password = Entry(inner_frame, textvariable=entry_username1, font=("ariel", 16, "italic"))
        entry_password.place(x=645, y=110)

        def hide_1():
            entry_password = Entry(inner_frame, textvariable=entry_username1, font=("ariel", 16, "italic"), show="*")
            entry_password.place(x=645, y=110)

            Button(inner_frame, text="show", command=show_1).place(x=848, y=110)

        Button(inner_frame, text="hide", command=hide_1).place(x=848, y=110)

    Button(inner_frame, text="show", command=show_1).place(x=848, y=110)

    # -----------------------------------Forgot password-------------------------------------------
    def change():

        change_password = Tk()

        change_password.title("Change password")

        ch_lf1 = LabelFrame(change_password, text="Change Password")

        ch_lf1.pack()

        Label(ch_lf1, text="Username ", font=("bold", 25)).pack()

        ch_e1 = Entry(ch_lf1, font=("bold", 25))

        ch_e1.pack()

        Label(ch_lf1, text=" ", font=("bold", 25)).pack()

        Label(ch_lf1, text="New Password ", font=("bold", 25)).pack()

        ch_e2 = Entry(ch_lf1, font=("bold", 25))

        ch_e2.pack()

        Label(ch_lf1, text=" ", font=("bold", 25)).pack()

        Label(ch_lf1, text="Confirm Password ", font=("bold", 25)).pack()

        ch_e3 = Entry(ch_lf1, font=("bold", 25))

        ch_e3.pack()

        Label(ch_lf1, text=" ", font=("bold", 25)).pack()

        def change_out():
            if ch_e2.get() == ch_e3.get():
                try:
                    passchange = db.cursor()

                    content = 'update login set password = "' + ch_e2.get() + '" where username = "' + ch_e1.get() + '"'

                    passchange.execute(content)

                    db.commit()

                    messagebox.showinfo("success", "Password changed successfully..")

                    change_password.destroy()

                except Exception:
                    messagebox.showerror("Incorrect", "username is invalid")

                    change_password.destroy()

                    change()

            else:
                messagebox.showerror("Incorrect", "pass doesn't match enter it correctly")

                change_password.destroy()

                change()

        Button(ch_lf1, text="Change", command=change_out, font=("bold", 20)).pack()

        Label(ch_lf1, text=" ", font=("bold", 25)).pack()

    Button(inner_frame, text="change password", command=change, font=("ariel", 12)).place(x=1000, y=170)

    # ----------------------------------Login page------------------------------------------------------------------------
    def hotel_reservation1():

        try:

            login_data = db.cursor()

            content = 'select password from login where username="' + (entry_name.get() + '"')

            login_data.execute(content)

            password = login_data.fetchall()

            if password[0][0] == entry_username1.get():

                main_frame.destroy()

                main_frame2 = LabelFrame(main_window, width=1200, height=800)

                main_frame2.grid(row=0, column=0)

                for i in range(1):
                    Label(main_frame2, text="Please wait       ", font=("bold", 40)).place(x=500, y=400)

                    main_window.update()

                    sleep(0.5)

                    Label(main_frame2, text="Please wait .     ", font=("bold", 40)).place(x=500, y=400)

                    main_window.update()

                    sleep(0.5)

                    Label(main_frame2, text="Please wait . .  ", font=("bold", 40)).place(x=500, y=400)

                    main_window.update()

                    sleep(0.5)

                    Label(main_frame2, text="Please wait . . .", font=("bold", 40)).place(x=500, y=400)

                    main_window.update()

                    sleep(0.5)

                Label(main_frame2, text="Logged in successfully...", font=("bold", 40)).place(x=300, y=400)

                main_window.update()

                sleep(0.5)

                main_frame2.destroy()

                def hotel_reservation2():

                    main_frame1 = LabelFrame(main_window, width=1200, height=800)

                    main_frame1.grid(row=0, column=0)

                    x = "back1.jpg"
                    img = Image.open(x)
                    img = img.resize((1300, 800), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(main_frame1, image=img)
                    panel.image = img
                    panel.place(x=0, y=0)

                    left_frame = LabelFrame(main_frame1, text="Reception", width=300, height=800,
                                            font=("ariel", 30, "italic"),
                                            fg="blue")

                    left_frame.grid(row=0, column=0)

                    x = "gy.jpg"
                    img = Image.open(x)
                    img = img.resize((300, 800), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(left_frame, image=img)
                    panel.image = img
                    panel.pack()

                    right_frame = LabelFrame(main_frame1, width=900, height=850, font=("ariel", 30, "italic"),
                                             fg="blue")

                    right_frame.grid(row=0, column=1)

                    x = "bed2.jpg"
                    img = Image.open(x)
                    img = img.resize((900, 850), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(right_frame, image=img)
                    panel.image = img
                    panel.pack()

                    Label(right_frame, text="WELCOME TO TAJ HOTEL", font=("ariel", 35, "italic", "bold"), bd=4).place(
                        x=200,
                        y=50)

                    #                                                          INSIDE BOTTOM FRAME - LEFT FRAME

                    left_frame1 = LabelFrame(right_frame, width=300, height=400, bd=4)

                    left_frame1.place(x=80, y=290)

                    x = "bed2.jpg"
                    img = Image.open(x)
                    img = img.resize((320, 420), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(left_frame1, image=img)
                    panel.image = img
                    panel.pack()

                    Label(left_frame1, text="* Best offers", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=15)

                    Label(left_frame1, text="* High tech hotel ", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                                 y=75)

                    Label(left_frame1, text="* Swiming pool", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                             y=135)

                    Label(left_frame1, text="* Free wifi", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=195)

                    Label(left_frame1, text="* Five stared hotel", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                                  y=255)

                    Label(left_frame1, text="* Fascinating rooms", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                                  y=315)

                    #                                                          INSIDE BOTTOM FRAME - RIGHT FRAME

                    right_frame1 = LabelFrame(right_frame, width=320, height=400, bd=4)

                    right_frame1.place(x=500, y=290)

                    x = "bed2.jpg"
                    img = Image.open(x)
                    img = img.resize((340, 420), Image.ANTIALIAS)
                    img = ImageTk.PhotoImage(img)
                    panel = Label(right_frame1, image=img)
                    panel.image = img
                    panel.pack()

                    Label(right_frame1, text="* Children play area", font=("ariel", 20, "italic"), fg="blue").place(
                        x=15,
                        y=15)

                    Label(right_frame1, text="* Friendly lobby", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                                y=75)

                    Label(right_frame1, text="* Night Camp fire", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                                 y=135)

                    Label(right_frame1, text="* Nature friendly rooms", font=("ariel", 20, "italic"), fg="blue").place(
                        x=15,
                        y=195)

                    Label(right_frame1, text="* Nearby Airport", font=("ariel", 20, "italic"), fg="blue").place(x=15,
                                                                                                                y=255)

                    # ---------------------------------------------------------------------------------------------------------------------------------------------------------

                    #
                    #
                    #       ====================================  Registration form   ==================================================
                    def registration1():
                        right_frame1 = LabelFrame(main_frame1, text="Registration", width=1100, height=850,
                                                  font=("ariel", 30, "italic"), fg="white", bg="black")

                        right_frame1.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 850), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(right_frame1, image=img)
                        panel.image = img
                        panel.place(x=0, y=0)

                        date1 = StringVar()

                        #                       Labels - Registration form

                        Label(right_frame1, text="P_id ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                               y=25)

                        Label(right_frame1, text="Name ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                               y=95)

                        Label(right_frame1, text="Age ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                              y=165)

                        Label(right_frame1, text="Gender ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                                 y=235)

                        Label(right_frame1, text="Address ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                                  y=305)

                        Label(right_frame1, text="Phone no ", font=("italic", 18), bg="skyblue", fg="black").place(
                            x=105,
                            y=375)

                        Label(right_frame1, text="E-mail ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                                 y=445)

                        Label(right_frame1, text="Date(dd/mm/yyyy) ", font=("italic", 18), bg="skyblue",
                              fg="black").place(x=105, y=515)

                        Label(right_frame1, text="Time ", font=("italic", 18), bg="skyblue", fg="black").place(x=105,
                                                                                                               y=585)

                        #                       Entries - Registration form

                        spinvar1 = StringVar()

                        spinvar2 = StringVar()

                        spinvar3 = StringVar()

                        spinvar4 = StringVar()

                        spinvar5 = StringVar()

                        spinvar6 = StringVar()

                        spinvar7 = StringVar()

                        p_id_data = db.cursor()

                        reg_content = "select *from registration "

                        p_id_data.execute(reg_content)

                        p_id_level = p_id_data.fetchall()

                        spinvar1.set(len(p_id_level) + 1)

                        res_entry1 = Entry(right_frame1, font=("italic", 15), textvariable=spinvar1, state=DISABLED)

                        res_entry1.place(x=605, y=25)

                        res_entry2 = Entry(right_frame1, font=("italic", 15), textvariable=spinvar2)

                        res_entry2.place(x=605, y=95)

                        spin_box1 = Spinbox(right_frame1, textvariable=spinvar3, from_=18, to=99, width=15,
                                            font=("ariel", 18))

                        spin_box1.place(x=605, y=165)

                        spinvar4.set("O")

                        radio_1 = Radiobutton(right_frame1, text="Male", variable=spinvar4, value="M")

                        radio_1.place(x=605, y=235)

                        radio_1 = Radiobutton(right_frame1, text="Female", variable=spinvar4, value="F")

                        radio_1.place(x=665, y=235)

                        radio_1 = Radiobutton(right_frame1, text="Others", variable=spinvar4, value="O")

                        radio_1.place(x=735, y=235)

                        scrolled_text1 = scrolledtext.ScrolledText(right_frame1, height=1, width=25)

                        scrolled_text1.place(x=605, y=305)

                        res_entry6 = Entry(right_frame1, font=("italic", 15), textvariable=spinvar6)

                        res_entry6.place(x=605, y=375)

                        res_entry7 = Entry(right_frame1, font=("italic", 15), textvariable=spinvar7)

                        res_entry7.place(x=605, y=445)

                        res_entry8 = Entry(right_frame1, textvariable=date1, font=("italic", 15), state=DISABLED)

                        res_entry8.place(x=605, y=515)

                        time1 = StringVar()

                        res_entry9 = Entry(right_frame1, font=("italic", 15), textvariable=time1, state=DISABLED)

                        res_entry9.place(x=605, y=585)

                        def date_1():
                            date = time.strftime("%d")

                            month = time.strftime("%m")

                            year = time.strftime("%Y")

                            date1.set(date + "/" + month + '/' + year)

                        date_1()

                        # ----------------------------------------------------------------------------------------------------------------------------
                        # ==========================================  REGISTRATION FORM ==============================================================
                        # ================================= data validation and data base insertion ==================================================
                        def data_registration():

                            reg_go = 0

                            if spinvar2.get().isalpha() and spinvar2.get() != "" and spinvar2.get() != " " and spinvar2.get() != "  ":

                                try:
                                    a = int(spinvar3.get())

                                    if not (len(spinvar3.get()) < 3):
                                        messagebox.showerror("Error", "Enter a valid age..._")

                                    elif not(int(spinvar3.get()) >= 18):
                                        messagebox.showerror("Error",
                                                             "Person with minimum age of 18 is allowed to register")
                                    elif not(len(scrolled_text1.get(1.0, END)) > 5):

                                        messagebox.showerror("Error", "Enter a valid address...")
                                    else:
                                        try:
                                            a = int(spinvar6.get())

                                            if len(spinvar6.get()) == 10:
                                                if len(spinvar7.get()) > 10:
                                                    register = db.cursor()

                                                    content = "insert into registration values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                                        res_entry1.get(), res_entry2.get(), spin_box1.get(),
                                                        spinvar4.get(),
                                                        scrolled_text1.get(1.0, END),
                                                        res_entry6.get(), res_entry7.get(), res_entry8.get(),
                                                        res_entry9.get())

                                                    register.execute(content)

                                                    db.commit()

                                                    messagebox.showinfo("Success", "Registration successfull")

                                                    main_frame1.destroy()

                                                    hotel_reservation2()

                                                    reg_go += 1


                                                else:
                                                    messagebox.showerror("Error", "Enter a valid Email id...")
                                                    reg_go -= 1

                                            else:
                                                messagebox.showerror("Error", "Enter a valid mobile number...")

                                        except Exception as e:
                                            print(e)
                                            messagebox.showerror("Error", "Enter a valid mobile number...")



                                except Exception as e:
                                    print(e)
                                    messagebox.showerror("Error", "Enter a valid age...")
                                    reg_go -= 1
                            else:

                                messagebox.showwarning("Warning", "Enter name correctly ...")

                        # ---------------------------------------- ENTRY BOX CLEAR FUNCTION -----------------------------------------------------------------------

                        def clear_1():
                            spinvar2.set('')

                            spinvar3.set("select")

                            spinvar4.set('M')

                            scrolled_text1.delete(1.0, END)

                            spinvar6.set("")

                            spinvar7.set("")

                        Button(right_frame1, text="sign up", font=("ariel", 18), width=20, bg="skyblue", fg="black",
                               command=data_registration).place(x=130, y=670)
                        Button(right_frame1, text="clear", font=("ariel", 18), width=20, bg="skyblue", fg="black",
                               command=clear_1).place(x=550,
                                                      y=670)

                        try:
                            def time_1():
                                hour = time.strftime("%H")

                                minute = time.strftime("%M")

                                second = time.strftime("%S")

                                meridian = time.strftime("%p")

                                time1.set(hour + ':' + minute + ":" + second + " " + meridian)

                                main_window.update()
                                sleep(0.1)

                                if True:
                                    time_1()

                            time_1()
                        except Exception:
                            pass

                    Button(left_frame, text="Registration", command=registration1, width=15).place(x=90, y=50)

                    # --------------------------------------------------------------------------------------------------------------------------
                    #
                    #  ==========================================  Guest registration form    ===============================================
                    def guest1():

                        right_frame2 = LabelFrame(main_frame1, text="Guest form", width=1100, height=850,
                                                  font=("ariel", 30, "italic"), fg="white",
                                                  bg="black")

                        right_frame2.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 850), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(right_frame2, image=img)
                        panel.image = img
                        panel.place(x=0, y=0)

                        g_en1 = StringVar()
                        g_en2 = StringVar()
                        g_en7 = IntVar()
                        g_en10 = StringVar()
                        g_var1 = StringVar()
                        g_var2 = StringVar()
                        g_var3 = StringVar()
                        g_var1.set("Select")
                        g_var2.set("Select")
                        g_var3.set("Select")

                        spinvar1 = StringVar()

                        #                   Label Declaration

                        lb1_1 = Label(right_frame2, text="First Name ", bg="skyblue", fg="black", font=("bold", 15),
                                      anchor=W)

                        lb1_1.place(x=155, y=55)

                        lb2_1 = Label(right_frame2, text="Last Name ", bg="skyblue", fg="black", font=("bold", 15),
                                      anchor=W)

                        lb2_1.place(x=155, y=135)

                        lb5_2 = Label(right_frame2, text="Address ", bg="skyblue", fg="black", font=("bold", 15))

                        lb5_2.place(x=155, y=215)

                        lb7_1 = Label(right_frame2, text="Contact No ", bg="skyblue", fg="black", font=("bold", 15),
                                      anchor=W)

                        lb7_1.place(x=155, y=295)

                        lb7_1 = Label(right_frame2, text="Room No ", bg="skyblue", fg="black", font=("bold", 15),
                                      anchor=W)

                        lb7_1.place(x=155, y=375)

                        lb7_1 = Label(right_frame2, text="Room Type ", bg="skyblue", fg="black", font=("bold", 15),
                                      anchor=W)

                        lb7_1.place(x=155, y=455)

                        lb8_1 = Label(right_frame2, text="Gender ", bg="skyblue", fg="black", font=("bold", 15),
                                      anchor=W)

                        lb8_1.place(x=155, y=535)

                        lb10_1 = Label(right_frame2, text="E-Mail id ", bg="skyblue", fg="black", font=("bold", 15),
                                       anchor=W)

                        lb10_1.place(x=155, y=625)

                        #                   Entry Declaration

                        e1 = Entry(right_frame2, textvariable=g_en1, width=20, font=("bold", 15))

                        e1.place(x=555, y=55)

                        e2 = Entry(right_frame2, textvariable=g_en2, width=20, font=("bold", 15))

                        e2.place(x=555, y=135)

                        gf_lst1 = scrolledtext.ScrolledText(right_frame2, width=20, height=0.5, font=("bold", 15))

                        gf_lst1.place(x=555, y=215)

                        e7 = Entry(right_frame2, textvariable=g_en7, width=20, font=("bold", 15))

                        e7.place(x=555, y=295)

                        room_data = db.cursor()

                        content = "select room_no from g_room where check1='-'"

                        room_data.execute(content)

                        table = room_data.fetchall()

                        leng = len(table)

                        table1 = '" "'

                        for i in range(len(table)):
                            table1 = table1 + ',"' + str(table[i][0]) + '"'

                        sp6 = ttk.Combobox(right_frame2, textvariable=spinvar1)

                        sp6['values'] = (eval(table1))

                        sp6.place(x=555, y=375)

                        s8 = OptionMenu(right_frame2, g_var2, "Ac", "Non-AC")

                        s8.place(x=555, y=455)

                        s9 = OptionMenu(right_frame2, g_var3, "Male", "Female", "Others")

                        s9.place(x=555, y=535)

                        e10 = Entry(right_frame2, textvariable=g_en10, width=20, font=("bold", 15))

                        e10.place(x=555, y=625)

                        # --------------------------------------------------------------------------------------------------------------------

                        #                                  Button declaration
                        def save():

                            go = 0

                            if g_en1.get().isalpha() and g_en1.get() != "" and g_en1.get() != " " and g_en1.get() != "  ":

                                if g_en2.get().isalpha() and g_en2.get() != "" and g_en2.get() != " " and g_en2.get() != "  ":

                                    if len(gf_lst1.get(1.0, END)) > 10:
                                        try:
                                            a = int(g_en7.get())
                                            if len(str(g_en7.get())) == 10:
                                                if g_var2.get() != "select" and g_var2.get() != "Select":
                                                    if g_var3.get() != "select" and g_var3.get() != "Select":
                                                        if len(g_en10.get()) > 10:
                                                            pass
                                                        else:
                                                            messagebox.showerror("Error",
                                                                                 "Enter the Email id correctly....")
                                                            go -= 1
                                                    else:
                                                        messagebox.showerror("Error",
                                                                             "Select the Gender correctly...._")
                                                        go -= 1
                                                else:
                                                    messagebox.showerror("Error", "Select the room type correctly...._")
                                                    go -= 1
                                            else:
                                                messagebox.showerror("Error", "Enter the contact number correctly...._")
                                                go -= 1
                                        except Exception:
                                            messagebox.showerror("Error", "Enter the Contact number correctly....")
                                            go -= 1

                                    else:
                                        messagebox.showerror("Error", "Enter the Address correctly....")
                                        go -= 1

                                else:
                                    messagebox.showerror("Error", "Enter the Last name correctly....")
                                    go -= 1

                            else:
                                messagebox.showerror("Error", "Enter the First name correctly....")
                                go -= 1

                            if go == 0:

                                if len(spinvar1.get()) == 4:
                                    try:
                                        g_rm_data = db.cursor()

                                        content = "select room_no, check1 from g_room"

                                        g_rm_data.execute(content)

                                        g_rm_no = g_rm_data.fetchall()

                                        for i in range(len(g_rm_no)):
                                            if g_rm_no[i][1] == '-':

                                                if g_rm_no[i][0] == spinvar1.get():
                                                    break
                                        else:
                                            messagebox.showerror("Error", "Select the room no correctly...._")

                                    except Exception as e:
                                        print(e)
                                        messagebox.showerror("Error", "Select the room no correctly...._")

                                else:
                                    messagebox.showerror("Error", "Select the room no correctly...._")
                                    go -= 1

                            if go == 0:

                                try:

                                    guest_data = db.cursor()

                                    content0 = "select check1 from g_room where room_no='" + spinvar1.get() + "'"

                                    guest_data.execute(content0)

                                    test = guest_data.fetchall()

                                    if test[0][0] == "-":

                                        content = "insert into guest values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                            spinvar1.get(), g_en1.get(), g_en2.get(), gf_lst1.get(1.0, END),
                                            g_en7.get(),
                                            g_var2.get(), g_var3.get(), g_en10.get())

                                        content1 = "update g_room set check1='/' where room_no='" + spinvar1.get() + "'"

                                        guest_data.execute(content)

                                        guest_data.execute(content1)

                                        db.commit()

                                        messagebox.showinfo("Success",
                                                            "Congratulation! \n\nGuest id stored successfully")

                                    else:
                                        messagebox.showwarning("warning", "Please refresh the form")
                                except Exception:
                                    messagebox.showwarning("warning", "Select a valid room number")


                            else:

                                messagebox.showwarning("warning", "Please Enter all the details")

                        # ----------------------------------------------------------------------------------------------------------------------

                        def Clear():
                            e1.delete(0, END)
                            g_en2.set("")
                            g_en7.set("")
                            g_en10.set("")
                            g_var1.set("selcet")
                            gf_lst1.delete(1.0, END)

                        g_bt1 = Button(right_frame2, text="Save", width=15, bg="skyblue", activebackground="blue",
                                       activeforeground="yellow", font=("bold", 15), command=save)

                        g_bt1.place(x=85, y=705)

                        g_bt2 = Button(right_frame2, text="Clear", bg="skyblue", activebackground="blue",
                                       activeforeground="yellow", width=15, font=("bold", 15), command=Clear)

                        g_bt2.place(x=355, y=705)

                        def guest_list():
                            gt_list = Tk()

                            gt_list.title("Guest List")

                            gt_lst = ['Room No', 'First Name ', 'Last Name ', 'Contact No ', 'Rome Type', 'Gender ']

                            gt_lf1 = LabelFrame(gt_list, text="GUEST LIST", font=("bold", 30))

                            gt_lf1.grid(row=1, column=1)

                            for i in range(len(gt_lst)):
                                Label(gt_lf1, text="  ", font=("italic", 25)).grid(row=1, column=i * 2)

                                Label(gt_lf1, text=gt_lst[i], font=("italic", 25)).grid(row=1, column=i * 2 + 1)

                            guest_data = db.cursor()

                            content = "select room_no, f_name, l_name, contact_no, room_type, gender from guest"

                            guest_data.execute(content)

                            text1 = guest_data.fetchall()

                            lent = len(text1)
                            lent1 = len(text1[0])

                            for i in range(lent):
                                for j in range(lent1):
                                    Label(gt_lf1, text="  ", font=("italic", 25)).grid(row=i + 2, column=j * 2)

                                    Label(gt_lf1, text=text1[i][j], font=("ariel", 17)).grid(row=i + 2,
                                                                                             column=(j * 2) + 1)

                        g_bt3 = Button(right_frame2, text="Guest list", bg="skyblue", activebackground="blue",
                                       activeforeground="yellow", width=15, font=("bold", 15), command=guest_list)

                        g_bt3.place(x=660, y=705)

                    Button(left_frame, text="Guest", command=guest1, width=15).place(x=90, y=150)

                    # ----------------------------------------------------------------------------------------------------------------------------------------
                    # ----------------------------------------------------------------------------------------------------------------------------------------

                    #
                    #
                    #                               Reservation form
                    def reservation1():

                        spinvar1 = StringVar()

                        spinvar2_1 = StringVar()

                        spinvar2_2 = StringVar()

                        spinvar3_1 = StringVar()

                        spinvar3_2 = StringVar()

                        spinvar4_1 = StringVar()

                        spinvar4_2 = StringVar()

                        spinvar5_1 = StringVar()

                        spinvar5_2 = StringVar()

                        spinvar6_1 = StringVar()

                        spinvar6_2 = StringVar()

                        spinvar7_1 = StringVar()

                        spinvar7_2 = StringVar()

                        spinvar8_1 = StringVar()

                        spinvar8_2 = StringVar()

                        test_date = StringVar()

                        date1 = StringVar()

                        def calendar1():

                            root = Tk()

                            cal = Calendar(root, selectmode="day", year=2020)

                            cal.pack()

                            def grab_date():
                                num1 = cal.get_date()
                                if '/' == num1[1]:
                                    num1 = '0' + num1

                                if '/' == num1[4]:
                                    num1 = num1[0:3] + '0' + num1[3:]

                                date_check = StringVar()

                                date = time.strftime("%d")

                                month = time.strftime("%m")

                                year = time.strftime("%y")

                                date_check.set(month + "/" + date + '/' + year)

                                if date_check.get()[6:] == num1[6:]:
                                    if date_check.get()[0:2] <= num1[0:2]:
                                        if date_check.get()[3:5] <= num1[3:5]:
                                            spinvar6_1.set(num1)
                                        else:
                                            messagebox.showerror('Error',
                                                                 "You can't book for the date before today's date1")


                                    else:
                                        messagebox.showerror('Error',
                                                             "You can't book for the date before today's date2")

                                elif date_check.get()[6:] < num1[6:]:
                                    spinvar6_1.set(num1)

                                else:
                                    messagebox.showerror('Error', "You can't book for the date before today's date3")


                                root.destroy()

                            my_button = Button(root, text="Get Date", command=grab_date)

                            my_button.pack(pady=20)

                            root.mainloop()

                        date2 = StringVar()

                        def calendar2():

                            if spinvar6_1.get() != "":

                                root = Tk()

                                cal = Calendar(root, selectmode="day", year=2020)

                                cal.pack()

                                def grab_date():

                                    if spinvar6_1.get() != "":

                                        num1 = cal.get_date()
                                        if '/' == num1[1]:
                                            num1 = '0' + num1

                                        if '/' == num1[4]:
                                            num1 = num1[0:3] + '0' + num1[3:]

                                        date_check = StringVar()

                                        date = time.strftime("%d")

                                        month = time.strftime("%m")

                                        year = time.strftime("%y")

                                        date_check.set(month + "/" + date + '/' + year)

                                        if spinvar6_1.get()[6:] == num1[6:]:
                                            if spinvar6_1.get()[0:2] == num1[0:2]:
                                                if spinvar6_1.get()[3:5] <= num1[3:5]:
                                                    spinvar6_2.set(num1)
                                                else:
                                                    messagebox.showerror('Error',
                                                                         "Check out date can't be lesser than check in date")

                                            elif date_check.get()[0:2] < num1[0:2]:
                                                spinvar6_2.set(num1)
                                                
                                            else:
                                                messagebox.showerror('Error',
                                                                     "Check out date can't be lesser than check in date")
                                        elif date_check.get()[6:] < num1[6:]:
                                            spinvar6_2.set(num1)
                                        else:
                                            messagebox.showerror('Error',
                                                                 "Check out date can't be lesser than check in date")

                                        root.destroy()

                                    else:
                                        messagebox.showerror('Error', "Please select the checkin date first")

                                my_button = Button(root, text="Get Date", command=grab_date)

                                my_button.pack(pady=20)

                                root.mainloop()
                            else:
                                messagebox.showerror('Error', "Please select the checkin date first")

                        rf_lf1 = LabelFrame(main_frame1, text="Reservation Form", font=("bold", 22), width=1100,
                                            height=810,
                                            fg="white", bg="black")

                        rf_lf1.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 810), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(rf_lf1, image=img)
                        panel.image = img
                        panel.grid(row=0, column=1)

                        #                                  Label declaration

                        rf_lst = ["P_ID ", "  ", "Guest Name ", "No.Of.Adults ", "Room Type ", "No.Of.Children ",
                                  "Room No ", "Discount Type ", "Room Rate(per day)", "Total(per day)",
                                  "Check In Date ", "Check Out Date ", "No.Of.Days ", "Total Amount ",
                                  "Advance Payment ", "Total Balance "]

                        for i in range(len(rf_lst)):

                            if i % 2 == 0:

                                Label(rf_lf1, text=rf_lst[i], font=("bold", 18), bg="skyblue").place(x=45,
                                                                                                     y=15 + (i * 40))

                            else:

                                if i != 1:
                                    Label(rf_lf1, text=rf_lst[i], font=("bold", 18), bg="skyblue").place(x=625,
                                                                                                         y=15 + ((
                                                                                                                             i - 1) * 40))

                        #                                       Entry declaration

                        rf_et1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar1)

                        rf_et1.place(x=295, y=15)

                        rf_et2_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar2_1)

                        rf_et2_1.place(x=295, y=95)

                        rf_et2_2 = Spinbox(rf_lf1, from_=0, to=2, font=("bold", 16))

                        rf_et2_2.place(x=805, y=95)

                        def room_no(a):
                            spinvar4_1.set("Select the room no")

                            room_data = db.cursor()

                            content = "select room_no, check1 from room where rm_type = '" + spinvar3_1.get() + "'"

                            room_data.execute(content)

                            table = room_data.fetchall()

                            leng = len(table)

                            table1 = '"Select"'

                            for i in range(len(table)):
                                if table[i][1] == '-':
                                    table1 = table1 + ',"' + str(table[i][0]) + '"'

                            rf_et4_1 = ttk.Combobox(rf_lf1, textvariable=spinvar4_1, width=30)

                            rf_et4_1['values'] = (eval(table1))

                            rf_et4_1.place(x=295, y=255)

                        spinvar3_1.set("Select")

                        rf_et3_1 = OptionMenu(rf_lf1, spinvar3_1, "AC", "Non-AC", command=room_no)

                        rf_et3_1.place(x=295, y=175)

                        rf_et3_2 = Spinbox(rf_lf1, from_=0, to=3, font=("bold", 16))

                        rf_et3_2.place(x=805, y=175)

                        spinvar4_1.set("Select the room type first")

                        table1 = "'Select'"

                        rf_et4_1 = ttk.Combobox(rf_lf1, textvariable=spinvar4_1, width=30, state=DISABLED)

                        rf_et4_1['values'] = (eval(table1))

                        rf_et4_1.place(x=295, y=255)

                        spinvar4_2.set("None")

                        rf_et4_2 = OptionMenu(rf_lf1, spinvar4_2, "None", "Regular", "VIP")

                        rf_et4_2.place(x=835, y=255)

                        rf_et5_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5_1, state=DISABLED)

                        rf_et5_1.place(x=295, y=335)

                        def rate():

                            rate = db.cursor()

                            content = "select * from discount"

                            rate.execute(content)

                            rate_var = rate.fetchall()

                            if spinvar3_1.get() == "AC":
                                spinvar5_1.set("3000")

                                spinvar5_2.set(str(3000 + (int(rf_et2_2.get()) * 900) + (int(rf_et3_2.get()) * 300)))

                                if spinvar4_2.get() == "Regular":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[1][1] / 100))))

                                elif spinvar4_2.get() == "VIP":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[2][1] / 100))))

                                else:
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[0][1] / 100))))

                            elif spinvar3_1.get() == "Non-AC":
                                spinvar5_1.set("2200")

                                spinvar5_2.set(str(2200 + (int(rf_et2_2.get()) * 800) + (int(rf_et3_2.get()) * 250)))

                                if spinvar4_2.get() == "Regular":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[1][1] / 100))))

                                elif spinvar4_2.get() == "VIP":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[2][1] / 100))))

                                else:
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[0][1] / 100))))

                            else:
                                messagebox.showerror("Error", "select room type correctly")

                        Button(rf_lf1, text="check", command=rate).place(x=495, y=335)

                        rf_et5_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5_2, state=DISABLED)

                        rf_et5_2.place(x=835, y=335)

                        rf_et6_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar6_1, state=DISABLED)

                        rf_et6_1.place(x=295, y=415)

                        Button(rf_lf1, text="Select", command=calendar1).place(x=494, y=416)

                        rf_et6_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar6_2, state=DISABLED)

                        rf_et6_2.place(x=835, y=415)

                        Button(rf_lf1, text="Select", command=calendar2).place(x=1035, y=415)

                        rf_et7_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar7_1, state=DISABLED)

                        rf_et7_1.place(x=295, y=495)

                        global go

                        go = 0

                        def day_no1():

                            days = 'asd'

                            try:

                                num1 = spinvar6_1.get()

                                num2 = spinvar6_2.get()

                                if (spinvar6_1.get() != "") and (spinvar6_2.get() != ""):

                                    if '/' == num1[1]:
                                        num1 = '0' + num1

                                    if '/' == num1[4]:
                                        num1 = num1[0:3] + '0' + num1[3:]

                                    if '/' == num2[1]:
                                        num2 = '0' + num2

                                    if '/' == num2[4]:
                                        num2 = num2[0:3] + '0' + num2[3:]

                                    months_1 = [1, 3, 5, 7, 8, 10, 12]

                                    months_2 = [4, 6, 9, 11, 0, 0, 0]

                                    if (int(num2[6:]) == int(num1[6:])):

                                        if (int(num2[0:2]) - int(num1[0:2])) < 2:

                                            if (int(num2[0:2]) == int(num1[0:2])):

                                                days = int(num2[3:5]) - int(num1[3:5]) + 1

                                            elif (int(num2[0:2]) > int(num1[0:2])):

                                                for i in range():

                                                    if (int(num1[0:2]) == month_1):

                                                        days = int(num2[3:5]) + (31 - int(num1[3:5])) + 1

                                                        go += 1

                                                    elif (int(num1[0:2]) == month_2):

                                                        days = int(num2[3:5]) + (30 - int(num1[3:5])) + 1

                                                    else:

                                                        if (int(num2[6:]) % 2 == 0):
                                                            days = int(num2[3:5]) + (29 - int(num1[3:5])) + 1

                                                        else:
                                                            days = int(num2[3:5]) + (28 - int(num1[3:5])) + 1

                                            else:
                                                messagebox.showerror('Error',
                                                                     'Checkout month is lesser than checkin month')

                                        else:
                                            messagebox.showerror('Error', 'You cannot Reserve for more than one month')

                                    elif (int(num2[6:]) > int(num1[6:])):

                                        if int(num2[0:2]) == 1:

                                            days = int(num2[3:5]) + (31 - int(num1[3:5])) + 1

                                        else:
                                            messagebox.showerror('Error', 'You cannot Reserve for more than one month')


                                    elif (int(num2[6:]) < int(num1[6:])):
                                        messagebox.showerror('Error', 'Checkout year is lesser than checkin year')

                                    try:

                                        if days < 1:

                                            messagebox.showerror('Error', 'Checkout date is lesser than checkin date')

                                        elif days <= 30:

                                            spinvar7_1.set(days)

                                        else:
                                            messagebox.showerror('Error', 'You cannot Reserve for more than 30 days')

                                    except Exception:
                                        pass

                                    if len(str(spinvar5_2.get())) > 1:
                                        var = spinvar5_2.get()

                                        leng = len(spinvar5_2.get())

                                        spinvar7_2.set(int(spinvar7_1.get()) * (int(var[:leng - 2])))
                                    else:
                                        messagebox.showerror('Error', 'Please check the room rate first..')
                                else:
                                    messagebox.showerror('Error', 'Either checkin or checkout is missing')

                            except Exception as e:

                                pass  # messagebox.showerror('Error', 'Checkin or checkout date is invalid. \n select it correctly')

                        Button(rf_lf1, text="check", command=day_no1).place(x=495, y=495)

                        rf_et7_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar7_2, state=DISABLED)

                        rf_et7_2.place(x=835, y=495)

                        rf_et8_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar8_1)

                        rf_et8_1.place(x=295, y=575)

                        rf_et8_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar8_2, state=DISABLED)

                        rf_et8_2.place(x=835, y=575)

                        p_id_data = db.cursor()

                        p_id_content = "select p_id from registration"

                        p_id_data.execute(p_id_content)

                        p_ids = p_id_data.fetchall()

                        def rate2():
                            try:
                                a = int(spinvar8_1.get())

                                if int(spinvar7_2.get()) != "":

                                    if int(spinvar8_1.get()) > 0:
                                        if int(spinvar7_2.get()) - int(spinvar8_1.get()) > 0:
                                            spinvar8_2.set(int(spinvar7_2.get()) - int(spinvar8_1.get()))
                                        else:
                                            messagebox.showinfo('Info',
                                                                "You don't need to pay more amount than the total amount...")
                                    else:
                                        messagebox.showerror('Error', "Please enter the correct advance amount...")
                                else:
                                    messagebox.showerror('Error', "Please check the number of days")

                            except Exception:
                                messagebox.showerror('Error', "Please enter the correct advance amount...")

                        Button(rf_lf1, text="check", command=rate2).place(x=1035, y=575)

                        def clear_1():
                            spinvar1.set("")
                            spinvar2_1.set("")
                            spinvar2_2.set("")
                            spinvar3_1.set("Select")
                            spinvar3_2.set("")
                            spinvar4_1.set("")
                            spinvar4_2.set("Select")
                            spinvar5_1.set("")
                            spinvar5_2.set("")
                            spinvar6_1.set("")
                            spinvar6_2.set("")
                            spinvar7_1.set("")
                            spinvar7_2.set("")
                            spinvar8_1.set("")
                            spinvar8_2.set("")

                        def checkin_2():

                            go = 0

                            p_id_data = db.cursor()

                            p_id_content = "select p_id from registration"

                            p_id_data.execute(p_id_content)

                            p_ids = p_id_data.fetchall()


                            try:

                                for i in range(len(p_ids)):
                                    if int(str(p_ids[i][0])) == int(spinvar1.get()):
                                        go += 1
                                        break
                                else:
                                    messagebox.showerror('Error',
                                                         'Enter a valid p_id if available else please register it first')

                            except Exception:
                                messagebox.showerror('Error',
                                                     'You cannot use the same id which is already in use')

                            try:

                                a = int(str(spinvar4_1.get()))

                                room_data = db.cursor()

                                content = "select room_no, check1 from room where rm_type = '" + spinvar3_1.get() + "'"

                                room_data.execute(content)

                                table = room_data.fetchall()

                                leng = len(table)

                                avail_room = list()

                                for i in range(len(table)):
                                    if table[i][1] == '-':
                                        print(spinvar4_1.get(), table[i][0])
                                        if spinvar4_1.get() == table[i][0]:
                                            if spinvar2_1.get().isalpha() and spinvar2_1.get() != "" and spinvar2_1.get() != " " and spinvar2_1.get() != "  ":
                                                try:
                                                    a = int(rf_et2_2.get())

                                                    if a > 5:
                                                        messagebox.showerror('Error', 'Enter Proper Adult count')

                                                        go -= 1

                                                    else:
                                                        try:
                                                            a = int(rf_et3_2.get())

                                                            if a > 5:
                                                                messagebox.showerror('Error',
                                                                                     'Enter Proper child count')

                                                                go -= 1

                                                            else:
                                                                if rf_et6_1.get() != "":
                                                                    if rf_et6_2.get() != "":

                                                                        try:
                                                                            a = int(spinvar8_2.get())

                                                                            if int(spinvar8_2.get()) >= 0:

                                                                                go += 1

                                                                            else:
                                                                                messagebox.showerror('Error',
                                                                                                     'Check the balance amount')


                                                                        except Exception:
                                                                            messagebox.showerror('Error',
                                                                                                 'Check the balance amount')

                                                                    else:

                                                                        messagebox.showerror('Error',
                                                                                             'Enter the check out date')

                                                                else:

                                                                    messagebox.showerror('Error',
                                                                                         'Enter the check in date')

                                                        except Exception:
                                                            messagebox.showerror('Error', 'Enter Proper child count')



                                                except Exception:
                                                    messagebox.showerror('Error', 'Enter Proper Adult count')

                                            else:

                                                messagebox.showerror('Error', 'Enter the Guest name correctly')
                                            break

                                else:
                                    messagebox.showerror('Error', 'Enter correct room number')

                            except Exception as e:

                                messagebox.showerror('Error', 'Enter correct room number')


                            if go == 2:
                                c_in_data = db.cursor()

                                content = "insert into c_in_out(p_id, g_name, n_o_a, rm_no, n_o_c, rm_type, discount_type, rm_rate, sub_tot, ch_in, ch_out, n_o_d, total_amount, ad_py, tot_bal) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                    spinvar1.get(), spinvar2_1.get(), rf_et2_2.get(), spinvar4_1.get(), rf_et3_2.get(),
                                    spinvar3_1.get(), spinvar4_2.get(), spinvar5_1.get(),
                                    spinvar5_2.get(), spinvar6_1.get(), spinvar6_2.get(), spinvar7_1.get(),
                                    spinvar7_2.get(),
                                    spinvar8_1.get(), spinvar8_2.get())

                                content3 = "insert into permanent_data(p_id, g_name, n_o_a, rm_no, n_o_c, rm_type, discount_type, rm_rate, sub_tot, ch_in, ch_out, n_o_d, total_amount, ad_py, tot_bal, c_in_check, c_out_check) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                    spinvar1.get(), spinvar2_1.get(), rf_et2_2.get(), spinvar4_1.get(), rf_et3_2.get(),
                                    spinvar3_1.get(), spinvar4_2.get(), spinvar5_1.get(),
                                    spinvar5_2.get(), spinvar6_1.get(), spinvar6_2.get(), spinvar7_1.get(),
                                    spinvar7_2.get(),
                                    spinvar8_1.get(), spinvar8_2.get(), 'yes', 'no')

                                content1 = "update room set check1='/' where room_no='" + spinvar4_1.get() + "'"

                                c_in_data.execute(content)

                                c_in_data.execute(content3)

                                c_in_data.execute(content1)

                                db.commit()

                                test_val = 3

                                messagebox.showinfo("success", "Successfully checked in...")

                                main_frame1.destroy()

                                hotel_reservation2()

                        rf_b1 = Button(rf_lf1, text="Reserve", command=checkin_2, font=("bold", 16),
                                       activeforeground="white", activebackground="black", width=20)
                        rf_b1.place(x=235, y=675)

                        rf_b2 = Button(rf_lf1, text="Clear", command=clear_1, font=("bold", 16),
                                       activeforeground="white",
                                       activebackground="blue", width=20)
                        rf_b2.place(x=635, y=675)

                    Button(left_frame, text="Reservation", command=reservation1, width=15).place(x=90, y=250)

                    # ------------------------------------------------------------------------------------------------------------------------------------------------
                    # ------------------------------------------------------------------------------------------------------------------------------------------------

                    #
                    #
                    #                                           Checkin form
                    def checkin1():

                        spinvar1 = StringVar()

                        spinvar2_1 = StringVar()

                        spinvar2_2 = StringVar()

                        spinvar3_1 = StringVar()

                        spinvar3_2 = StringVar()

                        spinvar4_1 = StringVar()

                        spinvar4_2 = StringVar()

                        spinvar5_1 = StringVar()

                        spinvar5_2 = StringVar()

                        spinvar6_1 = StringVar()

                        spinvar6_2 = StringVar()

                        spinvar7_1 = StringVar()

                        spinvar7_2 = StringVar()

                        spinvar8_1 = StringVar()

                        spinvar8_2 = StringVar()

                        date1 = StringVar()

                        def calendar1():

                            root = Tk()

                            cal = Calendar(root, selectmode="day", year=2020)

                            cal.pack()

                            def grab_date():
                                num1 = cal.get_date()
                                if '/' == num1[1]:
                                    num1 = '0' + num1

                                if '/' == num1[4]:
                                    num1 = num1[0:3] + '0' + num1[3:]

                                date_check = StringVar()

                                date = time.strftime("%d")

                                month = time.strftime("%m")

                                year = time.strftime("%y")

                                date_check.set(month + "/" + date + '/' + year)

                                if date_check.get()[6:] <= num1[6:]:
                                    if date_check.get()[0:2] <= num1[0:2]:
                                        if date_check.get()[3:5] <= num1[3:5]:
                                            spinvar6_1.set(num1)
                                        else:
                                            messagebox.showerror('Error',
                                                                 "You can't book for the date before today's date1")


                                    else:
                                        messagebox.showerror('Error',
                                                             "You can't book for the date before today's date2")

                                else:
                                    messagebox.showerror('Error', "You can't book for the date before today's date3")

                                root.destroy()

                            my_button = Button(root, text="Get Date", command=grab_date)

                            my_button.pack(pady=20)

                            root.mainloop()

                        date2 = StringVar()

                        def calendar1():

                            root = Tk()

                            cal = Calendar(root, selectmode="day", year=2020)

                            cal.pack()

                            def grab_date():
                                num1 = cal.get_date()
                                if '/' == num1[1]:
                                    num1 = '0' + num1

                                if '/' == num1[4]:
                                    num1 = num1[0:3] + '0' + num1[3:]

                                date_check = StringVar()

                                date = time.strftime("%d")

                                month = time.strftime("%m")

                                year = time.strftime("%y")

                                date_check.set(month + "/" + date + '/' + year)

                                if date_check.get()[6:] == num1[6:]:
                                    if date_check.get()[0:2] <= num1[0:2]:
                                        if date_check.get()[3:5] <= num1[3:5]:
                                            spinvar6_1.set(num1)
                                        else:
                                            messagebox.showerror('Error',
                                                                 "You can't book for the date before today's date1")


                                    else:
                                        messagebox.showerror('Error',
                                                             "You can't book for the date before today's date2")

                                elif date_check.get()[6:] < num1[6:]:
                                    spinvar6_1.set(num1)

                                else:
                                    messagebox.showerror('Error', "You can't book for the date before today's date3")


                                root.destroy()

                            my_button = Button(root, text="Get Date", command=grab_date)

                            my_button.pack(pady=20)

                            root.mainloop()

                        date2 = StringVar()

                        def calendar2():

                            if spinvar6_1.get() != "":

                                root = Tk()

                                cal = Calendar(root, selectmode="day", year=2020)

                                cal.pack()

                                def grab_date():

                                    if spinvar6_1.get() != "":

                                        num1 = cal.get_date()
                                        if '/' == num1[1]:
                                            num1 = '0' + num1

                                        if '/' == num1[4]:
                                            num1 = num1[0:3] + '0' + num1[3:]

                                        date_check = StringVar()

                                        date = time.strftime("%d")

                                        month = time.strftime("%m")

                                        year = time.strftime("%y")

                                        date_check.set(month + "/" + date + '/' + year)

                                        if spinvar6_1.get()[6:] == num1[6:]:
                                            if spinvar6_1.get()[0:2] == num1[0:2]:
                                                if spinvar6_1.get()[3:5] <= num1[3:5]:
                                                    spinvar6_2.set(num1)
                                                else:
                                                    messagebox.showerror('Error',
                                                                         "Check out date can't be lesser than check in date")

                                            elif date_check.get()[0:2] < num1[0:2]:
                                                spinvar6_2.set(num1)
                                                
                                            else:
                                                messagebox.showerror('Error',
                                                                     "Check out date can't be lesser than check in date")
                                        elif date_check.get()[6:] < num1[6:]:
                                            spinvar6_2.set(num1)
                                        else:
                                            messagebox.showerror('Error',
                                                                 "Check out date can't be lesser than check in date")

                                        root.destroy()

                                    else:
                                        messagebox.showerror('Error', "Please select the checkin date first")

                                my_button = Button(root, text="Get Date", command=grab_date)

                                my_button.pack(pady=20)

                                root.mainloop()
                            else:
                                messagebox.showerror('Error', "Please select the checkin date first")

                        rf_lf1 = LabelFrame(main_frame1, text="Checkin Form", font=("bold", 22), width=1100, height=810,
                                            fg="white", bg="black")

                        rf_lf1.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 810), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(rf_lf1, image=img)
                        panel.image = img
                        panel.grid(row=0, column=1)

                        #                                  Label declaration

                        rf_lst = ["P_ID ", "  ", "Guest Name ", "No.Of.Adults ", "Room Type ", "No.Of.Children ",
                                  "Room No ", "Discount Type ", "Room Rate(per day)", "Total(per day)",
                                  "Check In Date ", "Check Out Date ", "No.Of.Days ", "Total Amount ",
                                  "Advance Payment ", "Total Balance "]

                        for i in range(len(rf_lst)):

                            if i % 2 == 0:

                                Label(rf_lf1, text=rf_lst[i], font=("bold", 18), bg="skyblue").place(x=45,
                                                                                                     y=15 + (i * 40))

                            else:

                                if i != 1:
                                    Label(rf_lf1, text=rf_lst[i], font=("bold", 18), bg="skyblue").place(x=625,
                                                                                                         y=15 + ((
                                                                                                                             i - 1) * 40))

                        #                                       Entry declaration

                        rf_et1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar1)

                        rf_et1.place(x=295, y=15)

                        rf_et2_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar2_1)

                        rf_et2_1.place(x=295, y=95)

                        rf_et2_2 = Spinbox(rf_lf1, from_=0, to=2, font=("bold", 16))

                        rf_et2_2.place(x=805, y=95)

                        def room_no(a):

                            spinvar4_1.set("Select the room no")

                            room_data = db.cursor()

                            content = "select room_no, check1 from room where rm_type = '" + spinvar3_1.get() + "'"

                            room_data.execute(content)

                            table = room_data.fetchall()

                            leng = len(table)

                            table1 = '"Select"'

                            for i in range(len(table)):
                                if table[i][1] == '-':
                                    table1 = table1 + ',"' + str(table[i][0]) + '"'

                            rf_et4_1 = ttk.Combobox(rf_lf1, textvariable=spinvar4_1, width=30)

                            rf_et4_1['values'] = (eval(table1))

                            rf_et4_1.place(x=295, y=255)

                        spinvar3_1.set("Select")

                        rf_et3_1 = OptionMenu(rf_lf1, spinvar3_1, "AC", "Non-AC", command=room_no)

                        rf_et3_1.place(x=295, y=175)

                        rf_et3_2 = Spinbox(rf_lf1, from_=0, to=3, font=("bold", 16))

                        rf_et3_2.place(x=805, y=175)

                        spinvar4_1.set("Select the room type first")

                        table1 = "'Select'"

                        rf_et4_1 = ttk.Combobox(rf_lf1, textvariable=spinvar4_1, width=30, state=DISABLED)

                        rf_et4_1['values'] = (eval(table1))

                        rf_et4_1.place(x=295, y=255)

                        spinvar4_2.set("None")

                        rf_et4_2 = OptionMenu(rf_lf1, spinvar4_2, "None", "Regular", "VIP")

                        rf_et4_2.place(x=835, y=255)

                        rf_et5_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5_1, state=DISABLED)

                        rf_et5_1.place(x=295, y=335)

                        def rate():

                            rate = db.cursor()

                            content = "select * from discount"

                            rate.execute(content)

                            rate_var = rate.fetchall()

                            if spinvar3_1.get() == "AC":
                                spinvar5_1.set("3000")

                                spinvar5_2.set(str(3000 + (int(rf_et2_2.get()) * 900) + (int(rf_et3_2.get()) * 300)))

                                if spinvar4_2.get() == "Regular":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[1][1] / 100))))

                                elif spinvar4_2.get() == "VIP":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[2][1] / 100))))

                                else:
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[0][1] / 100))))

                            elif spinvar3_1.get() == "Non-AC":
                                spinvar5_1.set("2200")

                                spinvar5_2.set(str(2200 + (int(rf_et2_2.get()) * 800) + (int(rf_et3_2.get()) * 250)))

                                if spinvar4_2.get() == "Regular":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[1][1] / 100))))

                                elif spinvar4_2.get() == "VIP":
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[2][1] / 100))))

                                else:
                                    spinvar5_2.set(
                                        str(int(spinvar5_2.get()) - (int(spinvar5_2.get()) * (rate_var[0][1] / 100))))

                            else:
                                messagebox.showerror("Error", "select room type correctly")

                        Button(rf_lf1, text="check", command=rate).place(x=495, y=335)

                        rf_et5_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5_2, state=DISABLED)

                        rf_et5_2.place(x=835, y=335)

                        rf_et6_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar6_1, state=DISABLED)

                        rf_et6_1.place(x=295, y=415)

                        Button(rf_lf1, text="Select", command=calendar1).place(x=494, y=416)

                        rf_et6_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar6_2, state=DISABLED)

                        rf_et6_2.place(x=835, y=415)

                        Button(rf_lf1, text="Select", command=calendar2).place(x=1035, y=415)

                        rf_et7_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar7_1, state=DISABLED)

                        rf_et7_1.place(x=295, y=495)

                        global go

                        go = 0

                        def day_no1():

                            days = 'asd'

                            try:

                                num1 = spinvar6_1.get()

                                num2 = spinvar6_2.get()

                                if (spinvar6_1.get() != "") and (spinvar6_2.get() != ""):

                                    if '/' == num1[1]:
                                        num1 = '0' + num1

                                    if '/' == num1[4]:
                                        num1 = num1[0:3] + '0' + num1[3:]

                                    if '/' == num2[1]:
                                        num2 = '0' + num2

                                    if '/' == num2[4]:
                                        num2 = num2[0:3] + '0' + num2[3:]

                                    months_1 = [1, 3, 5, 7, 8, 10, 12]

                                    months_2 = [4, 6, 9, 11, 0, 0, 0]

                                    if (int(num2[6:]) == int(num1[6:])):

                                        if (int(num2[0:2]) - int(num1[0:2])) < 2:

                                            if (int(num2[0:2]) == int(num1[0:2])):

                                                days = int(num2[3:5]) - int(num1[3:5]) + 1

                                            elif (int(num2[0:2]) > int(num1[0:2])):

                                                for i in range():

                                                    if (int(num1[0:2]) == month_1):

                                                        days = int(num2[3:5]) + (31 - int(num1[3:5])) + 1

                                                        go += 1

                                                    elif (int(num1[0:2]) == month_2):

                                                        days = int(num2[3:5]) + (30 - int(num1[3:5])) + 1

                                                    else:

                                                        if (int(num2[6:]) % 2 == 0):
                                                            days = int(num2[3:5]) + (29 - int(num1[3:5])) + 1

                                                        else:
                                                            days = int(num2[3:5]) + (28 - int(num1[3:5])) + 1

                                            else:
                                                messagebox.showerror('Error',
                                                                     'Checkout month is lesser than checkin month')

                                        else:
                                            messagebox.showerror('Error', 'You cannot Reserve for more than one month')

                                    elif (int(num2[6:]) > int(num1[6:])):

                                        if int(num2[0:2]) == 1:

                                            days = int(num2[3:5]) + (31 - int(num1[3:5])) + 1

                                        else:
                                            messagebox.showerror('Error', 'You cannot Reserve for more than one month')


                                    elif (int(num2[6:]) < int(num1[6:])):
                                        messagebox.showerror('Error', 'Checkout year is lesser than checkin year')

                                    try:

                                        if days < 1:

                                            messagebox.showerror('Error', 'Checkout date is lesser than checkin date')

                                        elif days <= 30:

                                            spinvar7_1.set(days)

                                        else:
                                            messagebox.showerror('Error', 'You cannot Reserve for more than 30 days')

                                    except Exception:
                                        pass

                                    if len(str(spinvar5_2.get())) > 1:
                                        var = spinvar5_2.get()

                                        leng = len(spinvar5_2.get())

                                        spinvar7_2.set(int(spinvar7_1.get()) * (int(var[:leng - 2])))
                                    else:
                                        messagebox.showerror('Error', 'Please check the room rate first..')
                                else:
                                    messagebox.showerror('Error', 'Either checkin or checkout is missing')

                            except Exception as e:

                                pass  # messagebox.showerror('Error', 'Checkin or checkout date is invalid. \n select it correctly')

                        Button(rf_lf1, text="check", command=day_no1).place(x=495, y=495)

                        rf_et7_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar7_2, state=DISABLED)

                        rf_et7_2.place(x=835, y=495)

                        rf_et8_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar8_1)

                        rf_et8_1.place(x=295, y=575)

                        rf_et8_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar8_2, state=DISABLED)

                        rf_et8_2.place(x=835, y=575)

                        def rate2():
                            try:
                                a = int(spinvar8_1.get())

                                if int(spinvar7_2.get()) != "":

                                    if int(spinvar8_1.get()) > 0:
                                        if int(spinvar7_2.get()) - int(spinvar8_1.get()) > 0:
                                            spinvar8_2.set(int(spinvar7_2.get()) - int(spinvar8_1.get()))
                                        else:
                                            messagebox.showinfo('Info',
                                                                "You don't need to pay more amount than the total amount...")
                                    else:
                                        messagebox.showerror('Error', "Please enter the correct advance amount...")
                                else:
                                    messagebox.showerror('Error', "Please check the number of days")

                            except Exception:
                                messagebox.showerror('Error', "Please enter the correct advance amount...")

                        Button(rf_lf1, text="check", command=rate2).place(x=1035, y=575)

                        def clear_1():
                            spinvar1.set("")
                            spinvar2_1.set("")
                            spinvar2_2.set("")
                            spinvar3_1.set("Slect")
                            spinvar3_2.set("")
                            spinvar4_1.set("")
                            spinvar4_2.set("Select")
                            spinvar5_1.set("")
                            spinvar5_2.set("")
                            spinvar6_1.set("")
                            spinvar6_2.set("")
                            spinvar7_1.set("")
                            spinvar7_2.set("")
                            spinvar8_1.set("")
                            spinvar8_2.set("")

                        def checkin_2():
                            go = 0

                            p_id_data = db.cursor()

                            p_id_content = "select p_id from registration"

                            p_id_data.execute(p_id_content)

                            p_ids = p_id_data.fetchall()


                            try:

                                for i in range(len(p_ids)):
                                    if int(str(p_ids[i][0])) == int(spinvar1.get()):
                                        go += 1
                                        break
                                else:
                                    messagebox.showerror('Error',
                                                         'Enter a valid p_id if available else please register it first')

                            except Exception:
                                messagebox.showerror('Error',
                                                     'You cannot use the same id which is already in use')

                            try:

                                a = int(str(spinvar4_1.get()))

                                room_data = db.cursor()

                                content = "select room_no, check1 from room where rm_type = '" + spinvar3_1.get() + "'"

                                room_data.execute(content)

                                table = room_data.fetchall()

                                leng = len(table)

                                avail_room = list()

                                for i in range(len(table)):
                                    if table[i][1] == '-':
                                        print(spinvar4_1.get(), table[i][0])
                                        if spinvar4_1.get() == table[i][0]:
                                            if spinvar2_1.get().isalpha() and spinvar2_1.get() != "" and spinvar2_1.get() != " " and spinvar2_1.get() != "  ":
                                                try:
                                                    a = int(rf_et2_2.get())

                                                    if a > 5:
                                                        messagebox.showerror('Error', 'Enter Proper Adult count')

                                                        go -= 1

                                                    else:
                                                        try:
                                                            a = int(rf_et3_2.get())

                                                            if a > 5:
                                                                messagebox.showerror('Error',
                                                                                     'Enter Proper child count')

                                                                go -= 1

                                                            else:
                                                                if rf_et6_1.get() != "":
                                                                    if rf_et6_2.get() != "":

                                                                        try:
                                                                            a = int(spinvar8_2.get())

                                                                            if int(spinvar8_2.get()) >= 0:

                                                                                go += 1

                                                                            else:
                                                                                messagebox.showerror('Error',
                                                                                                     'Check the balance amount')


                                                                        except Exception:
                                                                            messagebox.showerror('Error',
                                                                                                 'Check the balance amount')

                                                                    else:

                                                                        messagebox.showerror('Error',
                                                                                             'Enter the check out date')

                                                                else:

                                                                    messagebox.showerror('Error',
                                                                                         'Enter the check in date')

                                                        except Exception:
                                                            messagebox.showerror('Error', 'Enter Proper child count')



                                                except Exception:
                                                    messagebox.showerror('Error', 'Enter Proper Adult count')

                                            else:

                                                messagebox.showerror('Error', 'Enter the Guest name correctly')
                                            break

                                else:
                                    messagebox.showerror('Error', 'Enter correct room number')

                            except Exception as e:

                                messagebox.showerror('Error', 'Enter correct room number')


                            if go == 2:
                                c_in_data = db.cursor()

                                content = "insert into c_in_out(p_id, g_name, n_o_a, rm_no, n_o_c, rm_type, discount_type, rm_rate, sub_tot, ch_in, ch_out, n_o_d, total_amount, ad_py, tot_bal) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                    spinvar1.get(), spinvar2_1.get(), rf_et2_2.get(), spinvar4_1.get(), rf_et3_2.get(),
                                    spinvar3_1.get(), spinvar4_2.get(), spinvar5_1.get(),
                                    spinvar5_2.get(), spinvar6_1.get(), spinvar6_2.get(), spinvar7_1.get(),
                                    spinvar7_2.get(),
                                    spinvar8_1.get(), spinvar8_2.get())

                                content3 = "insert into permanent_data(p_id, g_name, n_o_a, rm_no, n_o_c, rm_type, discount_type, rm_rate, sub_tot, ch_in, ch_out, n_o_d, total_amount, ad_py, tot_bal, c_in_check, c_out_check) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                    spinvar1.get(), spinvar2_1.get(), rf_et2_2.get(), spinvar4_1.get(), rf_et3_2.get(),
                                    spinvar3_1.get(), spinvar4_2.get(), spinvar5_1.get(),
                                    spinvar5_2.get(), spinvar6_1.get(), spinvar6_2.get(), spinvar7_1.get(),
                                    spinvar7_2.get(),
                                    spinvar8_1.get(), spinvar8_2.get(), 'yes', 'no')

                                content1 = "update room set check1='/' where room_no='" + spinvar4_1.get() + "'"

                                c_in_data.execute(content)

                                c_in_data.execute(content3)

                                c_in_data.execute(content1)

                                db.commit()

                                test_val = 3

                                messagebox.showinfo("success", "Successfully checked in...")

                                main_frame1.destroy()

                                hotel_reservation2()

                        rf_b1 = Button(rf_lf1, text="Checkin", command=checkin_2, font=("bold", 16),
                                       activeforeground="white", activebackground="black", width=20)
                        rf_b1.place(x=235, y=675)

                        rf_b2 = Button(rf_lf1, text="Clear", command=clear_1, font=("bold", 16),
                                       activeforeground="white",
                                       activebackground="blue", width=20)
                        rf_b2.place(x=635, y=675)

                    Button(left_frame, text="Check in", command=checkin1, width=15).place(x=90, y=350)

                    #
                    #
                    #                                                Checkout form
                    def checkout1():

                        spinvar1 = StringVar()

                        spinvar2_1 = StringVar()

                        spinvar2_2 = StringVar()

                        spinvar3_1 = StringVar()

                        spinvar3_2 = StringVar()

                        spinvar4_1 = StringVar()

                        spinvar4_2 = StringVar()

                        spinvar5_1 = StringVar()

                        spinvar5_2 = StringVar()

                        spinvar6_1 = StringVar()

                        spinvar6_2 = StringVar()

                        spinvar7_1 = StringVar()

                        spinvar7_2 = StringVar()

                        spinvar8_1 = StringVar()

                        spinvar8_2 = StringVar()

                        entry10 = StringVar()

                        rf_lf1 = LabelFrame(main_frame1, text="Checkout Form", font=("bold", 22), width=1100,
                                            height=810,
                                            fg="white", bg="black")

                        rf_lf1.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 810), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(rf_lf1, image=img)
                        panel.image = img
                        panel.grid(row=0, column=1)

                        #                                  Label declaration

                        rf_lst = ["P_ID ", "  ", "Guest Name ", "No.Of.Adults ", "Room Type ", "No.Of.Children ",
                                  "Room No ", "Discount Type ", "Room Rate(per day)", "Total(per day)",
                                  "Check In Date ", "Check Out Date ", "No.Of.Days ", "Total Amount ",
                                  "Advance Payment ", "Total Balance "]

                        for i in range(len(rf_lst)):

                            if i % 2 == 0:

                                Label(rf_lf1, text=rf_lst[i], font=("bold", 18), bg="skyblue").place(x=45,
                                                                                                     y=15 + (i * 40))

                            else:

                                if i != 1:
                                    Label(rf_lf1, text=rf_lst[i], font=("bold", 18), bg="skyblue").place(x=625,
                                                                                                         y=15 + ((
                                                                                                                             i - 1) * 40))

                        #                                       Entry declaration

                        rf_et1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar1)

                        rf_et1.place(x=295, y=15)

                        rf_et2_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar2_1, state=DISABLED)

                        rf_et2_1.place(x=295, y=95)

                        rf_et2_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar2_2, state=DISABLED)

                        rf_et2_2.place(x=835, y=95)

                        rf_et3_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar3_1, state=DISABLED)

                        rf_et3_1.place(x=295, y=175)

                        rf_et3_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar3_2, state=DISABLED)

                        rf_et3_2.place(x=835, y=175)

                        rf_et4_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar4_1, state=DISABLED)

                        rf_et4_1.place(x=295, y=255)

                        rf_et4_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar4_2, state=DISABLED)

                        rf_et4_2.place(x=835, y=255)

                        rf_et5_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5_1, state=DISABLED)

                        rf_et5_1.place(x=295, y=335)

                        rf_et5_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar5_2, state=DISABLED)

                        rf_et5_2.place(x=835, y=335)

                        rf_et6_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar6_1, state=DISABLED)

                        rf_et6_1.place(x=295, y=415)

                        rf_et6_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar6_2, state=DISABLED)

                        rf_et6_2.place(x=835, y=415)

                        rf_et7_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar7_1, state=DISABLED)

                        rf_et7_1.place(x=295, y=495)

                        rf_et7_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar7_2, state=DISABLED)

                        rf_et7_2.place(x=835, y=495)

                        rf_et8_1 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar8_1, state=DISABLED)

                        rf_et8_1.place(x=295, y=575)

                        rf_et8_2 = Entry(rf_lf1, font=("bold", 16), textvariable=spinvar8_2, state=DISABLED)

                        rf_et8_2.place(x=835, y=575)

                        def clear_1():
                            spinvar1.set("")
                            spinvar2_1.set("")
                            spinvar2_2.set("")
                            spinvar3_1.set("")
                            spinvar3_2.set("")
                            spinvar4_1.set("")
                            spinvar4_2.set("")
                            spinvar5_1.set("")
                            spinvar5_2.set("")
                            spinvar6_1.set("")
                            spinvar6_2.set("")
                            spinvar7_1.set("")
                            spinvar7_2.set("")
                            spinvar8_1.set("")
                            spinvar8_2.set("")

                        def verify():

                            try:
                                c_out_data = db.cursor()

                                content = "select p_id, g_name, n_o_a, rm_type, n_o_c, rm_no, discount_type, rm_rate, sub_tot, ch_in, ch_out, n_o_d, total_amount, ad_py, tot_bal from c_in_out where p_id = '" + str(
                                    rf_et1.get()) + "'"

                                c_out_data.execute(content)

                                data = c_out_data.fetchall()

                                data1 = data[0]

                                spinvar1.set(data1[0])

                                spinvar2_1.set(data1[1])

                                spinvar2_2.set(data1[2])

                                spinvar3_1.set(data1[3])

                                spinvar3_2.set(data1[4])

                                spinvar4_1.set(data1[5])

                                spinvar4_2.set(data1[6])

                                spinvar5_1.set(data1[7])

                                spinvar5_2.set(data1[8])

                                spinvar6_1.set(data1[9])

                                spinvar6_2.set(data1[10])

                                spinvar7_1.set(data1[11])

                                spinvar7_2.set(data1[12])

                                spinvar8_1.set(data1[13])

                                spinvar8_2.set(data1[14])

                                entry10.set(spinvar8_2.get())

                            except Exception as e:

                                print(e)
                                messagebox.showwarning("Warning", "No transaction id found. Enter a valid one")

                        Button(rf_lf1, text="Verify", command=verify).place(x=495, y=15)

                        def checkout_1():
                            if spinvar2_1.get() != "":

                                c_out_data = db.cursor()

                                content1 = "update room set check1='-' where room_no='" + spinvar4_1.get() + "'"

                                content2 = "delete from c_in_out where p_id='" + spinvar1.get() + "'"

                                content3 = "update permanent_data set c_out_check='yes' where p_id ='" + spinvar1.get() + "'"

                                c_out_data.execute(content1)

                                c_out_data.execute(content2)

                                c_out_data.execute(content3)

                                db.commit()

                                messagebox.showinfo("Success", "Checked out successfully")

                                main_frame1.destroy()

                                hotel_reservation2()

                            else:
                                messagebox.showwarning("Warning", "Enter all details")

                        Label(rf_lf1, text="Change", font=("bold", 16)).place(x=45, y=655)

                        co_et9_2 = Entry(rf_lf1, textvariable=entry10, font=("bold", 16), state=DISABLED)

                        co_et9_2.place(x=235, y=655)

                        Button(rf_lf1, text="checkout", command=checkout_1, font=("bold", 18), bg="skyblue").place(
                            x=605,
                            y=715)

                    Button(left_frame, text="Check out", command=checkout1, width=15).place(x=90, y=450)

                    #
                    #
                    #                                          Discount form
                    def discount1():

                        right_frame6 = LabelFrame(main_frame1, text="Discount update", width=1100, height=850,
                                                  font=("ariel", 30, "italic"), fg="blue")

                        right_frame6.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 850), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(right_frame6, image=img)
                        panel.image = img
                        panel.place(x=0, y=0)

                        Label(right_frame6, text="Discount Type ", font=("Bold", 18), bg="skyblue", fg="black").place(
                            x=105,
                            y=205)

                        Label(right_frame6, text="Discount Percent ", font=("Bold", 18), bg="skyblue",
                              fg="black").place(
                            x=105,
                            y=305)

                        combo_var2 = StringVar()

                        combo_entry1 = ttk.Combobox(right_frame6, textvariable=combo_var2, font=("ariel", 15), width=18)

                        combo_entry1['values'] = ("None", "Regular", "VIP")

                        combo_entry1.place(x=605, y=205)

                        combo_var3 = StringVar()

                        discount_entry2 = Entry(right_frame6, font=("ariel", 15), textvariable=combo_var3)

                        discount_entry2.place(x=605, y=305)

                        def update():
                            if combo_var2.get() == "None" or combo_var2.get() == "Regular" or combo_var2.get() == "VIP":
                                try:
                                    a = int(combo_var3.get())
                                    if len(combo_var3.get()) == 2 or len(combo_var3.get()) == 1:
                                        if int(combo_var3.get()) > 0:

                                            update_data = db.cursor()

                                            content = "update discount set dis_amount=" + str(
                                                discount_entry2.get()) + " where dis_type ='" + str(
                                                combo_var2.get()) + "'"

                                            update_data.execute(content)

                                            db.commit()

                                            messagebox.showinfo("Success", "Discount change successfully updated")
                                        else:
                                            messagebox.showerror("Error", "Enter the Discount percentage correctly")

                                    else:
                                        messagebox.showerror("Error", "Enter the Discount percentage correctly")

                                except Exception:
                                    messagebox.showerror("Error", "Enter the Discount Percentage correctly")

                            else:
                                messagebox.showerror("Error", "Select the Discount type correctly")

                        Button(right_frame6, text="Update", font=("ariel", 15), command=update).place(x=155, y=405)

                        def cancel():
                            main_frame1.destroy()

                            hotel_reservation2()

                        Button(right_frame6, text="Cancel", font=("ariel", 15), command=cancel).place(x=705, y=405)

                    Button(left_frame, text="discount", command=discount1, width=15).place(x=90, y=550)

                    #
                    #
                    #                                           Room form
                    def room1():

                        right_frame7 = LabelFrame(main_frame1, text="Room update", width=1100, height=850,
                                                  font=("ariel", 30, "italic"), fg="blue")

                        right_frame7.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 850), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(right_frame7, image=img)
                        panel.image = img
                        panel.place(x=0, y=0)

                        Label(right_frame7, text="New Room ", font=("italic", 20, "bold"), bg="skyblue",
                              fg="black").place(
                            x=105, y=145)

                        Label(right_frame7, text="Room Number ", font=("italic", 16), bg="skyblue", fg="black").place(
                            x=105,
                            y=245)

                        Label(right_frame7, text="Room type ", font=("italic", 16), bg="skyblue", fg="black").place(
                            x=105,
                            y=345)

                        Label(right_frame7, text="Room Rate ", font=("italic", 16), bg="skyblue", fg="black").place(
                            x=105,
                            y=445)

                        Label(right_frame7, text="No.of.Occompany ", font=("italic", 16), bg="skyblue",
                              fg="black").place(
                            x=105,
                            y=545)

                        room_entry1 = Entry(right_frame7, font=("ariel", 15))

                        room_entry1.place(x=605, y=245)

                        combo_var1 = StringVar()

                        def val(arg):
                            if combo_var1.get() == "AC":
                                spinbox2.set("3000")
                            elif combo_var1.get() == "Non-AC":
                                spinbox2.set("2250")

                        combo_var1.set("Select")

                        combo_entry2 = OptionMenu(right_frame7, combo_var1, "AC", "Non-AC", command=val)

                        combo_entry2.place(x=605, y=345)

                        spinbox2 = StringVar()

                        room_entry3 = Entry(right_frame7, textvariable=spinbox2, font=("ariel", 15), state=DISABLED)

                        room_entry3.place(x=605, y=445)

                        spinbox1 = StringVar()

                        spinbox1.set("5")

                        spin_entry4 = Spinbox(right_frame7, textvariable=spinbox1, from_=0, to=10, font=("ariel", 15),
                                              state=DISABLED)

                        spin_entry4.place(x=605, y=545)

                        def update():

                            if len(room_entry1.get()) <= 3 and len(room_entry1.get()) > 0:

                                try:
                                    a = int(room_entry1.get())

                                    if int(room_entry1.get()) > 0:

                                        if combo_var1.get() == "AC" or combo_var1.get() == "Non-AC":

                                            room_data = db.cursor()

                                            content = 'insert into room values("{}", "{}", "{}", "{}", "{}")'.format(
                                                room_entry1.get(), '-', room_entry3.get(), combo_var1.get(),
                                                spinbox1.get())

                                            room_data.execute(content)

                                            db.commit()

                                            messagebox.showinfo("Success", "Room change successfully updated")
                                        else:
                                            messagebox.showerror("Error", "Select the room type correctly")
                                    else:
                                        messagebox.showerror("Error", "Enter a valid room number correctly")

                                except Exception:
                                    messagebox.showerror("Error", "Enter a valid room number correctly")

                            else:
                                messagebox.showerror("Error", "Enter a valid room number correctly")

                        def room_list1():

                            room_data = db.cursor()

                            content = 'select * from room'

                            room_data.execute(content)

                            data_collection = room_data.fetchall()

                            room_list = Tk()

                            room_list.title("Room List")

                            lbl_fr1 = LabelFrame(room_list, text="Room List", font=("ariel", 16))

                            lbl_fr1.grid(row=1, column=1)

                            Label(lbl_fr1, text="Room No ", font=("ariel", 16)).grid(row=1, column=1)

                            Label(lbl_fr1, text="Room Status ", font=("ariel", 16)).grid(row=1, column=2)

                            Label(lbl_fr1, text="Room Rent ", font=("ariel", 16)).grid(row=1, column=3)

                            Label(lbl_fr1, text="Room Type ", font=("ariel", 16)).grid(row=1, column=4)

                            Label(lbl_fr1, text="Maximum occumpany ", font=("ariel", 16)).grid(row=1, column=5)

                            for i in range(len(data_collection)):
                                for j in range(len(data_collection[0])):

                                    if j != 1:
                                        Label(lbl_fr1, text=data_collection[i][j], font=("ariel", 16)).grid(row=i + 2,
                                                                                                            column=j + 1)

                                    else:
                                        if data_collection[i][j] == '-':
                                            Label(lbl_fr1, text="Free", font=("ariel", 16)).grid(row=i + 2,
                                                                                                 column=j + 1)
                                        else:
                                            Label(lbl_fr1, text="Booked", font=("ariel", 16)).grid(row=i + 2,
                                                                                                   column=j + 1)

                        def cancel_2():

                            main_frame1.destroy()

                            hotel_reservation2()

                        Button(right_frame7, text="Update", font=("ariel", 15), command=update).place(x=155, y=645)

                        Button(right_frame7, text="Cancel", font=("ariel", 15), command=cancel_2).place(x=405, y=645)

                        Button(right_frame7, text="Room list", font=("ariel", 15), command=room_list1).place(x=655,
                                                                                                             y=645)

                    Button(left_frame, text="Room alter", command=room1, width=15).place(x=90, y=650)

                    #
                    #
                    #                                           Search form
                    def search1():

                        right_frame8 = LabelFrame(main_frame1, text="Search", width=1100, height=850,
                                                  font=("ariel", 30, "italic"), fg="blue")

                        right_frame8.grid(row=0, column=1)

                        top_frame1 = LabelFrame(right_frame8, width=1100, height=200)

                        top_frame1.grid(row=0, column=1)

                        x = "back1.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 200), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(top_frame1, image=img)
                        panel.image = img
                        panel.place(x=0, y=0)

                        bottom_frame1 = LabelFrame(right_frame8, width=1100, height=600)

                        bottom_frame1.grid(row=1, column=1)

                        x = "search list.jpg"
                        img = Image.open(x)
                        img = img.resize((1100, 600), Image.ANTIALIAS)
                        img = ImageTk.PhotoImage(img)
                        panel = Label(bottom_frame1, image=img)
                        panel.image = img
                        panel.place(x=0, y=0)

                        Label(top_frame1, text="Customer search ", font=("ariel", 20, "italic", "bold")).place(x=15,
                                                                                                               y=50)

                        Label(top_frame1, text="Search by Name ", font=("ariel", 16)).place(x=15, y=130)

                        Label(top_frame1, text="Search by Date ", font=("ariel", 16)).place(x=605, y=130)

                        search_entry1 = Entry(top_frame1, font=("ariel", 15))

                        search_entry1.place(x=200, y=130)

                        search_entry2 = Entry(top_frame1, font=("ariel", 15))

                        search_entry2.place(x=775, y=130)

                        def search1():

                            result_frame1 = LabelFrame(bottom_frame1, width=1100, height=600)

                            result_frame1.place(x=120, y=150)

                            gt_lst = ['P_id', 'Person Name ', 'Room No ', 'Check In  ', 'Check Out']

                            gt_lf1 = LabelFrame(result_frame1, text="GUEST LIST", font=("bold", 30))

                            gt_lf1.grid(row=1, column=1)

                            for i in range(len(gt_lst)):
                                Label(result_frame1, text="  ", font=("italic", 25)).grid(row=1, column=i * 2)

                                Label(result_frame1, text=gt_lst[i], font=("italic", 25)).grid(row=1, column=i * 2 + 1)

                            try:

                                search_data = db.cursor()

                                content = "select p_id, g_name, rm_no, ch_in, ch_out  from c_in_out where g_name='" + search_entry1.get() + "'"

                                search_data.execute(content)

                                text1 = search_data.fetchall()

                                lent = len(text1)
                                lent1 = len(text1[0])

                                for i in range(lent):
                                    for j in range(lent1):
                                        Label(result_frame1, text="  ", font=("italic", 25)).grid(row=i + 2,
                                                                                                  column=j * 2)

                                        Label(result_frame1, text=text1[i][j], font=("ariel", 17)).grid(row=i + 2,
                                                                                                        column=(
                                                                                                                           j * 2) + 1)

                            except Exception:
                                Label(bottom_frame1, text="No match found", font=("italic", 25), bg="white").place(
                                    x=130,
                                    y=210)

                        def search2():

                            result_frame1 = LabelFrame(bottom_frame1, width=1100, height=600)

                            result_frame1.place(x=120, y=150)

                            gt_lst = ['P_id', 'Person Name ', 'Room No ', 'Check In  ', 'Check Out']

                            gt_lf1 = LabelFrame(result_frame1, text="GUEST LIST", font=("bold", 30))

                            gt_lf1.grid(row=1, column=1)

                            for i in range(len(gt_lst)):
                                Label(result_frame1, text="  ", font=("italic", 25)).grid(row=1, column=i * 2)

                                Label(result_frame1, text=gt_lst[i], font=("italic", 25)).grid(row=1, column=i * 2 + 1)

                            try:

                                search_data = db.cursor()

                                content = "select p_id, g_name, rm_no, ch_in, ch_out  from c_in_out where ch_in='" + search_entry2.get() + "'"

                                search_data.execute(content)

                                text1 = search_data.fetchall()

                                lent = len(text1)
                                lent1 = len(text1[0])

                                for i in range(lent):
                                    for j in range(lent1):
                                        Label(result_frame1, text="  ", font=("italic", 25)).grid(row=i + 2,
                                                                                                  column=j * 2)

                                        Label(result_frame1, text=text1[i][j], font=("ariel", 17)).grid(row=i + 2,
                                                                                                        column=(
                                                                                                                           j * 2) + 1)

                            except Exception:
                                Label(bottom_frame1, text="No match found", font=("italic", 25), bg="white").place(
                                    x=130,
                                    y=210)

                        def history():

                            history1 = Toplevel()

                            history1.title("History")

                            result_frame1 = LabelFrame(history1, width=1100, height=600)

                            result_frame1.grid(row=0, column=0)

                            gt_lst = ['P_id', 'Person Name ', 'Room No ', 'Check In  ', 'Check Out', 'Checkin status', 'checkout status']

                            gt_lf1 = LabelFrame(result_frame1, text="customer LIST", font=("bold", 30))

                            gt_lf1.grid(row=1, column=1)

                            for i in range(len(gt_lst)):
                                Label(result_frame1, text="  ", font=("italic", 25)).grid(row=1, column=i * 2)

                                Label(result_frame1, text=gt_lst[i], font=("italic", 25)).grid(row=1, column=i * 2 + 1)

                            try:

                                search_data = db.cursor()

                                content = "select p_id, g_name, rm_no, ch_in, ch_out, c_in_check, c_out_check  from permanent_data"

                                search_data.execute(content)

                                text1 = search_data.fetchall()

                                lent = len(text1)
                                lent1 = len(text1[0])

                                for i in range(lent):
                                    for j in range(lent1):
                                        Label(result_frame1, text="  ", font=("italic", 25)).grid(row=i + 2,
                                                                                                  column=j * 2)

                                        Label(result_frame1, text=text1[i][j], font=("ariel", 17)).grid(row=i + 2,
                                                                                                        column=(
                                                                                                                           j * 2) + 1)

                            except Exception:
                                Label(history1, text="No match found", font=("italic", 25), bg="white").place(x=40,
                                                                                                              y=50)

                        Button(top_frame1, text="History", command=history).place(x=1030, y=0)

                        Button(top_frame1, text="search", command=search1).place(x=422, y=131)

                        Button(top_frame1, text="search", command=search2).place(x=997, y=131)

                    Button(left_frame, text="Search", command=search1, width=15).place(x=90, y=750)

                hotel_reservation2()
            else:
                messagebox.showerror("Incorrect", "Username or password is incorrect")
        except Exception as e:
            print(e)
            messagebox.showerror("Incorrect", "Username or password is incorrect")

    #                                                           TOP FRAME

    Button(inner_frame, text="login", width=20, font=("ariel", 14, "italic"), command=hotel_reservation1).place(x=920,
                                                                                                                y=100)

    #                                                           BOTTOM FRAME

    bottom_frame = LabelFrame(main_frame, width=1200, height=600)

    bottom_frame.grid(row=1, column=0)

    x = "hotel2.jpg"
    img = Image.open(x)
    img = img.resize((1200, 650), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(bottom_frame, image=img)
    panel.image = img
    panel.pack()

    Label(bottom_frame, text="TAJ HOTEL WELCOMES YOU", font=("ariel", 35, "italic", "bold"), bd=4, bg="khaki").place(
        x=200, y=50)

    #                                                          INSIDE BOTTOM FRAME - LEFT FRAME

    left_frame = LabelFrame(bottom_frame, width=300, height=400, bd=4)

    left_frame.place(x=120, y=180)

    x = "hotel2.jpg"
    img = Image.open(x)
    img = img.resize((320, 420), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(left_frame, image=img)
    panel.image = img
    panel.pack()

    Label(left_frame, text="* Best offers", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=15)

    Label(left_frame, text="* High tech hotel ", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=75)

    Label(left_frame, text="* Swiming pool", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=135)

    Label(left_frame, text="* Free wifi", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=195)

    Label(left_frame, text="* Five stared hotel", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=255)

    Label(left_frame, text="* Fascinating rooms", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=315)

    #                                                          INSIDE BOTTOM FRAME - RIGHT FRAME

    right_frame = LabelFrame(bottom_frame, width=320, height=400, bd=4)

    right_frame.place(x=700, y=180)

    x = "hotel2.jpg"
    img = Image.open(x)
    img = img.resize((340, 420), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(right_frame, image=img)
    panel.image = img
    panel.pack()

    Label(right_frame, text="* Children play area", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=15)

    Label(right_frame, text="* Friendly lobby", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=75)

    Label(right_frame, text="* Night Camp fire", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=135)

    Label(right_frame, text="* Nature friendly rooms", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=195)

    Label(right_frame, text="* Nearby Airport", font=("ariel", 20, "italic"), fg="blue").place(x=15, y=255)

    main_window.mainloop()


# ================================================= File validation  =======================================================
# ================================ To check whether the function call is called from the main file =========================
if __name__ == "__main__":
    main_screen()