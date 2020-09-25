import relacion_back
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as alerta

class mainHolder:
    def __init__(self):
        self.root = Tk()
        self.root.iconphoto(True,PhotoImage(file='img/logo.png'))
        self.root.title("FCC Toolkit - Relación")
        self.root.configure(background="white")
        self.root.minsize(1110,500)
        self.root.resizable(False,False)

        self.ejemplo = [(0,0),(0,1),(0,3),(1,0),(1,1),(2,2),(3,0),(3,3)]

        self.contents_created = False

    def back(self):
        import menu_btn
        self.root.destroy()
        get_back = menu_btn.mainHolder()

    def top_section(self):
        self.input_frame = tk.Frame(self.root,bg="white")
        self.input_frame.pack(anchor="nw",fill="x")

        self.btn_style = Style()
        self.btn_style.configure("my.TButton",font=("Segoe UI",15))

        self.volver = Button(self.input_frame,text="Volver",command = self.back,style="my.TButton")
        self.volver.pack(side="left",padx=(1,20))

        self.rel_text = tk.Label(self.input_frame,text="Ingresa el conjunto",font=("Segoe UI",15),bg="white")
        self.rel_input = Entry(self.input_frame,width=100)
        self.rel_input.insert(0,"{}")
        self.rel_text.pack(side="left",padx=(1,8))
        self.rel_input.pack(side="left",padx=(1,30),pady=(5,1))

        self.generar = Button(self.input_frame,text="Obtener propiedades",command = self.deploy,style="my.TButton")
        self.generar.pack(side="right")

    def show_results(self):
        if(self.contents_created):
            self.res_frame.destroy()
        props = relacion_back.relaciones(self.pares)        
        self.res_frame = tk.Frame(self.root,bg="white")
        self.res_frame.pack(anchor="w",fill="both",pady=(50,1))
        self.contents_created = True

        formated_dom = "{"
        for i in range(len(props.dominio)-1):
            formated_dom += str(props.dominio[i])
            formated_dom += ","
        else:
            formated_dom += str(props.dominio[i+1])
            formated_dom += "}"

        formated_ran = "{"
        for i in range(len(props.rango)-1):
            formated_ran += str(props.rango[i])
            formated_ran += ","
        else:
            formated_ran += str(props.rango[i+1])
            formated_ran += "}"

        text_elems = ["Reflexiva: ","Simétrica: ","Transitiva: ","Dominio: ","Codominio: ","Inyectiva: ","Sobreyectiva: ","Biyectiva: ","Es función: "]
        prop_funcs = [props.checkReflex,props.checkSimt,props.checkTran,formated_dom,formated_ran,props.checkInyec,props.checkSobre,props.checkBiy,props.checkFunc]
        properties_holder = []
        for i in range(len(text_elems)):
            current_text = text_elems[i] + (("Si" if(prop_funcs[i]()) else "No") if(i in range(3) or i in range(5,9)) else str(prop_funcs[i]))
            properties_holder.append(tk.Label(self.res_frame,text=current_text,font=("Segoe UI",20),bg="white"))
            properties_holder[i].pack()

    def deploy(self):
        if(self.rel_input.get() == "ejemplo"):
            self.rel_input.delete(0,"end")
            self.rel_input.insert(0,str(self.ejemplo))
            self.rel_input.delete(0,1)
            self.rel_input.delete(len(self.rel_input.get())-1,"end")
            self.pares = self.ejemplo
            self.show_results()
        else:
            self.pares = relacion_back.purgar(self.rel_input.get())
            if(type(self.pares) == int):
                alerta.showerror("Error en entrada","Verífica tu entrada (paréntesis o llaves complet@s, sin espacios)")
            else:
                self.show_results()

    def build(self):
        self.top_section()
        self.root.mainloop()

if __name__ == "__main__":
    import indebido
    '''cola = mainHolder()
    cola.build()'''
