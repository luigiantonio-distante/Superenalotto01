from Repository import Repository
from Sequenza import Sequenza
from Sistema import Sistema
from Menu import Menu
from IO import IO

def f1(repo):
    ns=IO.acqNumSequenze()
    sistema=Sistema(ns)
    repo.aggiungi(sistema)
    IO.visMsg("Sistema creato con ID: " + str(sistema.id))

def f2(repo):
    ns=IO.acqNumSistema()
    IO.visSistema(repo.getSistema(ns))
    
def f3(repo):
    pass

def f4(repo):
    ns=IO.acqNumSistema()
    seq = IO.acqSequenza()
    IO.visSistemaPunteggio(repo.getSistema(ns), seq)

def f5(repo):    
    seq = IO.acqSequenza()    
    L=list()
    for key in repo.diz:
        if repo.diz[key].esisteSequenzaPunteggio(2, seq):
            L.append(key)
    for s in L:
        print(s)


def f6(repo):    
    ns=IO.acqNumSistema()
    c=5
    for x in repo.diz[ns].lista:
        if x.filtrataSuper(lambda x,y:x>=y,c) == True:
            print(x)

def f7(repo):    
    pass

def main():
    repository = Repository()

    dictionary={
        '1':['Nuovo Sistema',f1],
        '2':['Visualizza Sistema',f2],
        '3':['Modificare',f3],
        '4':['Colonne Punteggi',f4],
        '5':['Elenco Sistemi Vincenti', f5],
        '6':['Sequenze Filtrate', f6],
        'U':['Uscita',f7]
    }    

    menu = Menu(dictionary, ['u','U'])
    menu.prospetta()
    scelta=menu.acqScelta()
    while not menu.uscita(scelta):
        dictionary[scelta][1](repository)
        menu.prospetta()
        scelta=menu.acqScelta()

main()
