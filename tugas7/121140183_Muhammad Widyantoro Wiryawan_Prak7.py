import tkinter as tk

def calculate():
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    operator = entry_operator.get()
    
    if operator == '+':
        hasil = num1 + num2
    elif operator == '-':
        hasil = num1 - num2
    elif operator == '*':
        hasil = num1 * num2
    elif operator == '/':
        hasil = num1 / num2
    else:
        hasil = 'Input tidak valid'
    
    label_hasil.config(text='hasil: ' + str(hasil))

window = tk.Tk()
window.title('Calculator')

label_num1 = tk.Label(window, text='Angka 1:')
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_operator = tk.Label(window, text='Operator:')
label_operator.pack()
entry_operator = tk.Entry(window)
entry_operator.pack()

label_num2 = tk.Label(window, text='Angka 2:')
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

btn_calculate = tk.Button(window, text='Hitung', command=calculate)
btn_calculate.pack()

label_hasil = tk.Label(window, text='hasil:')
label_hasil.pack()

window.mainloop()
