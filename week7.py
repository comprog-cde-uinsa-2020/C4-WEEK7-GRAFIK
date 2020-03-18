import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Grafik Maker')

name = []
skor = []

def add():
    try:
        if len(name) == 0:
            negara_corona1 = negara_corona.get()
            name1 = negara_corona1.split(',')
            for i in name1:
                name.append(i)

            skor1 = jumlah_corona.get()
            skor2 = skor1.split(",")
            skor3 = [int(i) for i in skor2]
            for x in skor3:
                skor.append(x)
        else:
            messagebox.showwarning('Perhatian !', 'Data Harus Terisi Lengkap dan Berpasangan !')
            return
    except:
        messagebox.showwarning('Perhatian !', 'Data Harus Terisi Lengkap dan Berpasangan !')
        return

    x = range(len(name))
    if a.get() == 1:
        plt.bar(x, skor)
        plt.xticks(x, name)
        plt.xlabel('Negara Corona')
        plt.ylabel('Jumlah Corona')
        plt.title('Grafik Batang Penderita Corona')
        plt.show()
    else:
        plt.plot(x, skor)
        plt.xticks(x, name)
        plt.xlabel('Negara Corona')
        plt.ylabel('Jumlah Corona')
        plt.title('Grafik Garis Penderita Corona')
        plt.show()
    return

def reset():
    negara_corona.delete(0, END)
    jumlah_corona.delete(0, END)

    a = []
    while len(name) > 0 and len(skor) > 0:
        q = name.pop()
        v = skor.pop()
        a.append(q)
        a.append(v)
        a.remove(q)
        a.remove(v)
    return

label= Label(root, text='Negara Corona:').grid(row=0, column=0, sticky=E, padx=2)
label1 = Label(root, text='Jumlah Corona:').grid(row=1, column=0, sticky=E, padx=2)

negara_corona = Entry(root, width=50)
negara_corona.grid(row=0, column=1, padx=4)
jumlah_corona = Entry(root, width=50)
jumlah_corona.grid(row=1, column=1, padx=4)

a = IntVar()
bar = Radiobutton(root, text="Grafik Batang", variable=a, value=1)
bar.grid(row=2, column=1, sticky=W)
line = Radiobutton(root, text="Grafik Garis", variable=a, value=2)
line.grid(row=2, column=1, sticky=E)

tombol1 = Button(root, text='Tampilkan', width=15, command=add).grid(row=4, columnspan=2, pady=2)
tombol2 = Button(root, text='Reset Data', width=15, command=reset).grid(row=5, columnspan=2, pady=2)
root.mainloop()
