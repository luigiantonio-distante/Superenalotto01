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
