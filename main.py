import tkinter as tk
import time
import sys
from pet import Virtual_Pet
default_name='Alb'
destroyed=False
def save_name(entry,frame,root):
    global default_name
    name=entry.get()
    default_name=name
    frame.destroy()
    updated_name=tk.Label(root,text=f"{default_name}")
    updated_name.pack()
    root.after(2000,updated_name.destroy)
    root.after(2000,lambda:create_pet(root))
    
    

def pet_config(root):
    frame=tk.Frame(root)
    frame.pack()
    greet=tk.Label(frame,text="Create Your Own pet")
    greet.pack()
    pet_name=tk.Entry(frame,text='Pet Name')
    pet_name.pack(anchor='center')
    pet_name.bind("<Return>",lambda event: save_name(pet_name,frame,root))
    submit_name=tk.Button(frame,text='Save',command=lambda:save_name(pet_name,frame,root))
    submit_name.pack()
    
def create_pet(root):
    frame=tk.Frame(root)
    frame.pack()
    greet=tk.Label(frame,text=f"{default_name}",background='#ffc0cb')
    greet.pack()
    v_pet=Virtual_Pet(default_name)
    canva=tk.Canvas(root,width=300,height=300)
    canva.create_oval(100,50,200,200,fill="#5ccd40",outline="")
    canva.create_oval(130,195,140,220,fill="#3ec81b",outline="")
    canva.create_oval(160,195,170,220,fill="#3ec81b",outline="")
    canva.create_oval(90,110,100,150,fill="#3ec81b",outline="")
    canva.create_oval(200,110,210,150,fill="#3ec81b",outline="")
    canva.create_oval(125,75,135,85,fill="#2874a6",outline="")
    canva.create_oval(165,75,175,85,fill="#2874a6",outline="")
    canva.create_oval(125,95,175,105,fill="#f0fa4e",outline="")
    canva.create_oval(125,106,175,116,fill="#f0fa4e",outline="")
    canva.pack()
    hunger_label=tk.Label(frame,text=f'Hunger: {v_pet.hunger}',background="#ffc0cb")
    hunger_label.pack()
    
    
    
def display_window():
    w=tk.Tk()
    w.config(bg='#ffc0cb')
    w.title('My Baby Pet')
    w.geometry('400x400')
    pet_config(w)
    w.mainloop()
    
def main():
    display_window()
    
if __name__=='__main__':
    main()