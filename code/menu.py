from tkinter import *
from tkinter.ttk import *
from random import randint as rand
from string import ascii_lowercase as asc

class mainHolder:
    def __init__(self):
        self.root = Tk()

        def suc():
            import sucesion_front
            self.root.destroy()
            new_suc = sucesion_front.mainHolder()
            new_suc.build()

        def rel():
            import relacion_front
            self.root.destroy()
            new_rel = relacion_front.mainHolder()
            new_rel.build()

        def cont():
            import conteo_front
            self.root.destroy()
            new_cont = conteo_front.mainHolder()
            new_cont.build()

        _hex = "".join(map(str,range(10))) + asc[:6]
        r,g,b = _hex[rand(0,15)], _hex[rand(0,15)], _hex[rand(0,15)]
        rand_color = "#%s%s%s%s%s%s" % (r,r,g,g,b,b)
        font_color = "black" if(int(rand_color[1:],16) >= 7000000) else "white"

        self.root.title("FCC Toolkit")
        self.root.iconphoto(True,PhotoImage(file='img/logo.png'))
        self.root.configure(background=rand_color)
        self.root.minsize(1110,300)
        self.root.maxsize(1210,400)

        bienv_style = Style()
        bienv_style.configure("my.Label",foreground=font_color,font=("Segoe UI",25),background=rand_color)
        bienv = Label(self.root,text="Bienvenido al FCC Toolkit",style="my.Label")
        bienv.pack()

        btn_style = Style()
        btn_style.configure("my.TButton",font=("Segoe UI",25))
        textos = ["Sucesiones","Relaciones","Conteo"]
        funciones = [suc,rel,cont]
        botones = []
        for i in range(len(textos)):
            botones.append(Button(self.root,text=textos[i],command = funciones[i],style= "my.TButton"))
            botones[i].pack(side="left",expand=True,fill="both")

        self.root.mainloop()

if __name__ == "__main__":
    app = mainHolder()
