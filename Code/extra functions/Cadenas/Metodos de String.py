# Aqui estudiaremos todos los metodos de lso string
Palabra = "Hola mundo"


print(Palabra[::-1])
print(f" {Palabra}")



for i in Palabra:
    print(i, end = " ")

print(Palabra.upper())
print(Palabra.lower())
print(Palabra.title())
print(Palabra.swapcase())
print(Palabra.capitalize())
print(Palabra.count("o"))
print(Palabra.find("o"))
print(Palabra.replace("o", "a"))
print(Palabra.split(" "))

for i in Palabra:
    if i.isupper():
        i = i.lower()
        print(i, end=" ")

if Palabra.startswith("Hola"):
    print("si")
elif Palabra.endswith("Hola"):
    print("si")


