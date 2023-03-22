from Sequenza import Sequenza
class Sistema:
    #inizializzo la lista che contiene le sequenze 
    def __init__(self, numSet=3):
        self.id=-1
        self.lista=list()
        #aggiungo un numeor di sequenze pari a "numSet"
        for x in range(numSet):
            self.lista.append(Sequenza())

    #aggiungo una sequenza generata
    def aggiungi(self):
        self.lista.append(Sequenza())
    
    #derfinisco la rappresentazione stringa di un sistema
    def __str__(self):
        s=""
        for seq in self.lista:
            s += str(seq) + " "
        return s
