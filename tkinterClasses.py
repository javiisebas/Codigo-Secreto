import tkinter as tk
from tkinter import messagebox

import io
import os


class mainAppWin():
    def __init__(self):
 
        self.window = tk.Tk()
        self.window.geometry('479x490') 
        self.window.title('Menú Codigo Secreto')
        self.xRes = self.window.winfo_screenwidth()
        self.yRes = self.window.winfo_screenheight()

        self.dir = 'icon.png'
        self.imgicon = tk.PhotoImage(file=self.dir)
        self.window.tk.call('wm', 'iconphoto', self.window._w, self.imgicon) 

        self.mails = []
        self.list_words = io.open('palabras.txt', mode="r", encoding="utf-8")
        self.words = self.list_words.read().split('\n')
        self.tam = len(self.words) - 1

        self.lbl = tk.Label(self.window, text="Correos")
        self.lbl.place(x=50, y=20)
        self.lbl.config(font=("Verdana",18,"bold"))

        self.text = ["Escribe  tu correo en  el siguiente recuadro y dale",
                      "a INCLUIR. Introduce  tantos correos como jefes ",
                      "espías, y cuando hayas terminado dale a ENVIAR ",
                      "y se os hará llegar el patrón del juego. "]
        self.y = 75

        for Text in self.text:
            self.lblText = tk.Label(self.window, text=Text)
            self.lblText.place(x=50, y=self.y)
            self.lblText.config(font=("Verdana",11))
            self.y += 20
        
        self.lbl = tk.Label(self.window, text="Palabras")
        self.lbl.place(x=50, y=255)
        self.lbl.config(font=("Verdana",18,"bold"))        
        
        self.text = ["Si deseas añadir más palabra a la lista del juego.",
                    "Escribe la palabra en el siguiete recuadro y pulsa",
                    "el botón de añadir:"]
        self.y = 310

        for Text in self.text:
            self.Text = tk.Label(self.window, text = Text)
            self.Text.place(x=50, y=self.y)
            self.Text.config(font=("Verdana",11))
            self.y += 20

        self.txtAdd = tk.Entry(self.window,width=37)
        self.txtAdd.place(x=52, y=385)
        self.txtAdd.config(font=("Verdana",11)) 
        
        self.btnAdd = tk.Button(self.window, text="Añadir", command=self.add, width = 40) 
        self.btnAdd.place(x=53, y=425)
        self.btnAdd.config(font=("Verdana",11))
        
            
        self.txt = tk.Entry(self.window,width=36)
        self.txt.place(x=52, y=165)
        self.txt.config(font=("Verdana",11))
        
        self.btnEnviar = tk.Button(self.window, text="Enviar", command=self.enviar, width = 17) 
        self.btnEnviar.place(x=51, y=205)
        self.btnEnviar.config(font=("Verdana",11))

        self.btnIncluir = tk.Button(self.window, text="Incluir", command=self.incluir, width = 17) 
        self.btnIncluir.place(x=252, y=205)
        self.btnIncluir.config(font=("Verdana",11))
        
        self.window.mainloop()
        

    def add(self):

        nueva = messagebox.askyesno(message="¿Está seguro de añadir \nla palabra '"+self.txtAdd.get()+"'?" 
                               , title="Nueva palabra")
        if nueva:
            if self.txtAdd.get() in self.words:
                messagebox.showinfo(message="Esta palabra ya existe", title="Mensaje de advertencia")
            else:
                listaEscribe = open('palabras.txt', mode="a+", encoding="utf-8")
                listaEscribe.write(self.txtAdd.get())
                listaEscribe.close()  

        self.txtAdd.delete(0, 'end')
        

    def incluir(self):

        if self.txt.get() != "":
            self.mails.append(self.txt.get())
            self.txt.delete(0, 'end')


    def enviar(self):
        if len(self.mails) == 0:
            messagebox.showinfo(message="Necesita incluir algún \ncorreo para poder enviar", title="Mensaje de advertencia")
        else:
            messagebox.showinfo(message="A jugar!", title="Mensaje de advertencia")
            self.window.destroy()

