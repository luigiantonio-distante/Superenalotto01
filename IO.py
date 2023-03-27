from Sequenza import Sequenza
class IO:
    def acqNumSequenze():
        num = int(input("Numero Sequenze"))
        return num
    def acqNumSistema():
        num = int(input("Numero Sistema"))
        return num
    
    def visMsg(msg):
        print(msg)
    
    def visSistema(sistema):
        print(sistema)

    def acqSequenza():
        str = input("Sequenza di numeri separati da spazio > ")
        lista = str.split(" ")
        i=0
        while i<len(lista):
            lista[i] = int(lista[i])
            i+=1
        seq=Sequenza(0)
        seq.fromList(lista)
        return seq

    def visSistemaPunteggio(sistema, sequenzaVincente):
        """
        per tutte le sequenze di sistema
        stampa la sequenza
        con relativo punteggio
        """
        for seq in sistema.getLista():
            print(seq,seq.calcolaPunteggio(sequenzaVincente))

