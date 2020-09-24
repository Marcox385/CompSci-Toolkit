def sintax(li, ls, f): 
    try:
        li = int(li)
        ls = int(ls)
    except:
        return 0

    if(li > ls):
        li, ls = ls, li
    elif(li == ls):
        return 8 
        
    nums = list(map(str,list(range(0,10))))
    signs = list("+ - / * ^")
    f = list(f)
    for i in range(0,len(f)-1):
        f[i] = "**" if(f[i] == "^") else f[i]

        if((f[i] in nums) and (type(f[i+1]) == str and f[i+1] not in signs and f[i+1] not in nums)):
            f.insert(i+1,"*") 

    f = "".join(f)

    return (li,ls,f)

def exec_rec(l_inf, l_sup, form):
    elems = []
    count = l_sup
    sum_tot = 0

    try:
        while(l_sup >= l_inf):
            k = l_sup

            if(l_sup == count):
                elems.append(("k(n):", eval(form)))
            else:
                elems.append(("k(n%d):" % (l_sup-count), eval(form)))

            sum_tot += eval(form)
            l_sup -= 1

        return (elems, sum_tot)
    except ZeroDivisionError:
        return 0
    except:
        return 1

if __name__ == "__main__":
    import indebido
