import conteo_back
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as alerta

class mainHolder:
    def __init__(self):
        self.root = Tk()
        self.root.iconphoto(True,PhotoImage(file='img/logo.png'))
        self.root.title("FCC Toolkit - Métodos de conteo")
        self.root.configure(background="white")
        self.root.minsize(700,300)
        self.root.resizable(False,False)

        self.var_perm = None
        self.contents_created = False

    def back(self):
        import menu_btn
        self.root.destroy()
        get_back = menu_btn.mainHolder()

    def get_opcion(self):
        print(self.var_perm.get())

    def ShowChoice(self):
        def mensaje(mod):
            error_header = "Error en entradas"

            if(mod == 0):
                alerta.showerror("Valores vacíos","Introduce los valores correspondientes.")
            elif(mod == 1):
                alerta.showinfo("Repeteciones","Para trabajar con números ingresa una lista separada por comas.\nPara trabajar con letras, ingresa una palabra.")
            elif(mod == -1):
                alerta.showerror(error_header,"Hay un problema con las entradas, verifícalas.")
            elif(mod == -2):
                alerta.showerror(error_header,"Los valores ingresados no son válidos, intenta de nuevo.")
            elif(mod == -3):
                alerta.showerror(error_header,"r es mayor que n, intenta de nuevo.")
            elif(mod == -5):
                alerta.showinfo("Entradas insuficientes","Longitud de entrada insuficiente, intenta agregar más elementos.")
            else:
                alerta.showerror("Error desconocido","Un error desconocido ha ocurrido, intenta de nuevo.")

        if(self.contents_created):
            self.res_frame.destroy()
        self.res_frame = tk.Frame(self.root,bg="white")
        self.res_frame.pack(anchor="w",fill="both",pady=(20,1))
        self.contents_created = True

        eleccion = self.var_perm.get()
        helper = conteo_back.conteo(1)

        if(eleccion != 1 and eleccion != 4):
            self.r.delete(0,"end")
            self.r.config(state="disabled")
            
            if(eleccion == 0):
                if(len(self.n.get()) == 0):
                    mensaje(0)
                else:
                    dato = conteo_back.purgar(0,self.n.get(),None)

                    if(dato < 0):
                        mensaje(dato)
                    else:
                        n_label = helper.p_forms[0].format("n","n","n")
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
                        n = helper.alt_factorial(dato,dato)
                        
                        n_label = helper.p_forms[0].format(self.n.get(),self.n.get(),self.n.get()) + " = " + str(n)
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
            if(eleccion == 2):
                if(len(self.n.get()) == 0):
                    mensaje(0)
                else:
                    dato = conteo_back.purgar(2,self.n.get(),None)
                    
                    if(dato < 0):
                        mensaje(dato)
                    else:
                        n_label = helper.p_forms[2].format("n")
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
                        n = helper.alt_factorial(dato,dato)
                        n_label = helper.p_forms[2].format(self.n.get(),self.n.get(),self.n.get()) + " = " + str(n)
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
            elif(eleccion == 3):
                mensaje(1)
                if(len(self.n.get()) == 0):
                    mensaje(0)
                else:
                    datos = conteo_back.purgar(3,self.n.get(),None)
                    
                    if(type(datos) != tuple):
                        mensaje(datos)
                    else:
                        h_n, h_r, modo = datos

                        n_label = helper.p_forms[3].format("n","n1","nk")
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()

                        holder, n = helper.d_rep(h_n,h_r)
                        n_holder = holder
                        elems_text = ""
                        for key,val in n_holder.items():
                            if(modo == 0):
                                elems_text = elems_text + "C{}: {};  ".format(key,val)
                            else:
                                elems_text = elems_text + "{}: {};  ".format(key,val)
                        holder = list(holder.keys())
                        
                        tk.Label(self.res_frame,text=elems_text[:-3],font=("Segoe UI",25),bg="white").pack()
                        n_label = helper.p_forms[3].format(h_n,"k"+holder[0],"k"+holder[-1]) + " = " + str(int(n))
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()


        else:
            self.n.config(state="enabled")
            self.r.config(state="enabled")

            if(len(self.n.get()) == 0 or len(self.r.get()) == 0):
                mensaje(0)
            else:
                datos = conteo_back.purgar(eleccion,self.n.get(),self.r.get())

                if(type(datos) != tuple):
                    mensaje(datos)
                else:
                    h_n,h_r = datos

                    n_label = helper.p_forms[1].format("n","r","n","n","r") if(eleccion == 1) else helper.c_form.format("n","r","n","r","n","r")
                    tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
                    n = helper.alt_factorial(h_n,h_r)
                    n = n if(eleccion == 1) else int(n/helper.alt_factorial(h_r,h_r))

                    if(eleccion == 1):
                        n_label = helper.p_forms[-1].format("n","r","n","n-1","n-r+1") + " = " + helper.p_forms[-1].format(h_n,h_r,h_n,h_n-1,h_n-h_r+1)
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
                    else:
                        n_label = helper.unnecesary_1.format("n","r","n","n-1","n-r+1","r") + " = " + helper.unnecesary_1.format(h_n,h_r,h_n,h_n-1,h_n-h_r+1,h_r)
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()
                        n_label = helper.c_form.format("n","n-r","n","(n-r)","n","(n-r)") + " = " + helper.c_form[:8].format(h_n,"{}-{}".format(h_n,h_r)) + " = " + helper.c_form.format(h_n,h_n-h_r,h_n,h_n-h_r,h_n,h_n-h_r)
                        tk.Label(self.res_frame,text=n_label,font=("Segoe UI",23),bg="white").pack()

                    n_label = helper.p_forms[1].format(h_n,h_r,h_n,h_n,h_r) if(eleccion == 1) else helper.c_form.format(h_n,h_r,h_n,h_r,h_n,h_r)
                    n_label = n_label + " = " + str(n)
                    tk.Label(self.res_frame,text=n_label,font=("Segoe UI",25),bg="white").pack()

    def top_section(self):
        def enable_back(event):
            self.r.config(state="enabled")

        self.input_frame = tk.Frame(self.root,bg="white")
        self.input_frame.pack(anchor="nw",fill="x")

        self.btn_style = Style()
        self.btn_style.configure("my.TButton",font=("Segoe UI",15))

        self.volver = Button(self.input_frame,text="Volver",command = self.back,style="my.TButton")
        self.volver.pack(side="left")

        self.input_params = tk.Frame(self.input_frame,bg="white")
        self.input_params.pack(side="left")
        self.n_text = tk.Label(self.input_params,text="n =",font=("Segoe UI",15),bg="white")
        self.n = Entry(self.input_params,width=18)
        self.r_text = tk.Label(self.input_params,text="r =",font=("Segoe UI",15),bg="white")
        self.r = Entry(self.input_params,width=18)
        self.n_text.pack(side="left",padx=(10,1))
        self.n.pack(side="left",pady=(10,1))
        self.r_text.pack(side="left",padx=(10,1))
        self.r.pack(side="left",pady=(10,1),padx=(1,10))
        self.r.bind("<Button-1>",enable_back)

        self.perm_frame = tk.LabelFrame(self.input_frame,bg="white",text="Métodos de conteo")
        self.perm_frame.pack(side="left",padx=(1,10)) 
        self.var_perm = tk.IntVar()
        self.var_perm.set(1)

        perm_texts = ["Todos los elementos","Subconjunto","Circular","Elementos repetidos","Combinación"]
        for val, ctext in enumerate(perm_texts):
            tk.Radiobutton(self.perm_frame,text=ctext,variable=self.var_perm,command=self.ShowChoice,value=val,bg="white").pack(side="left")

    def build(self):
        self.top_section()
        self.root.mainloop()

if __name__ == "__main__":
    import indebido
