from random import *


"""
    Las reglas ya todos las conocemos:
    
    papel gana piedra
    piedra gana tijeras
    tijera gana papel
    
    En cualquier otro caso es empate
"""


print("      Welcome    ")
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊ Rock") # Agregado para mas instruccion.
print("2) ✋ Paper")
print("3) ✌  Scissors")


""" 
      Este ciclo nos ayuda a controlar las entradas del usuario y solamente recopilar la informacion
      que necesita nuestro programa para funcionar, de esta manera evitando numeros mayores
      y el ingreso de otro tipo de datos que nuestro programa no necesita, como strings.
      
      Aunque posiblemente puedan ser necesario en caso de necesitar darle un nombre al player
      
"""


while True:
  
  player = input("Elige una opción (1-3): ")
  
  try:
    player = int(player)
    if player not in [1, 2, 3]:
      print("Porfavor, ingresa un numero dentro del rango (1-3)")
    else:
      break
  except ValueError:
   print("porfavor, ingresa un numero.")
   
    
cpu = randint(1,3)
simbols = ['✊','✋','✌']


if player == cpu:
  print("empate")


elif player == 3 and cpu == 1:
    print(f"cpu chose: {simbols[1-1]}\nYou chose: {simbols[3-1]}")
    print("Cpu gana")
    
elif cpu == 1 and player == 3:
    print(f"cpu chose: {simbols[3-1]}\nYou chose: {simbols[1-1]}")
    print("player gana")
    
elif player == 1 and cpu == 3:
    print(f"You chose: {simbols[1-1]}\ncpu chose: {simbols[3-1]}")
    print("player gana")
    
elif player == 3 and cpu == 2:
    print(f"You chose: {simbols[3-1]}\ncpu chose: {simbols[2-1]}")
    print("player gana")
    
elif cpu == 2 and player == 3:
    print(f"cpu chose: {simbols[3-1]}\nYou chose: {simbols[1-1]}")
    print("cpu gana")
    
elif player == 2 and cpu == 3:
    print(f"cpu chose: {simbols[2-1]}\nYou chose: {simbols[3-1]}")
    print("player gana")
    
elif cpu == 2 and player == 1:
    print(f"cpu chose: {simbols[3-1]}\nYou chose: {simbols[1-1]}")
    print("player gana")
    
elif player == 2 and cpu == 1:
    print(f"you chose: {simbols[3-1]}\ncpu chose: {simbols[1-1]}")
    print("Cpu gana")   
elif player == 1 and cpu == 2:
    print(f"cpu chose: {simbols[3-1]}\nYou chose: {simbols[1-1]}")
    print("cpu gana") 
      
else:
    print("Error de entrada.")


print(f"player: {player}, cpu: {cpu}")

# Gracias por revisar mi codigo!, acepto sugerencias y errores, estoy abierto al aprendizaje