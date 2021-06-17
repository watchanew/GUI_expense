from tkinter import *
from tkinter import ttk, messagebox, filedialog  # ttk is theme of Tk
from datetime import datetime
import csv

root = Tk()
root.title('Cost expense')
root.geometry('1200x600+100+100')
############
#Menu Bar
menubar = Menu(root)
root.config(menu=menubar)

#File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Google Sheet')
#Help menu
def About():
    messagebox.showinfo('About', 'Hello, This Program is saving data program\nIf you want to donate to me\nJust 1 BTC\nBTC address: knb12*562')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)
#donate
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
############

Img1 = PhotoImage(file=r'C:\Users\Asus\Pictures\GUI picture\wallet.png')
Img1 = Img1.subsample(5)
Img2 = PhotoImage(file=r'C:\Users\Asus\Pictures\GUI picture\Koffee.png')
Img2 = Img2.subsample(25)
Img3 = PhotoImage(file=r'C:\Users\Asus\Pictures\GUI picture\calculator.png')
Img3 = Img3.subsample(25)
Img4 = PhotoImage(file=r'C:\Users\Asus\Pictures\GUI picture\diskette.png')
Img4 = Img4.subsample(25)

Tab = ttk.Notebook(root)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

F2 = Frame(T2)
F2.pack()

Tab.add(T1, text=f'{"Add expense":^{25}}', image=Img3, compound='top')
Tab.add(T2, text=f'{"List":^{25}}', image=Img2, compound='top')


# B1 = ttk.Button(root, text="Hello")
# B1.pack(ipadx=50,ipady=20) #pack this button in root, ipadx is internal scale of button
F1 = Frame(T1)
F1.place(x=300, y=50)


def Save(event=None):
    expense = v_expense.get()  # bring value from v_expense = Stringvar()
    price = v_price.get()
    amount = v_amount.get()
    time = datetime.now()
    if expense == '':
        print('No data')
        messagebox.showwarning('Error', 'Please fill list')
        return
    elif price == '':
        print('no price')
        messagebox.showwarning('Error', 'Please fill price')
        return
    elif amount == '':
        amount = 1

    try:
        total = float(price) * int(amount)
        print('{} List: {}, Price: {} baht, Amout: {},Total: {}'.format(time, expense, price, amount, total))
        text = '{} List: {}, Price: {} baht, Amout: {},Total: {}'.format(time, expense, price, amount, total)
        v_result.set(text)
        # clear old data in box(textentry)
        v_expense.set('')
        v_price.set('')
        v_amount.set('')

        # save data to csv and don't forget to import csv!!!
        with open('savedata.csv', 'a', encoding='utf-8',
                  newline='') as f:  # encoding='utf-8' is make it can type Thai Language
            # with is command to open file automatic
            # 'a' is append| It can continue saving file after old data
            fw = csv.writer(f)  # create function for write data
            data = [time, expense, price, amount, total]
            fw.writerow(data)
        # Return cursor to E1
        E1.focus()
        update_table()

    except Exception as e:
        print('ERROR', e)
        messagebox.showwarning('Error', 'Please fill number again, Invalid number')
        v_expense.set('')
        v_price.set('')
        v_amount.set('')
    return expense, price, amount, total


# Make button to click by Enter
root.bind('<Return>', Save)  # ต้องเพิ่ม def Save(event=None)

Font1 = (None, 20)  # Change font
# List box
L = ttk.Label(F1, image=Img1, text='List', font=Font1, compound='top').pack()
v_expense = StringVar()  # Stringvar is spacial variable for saving data in GUI
E1 = ttk.Entry(F1, textvariable=v_expense, font=Font1, justify='center')
E1.pack()
# Price box
L = ttk.Label(F1, text='Price (Bath)', font=Font1).pack()
v_price = StringVar()  # Stringvar is spacial variable for saving data in GUI
E2 = ttk.Entry(F1, textvariable=v_price, font=Font1, justify='center')
E2.pack()
# Amount box
L = ttk.Label(F1, text='Amount', font=Font1).pack()
v_amount = StringVar()  # Stringvar is spacial variable for saving data in GUI
E3 = ttk.Entry(F1, textvariable=v_amount, font=Font1, justify='center')
E3.pack()

B2 = ttk.Button(F1, image=Img4, text="Save", command=Save, compound='left')
B2.pack(ipadx=30, ipady=10, pady=20)

v_result = StringVar()
v_result.set('--Result--')
result = ttk.Label(F1, textvariable=v_result, font=Font1, foreground='green')
result.pack(pady=20)


# Tab2
def read_csv():
    with open(r'C:\Users\Asus\PycharmProjects\watcha101\savedata.csv', newline='', encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data

#Table
L = ttk.Label(T2, text='Show Table', font=Font1, compound='top').pack(pady=20)
# Treeview widget
header = ['Time','List','Price','Amount','Total']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()

for h in header:
    resulttable.heading(h,text=h)

headerwidth = [150,170,80,80,80]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)


def update_table():
    resulttable.delete(*resulttable.get_children())
    data = read_csv()
    for d in data:
        resulttable.insert('',0,value=d)

update_table()


root.mainloop()

