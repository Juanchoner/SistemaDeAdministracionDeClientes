from tkinter import * 
from tkinter import ttk

class Sistema(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.frame1 = Frame(master, background="black") #Title frame
        self.frame1.grid(columnspan=2, column=0, row=0)
        self.logo = PhotoImage(file="LogoGYMTres.png")
        self.frame2 = Frame(master) #Image frame
        self.frame2.grid(column=2, row=0)

        self.frameRegistro = Frame(master, bg="black")
        self.frameRegistro.grid(column=0, row=1)
        self.frameBusqueda = Frame(master, bg="black")
        self.frameBusqueda.grid(column=1, row=1)

        self.frame3 = Frame(master,  bg="black") #Fields frame
        self.frame3.grid(column=0, row=2)
        self.frame4 = Frame(master, bg="black") #Buttons CRUD frame
        self.frame4.grid(column=0, row=3)
        self.frame5 = Frame(master, bg="black") #Buttons Shear frame
        self.frame5.grid(rowspan=2, column=1, row=2)
        self.frame6 = Frame(master, bg="black")
        self.frame6.grid(column=1, row=4)

        self.nombre = StringVar()
        self.domicilo = StringVar()
        self.escolaridad = StringVar()
        self.telefono = StringVar()
        self.pago = StringVar()
        self.fecha = StringVar()
        self.observaciones = StringVar()

        self.buscar_por = StringVar()
        self.buscar_txt = StringVar()

        self.create_wietgs()
    
    def create_wietgs(self):
        Label(self.frame1, text = "TAVO'S GYM", bg='gray', fg='white', font=('Roboto', 30)).grid(column=0, row=0)
        Label(self.frame2, image=self.logo).grid(column=0, row=0, sticky="we")
        Label(self.frameRegistro, text= "Registro", bg="black", fg = "white", font=('Roboto', 20)).grid(columnspan=2, column=0, row=0)
        Label(self.frame3, text= "Nombre:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=1, pady=12)
        Label(self.frame3, text= "Domicilio:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=2, pady=12)
        Label(self.frame3, text= "Escolaridad:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=3, pady=12)
        Label(self.frame3, text= "Telefono:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=4, pady=12)
        Label(self.frame3, text= "Pago:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=5, pady=12)
        Label(self.frame3, text= "Fecha:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=6, pady=12)
        Label(self.frame3, text= "Observaciones:", bg="black", fg = "white", font=('Roboto', 15)).grid(column=0, row=7, pady=12)

        Entry(self.frame3, textvariable=self.nombre, font=('Roboto', 15)).grid(column=1, row=1, pady=12, sticky="we")
        Entry(self.frame3, textvariable=self.domicilo, font=('Roboto', 15)).grid(column=1, row=2, pady=12, sticky="we")
        Entry(self.frame3, textvariable=self.escolaridad, font=('Roboto', 15)).grid(column=1, row=3, pady=12, sticky="we")
        Entry(self.frame3, textvariable=self.telefono, font=('Roboto', 15)).grid(column=1, row=4, pady=12, sticky="we")
        comobo_pago = ttk.Combobox(self.frame3, textvariable=self.pago, width=12, height=20, font=('Roboto', 10), state='readonly')
        comobo_pago['values'] = ("Todas las disiplinas $500.00", "Pesas y cardio $480.00", "Sólo área cardio $380.00", "Sólo área de pesas $300.00", "Spinning $320.00", "Pesas y spinning $350.00", "Strong y zumba $380.00", "Pesas-Zumba-Strong $380.00")
        comobo_pago.grid(column=1, row=5, pady=12, sticky="we")
        Entry(self.frame3, textvariable=self.fecha, font=('Roboto', 15)).grid(column=1, row=6, pady=12, sticky="we")
        Entry(self.frame3, textvariable=self.observaciones, font=('Roboto', 15)).grid(column=1, row=7, pady=12, sticky="we")

        Button(self.frame4, text="Guardar", width=12, font=('Roboto', 10)).grid(column=0, row=0, padx=13, pady=12)
        Button(self.frame4, text="Actualizar", width=12, font=('Roboto', 10)).grid(column=1, row=0, padx=13, pady=12)
        Button(self.frame4, text="Eliminar", width=12, font=('Roboto', 10)).grid(column=2, row=0, padx=13, pady=12)
        Button(self.frame4, text="Limpiar campos", width=12, font=('Roboto', 10), command=self.limpiar_campos).grid(columnspan=3, column=0, row=1, padx=13, pady=12)

        Label(self.frameBusqueda, text="Buscar por:", bg="black", fg="white", font=('Roboto', 15)).grid(column=0, row=0)
        comobo_buscar = ttk.Combobox(self.frameBusqueda, textvariable=self.buscar_por, width=12, height=20, font=('Roboto', 15), state="readonly")
        comobo_buscar['values'] = ("Nombre", "Telefono", "Pago")
        comobo_buscar.grid(column=1, row=0, padx=5, sticky="we")
        Entry(self.frameBusqueda, textvariable=self.buscar_txt, font=('Roboto', 15)).grid(column=2, row=0, padx=5)
        Button(self.frameBusqueda, text="Buscar", width=12, font=('Roboto', 10)).grid(column=3, row=0, padx=5)

        self.table = ttk.Treeview(self.frame5, height=23)
        self.table.grid(column=0, row=0)

        ladox = Scrollbar(self.frame5, orient=HORIZONTAL, command=self.table.xview)
        ladox.grid(column=0, row=3, sticky="ew")
        ladoy = Scrollbar(self.frame5, orient=VERTICAL, command=self.table.yview)
        ladoy.grid(column=1, rowspan=2, row=0, sticky="ns")
        self.table.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.table['columns'] = ("Domicilio", "Escolaridad", "Telefono", "Pago", "Fecha", "Observaciones")

        self.table.column('#0', minwidth=100, width=120, anchor='center')
        self.table.column('Domicilio', minwidth=100, width=120, anchor='center')
        self.table.column('Escolaridad', minwidth=100, width=120, anchor='center')
        self.table.column('Telefono', minwidth=100, width=120, anchor='center')
        self.table.column('Pago', minwidth=100, width=120, anchor='center')
        self.table.column('Fecha', minwidth=100, width=120, anchor='center')
        self.table.column('Observaciones', minwidth=100, width=120, anchor='center')

        self.table.heading('#0', text="Nombre", anchor="center")
        self.table.heading('Domicilio', text="Domicilio", anchor="center")
        self.table.heading('Escolaridad', text="Escolaridad", anchor="center")
        self.table.heading('Telefono', text="Telefono", anchor="center")
        self.table.heading('Pago', text="Pago", anchor="center")
        self.table.heading('Fecha', text="Fecha", anchor="center")
        self.table.heading('Observaciones', text="Observaciones", anchor="center")

        Button(self.frame6, text="Mostrar clientes", width=12, font=('Roboto', 10)).grid(column=0, row=0, padx=13, pady=12)
        Button(self.frame6, text="Generar .csv", width=12, font=('Roboto', 10)).grid(column=2, row=0, padx=13, pady=12)

    def limpiar_campos(self):
        self.nombre.set('')
        self.domicilo.set('')
        self.escolaridad.set('')
        self.telefono.set('')
        self.pago.set('')
        self.fecha.set('')
        self.observaciones.set('')
        
def main():
    ventana = Tk()
    ventana.wm_title("Sistema de adminstración: TAVO'S GYM")
    ventana.config(bg='black')
    ventana.geometry('1370x700+0+0')
    ventana.resizable(0,0)
    app = Sistema(ventana)
    app.mainloop()

if __name__=="__main__":
    main()