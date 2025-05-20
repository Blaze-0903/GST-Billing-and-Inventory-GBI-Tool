##LOGIN##
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import mysql.connector as ms
from datetime import *
from pytz import *
from tkcalendar import *
from num2words import num2words

wi=Tk()
wi.config(background='#D7D8D8')
wi.geometry('1366x768')
gl=PhotoImage(file='F:\Python\Project\Images\\gbi logo.png')
power=PhotoImage(file='F:\\Python\\Project\\Images\\powerb.png')
wi.iconphoto(True,gl)


IST= timezone('Asia/Kolkata')
varb=IntVar()
i_no=1
blazec=0

label=Label(wi,bg='#7B7571',padx=700,pady=15)
label.place(x=0,y=0)
l1=Label(wi,text='GBI Tool',font=('Comic Sans',20,'bold'),fg='white',bg='#7B7571',pady=6)
l1.place(x=10,y=0)
label1=Label(wi,padx=500,pady=41,relief=GROOVE,bg='white')
label1.place(x=150,y=49)
label0=Label(wi,padx=500,pady=71,relief=GROOVE,bg='white')
label0.place(x=150,y=148)
l2=Label(wi,text='Gst Billing and Invoice Creation Tool',fg='grey',font=('Arial',30),bg='white')
l2.place(x=151,y=50)
lg=Label(wi,image=gl,relief=FLAT,bg='white')
lg.place(x=950,y=65)
l3=Label(wi,text='S i m p l e s t   G s t   I n v o i c i n g         T o o l',font=('Arial',15),pady=10,padx=10,fg='grey',bg='white')
l3.place(x=151,y=100)
l31=Label(wi,text='G S T   I N V O I C I N G',font=('Arial',15,'bold'),fg='grey',bg='white')
l31.place(x=294,y=110)
la=Label(wi,text='#    Easily create invoices', font=('Times New Roman',13),bg='white')
la.place(x=180,y=160)
lb=Label(wi,text='#    Manage Inventory', font=('Times New Roman',13),bg='white')
lb.place(x=180,y=182)
lc=Label(wi,text='#    Keep Books and track balances', font=('Times New Roman',13),bg='white')
lc.place(x=180,y=204)

txt='''Login or SignUp
&
Start Billing!!!'''
t='''G
B
I

T
O
O
L'''
c=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
cr=c.cursor()

def nxt():
    w=Toplevel()      #window object
    w.title('Login')                         #Title of our window
    w.geometry('1366x768')
    lg1=PhotoImage(file='F:\\Python\\Project\\Images\\login1.png')
    l=Label(w,image=lg1,relief=FLAT)
    l.place(x=0,y=0)

    label=Label(w,bg='#7B7571',padx=700,pady=15)
    label.place(x=0,y=0)
    label1=Label(w,bg='#7B7571',padx=700,pady=15)
    label1.place(x=0,y=718)

    l1=Label(w,text='GBI Tool',font=('Comic Sans',20,'bold'),fg='white',bg='#7B7571',pady=6)
    l1.place(x=10,y=0)

    

    label=Label(w,   #window object and text to be shown
            font=('Arial',10,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='gold',   #label bg color
            relief=GROOVE,  #label border style
            padx=200,   #spacing of text from border in x axis
            pady=90)
    label.place(x=480,y=250+60)

    ll=Label(w,   #window object and text to be shown
            font=('Arial',10,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='gold',   #label bg color
            relief=GROOVE,  #label border style
            padx=200,   #spacing of text from border in x axis
            pady=42)
    ll.place(x=480,y=148+60)
    global txt
    dt=Label(w,text=txt,   #window object and text to be shown
            font=('Times New Roman',14),      #font name,size and style
            fg='black',   #text color
            bg='gold',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
    dt.place(x=615,y=160+60)


    label1=Label(w,text='Login',   #window object and text to be shown
            font=('Arial',15,'bold'),      #font name,size and style
            fg='snow',   #text color
            bg='midnightblue',   #label bg color
             relief=GROOVE,
                 padx=2,
            width=33,   #spacing of text from border in x axis
            pady=10)
    label1.place(x=480,y=101+60)

    label2=Label(w,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='gold',   #label bg color
            relief=GROOVE,
            padx=200,   #spacing of text from border in x axis
            pady=20)
    label2.place(x=480,y=250+60)

    username=Label(w,text='Username:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='gold',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
    username.place(x=500,y=264+60)

    passwd=Label(w,text='Password:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='gold',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
    passwd.place(x=500,y=335+60)

    entry_usr=Entry(w,font=('Arial',13),
            fg='black',
            bg='WHITE',)
    entry_usr.insert(0,'Sujal Junghare')     #sets default string with positional  argument(position,text)
    entry_usr.place(x=620,y=269+60)

    entry_pas=Entry(w,font=('Arial',13),
            fg='black',
            bg='WHITE',
            show='*')    #used to show different text insted of what is being inputed(like password is hidden with *) can be used with config
    entry_pas.insert(0,'Suj@l0903')     #sets default string with positional  argument(position,text)
    entry_pas.place(x=620,y=340+60)
    sh=0
    def show():
        nonlocal sh
        nonlocal entry_pas
        sh+=1
        if sh%2!=0:
            entry_pas.config(show='')
        else:
           entry_pas.config(show='*')
    show_p=PhotoImage(file='F:\\Python\\Project\\Images\\hidden.png')
    see_b=Button(w,image=show_p,bg='white',borderwidth=0,command=show,cursor='hand2')
    see_b.place(x=680+102,y=404)
    
    


    def submit():
        global cr
        usr=entry_usr.get()
        global pas
        pas=entry_pas.get()
        f=True
        cr.execute('select * from login')
        data=cr.fetchall()
        for i in data:
            if i[0]==usr and i[1]==pas:
                f=False

                def n_invoicem():
                    w3=Toplevel()
                    w3.geometry('1366x768')                    #Dimensions of our window
                    w3.config(background='white')

                    label=Label(w3,bg='#7B7571',padx=700,pady=15)
                    label.place(x=0,y=0)

                    l1=Label(w3,text='GBI Tool',font=('Comic Sans',20,'bold'),fg='white',bg='#7B7571',pady=6)
                    l1.place(x=10,y=0)

                    l2=Label(w3,text='Gst Invoice',font=('Arial',25),fg='#7B7571',bg='white')
                    l2.place(x=0,y=50)

                    def n_in():
                        nonlocal w3
                        
                        w3.destroy()
                        n_invoicem()

                    n_invoice=Button(w3,text='New Invoice',
                        font=('Comic Sans',10,'bold'),
                       fg="light grey",
                       bg='#7B7571',
                        cursor='hand2',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        command=n_in,
                       relief=FLAT)      #bg color of button when is clicked
                    n_invoice.config(state=NORMAL)
                    n_invoice.place(x=170,y=10)

                    def invoicest():
                        wiv=Tk()
                        wiv.geometry('1366x768')
                        wiv.config(background='white')

                        label=Label(wiv,text='Invoices', fg='grey',bg='white',
                                    font=('Arial',26))
                        label.place(x=0,y=0)

                        label2=Label(wiv,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=RAISED,
                                    padx=1000,   #spacing of text from border in x axis
                                     bg='#7B7571',
                                    pady=6)
                        label2.place(x=0,y=47)


                        iN=Label(wiv,text='Invoice Number',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        iN.place(x=8,y=50)

                        dat=Label(wiv,text='Date | Time',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        dat.place(x=308,y=50)

                        ct=Label(wiv,text='Customer',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        ct.place(x=708,y=50)
                        c=0
                        invoices=[]
                        global pas 
                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                        cr=ci.cursor()
                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                        no1=cr.fetchone()
                        gstp=str(no1[0])
                        ci.commit()
                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                        cr1=c1.cursor()
                        qchp='select * from invoices'
                        cr1.execute(qchp)
                        invoices=cr1.fetchall()
                        print(len(invoices))
                        c1.commit()
                        if len(invoices)==0:
                            label2=Label(wiv,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='white',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                            label2.place(x=0,y=82)
                            pn=Label(wiv,text='No data available in table',font=('Arial',12),bg='white')
                            pn.place(x=600,y=85)
                        else:
                            for i in invoices:
                                label2=Label(wiv,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='white',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                                label2.place(x=0,y=82+34*c)
                                pnv=Label(wiv,text=invoices[c][0],bg='white',font=('Arial',12,'bold'))
                                pnv.place(x=8,y=85+32*c+2*c)

                                ldt=str(invoices[c][1])
                                ltm=str(invoices[c][3])
                                ldm=ldt+' | '+ltm
                                gstv=Label(wiv,text=ldm,bg='white',font=('Arial',12,'bold'))
                                gstv.place(x=308,y=85+32*c+2*c)

                                rgv=Label(wiv,text=invoices[c][2],bg='white',font=('Arial',12,'bold'))
                                rgv.place(x=708,y=85+32*c+2*c)

                                def view(y=c):
                                    wview=Tk()
                                    wview.config(background='white')
                                    wview.geometry('1366x768')

                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    qchp='select * from invoices'
                                    cr1.execute(qchp)
                                    ldt=str(invoices[y][1])
                                    ltm=str(invoices[y][3])
                                    stxt='Invoice Date: '+ldt
                                    iblabel=Label(wview,padx=700,pady=8)
                                    iblabel.place(x=0,y=0)
                                    ilabel=Label(wview,text=stxt,font=('Arial',12,'bold'))
                                    ilabel.place(x=20,y=4)
                                    
                                    
                                    #Left Info
                                    cr.execute("select Business_name,Address,e_mail,Phone_no,Gst_no from Details where passwd='{}'".format(pas))
                                    data1=cr.fetchall()
                                    ci.commit()
                                    for j in data1:
                                        b_name=j[0]
                                        ad=j[1]
                                        em=j[2]
                                        ph=j[3]
                                        gn=j[4]
                                        
                                        
                                    itlabel=Label(wview,text=b_name,font=('Arial',12,'bold'),bg='white',pady=0)
                                    itlabel.place(x=20,y=60)
                                    
                                    sad=Label(wview,text=ad,font=('Arial',12),bg='white',pady=0)
                                    sad.place(x=20,y=80)

                                    etxt='EMAIL: '+em
                                    email=Label(wview,text=etxt,font=('Arial',12),bg='white',pady=0)
                                    email.place(x=20,y=100)

                                    ptxt='Phone: '+ph
                                    phone=Label(wview,text=ptxt,font=('Arial',12),bg='white',pady=0)
                                    phone.place(x=20,y=120)

                                    gtxt='GST No: '+gn
                                    gst=Label(wview,text=gtxt,font=('Arial',12),bg='white',pady=0)
                                    gst.place(x=20,y=140)

                                    #Right Info
                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    cr1.execute('select Customer,Address,State,Mob_no,GSt_no from customers,invoices where customers.name=invoices.customer')
                                    righti=cr1.fetchall()
                                    c1.commit()
                                    
                                    blabel=Label(wview,text='Billed To:',font=('Arial',12),bg='white',pady=0)
                                    blabel.place(x=900,y=60)

                                    cn=righti[y][0]   
                                    cname=Label(wview,text=cn,font=('Arial',12,'bold'),bg='white',pady=0)
                                    cname.place(x=900,y=100)

                                    cad=righti[y][1]
                                    state=righti[y][2]
                                    cadp=cad.split(',')
                                    if len(cadp)!=1:
                                        city=cadp[-1]+' , '+state
                                        clabel=Label(wview,text=city,font=('Arial',12),bg='white',pady=0)
                                        clabel.place(x=896,y=120)
                                    else:
                                        city=cadp[-1]+' , '+state
                                        clabel=Label(wview,text=city,font=('Arial',12),bg='white',pady=0)
                                        clabel.place(x=900,y=120)

                                    ph1=righti[y][3]
                                    ptxt1='Phone: '+ph1
                                    phone1=Label(wview,text=ptxt1,font=('Arial',12),bg='white',pady=0)
                                    phone1.place(x=900,y=140)

                                    gn1=righti[y][4]
                                    gtxt1='GST No: '+gn1
                                    gst1=Label(wview,text=gtxt1,font=('Arial',12),bg='white',pady=0)
                                    gst1.place(x=900,y=160)

                                    #Table Items
                                    nonlocal prd
                                    nonlocal qty
                                    nonlocal RTE
                                    nonlocal AWG
                                    nonlocal PER
                                    nonlocal SGST
                                    nonlocal CGST
                                    nonlocal AGL
                                    global blazec

                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    cr1.execute('select Gst_type from invoices')
                                    typ=cr1.fetchall()
                                    c1.commit()
                                    #Table stucture
                                    if int(typ[y][0])==0:
                                        labelh=Label(wview,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                        labelh.place(x=20,y=200)
                                        hlabel=Label(wview,text='#',font=('Arial',12,'bold'),bg='white',pady=0)
                                        hlabel.place(x=21,y=201)

                                        labelp=Label(wview,bg='white',pady=5,width=45,relief=GROOVE)
                                        labelp.place(x=38+7,y=200)
                                        PN=Label(wview,text='Items',font=('Arial',12,'bold'),bg='white',pady=0)
                                        PN.place(x=45+7,y=201)

                                        labelq=Label(wview,bg='white',pady=5,width=15,relief=GROOVE)
                                        labelq.place(x=300+7,y=200)
                                        qt=Label(wview,text='QTY',font=('Arial',12,'bold'),bg='white',pady=0)
                                        qt.place(x=302+7,y=201)

                                        labelr=Label(wview,bg='white',pady=5,width=20,relief=GROOVE)
                                        labelr.place(x=400+7,y=200)
                                        rt=Label(wview,text='Rate(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        rt.place(x=402+7,y=201)

                                        
                                        labelat=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelat.place(x=540+7,y=200)
                                        tat=Label(wview,text='Taxable Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        tat.place(x=542+7,y=201)

                                        labelgp=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelgp.place(x=726+7,y=200)
                                        gp=Label(wview,text='GST(%)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        gp.place(x=728+7,y=201)

                                        labelc=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelc.place(x=856+7,y=200)
                                        cg=Label(wview,text='CGST(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        cg.place(x=858+7,y=201)

                                        labels=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labels.place(x=986+7,y=200)
                                        sg=Label(wview,text='SGST(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        sg.place(x=988+7,y=201)

                                        labelto=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelto.place(x=1105+7,y=200)
                                        tot=Label(wview,text='Total Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        tot.place(x=1107+7,y=201)

                                        #Tabel Contents
                                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                        cr1=c1.cursor()
                                        qchp='select from invoices'
                                        cr1.execute('select distinct(Items),Qty,Rate,Tax_amt,Percent from product_details where date="{}" and time="{}"'.format(ldt,ltm))
                                        tc=cr1.fetchall()
                                        c1.commit()
                                        r=0
                                        tot=0
                                        ctot=0
                                        totb=0
                                        for i in range(len(tc)):
                                                labelh1=Label(wview,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                                labelh1.place(x=20,y=227+i*27)
                                                hlabel1=Label(wview,text=i+1,font=('Arial',12),bg='white',pady=0)
                                                hlabel1.place(x=21,y=228+i*27)

                                                labelp1=Label(wview,bg='white',pady=5,width=45,relief=GROOVE)
                                                labelp1.place(x=38+7,y=227+i*27)
                                                PN1=Label(wview,text=tc[i][0],font=('Arial',12),bg='white',pady=0)
                                                PN1.place(x=45+7,y=228+i*27)

                                                labelq1=Label(wview,bg='white',pady=5,width=15,relief=GROOVE)
                                                labelq1.place(x=300+7,y=227+i*27)
                                                qt1=Label(wview,text=tc[i][1],font=('Arial',12),bg='white',pady=0)
                                                qt1.place(x=302+7,y=228+i*27)

                                                labelr1=Label(wview,bg='white',pady=5,width=20,relief=GROOVE)
                                                labelr1.place(x=400+7,y=227+i*27)
                                                rt1=Label(wview,text=tc[i][2],font=('Arial',12),bg='white',pady=0)
                                                rt1.place(x=402+7,y=228+i*27)
                                                

                                                txam=int(tc[i][2])*int(tc[i][1])
                                                labelat1=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                                labelat1.place(x=540+7,y=227+i*27)
                                                tat1=Label(wview,text=txam,font=('Arial',12),bg='white',pady=0)
                                                tat1.place(x=542+7,y=228+i*27)
                                                tot+=txam

                                                labelgp1=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                                labelgp1.place(x=726+7,y=227+i*27)
                                                gp1=Label(wview,text=tc[i][4],font=('Arial',12),bg='white',pady=0)
                                                gp1.place(x=728+7,y=228+i*27)
                                                
                                                
                                                perc=int(tc[i][4])/2
                                                cgst=perc*txam/100
                                                labelc1=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                                labelc1.place(x=856+7,y=227+i*27)
                                                cg1=Label(wview,text=cgst,font=('Arial',12),bg='white',pady=0)
                                                cg1.place(x=858+7,y=228+i*27)
                                                ctot+=cgst

                                                labels1=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                                labels1.place(x=986+7,y=227+i*27)
                                                sg1=Label(wview,text=cgst,font=('Arial',12),bg='white',pady=0)
                                                sg1.place(x=988+7,y=228+i*27)

                                                totx=txam+2*cgst
                                                labelto1=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                                labelto1.place(x=1105+7,y=227+i*27)
                                                tot1=Label(wview,text=totx,font=('Arial',12),bg='white',pady=0)
                                                tot1.place(x=1107+7,y=228+i*27)
                                                totb+=totx
                                                
                                                r+=1

                                        #Table Total
                                        labelt=Label(wview,bg='white',pady=5,padx=7,width=74,relief=GROOVE)
                                        labelt.place(x=20,y=228+r*27)
                                        tlabel=Label(wview,text='Total:',font=('Arial',12,'bold'),bg='white',pady=0)
                                        tlabel.place(x=490+7,y=230+r*27)
                                                
                                        labelat2=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelat2.place(x=540+7,y=228+r*27)
                                        
                                        nonlocal ag4
                                        tlabel=Label(wview,text=tot,font=('Arial',12,'bold'),bg='white',pady=0)
                                        tlabel.place(x=542+7,y=230+r*27)
                                                
                                        labelgp2=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelgp2.place(x=726+7,y=228+r*27)
                                                
                                        labelc2=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelc2.place(x=856+7,y=228+r*27)
                                        
                                        ctlabel=Label(wview,text=ctot,font=('Arial',12,'bold'),bg='white',pady=0)
                                        ctlabel.place(x=858+7,y=230+r*27)
                                                
                                        labels2=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labels2.place(x=986+7,y=228+r*27)
                                        ctlabel=Label(wview,text=ctot,font=('Arial',12,'bold'),bg='white',pady=0)
                                        ctlabel.place(x=988+7,y=230+r*27)
                                                
                                        labelto2=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelto2.place(x=1105+7,y=228+r*27)
                                        atlabel=Label(wview,text=totb,font=('Arial',12,'bold'),bg='white',pady=0)
                                        atlabel.place(x=1107+7,y=230+r*27)

                                        twords=num2words(totb,lang='en_IN')+' only.'
                                        twordsf=twords.capitalize()
                                        labeltw=Label(wview,bg='white',pady=5,padx=1,width=111,relief=GROOVE)
                                        labeltw.place(x=510+7,y=260+r*27)
                                        labeltw1=Label(wview,text='Invoice Total in Words:',font=('Arial',12,'bold'),bg='white',pady=0)
                                        labeltw1.place(x=520+7,y=262+r*27)
                                        labeltw2=Label(wview,text=twordsf,font=('Arial',12,'bold'),bg='white',pady=0)
                                        labeltw2.place(x=700+7,y=262+r*27)

                                    else:
                                        labelh=Label(wview,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                        labelh.place(x=20,y=200)
                                        hlabel=Label(wview,text='#',font=('Arial',12,'bold'),bg='white',pady=0)
                                        hlabel.place(x=21,y=201)

                                        labelp=Label(wview,bg='white',pady=5,width=45,relief=GROOVE)
                                        labelp.place(x=38+7,y=200)
                                        PN=Label(wview,text='Items',font=('Arial',12,'bold'),bg='white',pady=0)
                                        PN.place(x=45+7,y=201)

                                        labelq=Label(wview,bg='white',pady=5,width=15,relief=GROOVE)
                                        labelq.place(x=300+7,y=200)
                                        qt=Label(wview,text='QTY',font=('Arial',12,'bold'),bg='white',pady=0)
                                        qt.place(x=302+7,y=201)

                                        labelr=Label(wview,bg='white',pady=5,width=20,relief=GROOVE)
                                        labelr.place(x=400+7,y=200)
                                        rt=Label(wview,text='Rate(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        rt.place(x=402+7,y=201)

                                        labelat=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelat.place(x=540+7,y=200)
                                        tat=Label(wview,text='Taxable Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        tat.place(x=542+7,y=201)

                                        labelgp=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelgp.place(x=726+7,y=200)
                                        gp=Label(wview,text='GST(%)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        gp.place(x=728+7,y=201)

                                        labelc=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelc.place(x=856+7,y=200)
                                        cg=Label(wview,text='IGST(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        cg.place(x=858+7,y=201)

                                        labelto=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelto.place(x=986+7,y=200)
                                        tot=Label(wview,text='Total Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                        tot.place(x=988+7,y=201)

                                        #Tabel Contents
                                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                        cr1=c1.cursor()
                                        qchp='select from invoices'
                                        cr1.execute('select distinct(Items),Qty,Rate,Tax_amt,Percent from product_details where date="{}" and time="{}"'.format(ldt,ltm))
                                        tc=cr1.fetchall()
                                        c1.commit()
                                        r=0
                                        tot=0
                                        itot=0
                                        totb=0
                                        for i in range(len(tc)):
                                                r+=1
                                                labelh1=Label(wview,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                                labelh1.place(x=20,y=227+i*27)
                                                hlabel1=Label(wview,text=i+1,font=('Arial',12),bg='white',pady=0)
                                                hlabel1.place(x=21,y=228+i*27)

                                                labelp1=Label(wview,bg='white',pady=5,width=45,relief=GROOVE)
                                                labelp1.place(x=38+7,y=227+i*27)
                                                PN1=Label(wview,text=tc[i][0],font=('Arial',12),bg='white',pady=0)
                                                PN1.place(x=45+7,y=228+i*27)

                                                labelq1=Label(wview,bg='white',pady=5,width=15,relief=GROOVE)
                                                labelq1.place(x=300+7,y=227+i*27)
                                                qt1=Label(wview,text=tc[i][1],font=('Arial',12),bg='white',pady=0)
                                                qt1.place(x=302+7,y=228+i*27)

                                                labelr1=Label(wview,bg='white',pady=5,width=20,relief=GROOVE)
                                                labelr1.place(x=400+7,y=227+i*27)
                                                rt1=Label(wview,text=tc[i][2],font=('Arial',12),bg='white',pady=0)
                                                rt1.place(x=402+7,y=228+i*27)

                                                txam=int(tc[i][2])*int(tc[i][1])
                                                labelat1=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                                labelat1.place(x=540+7,y=227+i*27)
                                                tat1=Label(wview,text=txam,font=('Arial',12),bg='white',pady=0)
                                                tat1.place(x=542+7,y=228+i*27)
                                                tot+=txam

                                                labelgp1=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                                labelgp1.place(x=726+7,y=227+i*27)
                                                gp1=Label(wview,text=tc[i][4],font=('Arial',12),bg='white',pady=0)
                                                gp1.place(x=728+7,y=228+i*27)

                                                perc=int(tc[i][4])/2
                                                igst=perc*txam/100
                                                labelc1=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                                labelc1.place(x=856+7,y=227+i*27)
                                                cg1=Label(wview,text=igst,font=('Arial',12),bg='white',pady=0)
                                                cg1.place(x=858+7,y=228+i*27)
                                                itot+=igst

                                                totx=txam+2*igst
                                                labelto1=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                                labelto1.place(x=986+7,y=227+i*27)
                                                tot1=Label(wview,text=AGL[i].get(),font=('Arial',12),bg='white',pady=0)
                                                tot1.place(x=988+7,y=228+i*27)
                                                totb+=totx

                                        #Table Total
                                        labelt=Label(wview,bg='white',pady=5,padx=7,width=74,relief=GROOVE)
                                        labelt.place(x=20,y=228+r*27)
                                        tlabel=Label(wview,text='Total:',font=('Arial',12,'bold'),bg='white',pady=0)
                                        tlabel.place(x=490+7,y=230+r*27)
                                                
                                        labelat2=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelat2.place(x=540+7,y=228+r*27)
                                        tlabel=Label(wview,text=tot,font=('Arial',12,'bold'),bg='white',pady=0)
                                        tlabel.place(x=542+7,y=230+r*27)
                                                
                                        labelgp2=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelgp2.place(x=726+7,y=228+r*27)
                                                
                                        labelc2=Label(wview,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelc2.place(x=856+7,y=228+r*27)
                                        
                                        itlabel=Label(wview,text=itot,font=('Arial',12,'bold'),bg='white',pady=0)
                                        itlabel.place(x=858+7,y=230+r*27)
                                                
                                        labelto2=Label(wview,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelto2.place(x=986+7,y=228+r*27)
                                        
                                        atlabel=Label(wview,text=totb,font=('Arial',12,'bold'),bg='white',pady=0)
                                        atlabel.place(x=988+7,y=230+r*27)

                                        twords=num2words(totb,lang='en_IN')+' only.'
                                        twordsf=twords.capitalize()
                                        labeltw=Label(wview,bg='white',pady=5,padx=2,width=111,relief=GROOVE)
                                        labeltw.place(x=510-120+7,y=260+r*27)
                                        labeltw1=Label(wview,text='Invoice Total in Words:',font=('Arial',12,'bold'),bg='white',pady=0)
                                        labeltw1.place(x=520-120+7,y=262+r*27)
                                        labeltw2=Label(wview,text=twordsf,font=('Arial',12,'bold'),bg='white',pady=0)
                                        labeltw2.place(x=700-120+7,y=262+r*27)

                                    wview.mainloop()
                                
                                   
                                v_btn=Button(wiv, text='View',
                                     padx=5,
                                     pady=0,
                                   font=('Arial',12),
                                   fg="white",
                                   bg='#0476D0',
                                     relief=FLAT,
                                    cursor='hand2',
                                    command=view,
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                                v_btn.place(x=1110,y=84+32*c+2*c)

                                def delete(x=c):
                                    nonlocal wiv
                                    nonlocal invoicest
                                    nonlocal invoices
                                    global pas 
                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    cr1.execute("delete from invoices where Invoice_no={}".format(invoices[x][0]))
                                    c1.commit()
                                    mb.showinfo("GBI Tool", "Invioce Deleted Successfully!",parent=wiv)
                                    wiv.destroy()
                                    invoicest()

                                d_btn=Button(wiv, text='Delete',
                                     padx=5,
                                     pady=0,
                                   font=('Arial',12),
                                   fg="white",
                                   bg='red',
                                     relief=FLAT,
                                    command=delete,
                                    cursor='hand2',
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                                d_btn.place(x=1275,y=84+32*c+2*c)

                                c+=1

                        wiv.mainloop()


                    invoices=Button(w3,text='Invoices',
                       font=('Comic Sans',10,'bold'),
                       fg="light grey",
                       bg='#7B7571',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        command=invoicest,
                        cursor='hand2',
                       relief=FLAT)      #bg color of button when is clicked
                    invoices.config(state=ACTIVE)
                    invoices.place(x=265,y=10)

                    def inventory():
                        win=Tk()
                        win.geometry('1366x768')
                        win.config(background='white')

                        label=Label(win,text='Inventory', fg='grey',bg='white',
                                    font=('Arial',26))
                        label.place(x=0,y=0)

                        label2=Label(win,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=RAISED,
                                    padx=1000,   #spacing of text from border in x axis
                                     bg='#7B7571',
                                    pady=6)
                        label2.place(x=0,y=47)
                        label2.config()

                        pn=Label(win,text='Product',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        pn.place(x=208,y=50)

                        st=Label(win,text='Current Stock',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        st.place(x=508,y=50)

                        lt=Label(win,text='Last transaction',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        lt.place(x=808,y=50)
                        c=0
                        producti=[]
                        global pas 
                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                        cr=ci.cursor()
                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                        no1=cr.fetchone()
                        gstp=str(no1[0])
                        ci.commit()
                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                        cr1=c1.cursor()
                        qchp='select Name, Total_stock, Last_T, time from products'
                        cr1.execute(qchp)
                        producti=cr1.fetchall()
                        c1.commit()
                        if len(producti)==0:
                            label2=Label(win,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='#EDEFEE',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                            label2.place(x=0,y=82)
                            pn=Label(win,text='No data available in table',font=('Arial',12),bg='light grey')
                            pn.place(x=600,y=85)
                        else:
                            for i in range(len(producti)):
                                def product_info(e,x=i):
                                    pi=Toplevel()
                                    pi.config(background='#dbebfc')
                                    pi.geometry('500x400+400+114')
                                    pi.overrideredirect(1)

                                    def on_enter(e):
                                        e.widget['image']=rc1

                                    def on_leave(e):
                                        e.widget['image']=bc1

                                    cr.execute('select Business_name from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    b_name=str(no1[0])
                                    ci.commit()
                        
                                    cr1.execute('select * from products')
                                    pd=[]
                                    pd=cr1.fetchall()
                                    c1.commit()

                                    
                                    LabelB=Label(pi,text=b_name,font=('Arial',20,'bold'),bg='#dbebfc',fg='#0476D0')
                                    LabelB.pack(anchor=N)

                                    cLabel=Label(pi,height=3,width=600,relief=GROOVE, border=2,bg='light grey')
                                    cLabel.pack(anchor=N)
                                    CLabel=Label(pi,text='Product Info',font=('Arial',18),fg='#0476D0',bg='light grey')
                                    CLabel.place(x=2,y=45)

                                    nc=pd[x][0]
                                    nlabel=Label(pi,text=nc,bg='#dbebfc',font=('Arial',18,'italic underline'),fg='#0476D0')
                                    nlabel.place(x=155,y=100)

                                    ng=pd[x][1]
                                    glabel=Label(pi,text='Total Stock:',bg='#dbebfc',font=('Arial',16,'bold'))
                                    glabel.place(x=120,y=150)
                                    Glabel=Label(pi,text=ng,bg='#dbebfc',font=('Arial',16,'italic'))
                                    Glabel.place(x=250,y=150)

                                    ca=pd[x][2]
                                    Alabel=Label(pi,text='Rate:',bg='#dbebfc',font=('Arial',16,'bold'))
                                    Alabel.place(x=189,y=177+27)
                                    alabel=Label(pi,text=ca,bg='#dbebfc',font=('Arial',16))
                                    alabel.place(x=250,y=177+27)
                                    
                                  

                                    ns=pd[x][3]
                                    Slabel=Label(pi,text='GST%:',bg='#dbebfc',font=('Arial',16,'bold'))
                                    Slabel.place(x=177,y=150+27*4)
                                    slabel=Label(pi,text=ns,bg='#dbebfc',font=('Arial',16,'italic'))
                                    slabel.place(x=250,y=150+27*4)

                                    if len(str(pd[x][4]))!=4:
                                        ldt=str(pd[x][4])
                                        ltm=str(pd[x][5])
                                        ldm=ldt+' | '+ltm
                                        tlabel=Label(pi,text='Last transaction:',bg='#dbebfc',font=('Arial',16,'bold'))
                                        tlabel.place(x=46,y=150+27*6)
                                        dlabel=Label(pi,text=ldm,bg='#dbebfc',font=('Arial',16,'italic'))
                                        dlabel.place(x=224,y=150+27*6)

                                    else:
                                        tlabel=Label(pi,text='Last transaction:',bg='#dbebfc',font=('Arial',16,'bold'))
                                        tlabel.place(x=46,y=150+27*6)
                                        dlabel=Label(pi,text='--------- | ----------',bg='#dbebfc',font=('Arial',16,'italic'))
                                        dlabel.place(x=224,y=150+27*6)

                                    

                                    rc1=PhotoImage(file='F:\\Python\\Project\\Images\\red_cross.png')
                                    bc1=PhotoImage(file='F:\\Python\Project\\Images\\blue_cross.png')
                                    def command():
                                        pi.destroy()
                                    d_btn=Button(pi,image=bc1,borderwidth=0,command=command)
                                    d_btn.place(x=0,y=0)
                                    d_btn.bind('<Enter>',on_enter)
                                    d_btn.bind('<Leave>',on_leave)


                                    pi.mainloop()

                                label2=Label(win,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='white',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                                label2.place(x=0,y=82+34*c)
                                pnv=Label(win,text=producti[i][0],bg='white',font=('Arial',12,'bold'),cursor='hand2',fg='#0476D0')
                                pnv.place(x=208,y=85+32*c+2*c)
                                pnv.bind('<Button-1>',product_info)

                                stv=Label(win,text=producti[i][1],bg='white',font=('Arial',12,'bold'))
                                stv.place(x=510,y=85+32*c+2*c)

                               
                                if len(str(producti[i][2]))!=4:
                                    pv=str(producti[i][2])+' | '+str(producti[i][3])
                                    ltv=Label(win,text=pv,bg='white',font=('Arial',12,'bold'))
                                    ltv.place(x=808,y=85+32*c+2*c)

                                else:
                                    ltv=Label(win,text='--------- | ----------',bg='white',font=('Arial',12,'bold'))
                                    ltv.place(x=808,y=85+32*c+2*c)
                                c+=1
                                
                        win.mainloop()


                    Inventory=Button(w3,text='Inventory',
                       font=('Comic Sans',10,'bold'),
                       fg="light grey",
                       bg='#7B7571',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        command=inventory,
                        cursor='hand2',
                       relief=FLAT)      #bg color of button when is clicked
                    Inventory.config(state=ACTIVE)
                    Inventory.place(x=329,y=10)

                    def book():
                        wb=Tk()
                        wb.geometry('1366x768')
                        wb.config(background='white')

                        label=Label(wb,text='Book', fg='grey',bg='white',
                                    font=('Arial',26))
                        label.place(x=0,y=0)

                        label2=Label(wb,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=RAISED,
                                    padx=1000,   #spacing of text from border in x axis
                                     bg='#7B7571',
                                    pady=6)
                        label2.place(x=0,y=47)
                        label2.config()

                        pn=Label(wb,text='Customer',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        pn.place(x=208,y=50)

                        cb=Label(wb,text='Total Transaction',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        cb.place(x=508,y=50)

                        lt=Label(wb,text='Last transaction',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        lt.place(x=808,y=50)
                        c=0
                        bi=[]
                        global pas 
                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                        cr=ci.cursor()
                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                        no1=cr.fetchone()
                        gstp=str(no1[0])
                        ci.commit()
                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                        cr1=c1.cursor()
                        qchp='select Name, Total_t, Last_T, last_Ttime from customers'
                        cr1.execute(qchp)
                        bi=cr1.fetchall()
                        c1.commit()
                        if len(bi)==0:
                            label2=Label(wb,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='#EDEFEE',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                            label2.place(x=0,y=82)
                            pn=Label(wb,text='No data available in table',font=('Arial',12),bg='light grey')
                            pn.place(x=600,y=85)
                        else:
                            for i in bi:
                                def customer_profile(e,y=c):
                                    cp1=Toplevel()
                                    cp1.config(background='#cce7ff')
                                    cp1.geometry('500x600+500+114')
                                    cp1.overrideredirect(1)

                                    def on_enter(e):
                                        e.widget['image']=rc

                                    def on_leave(e):
                                        e.widget['image']=bc

                                    cr.execute('select Business_name from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    b_name=str(no1[0])
                                    ci.commit()
                        
                                    cr1.execute('select * from customers')
                                    cd=[]
                                    cd=cr1.fetchall()
                                    c1.commit()
                                    
                                    LabelB=Label(cp1,text=b_name,font=('Arial',20,'bold'),bg='#cce7ff',fg='#0476D0')
                                    LabelB.pack(anchor=N)

                                    cLabel=Label(cp1,height=3,width=600,relief=GROOVE, border=2,bg='light grey')
                                    cLabel.pack(anchor=N)
                                    CLabel=Label(cp1,text='Customer Profile',font=('Arial',18),fg='#0476D0',bg='light grey')
                                    CLabel.place(x=2,y=45)

                                    nc=cd[y][0]
                                    nlabel=Label(cp1,text=nc,bg='#cce7ff',font=('Arial',18,'italic underline'),fg='#0476D0')
                                    nlabel.place(x=155,y=100)

                                    ng=cd[y][3]
                                    glabel=Label(cp1,text='GST NO:',bg='#cce7ff',font=('Arial',16,'bold'))
                                    glabel.place(x=100,y=150)
                                    Glabel=Label(cp1,text=ng,bg='#cce7ff',font=('Arial',16,'italic'))
                                    Glabel.place(x=200,y=150)

                                    ca=cd[y][2]
                                    cad=ca.split(',')
                                    cadf=''
                                    l=len(cad)
                                    Alabel=Label(cp1,text='Address:',bg='#cce7ff',font=('Arial',16,'bold'))
                                    Alabel.place(x=94,y=177+27)
                                    
                                    for i in range(1,len(cad)-1):
                                        cadf=cad[i]+','
                                        alabel=Label(cp1,text=cadf,bg='#cce7ff',font=('Arial',16,'italic'))
                                        alabel.place(x=190,y=150+27*(i+2))
                                    alabeli=Label(cp1,text=cad[0]+','
                                                  ,bg='#cce7ff',font=('Arial',16,'italic'))
                                    alabeli.place(x=200,y=177+27)
                                    alabel1=Label(cp1,text=cad[-1],bg='#cce7ff',font=('Arial',16,'italic'))
                                    alabel1.place(x=190,y=150+27*(l+1))

                                    ns=cd[y][4]
                                    Slabel=Label(cp1,text='State:',bg='#cce7ff',font=('Arial',16,'bold'))
                                    Slabel.place(x=127,y=150+27*(l+3))
                                    slabel=Label(cp1,text=ns,bg='#cce7ff',font=('Arial',16,'italic'))
                                    slabel.place(x=194,y=150+27*(l+3))

                                    nb=cd[y][1]
                                    Nlabel=Label(cp1,text='Phone:',bg='#cce7ff',font=('Arial',16,'bold'))
                                    Nlabel.place(x=114,y=150+27*(l+5))
                                    nlabel=Label(cp1,text=nb,bg='#cce7ff',font=('Arial',16,'italic'))
                                    nlabel.place(x=194,y=150+27*(l+5))

                                    ldt=str(cd[y][5])
                                    ltm=str(cd[y][7])
                                    ldm=ldt+' | '+ltm
                                    tlabel=Label(cp1,text='Last transaction:',bg='#cce7ff',font=('Arial',16,'bold'))
                                    tlabel.place(x=46,y=150+27*(l+7))
                                    dlabel=Label(cp1,text=ldm,bg='#cce7ff',font=('Arial',16,'italic'))
                                    dlabel.place(x=224,y=150+27*(l+7))

                                    tt=cd[y][6]
                                    tOlabel=Label(cp1,text='Total Transaction:',bg='#cce7ff',font=('Arial',16,'bold'))
                                    tOlabel.place(x=100,y=150+27*(l+9))
                                    tolabel=Label(cp1,text=tt,bg='#cce7ff',font=('Arial',16,'italic'))
                                    tolabel.place(x=284,y=150+27*(l+9))

                                    rc=PhotoImage(file='F:\\Python\\Project\\Images\\red_cross.png')
                                    bc=PhotoImage(file='F:\\Python\\Project\\Images\\blue_cross.png')
                                    def command():
                                        cp1.destroy()
                                    d_btn=Button(cp1,image=bc,borderwidth=0,command=command,cursor='hand2')
                                    d_btn.place(x=0,y=0)
                                    d_btn.bind('<Enter>',on_enter)
                                    d_btn.bind('<Leave>',on_leave)


                                    cp1.mainloop()
                                    
                                label2=Label(wb,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='white',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                                label2.place(x=0,y=82+34*c)
                                pnv=Label(wb,text=i[0],bg='white',font=('Arial',12,'bold'),cursor='hand2',fg='#0476D0')
                                pnv.place(x=208,y=85+32*c+2*c)
                                pnv.bind('<Button-1>',customer_profile)

                                stv=Label(wb,text=i[1],bg='white',font=('Arial',12,'bold'))
                                stv.place(x=510,y=85+32*c+2*c)

                                bv=str(i[2])+' | '+str(i[3])
                                ltv=Label(wb,text=bv,bg='white',font=('Arial',12,'bold'))
                                ltv.place(x=808,y=85+32*c+2*c)
                                
                                c+=1
  
                        wb.mainloop()


                    books=Button(w3,text='Books',
                       font=('Comic Sans',10,'bold'),
                       fg="light grey",
                       bg='#7B7571',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        command=book,
                        cursor='hand2',
                       relief=FLAT)      #bg color of button when is clicked
                    books.config(state=ACTIVE)
                    books.place(x=400,y=10)

                    def customersf():
                        def add_customer():
                            ac=Tk()
                            ac.geometry('1366x768')
                            ac.config(background='white')

                            acl=Label(ac,text='Add Customer', fg='grey',bg='white',
                                    font=('Arial',26))
                            acl.place(x=0,y=0)

                            label2=Label(ac,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                            label2.place(x=0,y=47)

                            label3=Label(ac,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=57)
                            label3.place(x=0,y=107)

                            label4=Label(ac,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                            label4.place(x=0,y=167+130+7)

                            label5=Label(ac,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                            label5.place(x=0,y=227+130+7)


                            Cn=Label(ac,text='Customer Name:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            Cn.place(x=455,y=60)

                            ad=Label(ac,text='Address:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            ad.place(x=517,y=120)

                            Cs=Label(ac,text='State:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            Cs.place(x=542,y=120+130+7)

                            ph=Label(ac,text='Phone:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            ph.place(x=534,y=180+130+7)

                            gn=Label(ac,text='GST  NO:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            gn.place(x=517,y=240+130+7)

                            add_p=[]

                            entry_Cn=Entry(ac,font=('Arial',13),
                                    fg='black',
                                    bg='#CDD9DF')
                            entry_Cn.place(x=620,y=65)
                            add_p.append(entry_Cn)

                            entry_ad=Text(ac,width=30,height=5,font=('Arial',13),
                                                            fg='black',
                                                            bg='#CDD9DF')
                            entry_ad.place(x=620,y=125)
                            add_p.append(entry_ad)


                            entry_Cs=Entry(ac,font=('Arial',13),
                                    fg='black',
                                    bg='#CDD9DF')
                            entry_Cs.place(x=620,y=125+130+7)
                            add_p.append(entry_Cs)

                            entry_ph=Entry(ac,font=('Arial',13),
                                    fg='black',
                                    bg='#CDD9DF')
                            entry_ph.place(x=620,y=185+130+7)
                            add_p.append(entry_ph)

                            entry_gn=Entry(ac,font=('Arial',13),
                                    fg='black',
                                    bg='#CDD9DF')
                            entry_gn.place(x=620,y=245+130+7)
                            add_p.append(entry_gn)

                            c_btn=Button(ac, text='Cancel',
                                     padx=5,
                                     pady=5,command=ac.destroy,
                                   font=('Arial',13,'bold'),
                                   fg="white",
                                   bg='red',
                                    cursor='hand2',
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                            c_btn.place(x=670,y=350+130+7)

                            def save_customer():
                                global pas
                                nonlocal wc
                                nonlocal customersf
                                
                                if len(add_p[0].get())!=0 and len(add_p[2].get())!=0 and len(add_p[3].get())!=0 and len(add_p[4].get())!=0:
                                    global pas 
                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    cr1.execute('insert into customers(Name,Address,State, Mob_no, Gst_no) values("{}","{}","{}","{}","{}")'.format(add_p[0].get(),add_p[1].get(1.0,'end-1c'),add_p[2].get(),add_p[3].get(),add_p[4].get()))
                                    c1.commit()
                                    mb.showinfo("GBI Tool", "Customer is added Successfully!",parent=ac)
                                    wc.destroy()
                                    ac.destroy()
                                    customersf()

                            a_btn=Button(ac, text='Add',
                                     padx=5,
                                     pady=5,
                                   font=('Arial',13,'bold'),
                                   fg="white",
                                   bg='#0476D0',
                                    cursor='hand2',
                                    command=save_customer,
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                            a_btn.place(x=570,y=350+130+7)

                        wc=Tk()
                        wc.geometry('1366x768')
                        wc.config(background='white')

                        label=Label(wc,text='Customers', fg='grey',bg='white',
                                    font=('Arial',26))
                        label.place(x=0,y=0)

                        a_btn=Button(wc, text='Add New',
                                     padx=5,
                                     pady=5,
                                   font=('Arial',13,'bold'),
                                     command=add_customer,
                                   fg="white",
                                   bg='#0476D0',
                                     relief=RAISED,
                                     cursor='hand2',
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                        a_btn.place(x=1250,y=0)


                        label2=Label(wc,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=RAISED,
                                    padx=1000,   #spacing of text from border in x axis
                                     bg='#7B7571',
                                    pady=6)
                        label2.place(x=0,y=47)

                        Cn=Label(wc,text='Customer Name',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        Cn.place(x=8,y=50)

                        Cs=Label(wc,text='State',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        Cs.place(x=308,y=50)

                        ph=Label(wc,text='Phone',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        ph.place(x=608,y=50)

                        gn=Label(wc,text='GST NO',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        gn.place(x=908,y=50)
                        c=0
                        customers=[]
                        global pas 
                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                        cr=ci.cursor()
                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                        no1=cr.fetchone()
                        gstp=str(no1[0])
                        ci.commit()
                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                        cr1=c1.cursor()
                        qchp='select Name,Address, State, Mob_no, Gst_no from customers'
                        cr1.execute(qchp)
                        customers=cr1.fetchall()
                        c1.commit()
                        
                        if len(customers)==0:
                            label2=Label(wc,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='#EDEFEE',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                            label2.place(x=0,y=82)
                            pn=Label(wc,text='No data available in table',font=('Arial',12),bg='#EDEFEE')
                            pn.place(x=600,y=85)
                        else:
                            for i in customers:
                                label2=Label(wc,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=GROOVE,
                                    bg='#EDEFEE',
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=6)
                                label2.place(x=0,y=82+34*c)
                                cnv=Label(wc,text=i[0],bg='#EDEFEE',font=('Arial',12,'bold'))
                                cnv.place(x=13,y=85+32*c+2*c)

                                csv=Label(wc,text=i[2],bg='#EDEFEE',font=('Arial',12,'bold'))
                                csv.place(x=310,y=85+32*c+2*c)

                                phv=Label(wc,text=i[3],bg='#EDEFEE',font=('Arial',12,'bold'))
                                phv.place(x=608,y=85+32*c+2*c)

                                gnv=Label(wc,text=i[4],bg='#EDEFEE',font=('Arial',12,'bold'))
                                gnv.place(x=906,y=85+32*c+2*c)

                                def edit(x=i):
                                    ec=Tk()
                                    ec.geometry('1366x768')
                                    ec.config(background='white')

                                    ecl=Label(ec,text='Edit Customer', fg='grey',bg='white',
                                            font=('Arial',26))
                                    ecl.place(x=0,y=0)

                                    label2=Label(ec,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #specing of text from border in x axis
                                            pady=20)
                                    label2.place(x=0,y=47)

                                    label3=Label(ec,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #specing of text from border in x axis
                                            pady=57)
                                    label3.place(x=0,y=107)

                                    label4=Label(ec,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #specing of text from border in x axis
                                            pady=20)
                                    label4.place(x=0,y=167+130+7)

                                    label5=Label(ec,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #specing of text from border in x axis
                                            pady=20)
                                    label5.place(x=0,y=227+130+7)


                                    Cn=Label(ec,text='Customer Name:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #specing of text from border in x axis
                                            pady=5)
                                    Cn.place(x=455,y=60)

                                    ad=Label(ec,text='Address:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #specing of text from border in x axis
                                            pady=5)
                                    ad.place(x=517,y=120)

                                    Cs=Label(ec,text='State:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #specing of text from border in x axis
                                            pady=5)
                                    Cs.place(x=542,y=120+130+7)

                                    ph=Label(ec,text='Phone:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #specing of text from border in x axis
                                            pady=5)
                                    ph.place(x=534,y=180+130+7)

                                    gn=Label(ec,text='GST  NO:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #specing of text from border in x axis
                                            pady=5)
                                    gn.place(x=517,y=240+130+7)

                                    edit_c=[]

                                    entry_Cn=Entry(ec,font=('Arial',13),
                                            fg='black',
                                            bg='#CDD9DF')
                                    entry_Cn.place(x=620,y=65)
                                    entry_Cn.insert(0,x[0])
                                    edit_c.append(entry_Cn)

                                    entry_ad=Text(ec,width=30,height=5,font=('Arial',13),
                                                                    fg='black',
                                                                    bg='#CDD9DF')
                                    entry_ad.place(x=620,y=125)
                                    entry_ad.insert(1.0,x[1])
                                    edit_c.append(entry_ad)


                                    entry_Cs=Entry(ec,font=('Arial',13),
                                            fg='black',
                                            bg='#CDD9DF')
                                    entry_Cs.place(x=620,y=125+130+7)
                                    entry_Cs.insert(0,x[2])
                                    edit_c.append(entry_Cs)

                                    entry_ph=Entry(ec,font=('Arial',13),
                                            fg='black',
                                            bg='#CDD9DF')
                                    entry_ph.place(x=620,y=185+130+7)
                                    entry_ph.insert(0,x[3])
                                    edit_c.append(entry_ph)

                                    entry_gn=Entry(ec,font=('Arial',13),
                                            fg='black',
                                            bg='#CDD9DF')
                                    entry_gn.place(x=620,y=245+130+7)
                                    entry_gn.insert(0,x[4])
                                    edit_c.append(entry_gn)

                                    c_btn=Button(ec, text='Cancel',
                                             padx=5,
                                             pady=5,command=ec.destroy,
                                           font=('Arial',13,'bold'),
                                           fg="white",
                                           bg='red',
                                            cursor='hand2',
                                           activeforeground='white',      #text color of button when is clicked
                                           activebackground='grey')      #button created to bring the entry into work
                                    c_btn.place(x=670,y=350+130+7)

                                    def edit_customer(s=x):
                                        nonlocal wc
                                        nonlocal customersf
                                        global pas
                                        nonlocal edit_c
                                        name=edit_c[0].get()
                                        adr=edit_c[1].get(1.0,'end-1c')
                                        st=edit_c[2].get()
                                        pho=edit_c[3].get()
                                        gn=edit_c[4].get()
                                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                        cr=ci.cursor()
                                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                        no1=cr.fetchone()
                                        gstep=str(no1[0])
                                        ci.commit()
                                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstep)
                                        cr1=c1.cursor()
                                        cr1.execute('update customers set Name="{}", address="{}", State="{}", Mob_no="{}", Gst_No="{}" where Gst_no="{}"'.format(name,adr,st,pho,gn,x[4]))
                                        c1.commit()
                                        mb.showinfo("GBI Tool", "Customer Updated Successfully!",parent=ec)
                                        wc.destroy()
                                        ec.destroy()
                                        customersf()

                                    a_btn=Button(ec, text='Save',
                                             padx=5,
                                             pady=5,
                                           font=('Arial',13,'bold'),
                                           fg="white",
                                           bg='#0476D0',
                                            cursor='hand2',
                                            command=edit_customer,
                                           activeforeground='white',      #text color of button when is clicked
                                           activebackground='grey')      #button created to bring the entry into work
                                    a_btn.place(x=570,y=350+130+7)

                                   
                                e_btn=Button(wc, text='Edit',
                                     padx=5,
                                     pady=0,
                                   font=('Arial',12),
                                   fg="white",
                                   bg='#0476D0',
                                     relief=FLAT,
                                    cursor='hand2',
                                    command=edit,
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                                e_btn.place(x=1210,y=84+32*c+2*c)

                                def delete(x=i):
                                    nonlocal wc
                                    nonlocal customersf
                                    global pas 
                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    cr1.execute("delete from customers where Gst_No='{}'".format(x[4]))
                                    c1.commit()
                                    mb.showinfo("GBI Tool", "Customer Deleted Successfully!",parent=wc)
                                    wc.destroy()
                                    customersf()

                                d_btn=Button(wc, text='Delete',
                                     padx=5,
                                     pady=0,
                                   font=('Arial',12),
                                   fg="white",
                                   bg='red',
                                     relief=FLAT,
                                    command=delete,
                                    cursor='hand2',
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                                d_btn.place(x=1275,y=84+32*c+2*c)

                                c+=1 
                        wc.mainloop()


                    Customers=Button(w3,text='Customers',
                                     command=customersf,
                       font=('Comic Sans',10,'bold'),
                       fg="light grey",
                       bg='#7B7571',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        cursor='hand2',
                       relief=FLAT)      #bg color of button when is clicked
                    Customers.config(state=ACTIVE)
                    Customers.place(x=450,y=10)

                    def productsM():
                        def add_product():
                            ap=Tk()
                            ap.geometry('1366x768')
                            ap.config(background='white')

                            apl=Label(ap,text='Add Product', fg='grey',bg='white',
                                    font=('Arial',26))
                            apl.place(x=0,y=0)

                            label2=Label(ap,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label2.place(x=0,y=47)

                            label3=Label(ap,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label3.place(x=0,y=107)

                            label4=Label(ap,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label4.place(x=0,y=167)

                            label5=Label(ap,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label5.place(x=0,y=227)

                            Pn=Label(ap,text='Product Name:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            Pn.place(x=475,y=60)

                            Pu=Label(ap,text='Product  Unit:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            Pu.place(x=483,y=120)

                            gp=Label(ap,text='GST %:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            gp.place(x=533,y=180)

                            rg=Label(ap,text='Rate without GST:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            rg.place(x=448,y=240)

                            add_p=[]
                            entry_Pn=Entry(ap,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_Pn.place(x=620,y=65)
                            add_p.append(entry_Pn)

                            entry_Pu=Entry(ap,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_Pu.place(x=620,y=125)
                            add_p.append(entry_Pu)

                            entry_gp=Entry(ap,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_gp.place(x=620,y=185)
                            add_p.append(entry_gp)

                            entry_rg=Entry(ap,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_rg.place(x=620,y=245)
                            add_p.append(entry_rg)

                            c_btn=Button(ap, text='Cancel',
                                         padx=5,
                                         pady=5,command=ap.destroy,
                                           font=('Arial',13,'bold'),
                                           fg="white",
                                           bg='red',
                                           cursor='hand2',
                                           activeforeground='white',      #text color of button when is clicked
                                           activebackground='grey')      #button created to bring the entry into work
                            c_btn.place(x=670,y=350)

                            def save_product():
                                global pas
                                nonlocal wp1
                                nonlocal productsM
                                
                                if len(add_p[0].get())!=0 and len(add_p[1].get())!=0 and len(add_p[2].get())!=0 and len(add_p[3].get())!=0:
                                    global pas 
                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    qch4n='select max(P_id) from products'
                                    cr1.execute(qch4n)
                                    pid=cr1.fetchone()
                                    P_id=int(pid[0])+1
                                    cr1.execute('insert into products(Name,Total_stock, Rate, Gst_P,P_id) values("{}",{},{},{},{})'.format(add_p[0].get(),int(add_p[1].get()),int(add_p[3].get()),int(add_p[2].get()),int(P_id)))
                                    c1.commit()
                                    mb.showinfo("GBI Tool", "Product is added Successfully!",parent=ap)
                                    wp1.destroy()
                                    ap.destroy()
                                    productsM()

                            s_btn=Button(ap, text='Add',
                                         padx=5,
                                         pady=5,
                                           font=('Arial',13,'bold'),
                                           fg="white",
                                           bg='#0476D0',
                                           cursor='hand2',
                                           command=save_product,
                                           activeforeground='white',      #text color of button when is clicked
                                           activebackground='grey')      #button created to bring the entry into work
                            s_btn.place(x=570,y=350)

                        wp1=Tk()
                        wp1.geometry('1366x768')
                        wp1.config(background='white')

                        label=Label(wp1,text='Products', fg='grey',bg='white',
                                    font=('Arial',26))
                        label.place(x=0,y=0)

                        a_btn=Button(wp1, text='Add New',
                                    padx=5,
                                     pady=5,
                                   font=('Arial',13,'bold'),
                                     command=add_product,
                                   fg="white",
                                   bg='#0476D0',
                                     relief=RAISED,
                                     cursor='hand2',
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                        a_btn.place(x=1250,y=0)


                        label2=Label(wp1,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    relief=RAISED,
                                    padx=1000,   #spacing of text from border in x axis
                                     bg='#7B7571',
                                    pady=6)
                        label2.place(x=0,y=47)

                        pn=Label(wp1,text='Product Name',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        pn.place(x=208,y=50)

                        gst=Label(wp1,text='GST %',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        gst.place(x=508,y=50)

                        rg=Label(wp1,text='Rate without GST',bg='#7B7571',fg='white',font=('Arial',12,'bold'))
                        rg.place(x=808,y=50)
                        c=0
                        global pas 
                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                        cr=ci.cursor()
                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                        no1=cr.fetchone()
                        gstp=str(no1[0])
                        ci.commit()
                        products=[]
                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                        cr1=c1.cursor()
                        qchp='select Name, Gst_P, Rate, Total_stock, P_id from products'
                        cr1.execute(qchp)
                        products=cr1.fetchall()
                        c1.commit()
                        if len(products)==0:
                            label2=Label(wp1,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            relief=GROOVE,
                                            bg='#EDEFEE',
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=6)
                            label2.place(x=0,y=82)
                            pn=Label(wp1,text='No data available in table',font=('Arial',12),bg='#EDEFEE')
                            pn.place(x=600,y=85)
                        else:
                            for i in products:
                                label2=Label(wp1,   #window object and text to be shown
                                                font=('Arial',13,'bold'),      #font name,size and style
                                                relief=GROOVE,
                                                bg='#EDEFEE',
                                                padx=1000,   #spacing of text from border in x axis
                                                pady=6)
                                label2.place(x=0,y=82+34*c)
                                pnv=Label(wp1,text=i[0],bg='#EDEFEE',font=('Arial',12,'bold'))
                                pnv.place(x=213,y=85+32*c+2*c)

                                gstv=Label(wp1,text=i[1],bg='#EDEFEE',font=('Arial',12,'bold'))
                                gstv.place(x=510,y=85+32*c+2*c)

                                rgv=Label(wp1,text=i[2],bg='#EDEFEE',font=('Arial',12,'bold'))
                                rgv.place(x=818,y=85+32*c+2*c)

                                def editp1(y=i):
                                    ep=Tk()
                                    ep.geometry('1366x768')
                                    ep.config(background='white')

                                    epl=Label(ep,text='Edit Product', fg='grey',bg='white',
                                            font=('Arial',26))
                                    epl.place(x=0,y=0)

                                    label2=Label(ep,   #window object and text to be shown
                                                    font=('Arial',13,'bold'),      #font name,size and style
                                                    fg='black',   #text color
                                                    bg='white',   #label bg color
                                                    relief=GROOVE,
                                                    padx=1000,   #spacing of text from border in x axis
                                                    pady=20)
                                    label2.place(x=0,y=47)

                                    label3=Label(ep,   #window object and text to be shown
                                                    font=('Arial',13,'bold'),      #font name,size and style
                                                    fg='black',   #text color
                                                    bg='white',   #label bg color
                                                    relief=GROOVE,
                                                    padx=1000,   #spacing of text from border in x axis
                                                    pady=20)
                                    label3.place(x=0,y=107)

                                    label4=Label(ep,   #window object and text to be shown
                                                    font=('Arial',13,'bold'),      #font name,size and style
                                                    fg='black',   #text color
                                                    bg='white',   #label bg color
                                                    relief=GROOVE,
                                                    padx=1000,   #spacing of text from border in x axis
                                                    pady=20)
                                    label4.place(x=0,y=167)

                                    label5=Label(ep,   #window object and text to be shown
                                                    font=('Arial',13,'bold'),      #font name,size and style
                                                    fg='black',   #text color
                                                    bg='white',   #label bg color
                                                    relief=GROOVE,
                                                    padx=1000,   #spacing of text from border in x axis
                                                    pady=20)
                                    label5.place(x=0,y=227)

                                    Pn=Label(ep,text='Product Name:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #spacing of text from border in x axis
                                            pady=5)
                                    Pn.place(x=476,y=60)

                                    Pu=Label(ep,text='Product  Unit:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #spacing of text from border in x axis
                                            pady=5)
                                    Pu.place(x=483,y=120)

                                    gp=Label(ep,text='GST %:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #spacing of text from border in x axis
                                            pady=5)
                                    gp.place(x=533,y=180)

                                    rg=Label(ep,text='Rate without GST:',   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            padx=5,   #spacing of text from border in x axis
                                            pady=5)
                                    rg.place(x=448,y=240)

                                    edit_p=[]
                                    entry_Pn=Entry(ep,font=('Arial',13),
                                                        fg='black',
                                                        bg='#CDD9DF')
                                    entry_Pn.place(x=620,y=65)
                                    entry_Pn.insert(0,y[0])
                                    edit_p.append(entry_Pn)

                                    entry_Pu=Entry(ep,font=('Arial',13),
                                                        fg='black',
                                                        bg='#CDD9DF')
                                    entry_Pu.place(x=620,y=125)
                                    entry_Pu.insert(0,y[3])
                                    edit_p.append(entry_Pu)

                                    entry_gp=Entry(ep,font=('Arial',13),
                                                        fg='black',
                                                        bg='#CDD9DF')
                                    entry_gp.place(x=620,y=185)
                                    entry_gp.insert(0,y[1])
                                    edit_p.append(entry_gp)

                                    entry_rg=Entry(ep,font=('Arial',13),
                                                        fg='black',
                                                        bg='#CDD9DF')
                                    entry_rg.place(x=620,y=245)
                                    entry_rg.insert(0,y[2])
                                    edit_p.append(entry_rg)

                                    c_btn=Button(ep, text='Cancel',
                                                 padx=5,
                                                 pady=5,command=ep.destroy,
                                                   font=('Arial',13,'bold'),
                                                   fg="white",
                                                   bg='red',
                                                   cursor='hand2',
                                                   activeforeground='white',      #text color of button when is clicked
                                                   activebackground='grey')      #button created to bring the entry into work
                                    c_btn.place(x=670,y=350)

                                    def edit_product(s=y):
                                        nonlocal wp1
                                        nonlocal productsM
                                        global pas
                                        nonlocal edit_p
                                        pnm=edit_p[0].get()
                                        pts=int(edit_p[1].get())
                                        ra=int(edit_p[3].get())
                                        gp=int(edit_p[2].get())
                                        ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                        cr=ci.cursor()
                                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                        no1=cr.fetchone()
                                        gstep=str(no1[0])
                                        ci.commit()
                                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstep)
                                        cr1=c1.cursor()
                                        cr1.execute('update products set Name="{}", Total_stock={}, Rate={}, Gst_P={} where P_id={}'.format(pnm,pts,ra,gp,s[4]))
                                        c1.commit()
                                        mb.showinfo("GBI Tool", "Product Updated Successfully!",parent=ep)
                                        wp1.destroy()
                                        ep.destroy()
                                        productsM()

                                    s_btn=Button(ep, text='Save',
                                         padx=5,
                                         pady=5,
                                           font=('Arial',13,'bold'),
                                           fg="white",
                                           bg='#0476D0',
                                           cursor='hand2',
                                           command=edit_product,
                                           activeforeground='white',      #text color of button when is clicked
                                           activebackground='grey')      #button created to bring the entry into work
                                    s_btn.place(x=570,y=350)

               
                                e_btn=Button(wp1, text='Edit',
                                             padx=5,
                                             pady=0,
                                               font=('Arial',12),
                                               fg="white",
                                               bg='#0476D0',
                                                relief=FLAT,
                                               cursor='hand2',
                                               command=editp1,
                                               activeforeground='white',      #text color of button when is clicked
                                               activebackground='grey')      #button created to bring the entry into work
                                e_btn.place(x=1210,y=84+32*c+2*c)

                                def delete(x=i):
                                    nonlocal wp1
                                    nonlocal productsM
                                    global pas 
                                    ci=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                                    cr=ci.cursor()
                                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                                    no1=cr.fetchone()
                                    gstp=str(no1[0])
                                    ci.commit()
                                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gstp)
                                    cr1=c1.cursor()
                                    qchdp='delete from products where name=%s'
                                    cr1.execute("delete from products where P_id={}".format(x[4]))
                                    c1.commit()
                                    mb.showinfo("GBI Tool", "Product Deleted Successfully!",parent=wp1)
                                    wp1.destroy()
                                    productsM()

                                d_btn=Button(wp1, text='Delete',
                                             padx=5,
                                             pady=0,
                                               font=('Arial',12),
                                               fg="white",
                                               bg='red',
                                                 relief=FLAT,
                                               command=delete,
                                               cursor='hand2',
                                               activeforeground='white',      #text color of button when is clicked
                                                activebackground='grey')      #button created to bring the entry into work
                                d_btn.place(x=1275,y=84+32*c+2*c)

                                c+=1 
                        wp1.mainloop()


                    Products=Button(w3,text='Products',
                       font=('Comic Sans',10,'bold'),
                        command=productsM,
                       fg="light grey",
                       bg='#7B7571',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        cursor='hand2',
                       relief=FLAT)      #bg color of button when is clicked
                    Products.config(state=ACTIVE)
                    Products.place(x=528,y=10)

                    def profile():
                        global cr
                        global pas
                        cr.execute("select Business_name,Address,State,e_mail,Phone_no,Gst_no from Details where passwd='{}'".format(pas))
                        data=cr.fetchall()
                        bname=''
                        add=''
                        sta=''
                        ml=''
                        pho=''
                        gs=''
                        for i in data:
                            bname=i[0]
                            add=i[1]
                            sta=i[2]
                            ml=i[3]
                            pho=i[4]
                            gs=i[5]

                        wp=Tk()
                        wp.geometry('1366x768')
                        wp.config(background='white')

                        label=Label(wp,text='Profile', fg='grey',bg='white',
                                    font=('Arial',26))
                        label.place(x=0,y=0)

                        label2=Label(wp,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                        label2.place(x=0,y=47)

                        label3=Label(wp,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                        label3.place(x=0,y=107)

                        label4=Label(wp,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                        label4.place(x=0,y=167)

                        label5=Label(wp,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                        label5.place(x=0,y=227)

                        label6=Label(wp,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                        label6.place(x=0,y=287)

                        label7=Label(wp,   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    relief=GROOVE,
                                    padx=1000,   #spacing of text from border in x axis
                                    pady=20)
                        label7.place(x=0,y=347)

                        bn=Label(wp,text='Business Name:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        bn.place(x=460,y=60)

                        ad=Label(wp,text='Address:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        ad.place(x=515,y=120)

                        st=Label(wp,text='State:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        st.place(x=539,y=180)

                        mail=Label(wp,text='Email Id:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        mail.place(x=520,y=240)

                        ph=Label(wp,text='Phone Number:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        ph.place(x=463,y=300)

                        gst=Label(wp,text='GST Number:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        gst.place(x=480,y=360)

                        bnv=Label(wp,text=bname,   #window object and text to be shown
                                    font=('Arial',13),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        bnv.place(x=610,y=60)

                        adv=Label(wp,text=add,   #window object and text to be shown
                                    font=('Arial',13),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        adv.place(x=610,y=120)

                        stv=Label(wp,text=sta,   #window object and text to be shown
                                    font=('Arial',13),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        stv.place(x=610,y=180)

                        mailv=Label(wp,text=ml,   #window object and text to be shown
                                    font=('Arial',13),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        mailv.place(x=610,y=240)

                        phv=Label(wp,text=pho,   #window object and text to be shown
                                    font=('Arial',13),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        phv.place(x=610,y=300)

                        gstv=Label(wp,text=gs,   #window object and text to be shown
                                    font=('Arial',13),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                        gstv.place(x=610,y=360)

                        def edit():
                            we=Tk()
                            we.geometry('1366x768')
                            we.config(background='white')

                            label=Label(we,text='Edit Profile', fg='grey',bg='white',
                                    font=('Arial',26))
                            label.place(x=0,y=0)

                            label2=Label(we,   #window object and text to be shown
                                        font=('Arial',13,'bold'),      #font name,size and style
                                        fg='black',   #text color
                                        bg='white',   #label bg color
                                        relief=GROOVE,
                                        padx=1000,   #spacing of text from border in x axis
                                        pady=20)
                            label2.place(x=0,y=47)

                            label3=Label(we,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label3.place(x=0,y=107)

                            label4=Label(we,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label4.place(x=0,y=167)

                            label5=Label(we,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label5.place(x=0,y=227)

                            label6=Label(we,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label6.place(x=0,y=287)

                            label7=Label(we,   #window object and text to be shown
                                            font=('Arial',13,'bold'),      #font name,size and style
                                            fg='black',   #text color
                                            bg='white',   #label bg color
                                            relief=GROOVE,
                                            padx=1000,   #spacing of text from border in x axis
                                            pady=20)
                            label7.place(x=0,y=347)

                            bn=Label(we,text='Business Name:',   #window object and text to be shown
                                        font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            bn.place(x=460,y=60)

                            ad=Label(we,text='Address:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            ad.place(x=515,y=120)

                            st=Label(we,text='State:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            st.place(x=539,y=180)

                            mail=Label(we,text='Email Id:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            mail.place(x=520,y=240)

                            ph=Label(we,text='Phone Number:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            ph.place(x=463,y=300)

                            gst=Label(we,text='GST Number:',   #window object and text to be shown
                                    font=('Arial',13,'bold'),      #font name,size and style
                                    fg='black',   #text color
                                    bg='white',   #label bg color
                                    padx=5,   #spacing of text from border in x axis
                                    pady=5)
                            gst.place(x=480,y=360)

                            c_btn=Button(we, text='Cancel',
                                     padx=5,
                                     pady=5,command=we.destroy,
                                   font=('Arial',13,'bold'),
                                   fg="white",
                                   bg='red',
                                    cursor='hand2',
                                   activeforeground='white',      #text color of button when is clicked
                                   activebackground='grey')      #button created to bring the entry into work
                            c_btn.place(x=670,y=420)

                            def save():
                                global cr
                                global c
                                global pas
                                bname=entry_bn.get()
                                add=entry_ad.get()
                                sta=entry_sta.get()
                                ml=entry_ma.get()
                                pho=entry_ph.get()
                                gs=entry_gst.get()
                                p=[bname,add,sta,ml,pho,gs]
                                cr.execute("update details set Business_name='{}', Address='{}', State='{}', e_mail='{}', Phone_no='{}',Gst_no='{}' where Passwd='{}'".format(bname,add,sta,ml,pho,gs,pas))
                                mb.showinfo("GBI Tool", "Data Saved Successfully!",parent=we)
                                c.commit()
                                nonlocal c_btn
                                nonlocal wp
                                c_btn.destroy
                                def exitb():
                                    we.destroy()
                                    wp.destroy()
                                    profile()
                                e_btn=Button(we, text='Exit',
                                             padx=5,width=6,
                                             pady=5,command=exitb,
                                               font=('Arial',13,'bold'),
                                               fg="white",
                                               bg='red',
                                               cursor='hand2',
                                               activeforeground='white',      #text color of button when is clicked
                                               activebackground='grey')     
                                e_btn.place(x=670,y=420)
                                nonlocal s_btn
                                s_btn.destroy
                                
                            s_btn=Button(we, text='Save',
                                         padx=5,
                                         pady=5,command=save,
                                           font=('Arial',13,'bold'),
                                           fg="white",
                                           bg='#0476D0',
                                           cursor='hand2',
                                           activeforeground='white',      #text color of button when is clicked
                                           activebackground='grey')      #button created to bring the entry into work
                            s_btn.place(x=570,y=420)

        
                            entry_bn=Entry(we,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_bn.insert(0,bname)
                            entry_bn.place(x=620,y=65)

                            entry_ad=Entry(we,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_ad.insert(0,add)
                            entry_ad.place(x=620,y=125)

                            entry_sta=Entry(we,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_sta.insert(0,sta)
                            entry_sta.place(x=620,y=185)

                            entry_ma=Entry(we,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_ma.insert(0,ml)
                            entry_ma.place(x=620,y=245)

                            entry_ph=Entry(we,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_ph.insert(0,pho)
                            entry_ph.place(x=620,y=305)

                            entry_gst=Entry(we,font=('Arial',13),
                                                fg='black',
                                                bg='#CDD9DF')
                            entry_gst.insert(0,gs)
                            entry_gst.place(x=620,y=365)

                        e_btn=Button(wp, text='Edit',
                                     padx=5,
                                     pady=5,command=edit,
                                       font=('Arial',13,'bold'),
                                       fg="white",
                                       bg='#0476D0',
                                       cursor='hand2',
                                       activeforeground='white',      #text color of button when is clicked
                                       activebackground='grey')      #button created to bring the entry into work
                        e_btn.place(x=610,y=420)


                        wp.mainloop()


                    Profile=Button(w3,text='Profile',
                       font=('Comic Sans',10,'bold'),
                        command=profile,
                       fg="light grey",
                       bg='#7B7571',
                        cursor='hand2',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                       relief=FLAT)      #bg color of button when is clicked
                    Profile.config(state=ACTIVE)
                    Profile.place(x=595,y=10)

                    def logout():
                        res=mb.askquestion('Logout','Confirm Logout??',parent=w3)
                        if res=='yes':
                            w3.destroy()

                    global power
                    LogOut=Button(w3,image=power,
                       font=('Comic Sans',10,'bold'),
                                  borderwidth=0,
                       fg="light grey",
                       bg='#7B7571',
                        cursor='hand2',
                       activeforeground='light grey',      #text color of button when is clicked
                       activebackground='#7B7571',
                        command=logout,
                       relief=FLAT)      #bg color of button when is clicked
                    LogOut.config(state=ACTIVE)
                    LogOut.place(x=1300,y=5)

                    
                    def update_clock():
                        nonlocal w3
                        global IST
                        raw_TS=datetime.now(IST)
                        cur_tm=raw_TS.strftime('%H:%M:%S %p')
                        cur_dt=raw_TS.strftime('%d %b %Y')
                        formatted_now=raw_TS.strftime('%d:%m:%Y')
                        dt_label=Label(w3,bg='#7B7571',fg='light grey',text='Date:',font=('Comic Sans',10,'bold'),relief=FLAT)
                        dt_label.place(x=1000,y=5)
                        tm_label=Label(w3,bg='#7B7571',fg='light grey',text='Time:',font=('Comic Sans',10,'bold'),relief=FLAT)
                        tm_label.place(x=1000,y=25)
                        dt_label.config(text=cur_dt)
                        tm_label.config(text=cur_tm)
                        tm_label.after(1000, update_clock)
                        return formatted_now

                    update_clock()
                    global i_no
                    global pas
                    c=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                    cr=c.cursor()
                    cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                    no1=cr.fetchone()
                    gst2=no1[0]
                    c.commit()
                    c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gst2)
                    cr1=c1.cursor()
                    qchn='select max(Invoice_no) from invoices'
                    cr1.execute(qchn)
                    gcheckn=cr1.fetchone()
                    c1.commit()
                    print(gcheckn)
                    if str(gcheckn[0])!='None':
                        gvn=int(gcheckn[0])
                        i_no=gvn+1
                    else:
                        i_no=1
                    
                    i_details=[]
                    l=Label(w3,bg='#F5F4F4',padx=700,pady=6,relief=GROOVE)
                    l.place(x=0,y=100)
                    L=Label(w3,text='Invoice details',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    L.place(x=1,y=102)

                    l2=Label(w3,bg='#F5F4F4',padx=700,pady=6,relief=GROOVE)
                    l2.place(x=0,y=129)
                    L2=Label(w3,text='Invoice Number',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    L2.place(x=1,y=131)
                    e_ino=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')
                    e_ino.place(x=325,y=130)
                    e_ino.insert(0,i_no)
                    i_details.append(e_ino)
                    
                    date=Label(w3,text='Date ',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')#B4B1B1
                    date.place(x=750,y=131)

                    def calendar():
                        cdr=Toplevel()
                        cdr.geometry('255x220+900+200')
                        cdr.overrideredirect(1)

                        cal=Calendar(cdr,selectmode='day', date_pattern='y-mm-dd')
                        cal.place(x=2,y=2)

                        def get_date():
                            dt.delete(0,END)
                            dt.insert(0,cal.get_date())
                            cdr.destroy()

                        Button(cdr, text='Get Date',fg='white',bg='#0476D0',
                               command=get_date,relief=FLAT).place(x=100,y=190)
                        cdr.mainloop()

                    calendarp=PhotoImage(file='F:\\Python\\Project\\Images\\calendar2.png')
                    datec=Button(w3,image=calendarp,font=('comic sans',16),borderwidth=0,command=calendar,relief=FLAT)
                    datec.place(x=969,y=131)
        
                    dt=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')     #Button-1 means when you right click on a widget 
                    dt.place(x=1000,y=130)
                    i_details.append(dt)

                    l3=Label(w3,bg='#F5F4F4',padx=700,pady=6,relief=GROOVE)
                    l3.place(x=0,y=175)
                    L3=Label(w3,text='Customer details',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    L3.place(x=1,y=177)
                    dta=[]
                    cst=[('Ramesh','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc'),('Archana','Kerala','jdgucbuhiucgfcbuifc')]
                    def panel(e):
                        nonlocal cst
                        nonlocal dta
                        p=Tk()
                        p.geometry('265x600+1092+71')
                        p.config(bg='white')
                        bl=Button(p,text='x',fg='white',bg='red',font=('Comic Sans',6),relief=GROOVE,cursor='hand2',command=p.destroy,pady=0)
                        bl.place(x=0,y=0)
                        c=-1
                        def da(e):
                            nonlocal w3
                            c_nm=Entry(w3,font=('comic sans',16),
                                width=30,
                                fg='black',
                                bg='white')
                            c_nm.insert(0,i[0])
                            c_nm.place(x=325,y=205)
                            st=Entry(w3,font=('comic sans',16),
                                width=30,
                                fg='black',
                                bg='white')
                            st.insert(0,i[1])
                            st.place(x=325,y=279)
                            cg=Entry(w3,font=('comic sans',16),
                                width=30,
                                fg='black',
                                bg='white')
                            cg.insert(0,i[2])
                            cg.place(x=1000,y=234)
                            
                        for i in cst:
                                c=c+1
                                t=i[0]+'\\n'+i[1]+'\\n'+i[2]+'\\n'+'******************************************'
                                ln=Label(p,bg='white',text=t,relief=FLAT,compound=LEFT,font=('Arial',12),cursor='hand2')
                                ln.place(x=2,y=0+c*70)
                                ln.bind('<Button-1>',da)
                                if c>6:
                                    break

                    C_details=[]
                    l4=Label(w3,bg='#F5F4F4',padx=700,pady=6,relief=GROOVE)
                    l4.place(x=0,y=204)
                    L4=Label(w3,text='Customer Name',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    L4.place(x=1,y=206)
                    c_nm=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')
                    c_nm.place(x=325,y=205)
                    C_details.append(c_nm)
                    
                    cad=Label(w3,text='Customer Address',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    cad.place(x=750,y=206)
                    cd=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')
                    cd.place(x=1000,y=205)
                    C_details.append(cd)
                    

                    l5=Label(w3,bg='#F5F4F4',padx=700,pady=6,relief=GROOVE)
                    l5.place(x=0,y=233)
                    L5=Label(w3,text='Customer Mobile Number',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    L5.place(x=1,y=235)
                    c_pn=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')
                    c_pn.place(x=325,y=234)
                    C_details.append(c_pn)
                    
                    cgst=Label(w3,text='Customer GST',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    cgst.place(x=750,y=235)
                    cg=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')
                    cg.place(x=1000,y=234)
                    C_details.append(cg)

                    l6=Label(w3,bg='#F5F4F4',padx=700,pady=6,relief=GROOVE)
                    l6.place(x=0,y=278)
                    L6=Label(w3,text='State',font=('comic sans',12,'bold'),relief=FLAT,bg='#F5F4F4')
                    L6.place(x=1,y=280)
                    st=Entry(w3,font=('comic sans',16),
                        width=30,
                        fg='black',
                        bg='white')
                    st.place(x=325,y=279)
                    C_details.append(st)
                    def onoff():
                        global blazec
                        blazec+=1
                        
                       
                    check_btn=Checkbutton(w3,text='IGST',compound='left',fg='grey',bg='#F5F4F4',activebackground='#F5F4F4',command=onoff,cursor='hand2',activeforeground='dark grey',font=('comic sans',12,'bold'),pady=0)
                    check_btn.place(x=1000,y=279)

                    l2=Label(w3,bg='#F5F4F4',padx=700,pady=3,relief=GROOVE)
                    l2.place(x=0,y=323)
                    L4=Label(w3,text='Items',font=('comic sans',9,'bold'),relief=FLAT,bg='#F5F4F4')
                    L4.place(x=1,y=325)

                    SRN=Label(w3,text='S_No',width=4,font=('comic sans',9,'bold'),relief=GROOVE,pady=5,height=1,padx=2)
                    SRN.place(x=0,y=347)
                    s=Label(w3,text=1,width=4,font=('comic sans',9),relief=GROOVE,height=1,pady=2,padx=2)
                    s.place(x=0,y=374)
                    for i in range(1,10):
                        s2=Label(w3,text=i+1,width=4,font=('comic sans',9),relief=GROOVE,height=1,pady=2,padx=2)
                        s2.place(x=0,y=374+i*19)
                        
                    prd=[]   
                    PRD=Label(w3,text='Product',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    PRD.place(x=34,y=347)
                    ep=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    ep.place(x=34,y=374)
                    prd.append(ep)
                    
                    ep1=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    ep1.place(x=34,y=374+19)
                    prd.append(ep1)
                    
                    ep2=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    ep2.place(x=34,y=374+19*2)
                    prd.append(ep2)
                
                    ep3=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep3.place(x=34,y=374+19*3)
                    prd.append(ep3)
                 
                    ep4=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep4.place(x=34,y=374+19*4)
                    prd.append(ep4)
                  
                    ep5=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep5.place(x=34,y=374+19*5)
                    prd.append(ep5)
                    
                    ep6=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep6.place(x=34,y=374+19*6)
                    prd.append(ep6)
                 
                    ep7=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep7.place(x=34,y=374+19*7)
                    prd.append(ep7)
                   
                    ep8=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep8.place(x=34,y=374+19*8)
                    prd.append(ep8)

                    ep9=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                    ep9.place(x=34,y=374+19*9)
                    prd.append(ep9)

                    qty=[]
                    
                    qty=[]
                    QTY=Label(w3,text='Quantity',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    QTY.place(x=185,y=347)
                    epq=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    epq.place(x=185,y=374)
                    qty.append(epq)
                    
                    epq1=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    epq1.place(x=185,y=374+19)
                    qty.append(epq1)
                    
                    epq2=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    epq2.place(x=185,y=374+19*2)
                    qty.append(epq2)
                    
                    for i in range(3,10):
                        ep2=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                        ep2.place(x=185,y=374+19*i)
                        qty.append(ep2)

                    RTE=[]
                    rte=Label(w3,text='Rate',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    rte.place(x=336,y=347)
                    rt=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    rt.place(x=336,y=374)
                    RTE.append(rt)
                    
                    rt1=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    rt1.place(x=336,y=374+19)
                    RTE.append(rt1)
                    
                    rt2=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    rt2.place(x=336,y=374+19*2)
                    RTE.append(rt2)
                    
                    for i in range(3,10):
                        rt3=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                        rt3.place(x=336,y=374+19*i)
                        RTE.append(rt3)

                    PER=[]
                    per=Label(w3,text='GST%',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    per.place(x=487,y=347)
                    pr=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    pr.place(x=487,y=374)
                    PER.append(pr)
                    
                    pr1=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    pr1.place(x=487,y=374+19)
                    PER.append(pr1)
                    
                    pr2=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='white')
                    pr2.place(x=487,y=374+19*2)
                    PER.append(pr2)
                    
                    for i in range(3,10):
                        pr3=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='white')
                        pr3.place(x=487,y=374+19*i)
                        PER.append(pr3)
                    
                    AWG=[]
                    def AG():
                        nonlocal qty
                        nonlocal RTE
                        nonlocal AWG
                        val=0
                        for i in range(len(qty)):
                            if len(qty[i].get())!=0 and len(RTE[i].get()):
                                val=float(qty[i].get())*float(RTE[i].get())
                                AWG[i].delete(0,END)
                                AWG[i].insert(0,val)
                                
                    awg=Label(w3,text='Amt. without GST',width=20,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    awg.place(x=638,y=347)
                    ag=Entry(w3,font=('comic sans',10),
                        width=20,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    ag.insert(0,'0.00')
                    ag.place(x=638,y=374)
                    AWG.append(ag)
                    
                    ag1=Entry(w3,font=('comic sans',10),
                        width=20,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    ag1.insert(0,'0.00')
                    ag1.place(x=638,y=374+19)
                    AWG.append(ag1)
                    
                    ag2=Entry(w3,font=('comic sans',10),
                        width=20,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    ag2.insert(0,'0.00')
                    ag2.place(x=638,y=374+19*2)
                    AWG.append(ag2)
                    
                    for i in range(3,10):
                        ag3=Entry(w3,font=('comic sans',10),
                            width=20,relief=GROOVE,
                            fg='black',
                            bg='light gray')
                        ag3.insert(0,'0.00')
                        ag3.place(x=638,y=374+19*i)
                        AWG.append(ag3)
      
                    ag4=Entry(w3,font=('comic sans',16),
                        width=20,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    ag4.insert(0,'0.00')
                    ag4.place(x=638,y=374+19*10)
                    
                    
                    

                    CGST=[]
                    def CGS():
                        nonlocal CGST
                        nonlocal PER
                        nonlocal AWG
                        cgsp=0
                        val2=0
                        for i in range(len(PER)):
                            if len(PER[i].get())!=0 and len(AWG[i].get()):
                                cgsp=int(PER[i].get())/2
                                CGST[i].delete(0,END)
                                val2=float(AWG[i].get())*cgsp/100
                                CGST[i].insert(0,val2)
                                
                        
                    cgst=Label(w3,text='CGST',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    cgst.place(x=782,y=347)
                    cg=Entry(w3,font=('comic sans',10),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    cg.insert(0,'0.00')
                    cg.place(x=782,y=374)
                    CGST.append(cg)
                    
                    for i in range(1,10):
                        cg2=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='light gray')
                        cg2.insert(0,'0.00')
                        cg2.place(x=782,y=374+19*i)
                        CGST.append(cg2)
                        
                    cg3=Entry(w3,font=('comic sans',16),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    cg3.insert(0,'0.00')
                    cg3.place(x=782,y=374+19*10)
                    
                    SGST=[]
                    def SGS():
                        nonlocal SGST
                        nonlocal CGST
                        nonlocal PER
                        nonlocal AWG
                        cgsp=0
                        val2=0
                        for i in range(len(PER)):
                            if len(PER[i].get())!=0 and len(AWG[i].get()):
                                cgsp=int(PER[i].get())/2
                                SGST[i].delete(0,END)
                                val2=float(AWG[i].get())*cgsp/100
                                SGST[i].insert(0,val2)
                    sgst=Label(w3,text='SGST',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    sgst.place(x=933,y=347)
                    for i in range(0,10):
                        sg=Entry(w3,font=('comic sans',10),
                            width=20,relief=GROOVE,
                            fg='black',
                            bg='light gray')
                        sg.insert(0,'0.00')
                        sg.place(x=933,y=374+19*i)
                        SGST.append(sg)
                        
                    sg2=Entry(w3,font=('comic sans',16),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    sg2.insert(0,'0.00')
                    sg2.place(x=933,y=374+19*10)
                        
                    IGST=[]
                    igst=Label(w3,text='IGST',width=20,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    igst.place(x=1078,y=347)
                    def IGS():
                        nonlocal RTE
                        nonlocal AWG
                        nonlocal IGST
                        global varb
                        cgsp=0
                        val2=0
                        for i in range(len(PER)):
                            if len(PER[i].get())!=0 and len(AWG[i].get()):
                                cgsp=int(PER[i].get())
                                IGST[i].delete(0,END)
                                val2=float(AWG[i].get())*cgsp/100
                                IGST[i].insert(0,val2)
                            
                        
                        
                    for i in range(0,10):
                        ig=Entry(w3,font=('comic sans',10),
                            width=19,relief=GROOVE,
                            fg='black',
                            bg='light gray')
                        ig.insert(0,'0.00')
                        ig.place(x=1078,y=374+19*i)
                        IGST.append(ig)
                    ig2=Entry(w3,font=('comic sans',16),
                        width=21,relief=GROOVE,
                        fg='black',
                        bg='light gray')
                    ig2.insert(0,'0.00')
                    ig2.place(x=1078,y=374+19*10)

                    def calculations(e):
                        nonlocal AG
                        nonlocal qty
                        nonlocal RTE
                        nonlocal AWG
                        nonlocal CGS
                        nonlocal CGST
                        nonlocal ag3
                        nonlocal ag4
                        nonlocal cg3
                        nonlocal SGS
                        nonlocal SGST
                        nonlocal sg2
                        nonlocal IGS
                        nonlocal IGST
                        nonlocal check_btn
                        nonlocal ig2
                        global varb
                        global blazec
                        nonlocal AGL
                        nonlocal AGLV
                        AG()
                        if blazec%2!=0:
                            IGS()
                            cg3.delete(0,END)
                            cg3.insert(0,0.00)
                            sg2.delete(0,END)
                            sg2.insert(0,0.00)
                        else:
                            CGS()
                            SGS()
                            ig2.delete(0,END)
                            ig2.insert(0,0.00)
                        AGLV()
                        tot1=0
                        tot2=0
                        tot3=0
                        tot4=0
                        tot5=0
                        for j in range(len(qty)):
                            if len(qty[j].get())!=0 and len(CGST[j].get())!=0 and len(SGST[j].get())!=0 and len(IGST[j].get()):
                                tot1+=float(AWG[j].get())
                                tot2+=float(CGST[j].get())
                                tot3+=float(SGST[j].get())
                                tot4+=float(IGST[j].get())
                                tot5+=float(AGL[j].get())
                        ag4.delete(0,END)
                        ag4.insert(0,tot1)
                        cg3.delete(0,END)
                        cg3.insert(0,tot2)
                        sg2.delete(0,END)
                        sg2.insert(0,tot3)
                        ig2.delete(0,END)
                        ig2.insert(0,tot4)
                        ag3.delete(0,END)
                        ag3.insert(0,tot5)
                            
                        
                    AGL=[]
                    def AGLV():
                        nonlocal AWG
                        nonlocal CGST
                        nonlocal SGST
                        nonlocal IGST
                        nonlocal AGL
                        valt=0
                        for j in range(len(PER)):
                            if len(CGST[j].get())!=0 and len(SGST[j].get())!=0 and len(IGST[j].get()) and len(AWG[j].get()):
                                valt=float(CGST[j].get())+float(SGST[j].get())+float(IGST[j].get())+float(AWG[j].get())
                                AGL[j].delete(0,END)
                                AGL[j].insert(0,valt)
                            
                    ag=Label(w3,text='Amt. with GST',width=21,font=('comic sans',9,'bold'),relief=GROOVE,pady=6)
                    ag.place(x=1215,y=347)
                    for i in range(0,10):
                        agl=Entry(w3,font=('comic sans',10),
                            width=21,relief=GROOVE,
                            fg='black',
                            bg='light gray')
                        agl.insert(0,'0.00')
                        agl.place(x=1215,y=374+19*i)
                        AGL.append(agl)
                        
                    ag3=Entry(w3,font=('comic sans',16),
                        width=21,relief=RAISED,
                        fg='white',
                        bg='#0476D0')
                    ag3.insert(0,'0.00')
                    ag3.place(x=1215,y=374+19*10)
                    ag3.bind('<Button-1>',calculations)
                        

                    tot=Label(w3,width=90,font=('comic sans',9,'bold'),relief=GROOVE,pady=5,height=1,padx=3)
                    tot.place(x=-2,y=374+19*10)
                    tot1=Label(w3,text='TOTAL',font=('comic sans',12,'bold'),relief=FLAT,pady=1)
                    tot1.place(x=578,y=565)

                    
                    def submit():
                        mb.showinfo("GBI Tool", "Data Saved Successfully!",parent=w3)
                        global i_no
                        i_no+=1
                        nonlocal C_details
                        nonlocal i_details
                        nonlocal ag3
                        global pas
                        nonlocal prd,RTE,PER,qty
                        
                        raw_TS=datetime.now(IST)
                        cur_tm1=raw_TS.strftime('%H:%M:%S')
                        cur_dt1=raw_TS.strftime('%d %b %Y')
                        total=float(ag3.get())

                        c=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
                        cr=c.cursor()
                        cr.execute('select Gst_no from details where passwd="{}"'.format(pas))
                        no=cr.fetchone()
                        gst1=no[0]
                        c.commit()
                        
                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gst1)
                        cr1=c1.cursor()
                        qch1='select Gst_no, Invoice_no from customers,invoices'
                        cr1.execute(qch1)
                        gcheck=cr1.fetchall()
                        found=False
                        global blazec
                        rblaze=int(blazec%2)

                        if len(gcheck)>0:
                            for i in gcheck:
                                if i[0]==C_details[3].get():
                                    qu1='update Customers set Total_T=Total_T+%s where Gst_no=%s'
                                    vu1=(float(ag3.get()),C_details[3].get())
                                    cr1.execute(qu1,vu1)
                                    cr1.execute('update Customers set Last_T="{}" where Gst_no="{}"'.format(i_details[1].get(),C_details[3].get()))
                                    cr1.execute('update Customers set last_Ttime="{}" where Gst_no="{}"'.format(str(cur_tm1),C_details[3].get()))
                                        
                                    c1.commit()
                                    found=True
                                    break
                                else:
                                    qc='insert into Customers values(%s,%s,%s,%s,%s,%s,%s,%s)'
                                    vc=(C_details[0].get(),C_details[2].get(),C_details[1].get(),C_details[3].get(),C_details[4].get(),i_details[1].get(),total,str(cur_tm1))
                                    cr1.execute(qc,vc)
                                    c1.commit()
                                    break
                        else:
                            qc='insert into Customers values(%s,%s,%s,%s,%s,%s,%s,%s)'
                            vc=(C_details[0].get(),C_details[2].get(),C_details[1].get(),C_details[3].get(),C_details[4].get(),i_details[1].get(),total,str(cur_tm1))
                            cr1.execute(qc,vc)
                            c1.commit()

                        if len(gcheck)>0:
                            for i in gcheck:
                                if i[1]!= int(i_details[0].get()):
                                    qi='insert into Invoices values(%s,%s,%s,%s,%s,%s)'
                                    vi=(i_details[0].get(),i_details[1].get(),C_details[0].get(),str(cur_tm1),float(ag3.get()),rblaze)
                                    cr1.execute(qi,vi)
                                    break
                                    
                                else:
                                    qui1='update invoices set customer=%s where Invoice_no=%s'
                                    vui1=(C_details[0].get(),int(i_details[0].get()))
                                    cr1.execute(qui1,vui1)
                                    qui2='update invoices set Date=%s where Invoice_no=%s'
                                    vui2=(i_details[1].get(),int(i_details[0].get()))
                                    cr1.execute(qui2,vui2)
                                    qui3='update invoices set Time=%s where Invoice_no=%s'
                                    vui3=(str(cur_tm1),int(i_details[0].get()))
                                    cr1.execute(qui3,vui3)
                                    break

                        else:
                            qi='insert into Invoices values(%s,%s,%s,%s,%s,%s)'
                            vi=(i_details[0].get(),i_details[1].get(),C_details[0].get(),str(cur_tm1),float(ag3.get()),rblaze)
                            cr1.execute(qi,vi)

                        c1.commit()

                        c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gst1)
                        cr1=c1.cursor()
                        qch3='select * from products'
                        cr1.execute(qch3)
                        gcheck3=cr1.fetchall()
                        P_id=0
                        
                        if len(gcheck3)>0:
                            for i in range(len(gcheck3)):
                                if gcheck3[i][0]==prd[i].get() and int(gcheck3[i][2])==int(RTE[i].get()) and int(gcheck3[i][3])==int(PER[i].get()):
                                    qup1='update Products set Total_stock=Total_stock-%s where P_id=%s'
                                    vup1=(int(qty[i].get()),int(gcheck3[i][6]))
                                    cr1.execute(qup1,vup1)
                                    cr1.execute('update Products set Last_T="{}" where P_id={}'.format(i_details[1].get(),int(gcheck3[i][6])))
                                    cr1.execute('update Products set TIME="{}" where P_id={}'.format(str(cur_tm1),int(gcheck3[i][6])))

                                else:
                                    qch4='select max(P_id) from products'
                                    cr1.execute(qch4)
                                    pid=cr1.fetchone()
                                    P_id=int(pid[0])+1
                                    if len(prd[i].get())!=0 and len(RTE[i].get())!=0 and len(PER[i].get())!=0 and len(qty[i].get())!=0:
                                        qcn='insert into Products values(%s,%s,%s,%s,%s,%s,%s)'
                                        vcn=(prd[i].get(),-(int(qty[i].get())),RTE[i].get(),PER[i].get(),i_details[1].get(),str(cur_tm1),P_id)
                                        cr1.execute(qcn,vcn)
                                        break

                        else:
                            for i in range(len(prd)):
                                if len(prd[i].get())!=0 and len(RTE[i].get())!=0 and len(PER[i].get())!=0 and len(qty[i].get())!=0:
                                    qch4='select max(P_id) from products'
                                    cr1.execute(qch4)
                                    pid=cr1.fetchone()
                                    if str(pid[0])=='None':
                                        P_id=1
                                    else:
                                        P_id=int(pid[0])+1
                                    qcn1='insert into Products values(%s,%s,%s,%s,%s,%s,%s)'
                                    vcn1=(prd[i].get(),-(int(qty[i].get())),RTE[i].get(),PER[i].get(),i_details[1].get(),str(cur_tm1),P_id)
                                    cr1.execute(qcn1,vcn1)

                        for i in range(len(prd)):
                            if len(prd[i].get())!=0 and len(qty[i].get())!=0 and len(RTE[i].get())!=0:
                                qcn3='insert into Product_details values(%s,%s,%s,%s,%s,%s,%s)'
                                vcn3=(prd[i].get(),int(qty[i].get()),RTE[i].get(),float(ag3.get()),PER[i].get(),i_details[1].get(),str(cur_tm1))
                                cr1.execute(qcn3,vcn3)
                                        
                        c1.commit()
                                        
                        def summary():
                            nonlocal cur_dt1
                            ws=Tk()
                            ws.config(background='white')
                            ws.geometry('1366x768')

                            cur_dts=raw_TS.strftime('%d %b %Y')
                            stxt='Invoice Date: '+cur_dts
                            iblabel=Label(ws,padx=700,pady=8)
                            iblabel.place(x=0,y=0)
                            ilabel=Label(ws,text=stxt,font=('Arial',12,'bold'))
                            ilabel.place(x=20,y=4)

                            #Left Info
                            global cr
                            global pas
                            cr.execute("select Business_name,Address,e_mail,Phone_no,Gst_no from Details where passwd='{}'".format(pas))
                            data1=cr.fetchall()
                            for j in data1:
                                b_name=j[0]
                                ad=j[1]
                                em=j[2]
                                ph=j[3]
                                gn=j[4]
                                
                                
                            itlabel=Label(ws,text=b_name,font=('Arial',12,'bold'),bg='white',pady=0)
                            itlabel.place(x=20,y=60)
                            
                            sad=Label(ws,text=ad,font=('Arial',12),bg='white',pady=0)
                            sad.place(x=20,y=80)

                            etxt='EMAIL: '+em
                            email=Label(ws,text=etxt,font=('Arial',12),bg='white',pady=0)
                            email.place(x=20,y=100)

                            ptxt='Phone: '+ph
                            phone=Label(ws,text=ptxt,font=('Arial',12),bg='white',pady=0)
                            phone.place(x=20,y=120)

                            gtxt='GST No: '+gn
                            gst=Label(ws,text=gtxt,font=('Arial',12),bg='white',pady=0)
                            gst.place(x=20,y=140)

                            #Right Info
                            blabel=Label(ws,text='Billed To:',font=('Arial',12),bg='white',pady=0)
                            blabel.place(x=900,y=60)

                            cn=C_details[0].get()   
                            cname=Label(ws,text=cn,font=('Arial',12,'bold'),bg='white',pady=0)
                            cname.place(x=900,y=100)

                            cad=C_details[1].get()
                            state=C_details[4].get()
                            cadp=cad.split(',')
                            if len(cadp)!=1:
                                city=cadp[-1]+' , '+state
                                clabel=Label(ws,text=city,font=('Arial',12),bg='white',pady=0)
                                clabel.place(x=896,y=120)
                            else:
                                city=cadp[-1]+' , '+state
                                clabel=Label(ws,text=city,font=('Arial',12),bg='white',pady=0)
                                clabel.place(x=900,y=120)

                            ph1=C_details[2].get()
                            ptxt1='Phone: '+ph1
                            phone1=Label(ws,text=ptxt1,font=('Arial',12),bg='white',pady=0)
                            phone1.place(x=900,y=140)

                            gn1=C_details[3].get()
                            gtxt1='GST No: '+gn1
                            gst1=Label(ws,text=gtxt1,font=('Arial',12),bg='white',pady=0)
                            gst1.place(x=900,y=160)

                            #Table Items
                            nonlocal prd
                            nonlocal qty
                            nonlocal RTE
                            nonlocal AWG
                            nonlocal PER
                            nonlocal SGST
                            nonlocal CGST
                            nonlocal AGL
                            global blazec

                            #Table stucture
                            if blazec%2==0:
                                labelh=Label(ws,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                labelh.place(x=20,y=200)
                                hlabel=Label(ws,text='#',font=('Arial',12,'bold'),bg='white',pady=0)
                                hlabel.place(x=21,y=201)

                                labelp=Label(ws,bg='white',pady=5,width=45,relief=GROOVE)
                                labelp.place(x=38+7,y=200)
                                PN=Label(ws,text='Items',font=('Arial',12,'bold'),bg='white',pady=0)
                                PN.place(x=45+7,y=201)

                                labelq=Label(ws,bg='white',pady=5,width=15,relief=GROOVE)
                                labelq.place(x=300+7,y=200)
                                qt=Label(ws,text='QTY',font=('Arial',12,'bold'),bg='white',pady=0)
                                qt.place(x=302+7,y=201)

                                labelr=Label(ws,bg='white',pady=5,width=20,relief=GROOVE)
                                labelr.place(x=400+7,y=200)
                                rt=Label(ws,text='Rate(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                rt.place(x=402+7,y=201)

                                labelat=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelat.place(x=540+7,y=200)
                                tat=Label(ws,text='Taxable Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                tat.place(x=542+7,y=201)

                                labelgp=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelgp.place(x=726+7,y=200)
                                gp=Label(ws,text='GST(%)',font=('Arial',12,'bold'),bg='white',pady=0)
                                gp.place(x=728+7,y=201)

                                labelc=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelc.place(x=856+7,y=200)
                                cg=Label(ws,text='CGST(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                cg.place(x=858+7,y=201)

                                labels=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labels.place(x=986+7,y=200)
                                sg=Label(ws,text='SGST(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                sg.place(x=988+7,y=201)

                                labelto=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelto.place(x=1105+7,y=200)
                                tot=Label(ws,text='Total Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                tot.place(x=1107+7,y=201)

                                #Tabel Contents
                                r=0
                                for i in range(len(prd)):
                                    if len(prd[i].get())!=0:
                                        r+=1
                                        labelh1=Label(ws,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                        labelh1.place(x=20,y=227+i*27)
                                        hlabel1=Label(ws,text=i+1,font=('Arial',12),bg='white',pady=0)
                                        hlabel1.place(x=21,y=228+i*27)

                                        labelp1=Label(ws,bg='white',pady=5,width=45,relief=GROOVE)
                                        labelp1.place(x=38+7,y=227+i*27)
                                        PN1=Label(ws,text=prd[i].get(),font=('Arial',12),bg='white',pady=0)
                                        PN1.place(x=45+7,y=228+i*27)

                                        labelq1=Label(ws,bg='white',pady=5,width=15,relief=GROOVE)
                                        labelq1.place(x=300+7,y=227+i*27)
                                        qt1=Label(ws,text=qty[i].get(),font=('Arial',12),bg='white',pady=0)
                                        qt1.place(x=302+7,y=228+i*27)

                                        labelr1=Label(ws,bg='white',pady=5,width=20,relief=GROOVE)
                                        labelr1.place(x=400+7,y=227+i*27)
                                        rt1=Label(ws,text=RTE[i].get(),font=('Arial',12),bg='white',pady=0)
                                        rt1.place(x=402+7,y=228+i*27)

                                        labelat1=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelat1.place(x=540+7,y=227+i*27)
                                        tat1=Label(ws,text=AWG[i].get(),font=('Arial',12),bg='white',pady=0)
                                        tat1.place(x=542+7,y=228+i*27)

                                        labelgp1=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelgp1.place(x=726+7,y=227+i*27)
                                        gp1=Label(ws,text=PER[i].get(),font=('Arial',12),bg='white',pady=0)
                                        gp1.place(x=728+7,y=228+i*27)

                                        labelc1=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelc1.place(x=856+7,y=227+i*27)
                                        cg1=Label(ws,text=CGST[i].get(),font=('Arial',12),bg='white',pady=0)
                                        cg1.place(x=858+7,y=228+i*27)

                                        labels1=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                        labels1.place(x=986+7,y=227+i*27)
                                        sg1=Label(ws,text=SGST[i].get(),font=('Arial',12),bg='white',pady=0)
                                        sg1.place(x=988+7,y=228+i*27)

                                        labelto1=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelto1.place(x=1105+7,y=227+i*27)
                                        tot1=Label(ws,text=AGL[i].get(),font=('Arial',12),bg='white',pady=0)
                                        tot1.place(x=1107+7,y=228+i*27)

                                #Table Total
                                labelt=Label(ws,bg='white',pady=5,padx=7,width=74,relief=GROOVE)
                                labelt.place(x=20,y=228+r*27)
                                tlabel=Label(ws,text='Total:',font=('Arial',12,'bold'),bg='white',pady=0)
                                tlabel.place(x=490+7,y=230+r*27)
                                        
                                labelat2=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelat2.place(x=540+7,y=228+r*27)
                                tot=0
                                nonlocal ag4
                                for i in AWG:
                                    tot+=float(i.get())
                                tlabel=Label(ws,text=ag4.get(),font=('Arial',12,'bold'),bg='white',pady=0)
                                tlabel.place(x=542+7,y=230+r*27)
                                        
                                labelgp2=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelgp2.place(x=726+7,y=228+r*27)
                                        
                                labelc2=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelc2.place(x=856+7,y=228+r*27)
                                ctot=0
                                for i in CGST:
                                    ctot+=float(i.get())
                                ctlabel=Label(ws,text=ctot,font=('Arial',12,'bold'),bg='white',pady=0)
                                ctlabel.place(x=858+7,y=230+r*27)
                                        
                                labels2=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labels2.place(x=986+7,y=228+r*27)
                                ctlabel=Label(ws,text=ctot,font=('Arial',12,'bold'),bg='white',pady=0)
                                ctlabel.place(x=988+7,y=230+r*27)
                                        
                                labelto2=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelto2.place(x=1105+7,y=228+r*27)
                                atot=0
                                for i in AGL:
                                    atot+=float(i.get())
                                atlabel=Label(ws,text=atot,font=('Arial',12,'bold'),bg='white',pady=0)
                                atlabel.place(x=1107+7,y=230+r*27)

                                twords=num2words(atot,lang='en_IN')+' only.'
                                twordsf=twords.capitalize()
                                labeltw=Label(ws,bg='white',pady=5,padx=1,width=111,relief=GROOVE)
                                labeltw.place(x=510+7,y=260+r*27)
                                labeltw1=Label(ws,text='Invoice Total in Words:',font=('Arial',12,'bold'),bg='white',pady=0)
                                labeltw1.place(x=520+7,y=262+r*27)
                                labeltw2=Label(ws,text=twordsf,font=('Arial',12,'bold'),bg='white',pady=0)
                                labeltw2.place(x=700+7,y=262+r*27)

                            else:
                                labelh=Label(ws,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                labelh.place(x=20,y=200)
                                hlabel=Label(ws,text='#',font=('Arial',12,'bold'),bg='white',pady=0)
                                hlabel.place(x=21,y=201)

                                labelp=Label(ws,bg='white',pady=5,width=45,relief=GROOVE)
                                labelp.place(x=38+7,y=200)
                                PN=Label(ws,text='Items',font=('Arial',12,'bold'),bg='white',pady=0)
                                PN.place(x=45+7,y=201)

                                labelq=Label(ws,bg='white',pady=5,width=15,relief=GROOVE)
                                labelq.place(x=300+7,y=200)
                                qt=Label(ws,text='QTY',font=('Arial',12,'bold'),bg='white',pady=0)
                                qt.place(x=302+7,y=201)

                                labelr=Label(ws,bg='white',pady=5,width=20,relief=GROOVE)
                                labelr.place(x=400+7,y=200)
                                rt=Label(ws,text='Rate(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                rt.place(x=402+7,y=201)

                                labelat=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelat.place(x=540+7,y=200)
                                tat=Label(ws,text='Taxable Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                tat.place(x=542+7,y=201)

                                labelgp=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelgp.place(x=726+7,y=200)
                                gp=Label(ws,text='GST(%)',font=('Arial',12,'bold'),bg='white',pady=0)
                                gp.place(x=728+7,y=201)

                                labelc=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelc.place(x=856+7,y=200)
                                cg=Label(ws,text='IGST(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                cg.place(x=858+7,y=201)

                                labelto=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelto.place(x=986+7,y=200)
                                tot=Label(ws,text='Total Amount(Rs.)',font=('Arial',12,'bold'),bg='white',pady=0)
                                tot.place(x=988+7,y=201)

                                #Tabel Contents
                                r=0
                                for i in range(len(prd)):
                                    if len(prd[i].get())!=0:
                                        r+=1
                                        labelh1=Label(ws,bg='white',pady=5,padx=2,width=3,relief=GROOVE)
                                        labelh1.place(x=20,y=227+i*27)
                                        hlabel1=Label(ws,text=i+1,font=('Arial',12),bg='white',pady=0)
                                        hlabel1.place(x=21,y=228+i*27)

                                        labelp1=Label(ws,bg='white',pady=5,width=45,relief=GROOVE)
                                        labelp1.place(x=38+7,y=227+i*27)
                                        PN1=Label(ws,text=prd[i].get(),font=('Arial',12),bg='white',pady=0)
                                        PN1.place(x=45+7,y=228+i*27)

                                        labelq1=Label(ws,bg='white',pady=5,width=15,relief=GROOVE)
                                        labelq1.place(x=300+7,y=227+i*27)
                                        qt1=Label(ws,text=qty[i].get(),font=('Arial',12),bg='white',pady=0)
                                        qt1.place(x=302+7,y=228+i*27)

                                        labelr1=Label(ws,bg='white',pady=5,width=20,relief=GROOVE)
                                        labelr1.place(x=400+7,y=227+i*27)
                                        rt1=Label(ws,text=RTE[i].get(),font=('Arial',12),bg='white',pady=0)
                                        rt1.place(x=402+7,y=228+i*27)

                                        labelat1=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelat1.place(x=540+7,y=227+i*27)
                                        tat1=Label(ws,text=AWG[i].get(),font=('Arial',12),bg='white',pady=0)
                                        tat1.place(x=542+7,y=228+i*27)

                                        labelgp1=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelgp1.place(x=726+7,y=227+i*27)
                                        gp1=Label(ws,text=PER[i].get(),font=('Arial',12),bg='white',pady=0)
                                        gp1.place(x=728+7,y=228+i*27)

                                        labelc1=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                        labelc1.place(x=856+7,y=227+i*27)
                                        cg1=Label(ws,text=IGST[i].get(),font=('Arial',12),bg='white',pady=0)
                                        cg1.place(x=858+7,y=228+i*27)

                                        labelto1=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                        labelto1.place(x=986+7,y=227+i*27)
                                        tot1=Label(ws,text=AGL[i].get(),font=('Arial',12),bg='white',pady=0)
                                        tot1.place(x=988+7,y=228+i*27)

                                #Table Total
                                labelt=Label(ws,bg='white',pady=5,padx=7,width=74,relief=GROOVE)
                                labelt.place(x=20,y=228+r*27)
                                tlabel=Label(ws,text='Total:',font=('Arial',12,'bold'),bg='white',pady=0)
                                tlabel.place(x=490+7,y=230+r*27)
                                        
                                labelat2=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelat2.place(x=540+7,y=228+r*27)
                                tot=0
                                for i in AWG:
                                    tot+=float(i.get())
                                tlabel=Label(ws,text=tot,font=('Arial',12,'bold'),bg='white',pady=0)
                                tlabel.place(x=542+7,y=230+r*27)
                                        
                                labelgp2=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelgp2.place(x=726+7,y=228+r*27)
                                        
                                labelc2=Label(ws,bg='white',pady=5,width=18,relief=GROOVE)
                                labelc2.place(x=856+7,y=228+r*27)
                                ctot=0
                                for i in IGST:
                                    ctot+=float(i.get())
                                itlabel=Label(ws,text=ctot,font=('Arial',12,'bold'),bg='white',pady=0)
                                itlabel.place(x=858+7,y=230+r*27)
                                        
                                labelto2=Label(ws,bg='white',pady=5,width=26,relief=GROOVE)
                                labelto2.place(x=986+7,y=228+r*27)
                                atot=0
                                for i in AGL:
                                    atot+=float(i.get())
                                atlabel=Label(ws,text=atot,font=('Arial',12,'bold'),bg='white',pady=0)
                                atlabel.place(x=988+7,y=230+r*27)

                                twords=num2words(atot,lang='en_IN')+' only.'
                                twordsf=twords.capitalize()
                                labeltw=Label(ws,bg='white',pady=5,padx=2,width=111,relief=GROOVE)
                                labeltw.place(x=510-120+7,y=260+r*27)
                                labeltw1=Label(ws,text='Invoice Total in Words:',font=('Arial',12,'bold'),bg='white',pady=0)
                                labeltw1.place(x=520-120+7,y=262+r*27)
                                labeltw2=Label(ws,text=twordsf,font=('Arial',12,'bold'),bg='white',pady=0)
                                labeltw2.place(x=700-120+7,y=262+r*27)

                            ws.mainloop()
                        summary()


                    s_btn=Button(w3, text='Submit',
                             padx=5,
                             pady=5,command=submit,
                           font=('Arial',13,'bold'),
                           fg="white",
                           bg='#0476D0',
                            cursor='hand2',
                           activeforeground='white',      #text color of button when is clicked
                           activebackground='grey')      #button created to bring the entry into work
                    s_btn.place(x=100,y=600)

                    label1=Label(w3,bg='#7B7571',padx=700,pady=15)
                    label1.place(x=0,y=718)

               
                    w3.mainloop()
                n_invoicem()

        if f==True:
            mb.showerror("GBI Tool", "Incorrect Details!!!",parent=w)
    
    

    s_btn=Button(w, text='Submit',
             padx=5,
             pady=5,command=submit,
           font=('Arial',13,'bold'),
           fg="white",
           bg='#0476D0',
            cursor='hand2',
           activeforeground='white',      #text color of button when is clicked
           activebackground='grey')      #button created to bring the entry into work
    s_btn.place(x=805,y=409+60)

    def sign():
        w1=Tk()
        w1.title('Signup')                         #Title of our window
        w1.geometry('1366x768')
        w1.config(background='white')
    

        label=Label(w1,text='Sign Up', fg='grey',bg='white',
            font=('Arial',20))
        label.place(x=0,y=0)

        label2=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label2.place(x=0,y=47)

        label3=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label3.place(x=0,y=107)

        label4=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label4.place(x=0,y=167)

        label5=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label5.place(x=0,y=227)

        label6=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label6.place(x=0,y=287)

        label7=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label7.place(x=0,y=347)

        label8=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label8.place(x=0,y=407)

        label9=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label9.place(x=0,y=467)

        label9=Label(w1,   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            relief=GROOVE,
            padx=1000,   #spacing of text from border in x axis
            pady=20)
        label9.place(x=0,y=527)


        username=Label(w1,text='Username:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        username.place(x=500,y=60)

        passwd=Label(w1,text='Password:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        passwd.place(x=500,y=120)

        cpasswd=Label(w1,text='Confirm Password:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        cpasswd.place(x=435,y=180)

        Bname=Label(w1,text='Business Name:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        Bname.place(x=460,y=240)

        add=Label(w1,text='Address:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        add.place(x=515,y=300)

        state=Label(w1,text='State:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        state.place(x=539,y=360)

        mail=Label(w1,text='Email Id:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        mail.place(x=520,y=420)

        phone=Label(w1,text='Phone Number:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        phone.place(x=463,y=480)

        gst=Label(w1,text='GST Number:',   #window object and text to be shown
            font=('Arial',13,'bold'),      #font name,size and style
            fg='black',   #text color
            bg='white',   #label bg color
            padx=5,   #spacing of text from border in x axis
            pady=5)
        gst.place(x=480,y=540)

        entry_usr=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_usr.place(x=620,y=65)

        entry_pas=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_pas.place(x=620,y=125)

        entry_cpa=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_cpa.place(x=620,y=185)

        entry_bn=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_bn.place(x=620,y=245)

        entry_ad=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_ad.place(x=620,y=305)

        entry_st=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_st.place(x=620,y=365)

        entry_mail=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_mail.place(x=620,y=425)

        entry_no=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_no.place(x=620,y=485)

        entry_gst=Entry(w1,font=('Arial',13),
            fg='black',
            bg='#CDD9DF')
        entry_gst.place(x=620,y=545)
    
        global t
        lb=Label(w1,text=t,font=('comic sans',20,'bold'),fg='white',bg='#7B7571',padx=10,pady=200)
        lb.place(x=0,y=48)
        lb1=Label(w1,font=('comic sans',20,'bold'),fg='white',bg='#7B7571',padx=20,pady=300)
        lb1.place(x=1325,y=48)

        def submit():
            nonlocal w1
            usr=entry_usr.get()
            pas=entry_pas.get()
            cp=entry_cpa.get()
            bn=entry_bn.get()
            ad=entry_ad.get()
            st=entry_st.get()
            mail=entry_mail.get()
            no=entry_no.get()
            gst=entry_gst.get()
            details=(gst,usr,cp,bn,ad,mail,no,st)
            login=(usr,cp)
            c=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database='Login_details')
            cr=c.cursor()
            if pas==cp:
                mb.showinfo("GBI Tool", "You are registered Successfully!",parent=w1)
                l_btn=Button(w1, text='Login',
                 padx=5,
                 pady=5,command=w1.destroy,
                   font=('Arial',13,'bold'),
                   fg="white",
                   bg='#0476D0',
                   activeforeground='white',      #text color of button when is clicked
                   activebackground='grey')      #button created to bring the entry into work
                l_btn.place(x=585,y=610)
                q='insert into details values(%s,%s,%s,%s,%s,%s,%s,%s)'
                cr.execute(q,details)
                q1='insert into login values(%s,%s)'
                cr.execute(q1,login)
                c.commit()
                cn=ms.connect(host='localhost' , user='root',passwd='Suj@l0903')
                crn=cn.cursor()
                crn.execute('Create database {}'.format(gst))
                cn.commit()
                c1=ms.connect(host='localhost' , user='root',passwd='Suj@l0903',database=gst)
                cr1=c1.cursor()
                cr1.execute('create table Customers(Name varchar(50), Mob_No varchar(10), Address varchar(100), Gst_No varchar(15), State varchar(20),last_T date, Total_T int, Last_Ttime time)')
                cr1.execute('create table products(Name varchar(20), Total_stock int, Rate int, Gst_P int, last_T date, Time time, P_id int)')
                cr1.execute('create table invoices(Invoice_no int, Date date, Customer varchar(20), Time time, T_amt int, GST_type int)')
                cr1.execute('create table product_details(Items varchar(50), QTY int, Rate int, Tax_amt int, Percent int, date date, time time)')
                c1.commit()
                
                l_btn=Button(w1, text='Login',padx=5,pady=5,font=('Arial',13,'bold'),fg="white",bg='#0476D0',width=6,
                     activeforeground='white',  command=w1.destroy,    
                     activebackground='grey')
                l_btn.place(x=585,y=610)
            
            else:
                mb.showerror("Error", "Enter same password in confirm password!!",parent=w1) 

        s_btn=Button(w1, text='Submit',
             padx=5,
             pady=5,command=submit,
           font=('Arial',13,'bold'),
           fg="white",
           bg='#0476D0',
            cursor='hand2',
           activeforeground='white',      #text color of button when is clicked
           activebackground='grey')      #button created to bring the entry into work
        s_btn.place(x=585,y=610)

        c_btn=Button(w1, text='Cancel',
             padx=5,
             pady=5,command=w1.destroy,
           font=('Arial',13,'bold'),
           fg="white",
           bg='red',
            cursor='hand2',
           activeforeground='white',      #text color of button when is clicked
           activebackground='grey')      #button created to bring the entry into work
        c_btn.place(x=680,y=610)
        
        w1.mainloop()

        
    s1_btn=Button(w, text='Sign Up',
             padx=50,
             pady=5,command=sign,
           font=('Arial',13,'bold'),
           fg="white",
           bg='midnightblue',
            cursor='hand2',
           activeforeground='white',      #text color of button when is clicked
           activebackground='grey')      #button created to bring the entry into work
    s1_btn.place(x=710,y=509)


    w.mainloop()

cr_btn=Button(wi, text='Create Invoice',
             padx=5,
             pady=2,command=nxt,
             relief=FLAT,
             font=('Times New Roman',13),
             fg="white",
             bg='#0483FD',
             cursor='hand2',
             activeforeground='white',      #text color of button when is clicked
             activebackground='grey')      #button created to bring the entry into work
cr_btn.place(x=170,y=240)


interface=PhotoImage(file='F:\Python\Project\Images\\interface.png')
lab=Label(wi,bg='#0483FD',pady=120,padx=150)
lab.place(x=30,y=370)
labt=Label(wi,text='Simple Interface',bg='#0483FD',fg='white',font=('Times New Roman',17))
labt.place(x=40,y=380)
labi=Label(wi,image=interface)
labi.place(x=40,y=420)

ci=PhotoImage(file='F:\Python\Project\Images\\customers1.png')
lab1=Label(wi,bg='#0483FD',pady=120,padx=150)
lab1.place(x=360,y=370)
labt=Label(wi,text='Keep Check On Customers',bg='#0483FD',fg='white',font=('Times New Roman',17))
labt.place(x=370,y=380)
labc=Label(wi,image=ci)
labc.place(x=370,y=420)


bi=PhotoImage(file='F:\Python\Project\Images\\book1.png')
lab2=Label(wi,bg='#0483FD',pady=120,padx=150)
lab2.place(x=690,y=370)
labt=Label(wi,text='Manage Books & Balances',bg='#0483FD',fg='white',font=('Times New Roman',17))
labt.place(x=700,y=380)
labc=Label(wi,image=bi)
labc.place(x=700,y=420)

ii=PhotoImage(file='F:\Python\Project\Images\\inventory1.png')
lab3=Label(wi,bg='#0483FD',pady=120,padx=150)
lab3.place(x=1020,y=370)
labt=Label(wi,text='Easy Inventory Management',bg='#0483FD',fg='white',font=('Times New Roman',17))
labt.place(x=1030,y=380)
labc=Label(wi,image=ii)
labc.place(x=1030,y=420)


wi.mainloop()




