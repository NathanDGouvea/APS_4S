import algoritmos
from time import perf_counter
import pandas as pd
import random
import sys


sys.setrecursionlimit(100000)


class TesteAlgoritmos:

    def __init__(self, caminho, repeticoes=5, quantidade=20000):
        self.caminho = caminho
        self.repeticoes = repeticoes
        self.quantidade = quantidade

        self.df, self.coluna = self.carregar_dados(caminho)

        self.vector = (
            self.df.sort_values(by=self.coluna, ascending=False)[self.coluna]
            .dropna()
            .head(self.quantidade)
            .tolist()
        )

        self.vector_random = self.vector.copy()
        random.shuffle(self.vector_random)

        self.algoritmos_teste = [
            ("Bubble Sort", algoritmos.bubble_sort),
            ("Insertion Sort", algoritmos.insertion_sort),
            ("Merge Sort", algoritmos.merge_sort),
            ("Quick Sort", algoritmos.quick_sort),
            ("Quick Sort Optimized", algoritmos.quick_sort_optimized),
            ("Selection Sort", algoritmos.selection_sort),
        ]

        self.resultados = []

    @staticmethod
    def carregar_dados(caminho):
        df = pd.read_csv(caminho, sep=",", decimal=".")

        coluna = next(
            c for c in df.columns
            if str(c).strip().lower() == "areamunkm"
        )

        return df, coluna

    def executar_teste(self, nome_cenario, vetor):
        for nome, algoritmo in self.algoritmos_teste:
            tempo_total = 0

            for _ in range(self.repeticoes):
                vetor_teste = vetor.copy()

                inicio = perf_counter()
                algoritmo(vetor_teste)
                fim = perf_counter()

                tempo_total += fim - inicio

            media = tempo_total / self.repeticoes

            self.resultados.append({
                "Cenário": nome_cenario,
                "Algoritmo": nome,
                "Quantidade de elementos": len(vetor),
                "Repetições": self.repeticoes,
                "Tempo médio (segundos)": media
            })

    def executar(self, arquivo_saida="resultados/resultado_testes.csv"):
        self.resultados = []

        self.executar_teste(
            "Inversamente ordenado",
            self.vector
        )

        self.executar_teste(
            "Aleatório",
            self.vector_random
        )

        df_resultados = pd.DataFrame(self.resultados)

        df_resultados.to_csv(
            arquivo_saida,
            index=False,
            sep=";",
            decimal=",",
            encoding="utf-8-sig"
        )