import tkinter as tk





# Dritarja e GUI
master = tk.Tk()
master.title("Automatic SQL Injection Test")
master.configure(bg='#8dabba')
master.geometry('450x150')
# Madhesia e kufizuar e dritares
master.resizable(0, 0)

url = tk.StringVar(master)
# Label e instruksionit
tk.Label(master, fg="#1d2122", bg="#8dabba", font=(None, 13),
         text="Give the url of the website that you want to test:").grid(row=0, column=1, padx=(5, 0), pady=(20, 0))
# Gjatesia e hapesires per vendojen e url-es
e1 = tk.Entry(master, width=52, textvariable=url)
e1.grid(row=1, column=1, padx=(0, 3), pady=(10, 0))

# Butoni CHECK
tk.Button(master, fg="#ffffff", bg="#253c5a", width=12, font=(None, 13), text="TEST", command=check_injection).grid(
    row=2, column=1, padx=(0, 190), pady=(15, 0))
# Butoni CLEAR
tk.Button(master, fg="#ffffff", bg="#253c5a", width=12, font=(None, 13), text="CLEAR", command=clear_clicked).grid(
    row=2, column=1, padx=(190, 0), pady=(15, 0))

master.mainloop()
