class Libro:
    pass

libro_1 = Libro()
libro_2 = Libro()

libro_1.autor = 'Dan Brown'
libro_1.titulo = 'Infierno'

libro_2.autor = 'Dan Brown'
libro_2.titulo = 'El Codigo Da Vinci'
libro_2.ann_de_publicacion = 2003

print("Atributos de libro_1:", libro_1.__dict__)
print("Atributos de libro_2:", libro_2.__dict__)
