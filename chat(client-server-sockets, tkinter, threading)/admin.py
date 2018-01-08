from tkinter import *
from threading import Thread
from socket import socket
from client import *

# Стартовое окно
def main_window():
        # Замена окна после нажатия кнопки
        def del_mw_for_b1():
                main.destroy()
                enter_log_pas()
        # Замена окна после нажатия кнопки
        def del_mw_for_b2():
                main.destroy()
                create_new_account()
        main = Tk()
        main.title('Spalah Chat')
        main.geometry('500x300+500+200')
        main.resizable(False, False)
        info = Label(main, font = 'Arial 18', text = 'Welcome to "Spalah Chat" \nHave you account or you want create new?')
        info.pack()
        b1= Button(text = 'Yes, I have', command = del_mw_for_b1)
        b1.pack()
        b2 = Button(text = 'No, I want create', command = del_mw_for_b2)
        b2.pack()
        b3 = Button(text = 'Quit', command = exit)
        b3.pack()
        main.mainloop()



# Окно введения имеющегося логина и пароля
def enter_log_pas():
        # Замена окна после нажатия кнопки
        def del_elp_for_b2():
                log_pas.destroy()
                main_window()
        # Введение и проверка логина и пароля
        def log_in():
                log = enter1.get()
                pas = enter2.get()
                lp = log.strip().lower() + ' ' + pas.strip().lower() +';\n'
                with open ('logs.txt', 'r') as txt:
                        r_content = txt.readlines()
                if lp in r_content:
                        nickname = log
                        log_pas.destroy()
                        chat(nickname)
                else:
                        info = Label(log_pas, font = 'Arial 18', text = 'Sorry, password or login uncorrect :(')
                        info.pack()
        log_pas = Tk()
        log_pas.title('Spalah Chat')
        log_pas.geometry('500x300+500+200')
        log_pas.resizable(False, False)
        info = Label(log_pas, font = 'Arial 18', text = 'Enter your login and password')
        info.pack()
        login = Label(log_pas, font = 'Calibri 15', text = 'Login:')
        login.pack()
        enter1 = Entry(log_pas)
        enter1.pack()
        password = Label(log_pas, font = 'Calibri 15', text = 'Password:')
        password.pack()
        enter2 = Entry(log_pas)
        enter2.pack()
        b1= Button(log_pas, text = 'Log In', command = log_in)
        b1.pack()
        b2 = Button(log_pas, text = 'Back', command = del_elp_for_b2)
        b2.pack()
        log_pas.mainloop()



# Окно создания нового аккаунта
def create_new_account():
        # Замена окна после нажатия кнопки
        def del_cna_for_b2():
                cna.destroy()
                main_window()
        # Запись нового логина и пароля
        def create_acc():
                n_log = enter1.get()
                n_pas = enter2.get()
                with open ('logs.txt', 'a') as txt:
                                w_content = n_log.lower() + ' ' + n_pas.lower() + ';\n'
                                txt.write(w_content)
                cna.destroy()
                main_window()
        cna = Tk()
        cna.title('Spalah Chat')
        cna.geometry('500x300+500+200')
        cna.resizable(False, False)
        info = Label(cna, font = 'Arial 18', text = 'Enter new login and new password')
        info.pack()
        login = Label(cna, font = 'Calibri 15', text = 'New login:')
        login.pack()
        enter1 = Entry(cna)
        enter1.pack()
        password = Label(cna, font = 'Calibri 15', text = 'New password:')
        password.pack()
        enter2 = Entry(cna)
        enter2.pack()
        b1= Button(cna, text = 'Create account', command = create_acc)
        b1.pack()
        b2 = Button(cna, text = 'Back', command = del_cna_for_b2)
        b2.pack()
        cna.mainloop()



# Окно чата
def chat(nickname):
        chat = Tk()
        text=StringVar()
        name=StringVar()
        name.set(nickname)
        text.set('')
        chat.title('Spalah Chat')
        chat.geometry('500x300+500+200')
        chat.resizable(False, False)
        info = Label(chat, font = 'Arial 18', text = '<<<Welcome to chat!>>>')
        info.pack()
        log = Text(chat)
        msg = Entry(chat, textvariable=text)
        msg.pack(side = 'bottom', fill = 'x', expand = 'true')
        log.pack(side = 'top', fill = 'both', expand = 'true')
        # Приветсвие с вошедшим пользователем
        def greeting():
                log.insert(END, 'Hello ' + name.get() + '!\n')
        # Отправка сообщения с использованием логина

        # создаем переменную, которую передадим в клиентский поток. Создаем заранее, чтобы
        # сослаться на нее в функции.
        data = {}
        def sendmsg(event):
                log.insert(END, name.get() + ':' + text.get() + '\n')
                # Используем  функцию из нашего словаря. Сейчас ее там нет, но sendmsg вызовется, когда
                # пользователь введет сообщение. Значит, окно уже отображается на экране. Значит
                # клиентский поток уже создан. Значит, он успел создать функцию внутри data

                data['flag'](name.get() + ':' + text.get())
                text.set('')
        msg.bind('<Return>', sendmsg)
        chat.after(1, greeting)
        correct = name.get() + ':' + text.get() + '\n'
        # Передаем data, чтобы клиентский поток создал в нем функцию
        Thread(target = client, args = [correct, data]).start()
        chat.mainloop()



main_window()
