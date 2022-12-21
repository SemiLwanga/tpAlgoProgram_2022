n = int(input("Entrer un nombre : "))
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(f"Le factoriel de {n} vaut: {factorial(n)}")