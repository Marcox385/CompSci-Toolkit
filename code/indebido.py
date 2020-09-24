try:
    from time import sleep as zzz

    print("Haz ejecutado el módulo como si pudiera mantenerse él solo")
    print("No debiste hacer eso...")

    for i in range(10,0,-1):
        zzz(0.75)
        print("%d" % i)

    for _ in range(100):
        print('\a')
        zzz(0.1)
except:
    print(">:( no lo vuelvas a hacer, por fa")
