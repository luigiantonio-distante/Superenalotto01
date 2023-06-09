from random import randint
class Sequenza:
    #inizializzo il set della sequenza
    def __init__(self, lung=6, min=1, max=90):
        self.myset = set()
        #riempio il set con numeir random da min a max
        while len(self.myset) < lung:
            self.myset.add(randint(min, max))

    def __str__(self):
        s="\n< "
        for c in self.myset:
            if c >= 10:
                s += str(c) + " "
            else:
                s += " "+str(c) + " "
        return s+  " >\n"
    def fromList(self, lista):
        self.myset=set()
        for x in lista:
            self.myset.add(x)
    def calcolaPunteggio(self, colonnaVincente):
        return len([x for x in self.myset if x in colonnaVincente.getSet()])
    def getSet(self):
        return self.myset
    def filtrata(self):
        return len([pari for pari in self.myset if pari%2==0])==0
    def filtrataSuper(self, criterio, k):
        return criterio(len([pari for pari in self.myset if pari%2==0]), k)
