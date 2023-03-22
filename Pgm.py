from Repository import Repository
from Sequenza import Sequenza
from Sistema import Sistema

def main():

    repository = Repository()
    for x in range(5):
        repository.aggiungi(Sistema())
    print(repository)

main()
