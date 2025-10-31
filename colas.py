class Cola:
  def __init__(self):
    self.cola = []
    
  def añadir(self, elemento):
    self.cola.append(elemento)

  def nueva_cola(self):
    if self.vacia():
      return "cola vacia"
    else:
      self.cola.pop(0)
      return self.cola
      

  def sacar_cola(self):
    print("_____<<>>_____")
    if self.vacia():
      return "cola vacia"
    else:
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
print("Elemen sacado cola", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("E")
print("Elem sacado cola", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem sacado cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("F")

print("Elem sacado cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem sacado cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem sacado cola:", mya.sacar_cola())
print("Nueva cola: ", mya.nueva_cola())
print("cola vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())