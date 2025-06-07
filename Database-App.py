# Define the external loop : 
import tkinter as tk
import numpy as np
from tkinter import messagebox 

name_list = []
age_list = [] 
ids_lst = []
running = True
id = 0



# ADD :
def add_function():    
    add_win = tk.Toplevel(root)
    add_win.title("Add User")
    add_win.geometry("300x200")
    name_label = tk.Label(add_win, text="Enter Name :")
    name_label.pack()
    name_entry = tk.Entry(add_win)
    name_entry.pack()
    age_label = tk.Label(add_win, text="Enter Age :")
    age_label.pack()
    age_entry = tk.Entry(add_win)
    age_entry.pack()
    def add_new_user():
        name = name_entry.get()
        age = int(age_entry.get())
        name_list.append(name)
        age_list.append(age)
        global id
        ids_lst.append(id)
        id = id + 1 
        messagebox.showinfo("User Added","Added Successfully !")
        add_win.destroy()
    submit_button = tk.Button(add_win, text="ADD USER", command=add_new_user)
    submit_button.pack(pady=10)



def Delete_Fcuntion():
    del_win = tk.Toplevel(root)
    del_win.title("Delete User")
    del_win.geometry("300x200")
    id_label = tk.Label(del_win,text="Enter ID :")
    id_label.pack(pady=10)
    id_entry = tk.Entry(del_win)
    id_entry.pack(pady=10)
    def delete_user():
        re_id = int(id_entry.get())
        item_index = -1
        for i in range(len(ids_lst)):
            if re_id == ids_lst[i]:
                item_index = i
                break
        if item_index != -1:
            name_list.pop(item_index)
            age_list.pop(item_index)
            ids_lst.pop(item_index)
        else:
            print("ID Not Found in the Database :( ")
        messagebox.showwarning("CONFIRM","Are you sure to remove this user permantently !")
        messagebox.showinfo("Status","Successfully Deleted !")
        del_win.destroy()
    del_button = tk.Button(del_win,text="DELETE",command=delete_user)
    del_button.pack(pady=10)

# DISPLAY : 
def Display_Info():
    display_win = tk.Toplevel(root)  
    display_win.title("Display User Info")
    display_win.geometry("300x200")
    ide_label = tk.Label(display_win,text="Enter ID:")
    ide_label.pack(pady=10)
    id_entry = tk.Entry(display_win)
    id_entry.pack(pady=10)
    def display_use_info():
        id_user = int(id_entry.get())
        print(type(id_user))
        name = name_list[id_user]
        age =age_list[id_user]
        messagebox.showinfo("User Information ",f"id is {id_user} ||| the Name : {name} ||| Age : {age}")
        display_win.destroy()
    dis_button = tk.Button(display_win,text="Display user info",command=display_use_info)
    dis_button.pack(pady=10)


# UPDATE : 
def upadte_data():
    update_win = tk.Toplevel(root)
    update_win.title("Update information :")
    update_win.geometry("300x200")
    choice_label = tk.Label(update_win,text="1 For Name , 2 For Age")
    choice_label.pack(pady=10)
    choice_entry = tk.Entry(update_win)
    choice_entry.pack(pady=10)
    def combine_Fn():
        user_choice = int(choice_entry.get())
        if user_choice == 1:
            update_win1= tk.Toplevel(root)
            update_win1.title("Update information :")
            update_win1.geometry("300x200")
            old_name_label = tk.Label(update_win1,text="Enter Old Name:")
            old_name_label.pack(pady=10)
            old_name_entry = tk.Entry(update_win1)
            old_name_entry.pack(pady=10)
            new_name_label = tk.Label(update_win1,text="Enter NEW Name:")
            new_name_label.pack(pady=10)
            new_name_entry = tk.Entry(update_win1)
            new_name_entry.pack(pady=10)
            def update_user_name():
                old_name = old_name_entry.get()
                new_name = new_name_entry.get()
                for i in range(len(name_list)):
                    if name_list[i] == old_name:
                        name_list[i]=new_name
                        break
                messagebox.showinfo("Status Name : ","Success")
                update_win1.destroy()
            update_button_one = tk.Button(update_win1,text="Update",command=update_user_name)
            update_button_one.pack(pady=10)
        elif user_choice == 2:
            update_win22 = tk.Toplevel(root)
            update_win22.title("Update information :")
            update_win22.geometry("300x200")
            old_age_label = tk.Label(update_win22,text="Enter Old Agw:")
            old_age_label.pack(pady=10)
            old_age_entry = tk.Entry(update_win22)
            old_age_entry.pack(pady=10)
            new_age_label = tk.Label(update_win22,text="Enter NEW Age:")
            new_age_label.pack(pady=10)
            new_age_entry = tk.Entry(update_win22)
            new_age_entry.pack(pady=10)
            def update_user_age():
                old_age = int(old_age_entry.get())
                new_age = int(new_age_entry.get())
                for j in range(len(age_list)):
                    if age_list[j] == old_age:
                        age_list[j] = new_age
                        break
                messagebox.showinfo("Status Name : ","Success")
                update_win22.destroy()
            update_button_two = tk.Button(update_win22,text="Update",command=update_user_age)
            update_button_two.pack(pady=10)
        update_win.destroy()
    choice_button = tk.Button(update_win,text="Click",command=combine_Fn)
    choice_button.pack(pady=10)
    for i in range(len(name_list)):
        print(f"ID: {ids_lst[i]}, Name: {name_list[i]}, Age: {age_list[i]}")
# Execution : 
root = tk.Tk()
root.title("DATABASE-APP")
root.geometry("400x300")
get_button = tk.Button(root, text="GET", command=Display_Info)
get_button.pack(pady=10)
add_button = tk.Button(root, text="ADD", command=add_function)
add_button.pack(pady=10)
update_button = tk.Button(root, text="UPDATE", command=upadte_data)
update_button.pack(pady=10)
delete_button = tk.Button(root, text="DELETE", command=Delete_Fcuntion)
delete_button.pack(pady=10)

root.mainloop()
