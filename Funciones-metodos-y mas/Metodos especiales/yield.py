# generacion peresoza

def pares_inf():
    n = 0
    while True:
        yield n
        n += 2

gen = pares_inf()

print(next(gen))  # 0
print(next(gen))  # 2
print(next(gen))  # 4

# yiel solo genera un dato cuando se lo pedimos
# y no pierde secuencia,es increible