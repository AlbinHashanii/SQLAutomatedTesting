import tkinter as tk
from tkinter import Label, Button, messagebox
import requests
import penetrationTesting as p
import re
import unittest

regex = re.compile(
    r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)



# Funksioni per skanimin e website
def give_result(url):
    if p.scan_sql_injection(url):
        return 'This website is vulnerable.'
    else:
        return 'This website is not vulnerable.'
    
    
# Funksioni i butonit TEST
def check_injection():
    if not (url.get().startswith("http://") or url.get().startswith("https://")):
        messagebox.showinfo("Result", "The url should start with http:// or https. Please try again?")
    elif verify_url(url.get()):
        messagebox.showinfo("Result", give_result(url.get()))
    else:
        messagebox.showerror("Result", "You have written an invalid url.")
        
# Funksioni per verifikimin e url
def verify_url(url):
    return re.match(regex, url) is not None



# Funksioni i butonit CLEAR
def clear_clicked():
    e1.delete(0, 'end'





# Dritarja e GUI
master = tk.Tk()
master.title("Automated SQL Injection Testing")
master.configure(bg='#34495e')
master.geometry('550x200')
# Madhesia e kufizuar e dritares
master.resizable(0, 0)
Font_tuple = ("Courier New", 13)

url = tk.StringVar(master)
tk.Label(master, fg="#000", font=Font_tuple,
         text="Give the url of the website that you want to test:").grid(row=0, column=1, padx=(5, 0), pady=(20, 0))
# Gjatesia e hapesires per vendojen e url-es
e1 = tk.Entry(master, width=52, textvariable=url,font=Font_tuple)
e1.grid(row=1, column=1, padx=(3, 3), pady=(10, 20))

# Butoni CHECK
tk.Button(master, fg="#000", bg="#a6acaf", width=12, font=Font_tuple, text="TEST", command=check_injection).grid(
    row=2, column=1, padx=(0, 190), pady=(15, 0))
# Butoni CLEAR
tk.Button(master, fg="#000", bg="#a6acaf", width=12, font=Font_tuple, text="CLEAR", command=clear_clicked).grid(
    row=2, column=1, padx=(190, 0), pady=(15, 0))

master.mainloop()
