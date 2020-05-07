from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_Software:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        title=Label(self.root,text='Billing Software',bd=12,relief=GROOVE,bg="grey",fg="black",font="lucide 30 bold",pady=2).pack(fill=X)
        ########## Variable ##############
        #   cosmatic var
        self.soap=IntVar()
        self.facecream=IntVar()
        self.facewash=IntVar()
        self.Hairspray=IntVar()
        self.Hairgell=IntVar()
        self.Bodyloshan=IntVar()
        # grocery var
        self.rice=IntVar()
        self.foodoil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.Tea=IntVar()
        # cold drinks var
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.slice=IntVar()
        self.ThumbsUp=IntVar()
        self.sprite=IntVar()
        ########## total product price $ tax
        self.cosmeticsPrice=StringVar()
        self.groceryPrice=StringVar()
        self.colddrinkPrice=StringVar()

        self.cosmatictax=StringVar()
        self.grocerytax=StringVar()
        self.colddrinktax=StringVar()

        self.cus_name=StringVar()
        self.cus_phn=StringVar()
        self.billNo=StringVar()
        x=random.randint(1000,9999)
        self.billNo.set(str(x))
        self.search_bill=StringVar()


        ########## customer info frame 1


        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text='Customer Detail',bg='grey',fg='gold',font='lucide 15 bold')
        F1.place(x=0,y=80,relwidth=1)

        cname_label=Label(F1,text='Customer name',bg='grey',fg="black",font="lucide 18 bold").grid(row=0,column=0,padx=20,pady=5)
        cname_Entry=Entry(F1,width=16,textvariable=self.cus_name,bd=7,relief=SUNKEN,font='aerial 10').grid(row=0,column=1,pady=5,padx=10)

        PhoneNo_label = Label(F1, text='Customer Phone No', bg='grey', fg="black", font="lucide 18 bold").grid(row=0,column=2,padx=20,pady=5)
        PhoneNo_Entry = Entry(F1, width=16,textvariable=self.cus_phn, bd=7, relief=SUNKEN,font='aerial 10').grid(row=0, column=3, pady=5,padx=10)

        bill_label = Label(F1, text='Bill Number', bg='grey', fg="black", font="lucide 18 bold").grid(row=0,column=4,padx=20,pady=5)
        bill_Entry = Entry(F1, width=16,textvariable=self.search_bill, bd=7, relief=SUNKEN,font='aerial 10').grid(row=0, column=5,pady=5,padx=10)

        bill_btn=Button(F1,text='Search',command=self.find_bill,width=10,bd=6,font="lucide 9 bold").grid(row=0,column=6,pady=10,padx=10)

        #################### Cosmatic Frame 2

        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text='Cosmetic',bg='grey',fg='gold',font='lucide 15 bold')
        F2.place(x=3,y=170,width=300,height=350)

        Soap_Label=Label(F2,text='Soap',bg='grey',fg="lightgreen",font="lucide 14 bold").grid(row=0,column=0,padx=10,pady=10,sticky='w')
        Soap_Entry=Entry(F2,width=10,textvariable=self.soap,bd=5,relief=SUNKEN,font='lucide 14 bold ').grid(row=0,column=1,pady=10,padx=10)

        FaceCream_Label = Label(F2, text='Face Cream', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=1, column=0,padx=10, pady=10,sticky='w')
        FaceCream_Entry = Entry(F2, width=10,textvariable=self.facecream, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=1, column=1, pady=10,padx=10)

        FaceWash_Label = Label(F2, text='Face Wash', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        FaceWash_Entry = Entry(F2, width=10,textvariable=self.facewash, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=2, column=1,pady=10, padx=10)

        HairSpray_Label = Label(F2, text='Hair Spray', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        HairSpray_Entry = Entry(F2, width=10,textvariable=self.Hairspray, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=3, column=1,pady=10, padx=10)

        HairGel_Label = Label(F2, text='Hair Gel', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        HairGel_Entry = Entry(F2, width=10,textvariable=self.Hairgell, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=4, column=1,pady=10, padx=10)

        Bodyloshan_label = Label(F2, text='Body Loshan', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        Bodyloshan_Entry = Entry(F2, width=10,textvariable=self.Bodyloshan, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=5, column=1,pady=10, padx=10)


        ################## Grocery Frame 3
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text='Grocery', bg='grey', fg='gold', font='lucide 15 bold')
        F3.place(x=303, y=170, width=300, height=350)

        Rice_Label = Label(F3, text='Rice', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=0, column=0,padx=10, pady=10,sticky='w')
        Rice_Entry = Entry(F3, width=10,textvariable=self.rice, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=0, column=1, pady=10,padx=10)

        Foodoil_Label = Label(F3, text='Food Oil', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        Foodoil_Entry = Entry(F3, width=10,textvariable=self.foodoil, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=1, column=1,pady=10, padx=10)

        Daal_label = Label(F3, text='Daal', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        Daal_Entry = Entry(F3, width=10,textvariable=self.daal, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=2, column=1, pady=10,padx=10)

        Wheat_Label = Label(F3, text='Wheat', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        Wheat_Entry = Entry(F3, width=10,textvariable=self.wheat, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=3, column=1,pady=10, padx=10)

        Sugar_Label = Label(F3, text='Sugar', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Sugar_Entry = Entry(F3, width=10,textvariable=self.sugar, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=4, column=1, pady=10,padx=10)

        Tea_label = Label(F3, text='Tea', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=5,column=0,padx=10,pady=10,sticky='w')
        Tea_Entry = Entry(F3, width=10,textvariable=self.Tea, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=5, column=1,pady=10, padx=10)

        ########### Cold drink frame 4
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text='Cold Drink', bg='grey', fg='gold', font='lucide 15 bold')
        F4.place(x=603, y=170, width=300, height=350)

        Maza_Label = Label(F4, text='Maza', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=0, column=0,padx=10, pady=10,sticky='w')
        Maza_Entry = Entry(F4, width=10,textvariable=self.maza, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=0, column=1, pady=10,padx=10)

        Cock_Label = Label(F4, text='Cock', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=1,column=0,padx=10,pady=10,sticky='w')
        Cock_Entry = Entry(F4, width=10,textvariable=self.cock, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=1, column=1,pady=10, padx=10)

        Frooti_Label = Label(F4, text='Frooti', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=2,column=0,padx=10,pady=10,sticky='w')
        Frooti_Entry = Entry(F4, width=10,textvariable=self.frooti, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=2, column=1, pady=10,padx=10)

        Slice_Label = Label(F4, text='Slice', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=3,column=0,padx=10,pady=10,sticky='w')
        Slice_Entry = Entry(F4, width=10,textvariable=self.slice, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=3, column=1,pady=10, padx=10)

        Thumbsup_Label = Label(F4, text='Thumbs Up', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Thumbsup_Entry = Entry(F4 ,width=10,textvariable=self.ThumbsUp, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=4, column=1, pady=10,padx=10)

        Sprite_label = Label(F4, text='Sprite', bg='grey', fg="lightgreen", font="lucide 14 bold").grid(row=6,column=0,padx=10,pady=10,sticky='w')
        Sprite_Entry = Entry(F4, width=10,textvariable=self.sprite, bd=5, relief=SUNKEN, font='lucide 14 bold ').grid(row=6, column=1,pady=10, padx=10)

        #############3 Bill Frame
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=905, y=170, width=369, height=350)
        Bill_label=Label(F5,text='Bill Area',font='aerial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.text=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.text.yview)
        self.text.pack(fill=BOTH,expand=1)

        ########## Button Menu
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text='Bill Menu', bg='grey', fg='gold', font='lucide 15 bold')
        F6.place(x=0, y=515,relwidth=1, height=150)

        m1=Label(F6,text='Total Cosmetic Price',bg='grey',fg='black',font='lucide 12 bold').grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_Entry=Entry(F6,width=15,textvariable=self.cosmeticsPrice,font='aerial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2 = Label(F6, text='Total Grocery Price', bg='grey', fg='black', font='lucide 12 bold').grid(row=1, column=0,padx=20, pady=1,sticky='w')
        m2_Entry = Entry(F6, width=15,textvariable=self.groceryPrice, font='aerial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10,pady=1)

        m3 = Label(F6, text='Total Cold Drinks Price', bg='grey', fg='black', font='lucide 12 bold').grid(row=2, column=0,padx=20, pady=1,sticky='w')
        m3_Entry = Entry(F6, width=15,textvariable=self.colddrinkPrice, font='aerial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10,pady=1)

        c1 = Label(F6, text='Cosmetic Tax', bg='grey', fg='black', font='lucide 12 bold').grid(row=0, column=2,padx=20, pady=1,sticky='w')
        c1_Entry = Entry(F6, width=15,textvariable=self.cosmatictax, font='aerial 10 bold', bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10,pady=1)

        c2 = Label(F6, text='Grocery Tax', bg='grey', fg='black', font='lucide 12 bold').grid(row=1,column=2,padx=20, pady=1,sticky='w')
        c2_Entry = Entry(F6, width=15,textvariable=self.grocerytax, font='aerial 10 bold', bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10,pady=1)

        c3 = Label(F6, text='Cold Drinks Tax', bg='grey', fg='black', font='lucide 12 bold').grid(row=2, column=2,padx=20, pady=1,sticky='w')
        c3_Entry = Entry(F6, width=15,textvariable=self.colddrinktax, font='aerial 10 bold', bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10,pady=1)

        btn_frame=Frame(F6,bd=7,relief=GROOVE)
        btn_frame.place(x=685,width=585,height=105)

        Total_btn=Button(btn_frame,command=self.total,text='Total',bg="cadetblue",fg='white',pady=15,width=11,font='aerial 12 bold').grid(row=0,column=0,padx=5,pady=5)

        G_btn = Button(btn_frame, text='Generate Bill',command=self.bill_area, bg="cadetblue", fg='white', pady=15, width=11,font='aerial 12 bold').grid(row=0, column=1, padx=5, pady=5)

        C_btn = Button(btn_frame, text='Clear', bg="cadetblue",command=self.clear_data, fg='white', pady=15, width=11,font='aerial 12 bold').grid(row=0, column=2, padx=5, pady=5)

        E_btn=Button(btn_frame,text='Exit',bg="cadetblue",command=self.exit_app,fg='white',pady=15,width=11,font='aerial 12 bold').grid(row=0,column=3,padx=5,pady=5)

        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*60
        self.c_fc_p=self.facecream.get()*300
        self.c_fw_p=self.facewash.get() *200
        self.c_hs_p=self.Hairspray.get() *400
        self.c_hg_p = self.Hairgell.get() * 200
        self.c_bl_p = self.Bodyloshan.get() * 250

        self.g_d_p=self.daal.get() * 90
        self.g_fo_p =self.foodoil.get() * 120
        self.g_w_p =self.wheat.get() * 200
        self.g_t_p =self.Tea.get() * 250
        self.g_s_p =self.sugar.get() * 80
        self.g_r_p =self.rice.get() * 300

        self.cd_m_p=self.maza.get() * 60
        self.cd_c_p =self.cock.get() * 40
        self.cd_s_p =self.slice.get() *60
        self.cd_tu_p =self.ThumbsUp.get() * 40
        self.cd_sp_p =self.sprite.get() * 50
        self.cd_f_p =self.frooti.get() * 60

        self.total_cosmatic_price=float(
                                    (self.c_s_p)+
                                        (self.c_fc_p)+
                                        (self.c_fw_p)+
                                        (self.c_hs_p)+
                                        (self.c_hg_p)+
                                        (self.c_bl_p)
                                    )
        self.cosmeticsPrice.set("Rs. "+str(self.total_cosmatic_price))
        self.c_tax=round((self.total_cosmatic_price*0.1),2)
        self.cosmatictax.set("Rs. "+str(self.c_tax))

        self.total_grocery_price = float(
                                    (self.g_d_p) +
                                        (self.g_fo_p)+
                                        (self.g_w_p) +
                                        (self.g_t_p) +
                                        (self.g_s_p) +
                                        (self.g_r_p)
                                    )
        self.groceryPrice.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.05),2)
        self.grocerytax.set("Rs. "+str(self.g_tax))

        self.total_colddrink_price = float(
                                    (self.cd_m_p) +
                                    (self.cd_c_p) +
                                    (self.cd_s_p) +
                                    (self.cd_tu_p) +
                                    (self.cd_sp_p) +
                                    (self.cd_f_p)
                                    )
        self.colddrinkPrice.set("Rs. "+str(self.total_colddrink_price))
        self.cd_tax=round((self.total_colddrink_price*0.05),2)
        self.colddrinktax.set("Rs. "+str(self.cd_tax))

        self.Total_bill=float(self.total_cosmatic_price+
                                  self.total_grocery_price+
                                  self.total_colddrink_price+
                                  self.c_tax+
                                  self.g_tax+
                                  self.cd_tax
                              )

    def welcome_bill(self):
        self.text.delete("1.0",END)
        self.text.insert(END,"\tWelcome Dreamvalley Retail\n")
        self.text.insert(END, f"\n Bill No : {self.billNo.get()}")
        self.text.insert(END, f"\n Customer Name : {self.cus_name.get()}")
        self.text.insert(END, f"\n Customer PhoneNo : {self.cus_phn.get()}")
        self.text.insert(END, f"\n========================================")
        self.text.insert(END, f"\n Products\t\tQty\t\tPrice")
        self.text.insert(END, f"\n========================================")

    def bill_area(self):
        if self.cus_name.get()=="" or self.cus_phn.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmeticsPrice.get()=="Rs. 0.0" and self.groceryPrice.get()=="Rs. 0.0" and self.colddrinkPrice.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Purchased")
        else:
            self.welcome_bill()
            ####cosmatic
            if self.soap.get()!=0:
                self.text.insert(END,f"\n Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.facecream.get()!=0:
                self.text.insert(END,f"\n Face Cream\t\t{self.facecream.get()}\t\t{self.c_fc_p}")
            if self.facewash.get()!=0:
                self.text.insert(END,f"\n Face wash\t\t{self.facewash.get()}\t\t{self.c_fw_p}")
            if self.Hairspray.get()!=0:
                self.text.insert(END,f"\n Hair spray\t\t{self.Hairspray.get()}\t\t{self.c_hs_p}")
            if self.Hairgell.get()!=0:
                self.text.insert(END,f"\n Hair gell\t\t{self.Hairgell.get()}\t\t{self.c_hg_p}")
            if self.Bodyloshan.get()!=0:
                self.text.insert(END,f"\n Body loshan\t\t{self.Bodyloshan.get()}\t\t{self.c_bl_p}")

            ######grocery
            if self.daal.get()!=0:
                self.text.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
            if self.foodoil.get()!=0:
                self.text.insert(END,f"\n FoodOil\t\t{self.foodoil.get()}\t\t{self.g_fo_p}")
            if self.wheat.get()!=0:
                self.text.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.Tea.get()!=0:
                self.text.insert(END,f"\n Tea\t\t{self.Tea.get()}\t\t{self.g_t_p}")
            if self.sugar.get()!=0:
                self.text.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.rice.get()!=0:
                self.text.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            ####drink
            if self.maza.get()!=0:
                self.text.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.cd_m_p}")
            if self.cock.get()!=0:
                self.text.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.cd_c_p}")
            if self.slice.get()!=0:
                self.text.insert(END,f"\n Slice\t\t{self.slice.get()}\t\t{self.cd_s_p}")
            if self.ThumbsUp.get()!=0:
                self.text.insert(END,f"\n ThumbsUp\t\t{self.ThumbsUp.get()}\t\t{self.cd_tu_p}")
            if self.sprite.get()!=0:
                self.text.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.cd_sp_p}")
            if self.frooti.get()!=0:
                self.text.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.cd_f_p}")

            self.text.insert(END,f"\n----------------------------------------")
            if self.cosmatictax.get()!="Rs. 0.0":
                self.text.insert(END,f"\n Cosmatic Tax\t\t\t{self.cosmatictax.get()}")
            if self.grocerytax.get()!="Rs. 0.0":
                self.text.insert(END,f"\n Grocery Tax\t\t\t{self.grocerytax.get()}")
            if self.colddrinktax.get()!="Rs. 0.0":
                self.text.insert(END,f"\n Cold Drink Tax\t\t\t{self.colddrinktax.get()}")
            self.text.insert(END, f"\n----------------------------------------")
            self.text.insert(END,f"\n Total Bill : \t\t\t Rs.{str(self.Total_bill)}")
            self.text.insert(END, f"\n----------------------------------------")
            self.save_bill()
    def save_bill(self):
        opp=messagebox.askyesno("Save bill","Do you want to save bill?")
        if opp>0:
            self.bill_data=self.text.get("1.0",END)
            f1=open("bills/"+str(self.billNo.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No : {self.billNo.get()} saved successfully")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}',"r")
                self.text.delete("1.0",END)
                for d in f1:
                    self.text.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid BillNo")
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear?")
        if op > 0:
            #   cosmatic var
            self.soap.set(0)
            self.facecream.set(0)
            self.facewash.set(0)
            self.Hairspray.set(0)
            self.Hairgell.set(0)
            self.Bodyloshan.set(0)
            # grocery var
            self.rice.set(0)
            self.foodoil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.Tea.set(0)
            # cold drinks var
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.slice.set(0)
            self.ThumbsUp.set(0)
            self.sprite.set(0)
            ########## total product price $ tax
            self.cosmeticsPrice.set("")
            self.groceryPrice.set("")
            self.colddrinkPrice.set("")

            self.cosmatictax.set("")
            self.grocerytax.set("")
            self.colddrinktax.set("")

            self.cus_name.set("")
            self.cus_phn.set("")
            self.billNo.set("")
            x=random.randint(1000,9999)
            self.billNo.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
root=Tk()
obj=Bill_Software(root)
root.mainloop()