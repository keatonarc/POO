class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    
    def metodo_a(self):
        print("Metodo heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    
    def metodo_b(self):
        print("Metodo heredado de B")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Clase C")
    
    def metodo_c(self):
        print("Metodo de clase C")

#clase C
objeto_c = C()

objeto_c.metodo_a()  
objeto_c.metodo_b()  
objeto_c.metodo_c()  
