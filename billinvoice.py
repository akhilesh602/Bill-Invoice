import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import*
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

t=tkinter.Tk()
t.geometry('1920x1080')
t.title('Invoice')
t.config(bg='light sea green')


    
def cal5():
    xa4=float(h4.get())
    xb4=float(j4.get())
    xc4=xa4*xb4
    m4.delete(0,100)
    m4.insert(0,str(xc4))
    
    xa3=float(h3.get())
    xb3=float(j3.get())
    xc3=xa3*xb3
    m3.delete(0,100)
    m3.insert(0,str(xc3))
    
    xa2=float(h2.get())
    xb2=float(j2.get())
    xc2=xa2*xb2
    m2.delete(0,100)
    m2.insert(0,str(xc2))
    
    xa1=float(h1.get())
    xb1=float(j1.get())
    xc1=xa1*xb1
    m1.delete(0,100)
    m1.insert(0,str(xc1))
    
    xa5=float(h5.get())
    xb5=float(j5.get())
    xc5=xa5*xb5
    m5.delete(0,100)
    m5.insert(0,str(xc5))
    
    xt1=float(m1.get())
    xt2=float(m2.get())
    xt3=float(m3.get())
    xt4=float(m4.get())
    xt5=float(m5.get())
    xt6=xt1+xt2+xt3+xt4+xt5
    n1.delete(0,100)
    n1.insert(0,str(xt6))
    
    xg=float(n1.get())
    xg1=0.18
    xg2=xg*xg1
    p1.delete(0,100)
    p1.insert(0,str(xg2))
    
    xf=float(n1.get())
    xf1=float(p1.get())
    xf2=xf+xf1
    messagebox.showinfo('Final amount',str(xf2))
    q1.delete(0,100)
    q1.insert(0,str(xf2))
    
def close():
    messagebox.showinfo('Thanks','Thankyou for shopping in ABC.SHOP')
    t.destroy()
    
def save():
    f=open(asksaveasfilename(),'a')
    f.write('\nName is : '+str(b1.get()))
    f.write('\nE-mail id is : '+str(d1.get()))
    f.write('\nContact no. is : '+str(e1.get()))
    f.write('\nAddress is : '+str(f1.get()))
    f.write('\nItem: '+str(g1.get())+'\tPrice: '+str(h1.get())+'\tQuantity: '+str(j1.get())+'\tAmount: '+str(m1.get()))
    f.write('\nItem: '+str(g2.get())+'\tPrice: '+str(h2.get())+'\tQuantity: '+str(j2.get())+'\tAmount: '+str(m2.get()))
    f.write('\nItem: '+str(g3.get())+'\tPrice: '+str(h3.get())+'\tQuantity: '+str(j3.get())+'\tAmount: '+str(m3.get()))
    f.write('\nItem: '+str(g4.get())+'\tPrice: '+str(h4.get())+'\tQuantity: '+str(j4.get())+'\tAmount: '+str(m4.get()))
    f.write('\nItem: '+str(g5.get())+'\tPrice: '+str(h5.get())+'\tQuantity: '+str(j5.get())+'\tAmount: '+str(m5.get()))
    f.write('\nTotal is : '+str(n1.get()))
    f.write('\nGST is :'+str(p1.get()))
    f.write('\nFinal is :'+str(q1.get()))
    f.close()
    
def send():
    from_address = "akhileshsisodia.602@gmail.com"
    to_address = (d1.get())

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Bill Invoice"
    msg['From'] = from_address
    msg['To'] = to_address

    f=open(askopenfilename(),'r')
    html=f.read()
    f.close()

    part1 = MIMEText(html, 'html')

    msg.attach(part1)

    username = 'akhileshsisodia.602@gmail.com'  
    password = 'eybwrfajrwrhzkqy'

    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login(username,password)  
    server.sendmail(from_address, to_address, msg.as_string())  
    server.quit()
    

a=Label(t,text='ABC.SHOP',font=('times new roman',34,UNDERLINE),fg='blue',bd=4,bg='light sea green')
a.place(x=630,y=20)


b=Label(t,text='Name',font=('times new roman',22),bg='light sea green')
b.place(x=120,y=120)
b1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
b1.place(x=300,y=120)

d=Label(t,text='E-Mail',font=('times new roman',22),bg='light sea green')
d.place(x=850,y=120)
d1=Entry(t,width=35,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
d1.place(x=1000,y=120)

e=Label(t,text='Contact no.',font=('times new roman',22),bg='light sea green')
e.place(x=120,y=180)
e1=Entry(t,width=25,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
e1.place(x=300,y=180)

f=Label(t,text='Address',font=('times new roman',22),bg='light sea green')
f.place(x=850,y=180)
f1=Entry(t,width=35,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
f1.place(x=1000,y=180)

g=Label(t,text='Item name',font=('times new roman',22),bg='light sea green')
g.place(x=100,y=250)
g1=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
g1.place(x=40,y=300)
g2=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
g2.place(x=40,y=350)
g3=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
g3.place(x=40,y=400)
g4=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
g4.place(x=40,y=450)
g5=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
g5.place(x=40,y=500)

h=Label(t,text='Price',font=('times new roman',22),bg='light sea green')
h.place(x=450,y=250)
h1=Entry(t,width=10,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
h1.place(x=420,y=300)
h2=Entry(t,width=10,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
h2.place(x=420,y=350)
h3=Entry(t,width=10,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
h3.place(x=420,y=400)
h4=Entry(t,width=10,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
h4.place(x=420,y=450)
h5=Entry(t,width=10,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
h5.place(x=420,y=500)

j=Label(t,text='Quantity',font=('times new roman',22),bg='light sea green')
j.place(x=700,y=250)
j1=Spinbox(t,from_=1,to=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
j1.place(x=630,y=300)
j2=Spinbox(t,from_=1,to=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
j2.place(x=630,y=350)
j3=Spinbox(t,from_=1,to=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
j3.place(x=630,y=400)
j4=Spinbox(t,from_=1,to=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
j4.place(x=630,y=450)
j5=Spinbox(t,from_=1,to=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
j5.place(x=630,y=500)

k=Label(t,text='Calculate',font=('times new roman',22),bg='light sea green')
k.place(x=950,y=250)

k3=Button(t,text='  Calculate  ',bd=4,font=1,bg='light slate gray',fg='cyan',command=cal5)
k3.place(x=955,y=400)


m=Label(t,text='Amount',font=('times new roman',22),bg='light sea green')
m.place(x=1200,y=250)
m1=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
m1.place(x=1150,y=300)
m2=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
m2.place(x=1150,y=350)
m3=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
m3.place(x=1150,y=400)
m4=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
m4.place(x=1150,y=450)
m5=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
m5.place(x=1150,y=500)

n=Label(t,text='Total',font=('times new roman',22),bg='light sea green')
n.place(x=1000,y=570)
n1=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
n1.place(x=1150,y=570)

p=Label(t,text='GST',font=('times new roman',22),bg='light sea green')
p.place(x=1000,y=620)
p1=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
p1.place(x=1150,y=620)

q=Label(t,text='Final',font=('times new roman',22),bg='light sea green')
q.place(x=1000,y=670)
q1=Entry(t,width=20,font=("Comic Sans MS", 14,"bold") ,fg='royalblue',bg='thistle',bd=4)
q1.place(x=1150,y=670)

r=Button(t,text='   Save   ',fg='green yellow',font=1,bd=5,bg='light slate gray',command=save)
r.place(x=100,y=620)
r=Button(t,text='   E-mail   ',fg='RoyalBlue3',bd=5,font=1,bg='light slate gray',command=send)
r.place(x=350,y=620)
r=Button(t,text='   Close   ',fg='brown',bd=5,font=1,bg='light slate gray',command=close)
r.place(x=650,y=620)

t.mainloop()