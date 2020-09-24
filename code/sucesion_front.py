import sucesion_back
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox as alerta

class mainHolder:
    def __init__(self):
        self.root = Tk()
        self.root.iconphoto(True,PhotoImage(file='logo.png'))
        self.root.title("FCC Toolkit - Sucesiones")
        self.root.configure(background="white")
        self.root.minsize(1110,475)
        self.root.resizable(False,False)

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
        self.volver.pack(side="left",padx=(1,100))

        self.lim_sup = tk.Label(self.input_frame,text="Límite superior",font=("Segoe UI",15),bg="white")
        self.input_box_sup = Entry(self.input_frame,width=10)
        self.lim_sup.pack(side="left",padx=(1,8))
        self.input_box_sup.pack(side="left",padx=(1,30),pady=(5,1))

        self.lim_inf = tk.Label(self.input_frame,text="Límite inferior",font=("Segoe UI",15),bg="white")
        self.input_box_inf = Entry(self.input_frame,width=10)
        self.lim_inf.pack(side="left",padx=(1,5))
        self.input_box_inf.pack(side="left",padx=(1,30),pady=(5,1))

        self.formula = tk.Label(self.input_frame,text="Fórmula (k)",font=("Segoe UI",15),bg="white")
        self.input_box_form = Entry(self.input_frame,width=10)
        self.formula.pack(side="left",padx=(1,5))
        self.input_box_form.pack(side="left",padx=(1,30),pady=(5,1))

        self.generar = Button(self.input_frame,text="Generar",command = self.deploy,style="my.TButton")
        self.generar.pack(side="right")

    def show_results(self):
        if(self.contents_created):
            self.res_frame.destroy()
            self.sum_result.destroy()
        
        self.sum_result = tk.Frame(self.root,bg="white")
        self.sum_result.pack(anchor="s",fill="x")

        text_result = "Suma = " + str(self.list_pos[1])
        result_label = tk.Label(self.sum_result,text=text_result,font=("Segoe UI",30),bg="white")
        result_label.pack()
        
        self.res_frame = tk.Frame(self.root,bg="white")
        self.res_frame.pack(anchor="w",fill="both")
        scroll = tk.Scrollbar(self.res_frame)
        scroll.pack(side="right",fill="y")
        self.contents_created = True

        list_holder = tk.Listbox(self.res_frame,height=20,bd=0,highlightthickness=0,font=("Segoe UI",10))
        for i in range(len(self.list_pos[0])):
            current_text = "Término " + self.list_pos[0][i][0] + " " + ("%.3f" % self.list_pos[0][i][1])
            list_holder.insert("end",current_text)
        list_holder.pack()
        
        if(len(self.list_pos[0]) <= 20):
            scroll.destroy()
        else:
            scroll.config(command=list_holder.yview)

    def deploy(self):
        ls = self.input_box_sup.get()
        li = self.input_box_inf.get()
        f = self.input_box_form.get()
        params = sucesion_back.sintax(li,ls,f)
        if(params == 8):
            alerta.showwarning("Límites iguales","Los límites son iguales, corrígelos por favor")
        elif(params == 0):
            alerta.showerror("Error en límites","Existe un error en los límites, corrígelos por favor")
        else:
            li, ls, f = params
            self.list_pos = sucesion_back.exec_rec(li,ls,f)
            if(self.list_pos == 0):
                alerta.showerror("División incorrecta","Ha ocurrido una división entre 0, revisa tus entradas")
            elif(self.list_pos == 1):
                alerta.showerror("Error en cálculo","Ha ocurrido un error, revisa tus entradas")
            else:
                self.show_results()

    def build(self):
        self.top_section()
        self.root.mainloop()

if __name__ == "__main__":
    import indebido

