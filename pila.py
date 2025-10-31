class Pila:
  def __init__(self):
    self.pila = []

  def añadir(self, elemento):
    self.pila.append(elemento)

  def nueva_pila(self):
    print("_____<<>>_____")
    print("Pila:",mya.pila)
    if len(self.pila) == 0:
        return "pila vacia"
    else:
        return self.pila.pop()

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

print("Elem sac pila: ", mya.nueva_pila())
print("Nueva pila: ", mya.pila)
print(" esta vacio: ", mya.vacia())
print("tamaño: ", mya.tamaño())
mya.añadir("D")
print("Elem sac pila: ", mya.nueva_pila())
print("Nueva pila: ", mya.pila)
print(" esta vacio: ", mya.vacia())
print("tamaño: ", mya.tamaño())
mya.añadir("E")
print("Elem sac pila: ", mya.nueva_pila())
print("Nueva pila: ", mya.pila)
print(" esta vacio: ", mya.vacia())
print("tamaño: ", mya.tamaño())
print("Elem sac pila: ", mya.nueva_pila())
print("Nueva pila: ", mya.pila)
print("esta vacio: ", mya.vacia())
print("tamaño: ", mya.tamaño())
mya.añadir("F")
print("Elem sac pila: ", mya.nueva_pila())
print("Nueva pila: ", mya.pila)
print("esta vacio: ", mya.vacia())
print("tamaño: ", mya.tamaño())
print("Elem sac pila: ", mya.nueva_pila())
print("Nueva pila: ", mya.pila)
print("esta vacio: ", mya.vacia())
print("tamaño: ", mya.tamaño())