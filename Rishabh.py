from tkMessageBox import *
import sqlite3
import Tkinter as tk
from Tkinter import *
def splashscrn():
    root = tk.Tk()
    image_file = "logo.gif"
    image = tk.PhotoImage(file ="hotel1.gif")
    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    t = tk.Canvas(root, width  = screen_width,
			       height = screen_height)
    root.overrideredirect(1)
    t.create_image(screen_width / 2, screen_height / 2,
                   image = image)
    t.create_text( screen_width / 2, screen_height / 2,
		  text = "HOTEL MANAGMENT \n\n RISHABH JAIN \n\n161B176. \n\n submited to mahesh kumar \n\n",
		  fill = "white", font = "times 50 bold italic underline")
    t.pack()
    root.after(7000, lambda: root.destroy())
    root.mainloop()
splashscrn()
root = Tk()
global bfst
bfst=[]
z2=0
z1=0
root.title("HOTEL MANAGMEMNT")
import sqlite3
con=sqlite3.Connection("hrdb")
cur=con.cursor()
cur.execute("create table if not exists emp1(id number primary key,ename varchar(20),edob Date,egender varchar(10),eadd varchar(50),epno number(10),eeid varchar(30))")

cur.execute("create table if not exists room2(cus_id number,room number primary key,status varchar(20))")
'''i=101
while(i<151):
    cur.execute("insert into room2(room) values(?)",[i])
    con.commit()
    i=i+1'''


def ncustomer():
    root=Toplevel()
    Label(root,text = " Customer Record Keeping System",font="forte 20 bold ",bd=10,bg='blue',fg='black',relief='raised').grid(row=0,column=0,columnspan=3)
    Label(root,text = "Enter Customer ID").grid(row=1,column=0)
    identity= Entry(root)
    identity.grid(row=1,column=1)
    Label(root,text = "Enter Name").grid(row=2,column=0)
    name= Entry(root)
    name.grid(row=2,column=1)
    Label(root,text = "Enter DOB").grid(row=3,column=0)
    dob = Entry(root)
    dob.grid(row=3,column=1)
    Label(root,text = "Enter Gender").grid(row=4,column=0)
    gender = Entry(root)
    gender.grid(row=4,column=1)
    Label(root,text = "Enter Address").grid(row=5,column=0)
    add= Entry(root)
    add.grid(row=5,column=1)
    Label(root,text = "Enter phone number").grid(row=6,column=0)
    pno= Entry(root)
    pno.grid(row=6,column=1)
    Label(root,text = "Enter Email Address").grid(row=7,column=0)
    eid= Entry(root)
    eid.grid(row=7,column=1)
    def insert():
        g=identity.get()
        cur.execute('select ename from emp1 where id=?',(int(g),))
        f=cur.fetchall()
        if len(f)>0:
            showerror('wrong','duplicate info')
        else:
            cur.execute("insert into emp1 values(?,?,?,?,?,?,?)",(identity.get(),name.get(),dob.get(),gender.get(),add.get(),pno.get(),eid.get()))
            dic=(identity.get(),name.get(),dob.get(),gender.get(),add.get(),pno.get(),eid.get())
            con.commit()
            name.delete(0,END)
            dob.delete(0,END)
            gender.delete(0,END)
            add.delete(0,END)
            pno.delete(0,END)
            eid.delete(0,END)
            identity.delete(0,END)
            showinfo('inserted info',dic)
    
    Button(root,text='Insert',command=insert,width=10,bd=5,font='times 12 bold italic',bg='blue',fg='white').grid(row=8,column=1)
def scustomer():
    root=Toplevel()
    Label(root,text = " Customer Information",font="forte 20 bold ",bd=10,bg='blue',fg='black',relief='raised').grid(row=0,column=0,columnspan=10)
    Label(root,text = "fetch Customer ID").grid(row=1,column=0)
    idNo= Entry(root)
    idNo.grid(row=1,column=1)
    def show():
        s = idNo.get()
        cur.execute('select ename,edob,egender,eadd,epno,eeid from emp1 where id=?',(s,))
        q=cur.fetchall()
        showinfo('dta',q)
    
    
    def showall():
        cur.execute('select * from emp1',())
        w=cur.fetchall()
        showinfo('every info',w)
    
    Button(root,text='Show',command=show,width=10,bd=5,font='times 12 bold italic',bg='blue',fg='black').grid(row=2,column=0)
    Button(root,text='Show All',command=showall,width=10,bd=5,font='times 12 bold italic',bg='blue',fg='black').grid(row=2,column=1)
    Button(root,text='Exit',command=root.destroy,width=10,bd=5,font='times 12 bold italic',bg='blue',fg='black').grid(row=2,column=2)

def order():
    root=Toplevel()
    root.title('Billing System')
    def breakfast():
        root=Toplevel()
        Label(root,text='Select your breakfast',fg='Black',font='times 20 bold').grid(row=1,column=1)
        v1=IntVar()
        v2=IntVar()
        v3=IntVar()
        v4=IntVar()
        v5=IntVar()
        v6=IntVar()
        v7=IntVar()
        v8=IntVar()
        v9=IntVar()
        v10=IntVar()
        v11=IntVar()
        v12=IntVar()
        v13=IntVar()
        v14=IntVar()
        v15=IntVar()
        v16=IntVar()

        Checkbutton(root,text='macroni(105)',variable=v1,onvalue=105).grid(row=3,column=0,sticky='W')
        Checkbutton(root,text='sandwich(80)',variable=v2,onvalue=80).grid(row=4,column=0,sticky='W')
        Checkbutton(root,text='Aloo Paratha(200)',variable=v3,onvalue=200).grid(row=5,column=0,sticky='W')
        Checkbutton(root,text='poha(50)',variable=v4,onvalue=50).grid(row=6,column=0,sticky='W')
        Checkbutton(root,text='noodles(120)',variable=v5,onvalue=120).grid(row=7,column=0,sticky='W')
        Checkbutton(root,text='egg(20)',variable=v6,onvalue=20).grid(row=8,column=0,sticky='W')
        Checkbutton(root,text='idli(60)',variable=v7,onvalue=60).grid(row=9,column=0,sticky='W')
        Checkbutton(root,text='upama(70)',variable=v8,onvalue=70).grid(row=10,column=0,sticky='W')
        Checkbutton(root,text='Pav bhaji(110)',variable=v9,onvalue=110).grid(row=3,column=2,sticky='W')
        Checkbutton(root,text='pasta(85)',variable=v10,onvalue=80).grid(row=4,column=2,sticky='W')
        Checkbutton(root,text='omelete(30)',variable=v11,onvalue=30).grid(row=5,column=2,sticky='W')
        Checkbutton(root,text='fruits(40)',variable=v12,onvalue=40).grid(row=6,column=2,sticky='W')
        Checkbutton(root,text='bread butter(90)',variable=v13,onvalue=20).grid(row=7,column=2,sticky='W')
        Checkbutton(root,text='sprouts(65)',variable=v14,onvalue=65).grid(row=8,column=2,sticky='W')
        Checkbutton(root,text='porage(55)',variable=v15,onvalue=55).grid(row=9,column=2,sticky='W')
        Checkbutton(root,text='milk corn flakes(25)',variable=v16,onvalue=25).grid(row=10,column=2,sticky='W')
        
        
        
        Label(root,text='select quantity').grid(row=3,column=8)
        v17=IntVar()
        r1=Radiobutton(root,text='1',variable=v17,value=1).grid(row=4,column=8,sticky='W')
        r2=Radiobutton(root,text='2',variable=v17,value=2).grid(row=5,column=8,sticky='W')
        r3=Radiobutton(root,text='3',variable=v17,value=3).grid(row=6,column=8,sticky='W')
        r4=Radiobutton(root,text='4',variable=v17,value=4).grid(row=7,column=8,sticky='W')
        r5=Radiobutton(root,text='5',variable=v17,value=5).grid(row=8,column=8,sticky='W')

        def choice():
            x={'macroni':105,'sandwich':80,'Aloo Paratha':200,'poha':50,'noodles':120,'egg':20,'idli':60,'upama':70,'Pav bhaji':110,'pasta':85,'omelete':30,'fruits':40,'bread butter':90,'sprouts':65,'porage':55,'milk corn flakes':25}
            a=int(v1.get())*int(v17.get())
            b=int(v2.get())*int(v17.get())
            c=int(v3.get())*int(v17.get())
            d=int(v4.get())*int(v17.get())
            e=int(v5.get())*int(v17.get())
            f=int(v6.get())*int(v17.get())
            g=int(v7.get())*int(v17.get())
            h=int(v8.get())*int(v17.get())
            i=int(v9.get())*int(v17.get())
            j=int(v10.get())*int(v17.get())
            k=int(v11.get())*int(v17.get())
            l=int(v12.get())*int(v17.get())
            m=int(v13.get())*int(v17.get())
            n=int(v14.get())*int(v17.get())
            o=int(v15.get())*int(v17.get())
            p=int(v16.get())*int(v17.get())
            global z1
            z1=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
            if z1==0:
              Label(root,text='please select the radio button ',fg='black',font='times 15 bold italic').grid(row=13)
            else:
                Label(root,text='Total amount of your breakfast = '+str(z1)+' INR    ',fg='black',font='times 15 bold italic').grid(row=13)
            for i,j in x.iteritems():
                if(v1.get()==j or v2.get()==j or v3.get()==j or v4.get()==j or v5.get()==j or v6.get()==j or v7.get()==j or v8.get()==j or v9.get()==j or v10.get()==j or v11.get()==j or v12.get()==j or v13.get()==j or v14.get()==j or v15.get()==j or v16.get()==j):
                    bfst.append(i)
                
    
        def fun():
            root.destroy()
        Button(root,text='Ckeck RS ',command=choice,width=10,bd=5,font='times 12 bold italic',bg='black',fg='white').grid(row=11,column=0)
        Button(root,text='Exit',command=fun,width=10,bd=5,font='times 12 bold italic',bg='black',fg='white').grid(row=11,column=2)
    def dinner():
        root=Toplevel()
        Label(root,text='Appetizers  ',fg='White',bg='brown',font='times 20 bold').grid(row=1,column=0)
        v1=IntVar()
        v2=IntVar()
        v3=IntVar()
        v4=IntVar()
        v5=IntVar()
        v6=IntVar()
        v7=IntVar()
        v8=IntVar()
        v9=IntVar()
        Checkbutton(root,text='spinach pakoras(30)',variable=v1,onvalue=30).grid(row=2,column=0,sticky='W')
        Checkbutton(root,text='potato pakoras(35)',variable=v2,onvalue=35).grid(row=3,column=0,sticky='W')
        Checkbutton(root,text='hot chilli pakoras(40)',variable=v3,onvalue=40).grid(row=4,column=0,sticky='W')
        Checkbutton(root,text='chicken pakoras(45)',variable=v4,onvalue=45).grid(row=5,column=0,sticky='W')
        Checkbutton(root,text='cut mirchi(50)',variable=v5,onvalue=50).grid(row=6,column=0,sticky='W')
        Checkbutton(root,text='masala vada(55)',variable=v6,onvalue=55).grid(row=7,column=0,sticky='W')
        Checkbutton(root,text='vegetable samosa(60)',variable=v7,onvalue=60).grid(row=8,column=0,sticky='W')
        Checkbutton(root,text='platter(65)',variable=v8,onvalue=65).grid(row=9,column=0,sticky='W')
        Checkbutton(root,text='chili chicken(70)',variable=v9,onvalue=70).grid(row=10,column=2,sticky='W')

        Label(root,text='Soups and Salads',fg='White',bg='brown',font='times 20 bold').grid(row=1,column=1)
        
        v10=IntVar()
        v11=IntVar()
        v12=IntVar()
        v13=IntVar()
        v14=IntVar()
        v15=IntVar()
        v16=IntVar()
        
        Checkbutton(root,text='Rasasm(75)',variable=v10,onvalue=75).grid(row=2,column=1,sticky='W')
        Checkbutton(root,text='idli sambhar(80)',variable=v11,onvalue=80).grid(row=3,column=1,sticky='W')
        Checkbutton(root,text='fresh green salad(85)',variable=v12,onvalue=85).grid(row=4,column=1,sticky='W')
        Checkbutton(root,text='tomato soup(90)',variable=v13,onvalue=90).grid(row=5,column=1,sticky='W')
        Checkbutton(root,text='raita(95)',variable=v14,onvalue=95).grid(row=6,column=1,sticky='W')
        Checkbutton(root,text='plain yogurt(20)',variable=v15,onvalue=20).grid(row=7,column=1,sticky='W')
        Checkbutton(root,text='delhi vada(25)',variable=v16,onvalue=25).grid(row=8,column=1,sticky='W')

        Label(root,text='vegetarian entries',fg='White',bg='brown',font='times 20 bold').grid(row=1,column=2)
        v17=IntVar()
        v18=IntVar()
        v19=IntVar()
        v20=IntVar()
        v21=IntVar()
        v22=IntVar()
        v23=IntVar()
        v24=IntVar()
        v25=IntVar()
        v26=IntVar()
        v27=IntVar()
        v28=IntVar()
        
        Checkbutton(root,text='Bhindi masala(100)',variable=v17,onvalue=100).grid(row=2,column=2,sticky='W')
        Checkbutton(root,text='aloo gobhi(105)',variable=v18,onvalue=105).grid(row=3,column=2,sticky='W')
        Checkbutton(root,text='vegetable korma(110)',variable=v19,onvalue=110).grid(row=4,column=2,sticky='W')
        Checkbutton(root,text='dal curry(115)',variable=v20,onvalue=115).grid(row=5,column=2,sticky='W')
        Checkbutton(root,text='dal makhani(120)',variable=v21,onvalue=120).grid(row=6,column=2,sticky='W')
        Checkbutton(root,text='chana masala(125)',variable=v22,onvalue=125).grid(row=7,column=2,sticky='W')
        Checkbutton(root,text='mutter paneer(130)',variable=v23,onvalue=130).grid(row=8,column=2,sticky='W')
        Checkbutton(root,text='palak paneer(135)',variable=v24,onvalue=135).grid(row=9,column=2,sticky='W')
        Checkbutton(root,text='chilli paneer(140)',variable=v25,onvalue=140).grid(row=10,column=2,sticky='W')
        Checkbutton(root,text='paneer masala(145)',variable=v26,onvalue=145).grid(row=11,column=2,sticky='W')
        Checkbutton(root,text='malai kofta(150)',variable=v27,onvalue=150).grid(row=12,column=2,sticky='W')
        Checkbutton(root,text='navratan korma(155)',variable=v28,onvalue=155).grid(row=13,column=2,sticky='W')

        Label(root,text=' Non vegetarian entries',fg='White',bg='brown',font='times 20 bold').grid(row=1,column=3)
        v29=IntVar()
        v30=IntVar()
        v31=IntVar()
        v32=IntVar()
        v33=IntVar()
        v34=IntVar()
        v35=IntVar()
        v36=IntVar()
        v37=IntVar()
        v38=IntVar()
        v39=IntVar()
        v40=IntVar()
        
        Checkbutton(root,text='egg curry(200)',variable=v29,onvalue=200).grid(row=2,column=3,sticky='W')
        Checkbutton(root,text='chicken curry(205)',variable=v30,onvalue=205).grid(row=3,column=3,sticky='W')
        Checkbutton(root,text='chicken masala(210)',variable=v31,onvalue=210).grid(row=4,column=3,sticky='W')
        Checkbutton(root,text='tandoori chicken(215)',variable=v32,onvalue=215).grid(row=5,column=3,sticky='W')
        Checkbutton(root,text='butter chicken(220)',variable=v33,onvalue=220).grid(row=6,column=3,sticky='W')
        Checkbutton(root,text='chicken saag(225)',variable=v34,onvalue=225).grid(row=7,column=3,sticky='W')
        Checkbutton(root,text='lamb curry(230)',variable=v35,onvalue=230).grid(row=8,column=3,sticky='W')
        Checkbutton(root,text='lamb saag(235)',variable=v36,onvalue=235).grid(row=9,column=3,sticky='W')
        Checkbutton(root,text='handi chicken(240)',variable=v37,onvalue=240).grid(row=10,column=3,sticky='W')
        Checkbutton(root,text='fish(245)',variable=v38,onvalue=245).grid(row=11,column=3,sticky='W')
        Checkbutton(root,text='shrimp masala(250)',variable=v39,onvalue=250).grid(row=12,column=3,sticky='W')
        Checkbutton(root,text='ginger prawns(255)',variable=v40,onvalue=255).grid(row=13,column=3,sticky='W')

        

        def choice():
            diner={'spinach pakoras':30,'potato pakoras':35,'hot chilli pakoras':40,'chicken pakoras':45,'cut mirchi':50,'masala vada':55,'vegetable samosa':60,'platter':65,'chili chicken':70,'Rasasm':75,'idli sambhar':80,'fresh green salad':85,'tomato soup':90,'raita':95,'plain yogurt':20,'delhi vada':25,'Bhindi masala':100,'aloo gobhi':105,'vegetable korma':110,'dal curry':115,'dal makhani':120,'chana masala':125,'mutter paneer':130,'palak paneer':135,'chilli paneer':140,'paneer masala':145,'malai kofta':150,'navratan korma':155,'egg curry':200,'chicken curry':205,'chicken masala':210,'tandoori chicken':215,'butter chicken':220,'chicken saag':225,'lamb curry':230,'lamb saag':235,'handi chicken':240,'fish':245,'shrimp masala':250,'ginger prawns':255}
            a=int(v1.get())
            b=int(v2.get())
            c=int(v3.get())
            d=int(v4.get())
            e=int(v5.get())
            f=int(v6.get())
            g=int(v7.get())
            h=int(v8.get())
            i=int(v9.get())
            j=int(v10.get())
            k=int(v11.get())
            l=int(v12.get())
            m=int(v13.get())
            n=int(v14.get())
            o=int(v15.get())
            p=int(v16.get())
            q=int(v17.get())
            r=int(v18.get())
            s=int(v19.get())
            t=int(v20.get())
            u=int(v21.get())
            v=int(v22.get())
            w=int(v23.get())
            x=int(v24.get())
            y=int(v25.get())
            a1=int(v26.get())
            b1=int(v27.get())
            c1=int(v28.get())
            d1=int(v29.get())
            e1=int(v30.get())
            f1=int(v31.get())
            g1=int(v32.get())
            h1=int(v33.get())
            i1=int(v34.get())
            j1=int(v35.get())
            k1=int(v36.get())
            l1=int(v37.get())
            m1=int(v38.get())
            n1=int(v39.get())
            o1=int(v40.get())
            global z2
            z2=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+a1+b1+c1+d1+e1+f1+g1+h1+i1+j1+k1+l1+m1+n1+o1
            Label(root,text='Total amount = '+str(z2)+' INR  ',fg='black',font='times 15 bold italic').grid(row=17,column=3)
            for i,j in diner.iteritems():
                if(v1.get()==j or v2.get()==j or v3.get()==j or v4.get()==j or v5.get()==j or v6.get()==j or v7.get()==j or v8.get()==j or v9.get()==j or v10.get()==j or v11.get()==j or v12.get()==j or v13.get()==j or v14.get()==j or v15.get()==j or v16.get()==j):
                    bfst.append(i)
        def fun():
            root.destroy()
        Button(root,text='Ckeck RS ',command=choice,width=10,bd=5,font='times 12 bold italic',bg='brown',fg='white').grid(row=16,column=0)
        Button(root,text='Exit',command=fun,width=10,bd=5,font='times 12 bold italic',bg='brown',fg='white').grid(row=16,column=3)
    Label(root,text='what would you like to have?',font='times 20 bold italic',bg='red',fg='black',relief='raised',bd=10).grid(row=1,column=1,columnspan=5)
    Button(root,text='BREAKFAST',command=breakfast,height=2,width=20,bg='red',font='times 10 bold',bd=5).grid(row=2,column=1)
    Button(root,text='LUNCH / DINNER',height=2,width=20,bg='red',font='times 10 bold',bd=5,command=dinner).grid(row=3,column=1)
    root.maxsize(height=1000,width=1000)
    root.mainloop()
def view():
    showinfo('YOUR ORDER ',bfst)

def rooms():
    root=Toplevel()
    def call(x):
        a=cur.execute("select * from room2 where room =?",(x,)).fetchall()
        if a[0][2]=='o':
            showerror('error','SORRY!!!! The room is currently occupied ')
        else:
            root=Toplevel()
            if(x>=101 and x<=110):
                Label(root,text = "The rent of the room is 500 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=111 and x<=120):
                Label(root,text = "The rent of the room is 1000 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=121 and x<=125):
                Label(root,text = "The rent of the room is 1500 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=126 and x<=130):
                Label(root,text = "The rent of the room is 2000 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=131 and x<=135):
                Label(root,text = "The rent of the room is 2500 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=136 and x<=140):
                Label(root,text = "The rent of the room is 3000 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=141 and x<=145):
                Label(root,text = "The rent of the room is 3500 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            elif(x>=146 and x<=150):
                Label(root,text = "The rent of the room is 4000 INR ",relief='raised',fg='black',bg='turquoise',font='times 20 bold').grid(row=0,columnspan=4)
            Label(root,text = "Enter Customer ID").grid(row=1,column=0,sticky=W)
            y= Entry(root)
            y.grid(row=1,column=1)
        def insert():
            cur.execute("update room2 set status=?,cus_id=? where room=?",("o",int(y.get()),x)).fetchall()
            con.commit()
        Button(root,text='Insert',fg='black',bg='turquoise',font='times 12 bold',bd=5,command=insert).grid(row=3,column=0)
        Button(root,text='Exit',fg='black',bg='turquoise',font='times 12 bold',bd=5,command=root.destroy).grid(row=3,column=1)
            
    Label(root,text='Single Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=0,column=0)
    Label(root,text='Double Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=1,column=0)
    Label(root,text='Twin Bedded Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=2,column=0)
    Label(root,text='Triple Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=3,column=0)
    Label(root,text='Quad Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=4,column=0)
    Label(root,text='Suite Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=5,column=0)
    Label(root,text='King Bed Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=6,column=0)
    Label(root,text='Queen Bed Room',fg='crimson',bg='yellowgreen',font='times 20 bold').grid(row=7,column=0)
    Button(root,text='R.101',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(101)).grid(row=0,column=1)
    Button(root,text='R.102',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(102)).grid(row=0,column=2)
    Button(root,text='R.103',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(103)).grid(row=0,column=3)
    Button(root,text='R.104',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(104)).grid(row=0,column=4)
    Button(root,text='R.105',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(105)).grid(row=0,column=5)
    Button(root,text='R.106',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(106)).grid(row=0,column=6)
    Button(root,text='R.107',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(107)).grid(row=0,column=7)
    Button(root,text='R.108',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(108)).grid(row=0,column=8)
    Button(root,text='R.109',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(109)).grid(row=0,column=9)
    Button(root,text='R.110',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(110)).grid(row=0,column=10)
    Button(root,text='R.111',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(111)).grid(row=1,column=1)
    Button(root,text='R.112',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(112)).grid(row=1,column=2)
    Button(root,text='R.113',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(113)).grid(row=1,column=3)
    Button(root,text='R.114',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(114)).grid(row=1,column=4)
    Button(root,text='R.115',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(115)).grid(row=1,column=5)
    Button(root,text='R.116',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(116)).grid(row=1,column=6)
    Button(root,text='R.117',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(117)).grid(row=1,column=7)
    Button(root,text='R.118',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(118)).grid(row=1,column=8)
    Button(root,text='R.119',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(119)).grid(row=1,column=9)
    Button(root,text='R.120',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(120)).grid(row=1,column=10)
    Button(root,text='R.121',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(121)).grid(row=2,column=1)
    Button(root,text='R.122',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(122)).grid(row=2,column=2)
    Button(root,text='R.123',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(123)).grid(row=2,column=3)
    Button(root,text='R.124',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(124)).grid(row=2,column=4)
    Button(root,text='R.125',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(125)).grid(row=2,column=5)
    Button(root,text='R.126',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(126)).grid(row=3,column=1)
    Button(root,text='R.127',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(127)).grid(row=3,column=2)
    Button(root,text='R.128',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(128)).grid(row=3,column=3)
    Button(root,text='R.129',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(129)).grid(row=3,column=4)
    Button(root,text='R.130',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(130)).grid(row=3,column=5)
    Button(root,text='R.131',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(131)).grid(row=4,column=1)
    Button(root,text='R.132',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(132)).grid(row=4,column=2)
    Button(root,text='R.133',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(133)).grid(row=4,column=3)
    Button(root,text='R.134',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(134)).grid(row=4,column=4)
    Button(root,text='R.135',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(135)).grid(row=4,column=5)
    Button(root,text='R.136',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(136)).grid(row=5,column=1)
    Button(root,text='R.137',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(137)).grid(row=5,column=2)
    Button(root,text='R.138',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(138)).grid(row=5,column=3)
    Button(root,text='R.139',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(139)).grid(row=5,column=4)
    Button(root,text='R.140',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(140)).grid(row=5,column=5)
    Button(root,text='R.141',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(141)).grid(row=6,column=1)
    Button(root,text='R.142',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(142)).grid(row=6,column=2)
    Button(root,text='R.143',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(143)).grid(row=6,column=3)
    Button(root,text='R.144',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(144)).grid(row=6,column=4)
    Button(root,text='R.145',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(145)).grid(row=6,column=5)
    Button(root,text='R.146',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(146)).grid(row=7,column=1)
    Button(root,text='R.147',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(147)).grid(row=7,column=2)
    Button(root,text='R.148',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(148)).grid(row=7,column=3)
    Button(root,text='R.149',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(149)).grid(row=7,column=4)
    Button(root,text='R.150',height=2,width=5,bg='tan',bd=10,fg='black',font='times 10 bold',command=lambda:call(150)).grid(row=7,column=5)

def bill():
    root=Toplevel()
    Label(root,text='Enter Customer ID to see customer details  : ',font='times 15 bold italic').grid(row=1)
    Label(root,text='Enter Customer ID :',font='times 13 bold ',fg='blue').grid(row=2,column=0,sticky=W)
    h=Entry(root,width=30,bd=3)
    h.grid(row=2,column=1,sticky=E)
    def details():
        root=Toplevel()
        cur.execute('select * from emp1 where id=(?)',[int(h.get())])
        n=cur.fetchall()      
        Label(root,text="Name               :"+str(n[0][1]),font='times 12 bold italic',fg='brown').grid(row=2,column=0,sticky=W)
        Label(root,text="DOB                :"+str(n[0][2]),font='times 12 bold italic',fg='brown').grid(row=3,column=0,sticky=W)
        Label(root,text="Gender             :"+str(n[0][3]),font='times 12 bold italic',fg='brown').grid(row=4,column=0,sticky=W)
        Label(root,text="Address            :"+str(n[0][4]),font='times 12 bold italic',fg='brown').grid(row=5,column=0,sticky=W)
        Label(root,text="Phone number       :"+str(n[0][5]),font='times 12 bold italic',fg='brown').grid(row=6,column=0,sticky=W)
        Label(root,text="Email Address      :"+str(n[0][6]),font='times 12 bold italic',fg='brown').grid(row=7,column=0,sticky=W)
        q=cur.execute("select distinct(room) from room2 where cus_id=(?)",(int(h.get()),)).fetchall()
        Label(root,text="rooms booked are      :"+str(q),font='times 12 bold italic',fg='brown').grid(row=8,column=0,sticky=W)
        single=cur.execute("select count(room) from room2 where cus_id =(?) and room >=101 and room <=110",(int(h.get()),)).fetchone()[0]
        double=cur.execute("select count(room) from room2 where cus_id =(?) and room >=111 and room <=120",(int(h.get()),)).fetchone()[0]
        twin=cur.execute("select count(room) from room2 where cus_id =(?) and room >=121 and room <=125",(int(h.get()),)).fetchone()[0]
        triple=cur.execute("select count(room) from room2 where cus_id =(?) and room >=126 and room <=130",(int(h.get()),)).fetchone()[0]
        quad=cur.execute("select count(room) from room2 where cus_id =(?) and room >=131 and room <=135",(int(h.get()),)).fetchone()[0]
        suite=cur.execute("select count(room) from room2 where cus_id =(?) and room >=136 and room <=140",(int(h.get()),)).fetchone()[0]
        king=cur.execute("select count(room) from room2 where cus_id =(?) and room >=141 and room <=145",(int(h.get()),)).fetchone()[0]
        queen=cur.execute("select count(room) from room2 where cus_id =(?) and room >=146 and room <=150",(int(h.get()),)).fetchone()[0]
        z3=(single*(500))+(double*(1000))+(twin*(1500))+(triple*(2000))+(quad*(2500))+(suite*(3000))+(king*(3500))+(queen*(4000))+z1+z2
        Label(root,text='Total amount = '+str(z3)+' INR  ',fg='black',font='times 15 bold italic').grid(row=17,column=3)
    Button(root,text='DETAIL',font='times 15 bold italic',bd=5,fg='black',bg='blue',command=details).grid(row=5,sticky=N)

    
Label(root,text='HOTEL MANAGEMENT SYSTEM',bg='blue',fg='black',relief='raised',bd=10,font='forte 20 bold',width=50).grid(row=0,column=0,columnspan=3)
img=PhotoImage(file='welcome.gif')
Label(root,image=img).grid(row=1,columnspan=3)
Label(root,text='Accomodations',fg='blue',font='times 20 bold').grid(row=2,column=0)
Label(root,text='Food orders',fg='blue',font='times 20 bold').grid(row=2,column=1)
Label(root,text='Customers',fg='blue',font='times 20 bold').grid(row=2,column=2)
Button(root,text='Rooms',height=2,width=20,bg='blue',bd=10,fg='black',font='times 12 bold',command=rooms).grid(row=3,column=0)
Button(root,text='Total Bill',height=2,width=20,bg='blue',bd=10,font='times 12 bold',command=bill).grid(row=4,column=0)
Button(root,text='New order',height=2,width=20,bg='blue',bd=10,font='times 12 bold',command=order).grid(row=3,column=1)
Button(root,text='View order',height=2,width=20,bg='blue',bd=10,font='times 12 bold',command=view).grid(row=4,column=1)
Button(root,text='New customer',height=2,width=20,bg='blue',bd=10,font='times 12 bold',command=ncustomer).grid(row=3,column=2)
Button(root,text='Search customer',height=2,width=20,bg='blue',bd=10,font='times 12 bold',command=scustomer).grid(row=4,column=2)
root.mainloop()
