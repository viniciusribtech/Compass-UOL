class Passaro:
    def voar(self):
        print("Voando...")
    def som(self):
        pass

class Pato(Passaro):
    def som(self):
        print("Pato emitindo som...")
        print("Quack Quack")

class Pardal(Passaro):
    def som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

print("Pato")
pato = Pato()
pato.voar()
pato.som()
print("Pardal")
pardal = Pardal()
pardal.voar()
pardal.som()