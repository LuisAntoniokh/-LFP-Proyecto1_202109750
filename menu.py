from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from analizador import getErrores, instruccion, operar_
import webbrowser

class Pantalla_Principal():
    def __init__(self):
        self.venMain = Tk()
        self.venMain.title("Proyecto 1, Luis Castro, 202109750")
        self.venMain.geometry("600x375")
        self.venMain.config(bg = "#1e272e")
        self.venMain.resizable(False, False)
        self.pan1()
        self.venMain.mainloop()

    def pan1(self):
        self.frameArchivo = Frame(self.venMain, bg="#00cec9", borderwidth=2, relief="ridge") #frameArchivo.grid(row = 0, column = 0)
        self.frameArchivo.place(x=0, y=0, width=300, height=400)

        self.Texto = ""

        Label(self.frameArchivo, bg="#006266", text="Archivo", width=50, height=1, fg="white", font=("Arial", 20, "bold")).pack() ##81ecec #006266 #2ecc71

        Button(self.frameArchivo, font=("Arial", 12), text="Abrir", width=20, bg ="#dfe4ea", command=self.abrirArchivo).place(x=50, y= 60)

        Button(self.frameArchivo, font=("Arial", 12), text="Guardar", width=20, bg ="#dfe4ea", command=self.guardar).place(x=50, y= 110)

        Button(self.frameArchivo, font=("Arial", 12), text="Guardar como", width=20, bg ="#dfe4ea", command=self.guardarComo).place(x=50, y= 160)

        Button(self.frameArchivo, font=("Arial", 12), text="Analizar", width=20, bg ="#dfe4ea", command=self.lizador).place(x=50, y= 210)

        Button(self.frameArchivo, font=("Arial", 12), text="Errores", width=20, bg ="#dfe4ea", command=self.getErrores).place(x=50, y= 260)

        Button(self.frameArchivo, font=("Arial", 12), text="Salir", width=20, command=self.salir, bg ="#dfe4ea").place(x=50, y= 310)

        self.frameAyuda = Frame(self.venMain, bg="#e67e22", borderwidth=2, relief="ridge")
        self.frameAyuda.place(x=300, y=0, width=300, height=400)
        
        Label(self.frameAyuda, bg="#d35400", text="Ayuda", width=50, height=1, fg="white", font=("Arial", 20, "bold")).pack() ##e67e22, #ff3f34,

        Button(self.frameAyuda, font=("Arial", 12), text="Manual de usuario", width=20, bg ="#dfe4ea", command=self.abrirManualUsuario).place(x=50, y= 60)

        Button(self.frameAyuda, font=("Arial", 12), text="Manual técnico", width=20, bg ="#dfe4ea", command=self.abrirManualUsuario).place(x=50, y= 110)

        Button(self.frameAyuda, font=("Arial", 12), text="Temas de ayuda", width=20, bg ="#dfe4ea", command=self.ayuda).place(x=50, y= 160)
        
        txt_data = Text(self.frameAyuda, width=23, height= 8, name="txt_data")
        txt_data.place(x=50, y= 210)

        self.frameAyuda.mainloop()
        self.frameArchivo.mainloop()

    def abrirArchivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = filedialog.askopenfilename(title="Selecciona un documento")
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                self.filename = filename
        except Exception as e:
            print(e)
            return
        
        self.Texto = x.strip()
        #print(self.Texto)

        txt_data = self.frameAyuda.nametowidget("txt_data")
        txt_data.delete(1.0, END)
        txt_data.insert(END, self.Texto)
        
    def guardarComo(self):
        n_arch = filedialog.asksaveasfile(title="Guardar archivo como")
        if n_arch:
            txt_data = self.frameAyuda.nametowidget("txt_data")
            n_arch.write(txt_data.get('1.0', 'end-1c')) 
            n_arch.close()
            
    def guardar(self):
        if self.filename:
            cont = self.frameAyuda.nametowidget("txt_data").get('1.0', END)
            with open(self.filename, 'w', encoding='utf-8') as outfile:
                outfile.write(cont)
        else:
            print("error")
        
    def lizador(self):
        instruccion(self.Texto)
        respuestas = operar_()
        for respuesta in respuestas:
            print(respuesta.operar(None))

    def getErrores(self):
        lista_errores = getErrores()
        contador = 1
        with open('ERRORES_202109750.txt', 'w') as outfile:
            outfile.write('{\n')
            while lista_errores:
                error = lista_errores.pop(0)
                outfile.write(str(error.operar(contador)) + ',\n')
                contador +=1
            outfile.write('}')

    def salir(self):
        self.venMain.destroy()

    def abrirManualUsuario(self):
        busquedaArchivo = filedialog.askopenfile(title="Selecciona un documento pdf", filetypes=[("Documentos pdf", "*.pdf")])
        webbrowser.open_new(busquedaArchivo)

    def ayuda(self):
        self.nventana = Toplevel(self.venMain)
        self.nventana.title("Informacion personal")
        self.nventana.geometry("400x200")
        self.nventana.config(bg = "#44bd32")
        self.nventana.resizable(False, False)

        Label(self.nventana, text="Luis Antonio Castro Padilla", fg="black", font=("Arial", 12), bg="#44bd32").pack()
        Label(self.nventana, text="Carnet: 202109750", fg="black", font=("Arial", 12), bg="#44bd32").pack()
        Label(self.nventana, text="Sección: B+", fg="black", font=("Arial", 12), bg="#44bd32").pack()

        def cerrarAyuda():
            self.nventana.destroy()    
        
        Button(self.nventana, text="Cerrar", fg="white", font=("Arial", 12), bg="red", command=cerrarAyuda).pack()

r = Pantalla_Principal()
