# conversiones implicitas / son las que python realiza automaticamente
num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

# conversions explicitas / son las que tienen que ser5 escritas en codigo mediante casting

num1 = 5.8

num2 = int(num1)
print(num2)
print(type(num2))

# ------------------

edad = input('Dime tu edad: ')
edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad

print(f'tu nueva "edad" es {nueva_edad}.')

# ---------------

num1 = "7.5"
num2 = "10"

print(float(num1) + float(num2))
# en este codigo se imprimio el resultado al mimso tiempo que se incluyo el casting dentro del print
