import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font

import io
import os

class MsgBox(Toplevel):
    def __init__(self, title=" ", message=" "):
        Toplevel.__init__(self)

        self.title(title)
        
        self.font = font.Font(size=12, family="Verdana")
        self.label = Label(self, text=message, font = self.font, justify=tk.LEFT)
        self.label["bg"] = "white"
        self.label.pack(ipadx=50, ipady=10, fill="both", expand=True)

        self.button = Button(self, text="Close")
        self.button["command"] = self.destroy
        self.button.pack(pady=10, padx=10, ipadx=20, side="left")


class mainAppWin():
    def __init__(self, MsgBox):
 
        self.window = tk.Tk()
        self.window.geometry("580x545") 
        self.window.title("Menú Codigo Secreto")
        self.xRes = self.window.winfo_screenwidth()
        self.yRes = self.window.winfo_screenheight()

        self.dir = "./data/icon.png"
        self.imgicon = tk.PhotoImage(file=self.dir)
        self.window.tk.call("wm", "iconphoto", self.window._w, self.imgicon) 

        self.mails = []
        self.list_words = io.open("./data/palabras.txt", mode="r", encoding="utf-8")
        self.words = self.list_words.read().split('\n')
        self.tam = len(self.words) - 1

        self.font = font.Font(size=12, family="Verdana")

        self.lbl = tk.Label(self.window, text="Palabras")
        self.lbl.place(x=70, y=30)
        self.lbl.config(font=("Verdana",18,"bold"))        
        
        self.text = ["Si deseas añadir más palabras a la lista del juego escribe lo que",
                     "quieras incorporar en el siguiete recuadro y pulsa el botón."]
        self.y = 80

        for Text in self.text:
            self.Text = tk.Label(self.window, text = Text)
            self.Text.place(x=55, y=self.y)
            self.Text.config(font=("Verdana",11))
            self.y += 22

        self.txtAdd = tk.Entry(self.window,width=32)
        self.txtAdd.place(x=60, y=143)
        self.txtAdd.config(font=("Verdana",11)) 
        
        self.btnAdd = tk.Button(self.window, text="Añadir", bg="#F5DEB3", command=self.add, width = 13) 
        self.btnAdd.place(x=400, y=138)
        self.btnAdd.config(font=("Verdana",11))



        self.lbl = tk.Label(self.window, text="Correos")
        self.lbl.place(x=70, y=200)
        self.lbl.config(font=("Verdana",18,"bold"))

        self.text = ["Escribe tu dirección de correo en el siguiente recuadro y dale al",
                     "botón 'Incluir', introduce  tantos  correos como jefes espías. Si",
                     "quieres ver los correo que ya has están añadidos dale al botón",
                     "'Ver Correos' y si te has equivocado, dale al botón 'Eliminar'.",
                     "Finalmente para  que se os haga llegar el patrón del juego dale",
                     "al botón 'Comenzar Juego'."]
        self.y = 250

        for Text in self.text:
            self.lblText = tk.Label(self.window, text=Text)
            self.lblText.place(x=55, y=self.y)
            self.lblText.config(font=("Verdana",11))
            self.y += 22      
            
        self.txt = tk.Entry(self.window,width=32)
        self.txt.place(x=60, y=403)
        self.txt.config(font=("Verdana",11))

        self.btnIncluir = tk.Button(self.window, text="Incluir", bg="#F5DEB3", command=self.incluir, width = 13) 
        self.btnIncluir.place(x=400, y=398)
        self.btnIncluir.config(font=("Verdana",11))
        
        self.btnVer = tk.Button(self.window, text="Ver Correos", bg="#F5DEB3", command=self.ver, width = 14) 
        self.btnVer.place(x=60, y=450)
        self.btnVer.config(font=("Verdana",11))

        self.btnIncluir = tk.Button(self.window, text="Eliminar", bg="#F5DEB3", command=self.eliminar, width = 14) 
        self.btnIncluir.place(x=212, y=450)
        self.btnIncluir.config(font=("Verdana",11))

        self.btnEnviar = tk.Button(self.window, text="Comenzar Juego", bg="red", fg="white", command=self.enviar, width = 17) 
        self.btnEnviar.place(x=365, y=450)
        self.btnEnviar.config(font=("Verdana",11))


        self.menubar = Menu(self.window)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Salir", command=self.exit)
        self.menubar.add_cascade(label="Configuración", menu=self.filemenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Información", command=self.about)
        self.menubar.add_cascade(label="Creador", menu=self.helpmenu)

        self.window.config(menu=self.menubar)
                
        self.window.mainloop()
        

    def exit(self):
        self.window.destroy()


    def about(self):
        message = """
        Este   juego   está   programado   por  Javier  Sebastián
        Fernández, este es la versión virtual del conocido  juego
        de mesa Código Secreto.  Está  creado  para  entretener 
        y disfrutar de nuestra capacidad de pensar.

        Este  no  busca ningún beneficio monetario, es  gratuito
        y de libre difusión. 

        Por  otro  lado, se  espera que  se valore  el trabajo y el 
        esfuerzo  existente  por  detrás  para  que  el  juego sea 
        completamente funcional. Por ello se agradeze cualquier
        tipo de  propuesta o crítica  para su mejora, para  ello el 
        correo de contacto del creador es:

                             - javi.sebas@hotmail.es -

        Cualquier mensaje será bienvenido. Gracias por disfrutar
        del juego.
        """
        msg = MsgBox("Information", message)


    def eliminar(self):
        decision = messagebox.askyesno(message="¿Está seguro de añadir \neliminar los correo ?" 
                               , title="Eliminar Correos")
        if decision:
            self.mails = []


    def ver(self):
        global MsgBox

        message = ""
        counter = 1
        if len(self.mails) == 0:
            message = "Ningún correo ha sido incluido"
        else:
            for mail in self.mails: # 
                message += ("\n"+str(counter)+".  "+mail) 
                counter += 1
            
        msg = MsgBox("Attached files", message) 


    def add(self):

        nueva = messagebox.askyesno(message="¿Está seguro de añadir \nla palabra '"+self.txtAdd.get()+"'?" 
                               , title="Nueva palabra")
        if nueva:
            if self.txtAdd.get() in self.words:
                messagebox.showinfo(message="Esta palabra ya existe", title="Mensaje de advertencia")
            else:
                listaEscribe = open('./data/palabras.txt', mode="a+", encoding="utf-8")
                listaEscribe.write(self.txtAdd.get())
                listaEscribe.close()  

        self.txtAdd.delete(0, "end")
        

    def incluir(self):

        if self.txt.get() != "":
            if self.txt.get() not in self.mails:

                self.mails.append(self.txt.get())
                self.txt.delete(0, "end")

            else:
                messagebox.showinfo(message="El correo ya ha sido \nincluido posteriormente", title="Mensaje de advertencia")
                self.txt.delete(0, "end")
        else:
            messagebox.showinfo(message="El correo introducido no es válido", title="Mensaje de advertencia")


    def enviar(self):
        if len(self.mails) == 0:
            messagebox.showinfo(message="Necesita incluir algún \ncorreo para poder enviar", title="Mensaje de advertencia")
        else:
            messagebox.showinfo(message="A jugar!", title="Mensaje de advertencia")
            self.window.destroy()

