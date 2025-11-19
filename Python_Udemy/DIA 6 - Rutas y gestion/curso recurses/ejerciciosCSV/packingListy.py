import csv,os 

ruta = os.path.join(os.path.dirname(__file__))

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]
try:
    with open ('packing_list.csv','r',encoding='utf-8') as file:
        reader = csv.reader(file)
        for fila in reader:
            print(fila)
except FileNotFoundError:
    print("Packing list not found")
    with open (os.path.join(ruta,"packing_list.csv"),"w",encoding="utf-8") as refile:
        writer = csv.writer(refile)
        writer.writerows(data)
    print("se escribio en el archivo.")