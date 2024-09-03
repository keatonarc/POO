#drilling ejercicio 6
usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}

id_usuario = '004'

try:
    print(usuarios[id_usuario])
except KeyError:
    print(f'La clave {id_usuario} no esta en el diccionario. Agregando clave...')
    usuarios[id_usuario] = 'Ninguno'
    print(usuarios)
