from tkinter import *
from tkinter import ttk

def write_message():
    data = [login.get(), password.get()]
    with open("data.txt", "a") as file:
        file.write(' '.join(data) + '\n')
    label["text"] = "Данные успешно записаны"

def read_message():
    with open("data.txt", "r") as file:
        lines = file.readlines()
    if lines:
        found = False
        for line in lines:
            data = line.strip().split()
            if len(data) >= 2:
                file_login, file_password = data[0], data[1]
                if login.get() == file_login and password.get() == file_password:
                    label["text"] = "Успешный вход"
                    found = True
                    break
        if not found:
            label["text"] = "Неверный логин или пароль"
    else:
        label["text"] = "Файл пуст"

root = Tk()
root.title("Вход")
root.geometry("600x400")
root.configure(background="#0C0C0C")

zag = ttk.Label(text="Вход в аккаунт", font=("Arial", 20))
zag.configure(background="#0C0C0C", foreground="white")
zag.pack(anchor=N)

login = ttk.Entry()
name = ttk.Label(text="Введите логин", font=("Arial", 14))
name.configure(background="#0C0C0C", foreground="white")
name.pack(anchor=CENTER, padx= 10, pady=10)
login.pack(anchor= CENTER, padx=5, pady=5, ipady=3, ipadx=12)

password = ttk.Entry()
pasmessage = ttk.Label(text="Введите пароль", font=("Arial", 14))
pasmessage.configure(background="#0C0C0C", foreground="white")
pasmessage.pack(anchor=CENTER, padx=10, pady=10)
password.pack(anchor= CENTER, padx=5, pady=5, ipady=3, ipadx=12)

reg = ttk.Button(text="Зарегистрироваться", command=write_message)
reg.pack(anchor=CENTER, ipadx=5,ipady=5, pady=10)

vh = ttk.Button(text="Войти", command=read_message)
vh.pack(anchor=CENTER, ipadx=5,ipady=5, pady=5)

label = ttk.Label()
label.configure(background="#0C0C0C", foreground="white")
label.pack(anchor=S, pady=20)
root.mainloop()