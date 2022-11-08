import tkinter as tk
from tkinter import ttk
from itertools import *
from random import randint

def clicked():
    vse_comb = list(combinations("qwertyuiopasdfghjklzxcvbnm", r= 3))          #функция, генерирующая код
    result = ''
    for i in range(4):
        chislo = randint(0, len(vse_comb)-1)
        a = [vse_comb[chislo][0], vse_comb[chislo][1], vse_comb[chislo][2]]
        a.append(str(chislo%10))
        potentials = list(permutations(a))
        chislo = randint(0, len(potentials)-1)
        rand_comb = potentials[chislo]
        result += rand_comb[0] + rand_comb[1] + rand_comb[2] + rand_comb[3]
    result = result[0:4] + "-" + result[4:8] + "-" + result[8:12] + "-" + result[12:]
    lbl_A.configure(text= result)

def close():                                                                   #функция, закрывающая окно
    window.destroy()

window = tk.Tk()                                                               #создаем окно
window.title("Генератор кода для получения 3000000кг рыбы в игре симулятор белого медведя")
window.geometry('627x417')
window.maxsize(627, 417)                                                       #задаем макисмальное и мимнимальное занчения размера окна
window.minsize(627, 417)
bg = tk.PhotoImage(file='miski1.png')

frame = ttk.Frame(window, padding=0)
frame.grid()

label_bg = tk.Label(frame, image=bg)
label_bg.place(x=0, y=0)

lbl_A = tk.Label(frame, text='место для рекламы', font=("Arial", 15), bg='#666699')             #добавляем надпись, на месте которой будет выводится код
lbl_A.grid(column=3, row=3, padx=19, pady=50)


lbl_your_Code = tk.Label(frame, text='Ваш  код:',  font=("Arial", 15), bg='#666699')            #добавляем надпись
lbl_your_Code.grid(column=3, row=2, padx=20, pady=0)


btn = tk.Button(frame, text='Сгенерировать уникальный код', font=("Arial", 15), command=clicked)     #добавляем кнопку, которая будет вызывать функцию генерации кода
btn.grid(column=2, row=1, padx=50, pady=30)
exit = tk.Button(frame, text='Закрыть', font=("Arial", 15), command=close)                       #добавляем кнопку, которая будет закрывать окно
exit.grid(column=3, row=5, padx=50, pady=100)


window.mainloop()