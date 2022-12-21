

try:
    mot = "+"
    n = int(input("Entrer n :"))
    for i in range(n):
        result  = mot * n
        print("{}".format(result))
except ValueError:
    print("Veullez entrer un entier")