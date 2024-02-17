from tkinter import *
window = Tk()
window.title('Mile To Km Converter')
window.resizable(False,False)
window.minsize(width=400,height=130)
entry1 = Entry(width=10)
entry1.grid(column=3, row=1, pady=20, padx=30)
def calculations():
    mile = float(entry1.get())
    km = mile * 1.60934
    result_label.config(text=f"{km:.2f}")

result_label=Label(text='')
result_label.grid(column=3,row=2,pady=5)
label = Label(text='Miles')
label.grid(column=4, row=1)
label.config(padx=30,pady=10)

label1 = Label(text='is equal to')
label1.grid(column=1, row=2)
label1.config(padx=30, pady=5)

label2 = Label(text='Km')
label2.grid(column=4, row=2)
label2.config(padx=30, pady=5)

calculate = Button(text='Calculate',command=calculations)
calculate.grid(column=3, row=3, pady=5,padx=30)
# calculate.config(pady=10)

window.mainloop()

