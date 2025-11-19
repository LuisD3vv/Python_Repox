sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(sent_message)
    
# el r+ significa que se puede tanto leer como escribir
with open('sent_message.txt', 'r+') as file:
    # Read the sent message from the file
    original_message = file.read()
    # Move the cursor to the beginning of the file
    # cuantos, desde donde .seek(offset,whence)
    file.seek(10, 0)
    file.truncate(len(sent_message))
    # Modify the message to simulate unsending
    unsent_message = 'This message has been unsent.'
    file.write(unsent_message)
    print(f"mensaje Original:  {original_message}")
    print(f"mensaje no enviado: {unsent_message}")
    
    
    '''
    .seek - mover el cursor a un lugar deseado (0) es el inicio del archivi por defecto
    
    .truncate - corta el archivo a cierto tamanno, si no tiene parametros, se elimina desde donde este el cursor actualmnente
    
    '''