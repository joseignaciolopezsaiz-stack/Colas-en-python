class Cola:
  def __init__(self):
    self.cola = []
    
  def añadir(self, elemento):
    self.cola.append(elemento)

  def nueva_cola(self):
    self.cola.pop(0)
    return self.cola
      

  def sacar_cola(self):
    print("_____<<>>_____")
    return self.cola[0]

  def vacia(self):
    #print("/////",len(self.cola) == 0)
    return len(self.cola) == 0

  def tamaño(self):
    return len(self.cola)

# Create a cola
mya= Cola()

mya.añadir("A")
mya.añadir("Z")
mya.añadir("S")
mya.añadir("D")

print("Cola: ", mya.cola)
print("Elemen a elim cola", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("E")
print("elem añad E")
print("Elem a elim cola", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem a elim cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("F")
print("Elem añad F")

print("Elem a elim cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem a elim cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem a elim cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("G")
print("Elem añad G")
mya.añadir("H")
print("Elem añad H")
print("Elem a elim cola",mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("Cola vacia",mya.vacia())
print("tamaño",mya.tamaño())