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
        lista = [int(x) for x in lista]
        seq=Sequenza(0)
        seq.fromList(lista)
        return seq

    def visSistemaPunteggio(sistema, sequenzaVincente):
        """
        per tutte le sequenze di sistema
        stampa la sequenza
        con relativo punteggio
        """
        """
        for seq in sistema.getLista():
            print(seq,seq.calcolaPunteggio(sequenzaVincente))
        """
        L = [seq for seq in sistema.getLista() if seq.calcolaPunteggio(sequenzaVincente) >= 2]
        for seq in L:
            print(seq, seq.calcolaPunteggio(sequenzaVincente))


        