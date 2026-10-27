
from datetime import datetime
from pathlib import Path

from testing_ground import TesteAlgoritmos


teste = [
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=10, quantidade=5000),
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=10, quantidade=10000),
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=10, quantidade=15000),
    TesteAlgoritmos(caminho="fonte/dadosCFiltro.csv", repeticoes=10, quantidade=20000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=10, quantidade=5000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=10, quantidade=10000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=10, quantidade=15000),
    TesteAlgoritmos(caminho="fonte/dadosSFiltro.csv", repeticoes=10, quantidade=20000),
]


for i, t in enumerate(teste, start=1):
    nome_fonte = Path(t.caminho).stem
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")

    arquivo_saida = (
        f"resultados/resultado_{i}_{nome_fonte}_{t.quantidade}_{data_hora}.csv"
    )

    t.executar(arquivo_saida=arquivo_saida)

    print(f"Resultado salvo em: {arquivo_saida}")
