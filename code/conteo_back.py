class conteo:
    def __init__(self,modo):
        self.modo = modo
        self.p_forms = ["P({},{}) = {}!","P({},{}) = {}!/({}-{})!","Pc = ({}-1)!","Pr = {}!/({}!...{}!)","P({},{}) = {}*{}*...*{}"]
        self.c_form = "C({},{}) = {}!/({}!({}-{})!)"
        self.unnecesary_1 = "C({},{}) = ({}*{}*...*({}))/{}!"

    def alt_factorial(self,n,r):
        resultado = 1
        for i in range(n,n-r,-1):
            resultado *= i
        return resultado

    def d_rep(self,n,r):
        holder = {}
        for i in r:
            if(i in holder.keys()):
                holder[i] = holder[i] + 1
            else:
                holder[i] = 1

        denom_text = list(holder.keys())
        denom_text.sort(reverse = True)

        denom = 1
        for i in holder.values():
            if(i != 1):
                denom *= self.alt_factorial(i,i)
        return (holder, self.alt_factorial(n,n) / denom)

def purgar(opc,n,r):
    if(opc == 0):
        try:
            n = int(n)
            if(n < 0):
                return -2
            else:
                return int(n)
        except:
            return -1
    elif(opc == 1 or opc == 4):
        try:
            n, r = int(n), int(r)
            if(n < 0 or r < 0):
                return -2
            elif(n < r):
                return -3
            else:
                return (n,r)
        except:
            return -1
    elif(opc == 2):
        try:
            n = int(n)
            if(n <= 0):
                return -2
            else:
                return int(n) - 1
        except:
            return -1
    else:
        from string import ascii_uppercase as mayus
        from string import ascii_lowercase as minus
        checker = mayus + minus
        try:
            if("," in n):
                print("aqui")
                n = list(n)
                for i in n:
                    if(i in checker or i not in list(map(str,range(10))) and i != ","):
                        return -2
                else:
                    n = "".join(n)

                n = n.split(",")
                if(len(n) < 2):
                    return -5
                else:
                    return (len(n),n,0)
            else:
                for i in n:
                    if(i not in checker):
                        return -2

                n = list(n)
                if(len(n) < 2):
                    return -5
                else:
                    return (len(n),n,1)
        except:
            return -99
    
if __name__ == "__main__":
    import indebido
