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
    def getLista(self):
        return self.lista
    def esisteSequenzaPunteggio(self, num, seq):
        ret=False
        i=0
        while not ret and i < len(self.lista):
            if self.lista[i].calcolaPunteggio(seq) >= num:
                ret=True
            i+=1
        return ret