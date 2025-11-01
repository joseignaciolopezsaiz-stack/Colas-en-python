class Pila:
  def __init__(self):
    self.pila = []

  def añadir(self, elemento):
    self.pila.append(elemento)

  def nueva_pila(self):
    print("_____<<>>_____")
    self.pila.pop()
    return self.pila

  def sacar_pila(self):
     return self.pila[-1]

  def vacia(self):
    return len(self.pila) == 0

  def tamaño(self):
    return len(self.pila)

# Create a stack
mya = Pila()

mya.añadir('A')
mya.añadir('B')
mya.añadir('C')
#print(type(mya))
print("pila: ", mya.pila)
print("Elemen a elim pila8", mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("pila vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("E")
print("elem añad E")
print("Elem a elim pila", mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("pila vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem a elim pila:", mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("pila vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("F")
print("Elem añad F")

print("Elem a elim pila:", mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("pila vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
print("Elem a elim pila:", mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("pila vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("G")
print("Elem añad G")
print("Elem a elim pila:", mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("pila vacia: ", mya.vacia())
print("Tamaño: ", mya.tamaño())
mya.añadir("H")
print("Elem añad H")
mya.añadir("I")
print("Elem añad I")
print("Elem a elim pila",mya.sacar_pila())
print("Nueva pila: ", mya.nueva_pila())
print("Pila vacia",mya.vacia())
print("tamaño",mya.tamaño())