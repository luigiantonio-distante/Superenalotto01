from Sistema import Sistema
class Repository:
    def __init__(self):
        self.diz=dict()
        self.progressivo=0
    def aggiungi(self, sistema):
        self.progressivo+=1
        sistema.id=self.progressivo
        self.diz[self.progressivo]=sistema
        return self.progressivo
    def getSistema(self, ns):
        return self.diz[ns]
    def __str__(self):
        s="\n"
        for x in self.diz:
            s += str(x)+ ": " + str(self.diz[x]) + "\n"
        return s
