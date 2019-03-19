from tkinter import *
import backend

# creates main window
main_win = Tk()
# Changes the title
main_win.title("Bookstore manager")

def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)
    e_title.delete(0, END)
    e_title.insert(END, selected_tuple[1])
    e_author.delete(0, END)
    e_author.insert(END, selected_tuple[2])
    e_year.delete(0, END)
    e_year.insert(END, selected_tuple[3])
    e_price.delete(0, END)
    e_price.insert(END, selected_tuple[4])


def view_command():
    list_box.delete(0, END)
    for row in backend.view():
        list_box.insert(END, row)

def search_command():
    list_box.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), price_text.get()):
        list_box.insert(END, row)
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_year.delete(0, END)
    e_price.delete(0, END)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), price_text.get())
    list_box.delete(0, END)
    list_box.insert(END,(title_text.get(), author_text.get(), year_text.get(), price_text.get()))
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_year.delete(0, END)
    e_price.delete(0, END)


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), price_text.get())
    view_command()

def mass_insert():
    pass

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


# Labels and entries
l_title = Label(main_win, text = "Title")
l_title.grid(row = 0, column = 0)
title_text = StringVar()
e_title = Entry(main_win, textvariable = title_text)
e_title.grid(row = 0, column = 1)

l_author = Label(main_win, text = "Author")
l_author.grid(row = 0, column = 2)
author_text = StringVar()
e_author = Entry(main_win, textvariable = author_text)
e_author.grid(row = 0, column = 3)


l_year = Label(main_win, text = "Year")
l_year.grid(row = 1, column = 0)
year_text = StringVar()
e_year = Entry(main_win, textvariable = year_text)
e_year.grid(row = 1, column = 1)

l_price = Label(main_win, text = "Price")
l_price.grid(row = 1, column = 2)
price_text = StringVar()
e_price = Entry(main_win, textvariable = price_text)
e_price.grid(row = 1, column = 3)



# List box
list_box = Listbox(main_win, height = 8, width = 55)
list_box.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
list_box.bind("<<ListboxSelect>>", get_selected_row)


# buttons
b_view = Button(main_win, text = "View all", width = 10, command = view_command)
b_view.grid(row = 2, column = 3)

b_search = Button(main_win, text = "Search", width = 10, command = search_command)
b_search.grid(row = 3, column = 3)

b_add = Button(main_win, text = "Add", width = 10, command = add_command)
b_add.grid(row = 4, column = 3)

b_update = Button(main_win, text = "Update", width = 10, command = update_command)
b_update.grid(row = 5, column = 3)

b_delete = Button(main_win, text = "Delete", width = 10, command = delete_command)
b_delete.grid(row = 6, column = 3)

b_exit = Button(main_win, text = "Exit", width = 10, command = main_win.destroy)
b_exit.grid(row = 7, column = 3)


#main loop
main_win.mainloop()
