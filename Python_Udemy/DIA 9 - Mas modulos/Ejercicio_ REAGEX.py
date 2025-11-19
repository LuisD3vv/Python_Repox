import re
def verificar_cp(cp):
	patron = r"^[A-Za-z]{2}\d{4}$" # los caracteres de la a-z pueden ser hasta dos eso signifa {2}
	if re.search(patron, cp):
		# otra forma  patron = r"^[A-[A-Za-z]Za-z]{2}\d{4}$"
		print(f"Codigo postal correcto {cp}")
	else:
		print("El código postal ingresado no es correcto.")



verificar_cp("we1253")


def verificar_saludo(frase):
	if re.search(r'^Hola...',frase):
		print(f"Frase correcta {frase}")
	else:
		print("No has saludado")


verificar_saludo("Hola Luis como has estado ultimamente")



def verificar_email(email):
    if re.search(r'\w+@\w+\.(com|mx|edu|com.br)$',email):
        print(f"email {email} correcto")
    else:
        print("La dirección de email es incorrecta")

    
verificar_email('usuario@host.com')