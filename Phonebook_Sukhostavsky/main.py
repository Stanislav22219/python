from tkinter import *
from tkinter import ttk, messagebox
from view import *

co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title("Телефонний довідник")
width_center = (window.winfo_screenwidth() // 2) - (1024 // 2)
height_center = (window.winfo_screenheight() // 2) - (768 // 2)
window.geometry(f'1024x768+{width_center}+{height_center}')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)
window.iconbitmap("Icons/contacts.ico")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", font=('Helvetica', 15), foreground=co0, background=co2)
style.configure("Treeview", font=('Helvetica', 14), rowheight=30)


def show():
    global tree
    listheader = ['Name', 'Telephone', 'Email', 'Address']
    data_list = view()

    tree = ttk.Treeview(frame_bottom, selectmode="extended", columns=listheader, show='headings')
    vsb = ttk.Scrollbar(frame_bottom, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_bottom, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set, height=11)

    tree.grid(column=0, row=0, sticky=NSEW)
    vsb.grid(column=1, row=0, sticky=NS)
    hsb.grid(column=0, row=1, sticky=EW)

    tree.heading(0, command=lambda c='Name': sort_treeview(tree, c, False), text=' ПІБ', anchor=NW)
    tree.heading(1, command=lambda c='Telephone': sort_treeview(tree, c, False), text=' Номер', anchor=NW)
    tree.heading(2, command=lambda c='Email': sort_treeview(tree, c, False), text=' Email', anchor=NW)
    tree.heading(3, command=lambda c='Address': sort_treeview(tree, c, False), text=' Адреса', anchor=NW)

    tree.column(0, width=350, minwidth=350, anchor=NW)
    tree.column(1, width=165, minwidth=165, anchor=NW)
    tree.column(2, width=280, minwidth=280, anchor=NW)
    tree.column(3, width=191, minwidth=500, anchor=NW)

    for item in data_list:
        tree.insert('', 'end', values=item)
    sort_treeview(tree, 'Name', False)


def sort_treeview(tree, col, descending):
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    data.sort(reverse=descending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)
    tree.heading(col, command=lambda: sort_treeview(tree, col, not descending))


def about():
    about_window = Toplevel(window)
    about_window.title("Про додаток")
    about_window.geometry('800x350')
    about_window.resizable(width=FALSE, height=FALSE)
    about_window.configure(background=co0)
    about_window.iconbitmap("Icons/about.ico")

    about_text = """Телефонний довідник - це додаток, створений для зберігання та організації контактної інформації.

    Основні можливості:
    - Додавання нових контактів
    - Перегляд всіх контактів
    - Оновлення існуючих контактів
    - Видалення контактів
    - Пошук контактів за іменем або номером телефону

    Інструкція для користувача:
    1. Введіть дані контакту в поля введення в середній частині вікна.
    2. Натисніть кнопку 'Додати', щоб додати новий контакт.
    3. Виберіть контакт у таблиці та натисніть 'Оновити', щоб змінити дані контакту.
    4. Виберіть контакт у таблиці та натисніть 'Видалити', щоб видалити контакт.
    5. Введіть ім'я або номер телефону в поле пошуку, щоб знайти контакт."""

    Label(about_window, text=about_text, bg=co0, font='Helvetica 12').pack(pady=30)

    about_window.mainloop()


def insert():
    Name = e_name.get()
    Address = t_address.get(1.0, 'end-1c')
    Telephone = e_telephone.get()
    Email = e_email.get()
    data = [Name, Telephone, Email, Address]
    if Name == '' or Address == '' or Telephone == '' or Email == '':
        messagebox.showwarning('Увага!', 'Будь ласка, заповніть усі поля')
    else:
        add(data)
        messagebox.showinfo('Успіх', 'Дані були успішно додані')
        e_name.delete(0, 'end')
        t_address.delete(0.0, 'end-1c')
        e_telephone.delete(0, 'end')
        e_email.delete(0, 'end')
        show()


def to_update():
    try:
        b_update.configure(state='disabled')
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        Name = str(tree_list[0])
        Telephone = str('{:+10}'.format(tree_list[1]))
        global old_telephone
        old_telephone = str(tree_list[1])
        Email = str(tree_list[2])
        Address = str(tree_list[3])
        e_name.insert(0, Name)
        e_telephone.insert(0, Telephone)
        e_email.insert(0, Email)
        t_address.insert(0.0, Address, 'end-1c')
        def confirm():
            new_name = e_name.get()
            new_telephone = str(e_telephone.get()).replace(" ", "")
            new_email = e_email.get()
            new_address = t_address.get(1.0, 'end-1c')
            if new_name == '' or new_address == '' or new_telephone == '' or new_email == '':
                messagebox.showwarning('Увага!', 'Будь ласка, заповніть усі поля')
            else:
                data = [old_telephone, new_name, new_telephone, new_email, new_address]
                update(data)
                messagebox.showinfo('Успіх', 'Дані були успішно оновлені')
                e_name.delete(0, 'end')
                t_address.delete(0.0, 'end-1c')
                e_telephone.delete(0, 'end')
                e_email.delete(0, 'end')
                for widget in frame_bottom.winfo_children():
                    widget.destroy()
                b_confirm.destroy()
                b_update.configure(state='normal')
                show()
        b_confirm = Button(frame_middle, text="Підтвердити", width=20, height=1, bg=co2, fg=co0,
                           font=('Helvetica 18 bold'), command=confirm)
        b_confirm.place(x=680, y=215)
    except IndexError:
        messagebox.showerror('Помилка', 'Оберіть контакт, який бажаєте оновити')
        b_update.configure(state='normal')


def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone = str(tree_list[1])
        remove(tree_telephone)
        messagebox.showinfo('Успіх', 'Дані були успішно видалені')
        for widget in frame_bottom.winfo_children():
            widget.destroy()
        show()
        clear()
    except IndexError:
        messagebox.showerror('Помилка', 'Оберіть контакт, який бажаєте видалити')


def to_search(sv):
    telephone = sv.get()
    data = search(telephone)
    tree.delete(*tree.get_children())

    for item in data:
        tree.insert('', 'end', values=item)


def clear():
    e_search.delete(0, 'end')


frame_top = Frame(window, width=1024, height=100, bg=co2)
frame_top.grid(row=0, column=0, padx=0, pady=1)

frame_middle = Frame(window, width=1024, height=280, bg=co0)
frame_middle.grid(row=1, column=0, padx=0, pady=1)

frame_bottom = Frame(window, width=1024, height=368, bg=co0, relief=GROOVE)
frame_bottom.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

app_name = Label(frame_top, text="Телефонний довідник", height=1, font=('Helvetica 40 bold'), fg=co0, bg=co2)
app_name.place(x=30, y=10)
b_about = Button(frame_top, text="Про додаток", bg=co2, fg=co0, font=('Helvetica 18 bold'),
                 highlightthickness=2, borderwidth=4, command=about)
b_about.place(x=820, y=22)

l_name = Label(frame_middle, text="ПІБ*", width=20, height=1, font=('Helvetica 20'), bg=co0, anchor=NW)
l_name.place(x=30, y=30)
e_name = Entry(frame_middle, width=35, justify='left', font=('Helvetica 16'), highlightthickness=1, relief="solid")
e_name.place(x=160, y=30)

l_telephone = Label(frame_middle, text="Номер*", height=1, font=('Helvetica 20'), bg=co0, anchor=NW)
l_telephone.place(x=30, y=90)
e_telephone = Entry(frame_middle, width=35, justify='left', font=('Helvetica 16'), highlightthickness=1, relief="solid")
e_telephone.place(x=160, y=90)

l_email = Label(frame_middle, text="Email*", height=1, font=('Helvetica 20'), bg=co0, anchor=NW)
l_email.place(x=30, y=150)
e_email = Entry(frame_middle, width=35, justify='left', font=('Helvetica 16'), highlightthickness=1, relief="solid")
e_email.place(x=160, y=150)

l_address = Label(frame_middle, text="Адреса*", width=20, height=1, font=('Helvetica 20'), bg=co0, anchor=NW)
l_address.place(x=30, y=210)
t_address = Text(frame_middle, width=38, height=2, font=('Helvetica 14 bold'), highlightthickness=1, relief="solid")
t_address.place(x=160, y=210)

l_search = Label(frame_middle, text="Пошук", height=1, bg=co2, fg=co0, font=('Helvetica 16 bold'))
l_search.place(x=680, y=30)
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: to_search(sv))
e_search = Entry(frame_middle, width=19, justify='left', font=('Helvetica 16'), highlightthickness=1, relief="solid",
                 textvariable=sv)
e_search.place(x=763, y=30)

b_clear = Button(frame_middle, text="Очистити", width=9, height=1, bg=co2, fg=co0, font=('Helvetica 18 bold'),
                 command=clear)
b_clear.place(x=680, y=75)

b_add = Button(frame_middle, text="Додати", width=9, height=1, bg=co2, fg=co0, font=('Helvetica 18 bold'),
               command=insert)
b_add.place(x=850, y=75)

b_update = Button(frame_middle, text="Редагувати", width=9, height=1, bg=co2, fg=co0, font=('Helvetica 18 bold'),
                  command=to_update)
b_update.place(x=850, y=145)

b_delete = Button(frame_middle, text="Видалити", width=9, height=1, bg=co2, fg=co0, font=('Helvetica 18 bold'),
                  command=to_remove)
b_delete.place(x=680, y=145)

show()

window.mainloop()
