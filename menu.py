from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

venMain = Tk()
venMain.title("Proyecto 1, Luis Castro, 202109750")
venMain.geometry("600x375")
venMain.config(bg = "#1e272e")
venMain.resizable(False, False)

frameArchivo = Frame(venMain, bg="#00cec9", borderwidth=2, relief="ridge") ##00cec9 #00d8d6 ##1abc9c ##2ed573
frameArchivo.place(x=0, y=0, width=300, height=400) #frameArchivo.grid(row = 0, column = 0)

labelArchivo = Label(frameArchivo, bg="#006266", text="Archivo", width=50, height=1, fg="white", font=("Arial", 20, "bold"))
labelArchivo.pack() ##81ecec #006266 #2ecc71

def abrirArchivo():
    pass

def guardarComo():
    pass

btnSaveAs = Button(frameArchivo, font=("Arial", 12), text="Guardar como", width=20, bg ="#dfe4ea", command=guardarComo)
btnSaveAs.place(x=50, y= 160)

btnOpen = Button(frameArchivo, font=("Arial", 12), text="Abrir", width=20, bg ="#dfe4ea", command=abrirArchivo)
btnOpen.place(x=50, y= 60)

btnSave = Button(frameArchivo, font=("Arial", 12), text="Guardar", width=20, bg ="#dfe4ea")
btnSave.place(x=50, y= 110)

def lizador():
    pass

btnAnalize = Button(frameArchivo, font=("Arial", 12), text="Analizar", width=20, bg ="#dfe4ea", command= lizador)
btnAnalize.place(x=50, y= 210)

btnError = Button(frameArchivo, font=("Arial", 12), text="Errores", width=20, bg ="#dfe4ea")
btnError.place(x=50, y= 260)

def salir():
    venMain.destroy()

btnExit = Button(frameArchivo, font=("Arial", 12), text="Salir", width=20, command=salir, bg ="#dfe4ea")
btnExit.place(x=50, y= 310)

frameAyuda = Frame(venMain, bg="#e67e22", borderwidth=2, relief="ridge") #ff5e57 
frameAyuda.place(x=300, y=0, width=300, height=400)

labelArchivo = Label(frameAyuda, bg="#d35400", text="Ayuda", width=50, height=1, fg="white", font=("Arial", 20, "bold")) ##e67e22, #ff3f34,
labelArchivo.pack()

def abrirManualUsuario():
    busquedaArchivo = filedialog.askopenfile(title="Selecciona un documento pdf", filetypes=[("Documentos pdf", "*.pdf")])
    webbrowser.open_new(busquedaArchivo)

btnUserMan = Button(frameAyuda, font=("Arial", 12), text="Manual de usuario", width=20, bg ="#dfe4ea", command=abrirManualUsuario)
btnUserMan.place(x=50, y= 60)

btnTecnicMan = Button(frameAyuda, font=("Arial", 12), text="Manual técnico", width=20, bg ="#dfe4ea", command=abrirManualUsuario)
btnTecnicMan.place(x=50, y= 110)

def ayuda():
    nventana = Toplevel(venMain)
    nventana.title("Informacion personal")
    nventana.geometry("400x200")
    nventana.config(bg = "#44bd32")
    nventana.resizable(False, False)

    Label(nventana, text="Luis Antonio Castro Padilla", fg="black", font=("Arial", 12), bg="#44bd32").pack()
    Label(nventana, text="Carnet: 202109750", fg="black", font=("Arial", 12), bg="#44bd32").pack()
    Label(nventana, text="Sección: B+", fg="black", font=("Arial", 12), bg="#44bd32").pack()

    def cerrarAyuda():
        nventana.destroy()    
    
    Button(nventana, text="Cerrar", fg="white", font=("Arial", 12), bg="red", command=cerrarAyuda).pack()

btnHelptopic = Button(frameAyuda, font=("Arial", 12), text="Temas de ayuda", width=20, bg ="#dfe4ea", command=ayuda)
btnHelptopic.place(x=50, y= 160)

venMain.mainloop()
