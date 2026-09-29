import algoritmos
from time import perf_counter
import pandas as pd

import sys

sys.setrecursionlimit(100000)


def carregar_dados(caminho):

    df = pd.read_csv(caminho, sep=",", decimal=".")

    coluna = next(
        c for c in df.columns
        if str(c).strip().lower() == "areamunkm"
    )

    return df, coluna


start = perf_counter()

df, coluna = carregar_dados("fonte/dadosCFiltro.csv")

vector = (
    df.sort_values(by=coluna, ascending=False)[coluna]
    .dropna()
    .head(40000)
    .tolist()
)

end = perf_counter()

print(f"Vetor gerado em: {end - start:.6f} segundos")
print(f"Coluna utilizada: {coluna}")
print(f"Quantidade de elementos: {len(vector)}")


algoritmos_teste = [
    # ("Bubble Sort", algoritmos.bubble_sort),
    # ("Bubble Sort Optimized", algoritmos.bubble_sort_optimized),
    # ("Insertion Sort", algoritmos.insertion_sort),
    # ("Merge Sort", algoritmos.merge_sort),
    ("Quick Sort", algoritmos.quick_sort),
    # ("Quick Sort Optimized", algoritmos.quick_sort_optimized),
    # ("Selection Sort", algoritmos.selection_sort),
]


for nome, algoritmo in algoritmos_teste:

    time = 0
    repetitions = 1

    for i in range(repetitions):

        vetor_teste = vector.copy()

        start = perf_counter()
        algoritmo(vetor_teste)
        end = perf_counter()

        time += end - start

    print(f"{nome}: {time / repetitions:.6f} segundos")