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
    pass
def f5(repo):
    pass

def main():
    repository = Repository()

    dictionary={
    '1':['Nuovo Sistema',f1],
    '2':['Visualizza Sistema',f2],
    '3':['Modificare',f3],
    '4':['Ricerca Filtrata',f4],
    'U':['Uscita',f5]
    }    

    menu = Menu(dictionary, ['u','U'])
    menu.prospetta()
    scelta=menu.acqScelta()
    while not menu.uscita(scelta):
        dictionary[scelta][1](repository)
        menu.prospetta()
        scelta=menu.acqScelta()

main()
