
from testing_ground import TesteAlgoritmos

teste = [
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=1, quantidade=5000),
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=1, quantidade=10000),
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=1, quantidade=15000),
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=1, quantidade=20000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=1, quantidade=5000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=1, quantidade=10000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=1, quantidade=15000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=1, quantidade=20000),
    ]

for t in teste:
    t.executar()
