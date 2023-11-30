from tkinter import * 
import PIL.Image as im 
import PIL.ImageTk as imtk 
import csv
from tkinter import messagebox

root = Tk()
root.wm_title("Contact_Book")
root.configure(bg="black")
root.geometry("1120x600") 
root.iconbitmap('call_img.png')

def Add_Cont():
    nw=Toplevel(root)
    nw.title("ADD CONTACT")
    nw.geometry("600x300")
    nw.iconbitmap('Add_call.jpg')
    nw.configure(bg='#F1EAFF')
    

    def Addtofile(entry_data):
        if len(firstname.get())==0 or len(lastname.get()) == 0 or len(num.get()) == 0 or len(email.get()) == 0:
            messagebox.showinfo("Register","You left one or more fields blank O_O")
        else:
            with open ('data.csv', mode='a', newline='') as file:
                writer=csv.writer(file)
                writer.writerow(entry_data)
                messagebox.showinfo('Added','Contact Added!')

    def on_submit():
        Fn=firstname.get()
        Fn_upper=Fn.upper()

        Ln=lastname.get()
        Ln_upper=Ln.upper()

        e=email.get()
        n=num.get()

        with open('data.csv','r') as searchfile:
            read=csv.reader(searchfile)
            for row in read:
                if row[0] == Fn_upper or row[2]==n:
                    messagebox.showerror('Name','Name/phone already exist in the file!')

        if n.isnumeric() == False or Ln_upper==' ':
            messagebox.showerror('Phone',"Please verify the Phone number, it can't be blank or an alphabet")
        else:
            lst=[Fn_upper,Ln_upper,n,e]
            Addtofile(lst)

    frm=Frame(nw, bg='#F1EAFF')
    frm.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    label1=Label(frm,text="First Name*", bg='#F1EAFF')
    label1.grid(row=0,column=0,padx=8,pady=7)
    firstname=Entry(frm,width=20)
    firstname.grid(row=0,column=1)

    label2=Label(frm,text="Last Name", bg='#F1EAFF')
    label2.grid(row=1,column=0,padx=8,pady=7)
    lastname=Entry(frm,width=20)
    lastname.grid(row=1,column=1)

    label3=Label(frm,text="Phone*", bg='#F1EAFF')
    label3.grid(row=2,column=0,padx=8,pady=7)
    num=Entry(frm,width=20)
    num.grid(row=2,column=1)

    label4=Label(frm,text="E-mail", bg='#F1EAFF')
    label4.grid(row=3,column=0,padx=8,pady=7)
    email=Entry(frm,width=20)
    email.grid(row=3,column=1)

    addbtn = Button( frm, text = "Add to contact", width=20,height=1,command=on_submit,bg='#E5D4FF',border=0) 
    addbtn.grid(row=6,column=0,columnspan=3,pady=10)    

def Search_cont():
    nw1=Toplevel(root)
    nw1.title("Search CONTACT")
    nw1.geometry("300x300")
    nw1.configure(bg='#FCF5ED')
    nw1.iconbitmap('search_img2.jpg')

    def on_search():
        n=s_entry.get()
        name=n.upper()
        with open('data.csv','r') as searchfile:
            read=csv.reader(searchfile)
            for row in read:
                if row[0] == name:
                    dis_1=Label(s_frm,text='Name:  '+name ,bg='#FCF5ED')
                    dis_1.grid(row=4,column=0,sticky=W)
                    dis_2=Label(s_frm,text='Lastname:  '+row[1] ,bg='#FCF5ED')
                    dis_2.grid(row=5,column=0,pady=2,sticky=W)
                    dis_3=Label(s_frm,text='Number:  '+row[2] ,bg='#FCF5ED')
                    dis_3.grid(row=6,column=0,pady=2,sticky=W)
                    dis_4=Label(s_frm,text='E-mail:  '+row[3] ,bg='#FCF5ED')
                    dis_4.grid(row=7,column=0,pady=2,sticky=W)

    s_frm=Frame(nw1 ,bg='#FCF5ED')
    s_frm.place(relx=0.5,rely=0.3,anchor=CENTER)
    s_label1=Label(s_frm,text="enter the Name of Contact to be searched" ,bg='#FCF5ED')
    s_label1.grid(row=0,column=0)
    s_entry=Entry(s_frm,width=20)
    s_entry.grid(row=1,column=0)
    s_btn=Button(s_frm,text="Search",command=on_search,border=0)
    s_btn.grid(row=2,column=0,pady=4)

def Edit_cont():
    nw2=Toplevel(root)
    nw2.title("Edit CONTACT")
    nw2.geometry("700x600")
    nw2.configure(bg='#F1EAFF')
    nw2.iconbitmap('edit_img.png')
    
    def on_edit():

        def on_update():
            n=edit_2.get()
            name=n.upper()
            field=int(e_3.get())
            value1=e_4.get()
            val=value1.upper()
            found=0

            with open('data.csv','r') as searchfile:
                reader=csv.reader(searchfile)
                rows=list(reader)
                for row in rows:
                    if row[0] == name:
                        if field==1:
                            row[0]=val
                            print(row)
                        elif field==2:
                            row[1]=val
                        elif field==3:
                            row[2]=val
                        elif field==4:
                            row[3]=val
                        else:
                            dis=Label(e_frm,text='invalid field',bg='#F1EAFF')
                            dis.grid(row=13,column=2)
                            return
                        found=1
            
            if found==0:
                print('not found!!')
            else:
                with open ('data.csv', mode='w', newline='') as file:
                    writer=csv.writer(file)
                    writer.writerows(rows)
                    messagebox.showinfo('Updated','Contact updated!')

        n=edit_2.get()
        name=n.upper()
        with open('data.csv','r') as searchfile:
            read=csv.reader(searchfile)
            for row in read:
                if row[0] == name:
                    dis_1=Label(e_frm,text='Name:  '+name,bg='#F1EAFF')
                    dis_1.grid(row=4,column=1,sticky=W,columnspan=2)
                    dis_2=Label(e_frm,text='Lastname:  '+row[1],bg='#F1EAFF')
                    dis_2.grid(row=5,column=1,pady=2,sticky=W,columnspan=2)
                    dis_3=Label(e_frm,text='Number:  '+row[2],bg='#F1EAFF')
                    dis_3.grid(row=6,column=1,pady=2,sticky=W,columnspan=2)
                    dis_4=Label(e_frm,text='E-mail:  '+row[3],bg='#F1EAFF')
                    dis_4.grid(row=7,column=1,pady=2,sticky=W,columnspan=2)
            
                    dis_5=Label(e_frm,text='Enter the field (1->Name,2->LastNane,3->Phone, 4->Email) to be edited and new value to be updated! ',bg='#F1EAFF')
                    dis_5.grid(row=9,column=0,columnspan=5,pady=10)

                    dis_6=Label(e_frm,text='Field',bg='#F1EAFF')
                    dis_6.grid(row=10,column=0)

                    e_3=Entry(e_frm,width=25)
                    e_3.grid(row=10,column=1)

                    dis_6=Label(e_frm,text='New Value',bg='#F1EAFF')
                    dis_6.grid(row=11,column=0)

                    e_4=Entry(e_frm,width=25)
                    e_4.grid(row=11,column=1)

                    edit_btn=Button(e_frm,text='Update',command=on_update,bg='#E5D4FF',border=0)
                    edit_btn.grid(row=13,column=1,pady=5)



    e_frm=Frame(nw2,bg='#F1EAFF')
    e_frm.place(relx=0.5,rely=0.3,anchor=CENTER)

    edit_1=Label(e_frm,text="Enter the Name of contact to be edited:",bg='#F1EAFF')
    edit_1.grid(row=0,column=0,columnspan=4)
    edit_2=Entry(e_frm,width=25)
    edit_2.grid(row=1,column=0,columnspan=4)
    e_btn=Button(e_frm,text="Edit",width=10,command=on_edit,bg='#E5D4FF',border=0)
    e_btn.grid(row=2,column=0,pady=10,columnspan=4) 

def Delete_Cont():
    nw3=Toplevel(root)
    nw3.title("ADD CONTACT")
    nw3.geometry("300x300")

    def clear_csv():
        try:
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # Writing an empty list effectively clears the file
                writer.writerows([])
            messagebox.showinfo('Cleared', 'Contacts has been cleared.')
        except Exception as e:
            messagebox.showerror('Error', 'An error occurred!')

    clear_l=Label(nw3,text='Are you sure you wanna clear the Contacts? ')
    clear_l.place(relx=0.5,rely=0.2,anchor=CENTER)
    clear_button = Button(nw3, text="Clear",width=20, command=clear_csv, bg="#07C8FB")
    clear_button.place(relx=0.5,rely=0.5,anchor=CENTER)


#images used
bg= imtk.PhotoImage(file="conct_img1.png")
ic1=imtk.PhotoImage(file="Add_call.jpg")

my_canvas= Canvas(root, width=300, height=300)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(-110,-50,image=bg,anchor="nw")

frame1 = Frame(my_canvas) 
frame1.place(x=800,y=120)

button1 = Button(frame1,text="Add Contact", width=30 ,height=2,bg="#07C8FB",font=("Trebuchet MS",9,"bold"),borderwidth=0,command=Add_Cont)
button1.grid(row=0,column=0,pady=15) 

button2 = Button( frame1, text = "Search contact", width=30,height=2,bg="#07C8FB", font=("Trebuchet MS",9,"bold"),border=0,command=Search_cont) 
button2.grid(row=1,column=0,pady=15)
  
button3 = Button( frame1, text = "Edit Contact", width=30,height=2,bg="#07C8FB",font=("Trebuchet MS",9,"bold"),border=0,command=Edit_cont) 
button3.grid(row=2,column=0,pady=15) 

button4 = Button( frame1, text = "Clear Contacts", width=30,height=2,bg="#07C8FB",font=("Trebuchet MS",9,"bold"),border=0,command=Delete_Cont) 
button4.grid(row=3,column=0,pady=15) 

root.mainloop()
