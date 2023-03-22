class Menu:
    def __init__(self, dictionary, listaCarUsc):
        self.dictionary = dictionary
        self.listaCarUsc=listaCarUsc
    def prospetta(self):
        for k in self.dictionary:
            print(k,self.dictionary[k][0])
    def acqScelta(self):
        return input("Scelta")
    def uscita(self,scelta )->bool:
        return scelta in self.listaCarUsc

