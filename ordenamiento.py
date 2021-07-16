class Ordenar:
    def __init__(self,lista):
        self.lista=lista
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux
    def insertar(self,valor):
        self.borbuja()
        auxlista=[]
        enc=False
        for pos,else in enumerate(self.lista):
            if ele > valor:
                auxlista.append(valor)
                enc=True
                break
        if enc:
            for i in range(pos):
                auxlista.append(self.lista[i])
            auxlista.append(valor)
            for j in range(pos,len(self.lista)):
                auxlista.append(self.lista[j])
        else:
            self.lista.append(valor)
        return self.lista


ord1 = Ordenar([10,15,20,70,80])
print(ord1.insertar(5))
ord1.borbuja()
print(ord1.lista)

###
herencia 
class Persona:
    _siguiente = 0
    def __init__(self,nombre="Invitado",activo=True):
        Persona.siguiente = Persona._siguiente+1
        self._codigo = Persona._siguiente
        self._nombre = nombre
        self.activo = activo

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nom):
        self._nombre = nom
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self,cod):
        self._codigo = cod
    
    def siguiente(self):
        Persona._siguiente = Persona._siguiente+1
        return Persona._siguiente

    def __nombreMayuscula(self, nombre=""):
        return nombre.upper()

per1 = Persona()
print(per1.nombre)
#print(per1._nombreMayuscula("juan"))
per2 = Persona("Daniel",False)
print(per2.nombre,per2.activo)




