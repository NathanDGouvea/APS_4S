
from testing_ground import TesteAlgoritmos

teste = [
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=2, quantidade=5000),
    #TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=5, quantidade=10000),
    #TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=5, quantidade=15000),
    #TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=5, quantidade=20000),
    #TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=5, quantidade=5000),
    #TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=5, quantidade=10000),
    #TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=5, quantidade=15000),
    #TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=5, quantidade=20000),
    ]

for t in teste:
    t.executar()
