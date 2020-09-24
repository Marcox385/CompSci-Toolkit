class relaciones:
    def __init__(self,pares):
        self.pares = pares
        self.dominio = []
        self.rango = []

        for i,j in pares:
            if(i not in self.dominio):
                self.dominio.append(i)
                
            if(j not in self.rango):
                self.rango.append(j)
                
        self.dominio.sort()
        self.rango.sort()


    def checkReflex(self):
        self.reflexiva = True
        
        for i in self.dominio:
            if((i,i) not in self.pares):
                self.reflexiva = False
                break

        return self.reflexiva

    
    def checkSimt(self):
        self.simetria = True
        
        for i,j in self.pares:
            if((j,i) not in self.pares):
                self.simetria = False
                break

        return self.simetria


    def checkTran(self):
        self.transitiva = True
        self.pares.sort()
        h1,h2,h3 = 0,0,0
        for i in range(len(self.pares)):
            h1 = self.pares[i][0]
            h2 = self.pares[i][1]
            for j in range(len(self.pares)):
                if(self.pares[j][0] == h2):
                    h3 = self.pares[j][1]
                    if((h1,h3) not in self.pares):
                        self.transitiva = False
                        break
            if(self.transitiva == False):
                break

        return self.transitiva


    def checkFunc(self):
        self.esFuncion = True
        holder = []

        for i in self.pares:
            holder.append(i[0])
            if(holder.count(i[0]) > 1):
                self.esFuncion = False
                break            
        
        return self.esFuncion

    def checkInyec(self):
        self.inyectiva = True
        holder = []

        for i in self.pares:
            if(i[1] in holder):
                self.inyectiva = False
            else:
                holder.append(i[1])

        return self.inyectiva

    def checkSobre(self):
        self.sobreyectiva = True
        return self.sobreyectiva

    def checkBiy(self):
        self.biyectiva = True if(self.inyectiva) else False
        return self.biyectiva


def purgar(pares):
    try:
        if("(" not in pares or ")" not in pares or " " in pares):
            return 1
        matching_pairs = (pares.count("{") - pares.count("}")) + (pares.count("(") - pares.count(")"))
        if("{" in pares or "}" in pares):
            only_pair_braces = True if(pares.count("{") == 1 and pares.count("}") == 1) else False
        else:
            only_pair_braces = True
        if(matching_pairs != 0 or not only_pair_braces):
            print(matching_pairs, only_pair_braces)
            return 1
        else:
            pares = ("".join([i for i in list(pares) if(i != "{" and i != "}")])).split(",")
            pares = [(pares[i][1:],pares[i+1][:-1]) for i in range(0,len(pares),2)]
    except:
        return 1
        

    try:
        holder, h_x, h_y = [], 0, 0
        for i in pares:
            h_x, h_y = int(i[0]), int(i[1])
            if((h_x,h_y) not in holder):
                holder.append((h_x,h_y))
        else:
            return holder
    except:
        holder, h_x, h_y = [], "", ""
        for i in pares:
            if(i not in holder):
                holder.append(i)
        else:
            return holder
        

def obtPares():
    try:
        tam = int(input("Ingresa el número de pares ordenados -> "))
        pares,x,y = [],0,0
        print("Sintaxis: x,y")
        
        for i in range(tam):
            x,y = input("Ingresa el par #%d -> " % (i+1)).split(",")
            pares.append((x,y))
            
        return purgar(pares)
    except:
        print("Hubo en error en el ingreso de los datos, reinicia el programa")
        exit()


if __name__ == "__main__":
    import indebido
