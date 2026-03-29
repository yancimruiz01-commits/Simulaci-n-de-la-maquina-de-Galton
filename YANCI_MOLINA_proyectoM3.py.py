import random
import matplotlib.pyplot as plt

def simular_galton(n_canicas=3000, n_niveles=12):
    """
    Simulacion de la máquina de Galton con n_canicas y n_niveles.
    Devuelve lista de conteos para contenedores 0..n_niveles.
    """
    contadores = [0] * (n_niveles + 1)

    for _ in range(n_canicas):
        derecha = 0
        for _ in range(n_niveles):
            if random.random() < 0.5:
                derecha += 1
        contadores[derecha] += 1

    return contadores

def graficar_histograma(contadores):
    """
    Grafica el resultado de la simulación de Galton.
    """
    indices = list(range(len(contadores)))
    valores = contadores

    plt.figure(figsize=(10, 6))
    plt.bar(indices, valores, color="skyblue", edgecolor="black")
    plt.xlabel("Contenedor")
    plt.ylabel("Número de canicas")
    plt.title("Resultado simulación máquina de Galton (3000 canicas)")
    plt.grid(axis="y", alpha=0.25, linestyle="--")
    plt.xticks(indices)
    plt.tight_layout()
    plt.show()
