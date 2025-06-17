import numpy as np
import plot
import rk4

l = 0.2     # taxa de infecção
k = 20      # número médio de contatos
i0 = 0.05   # fração inicial de infectados (todos começam em I1)
n_estados = 20  # número de estados de infecção (I1, ..., In)
u = 1     # taxa de progressão entre estados de infecção e recuperação
t = np.linspace(0, 5, 500)
h = t[1] - t[0] # intervalo de tempo


def sis():
  S, i_total, _ = rk4.rk4(l, k, i0, 1, u, t, h)  # Calcula o modelo SIS com n=1
  plot.sis(t, S, i_total)


def sins():
  S1, i1, _ = rk4.rk4(l, k, i0, 1, u, t, h)  # Calcula o modelo SIS com n estados
  S_total, i_total, _ = rk4.rk4(l, k, i0, n_estados, u * n_estados, t, h)
  plot.sins(S1, S_total, i1, i_total, t)


def n_compartimentos():
  resultados = []
  lista_estados = np.arange(1, 5)
  for n_estados in lista_estados:
    u = 1 * n_estados
    S, i_total, i_estados = rk4.rk4(l, k, i0, n_estados, u, t, h)
    resultados.append((S, i_total, i_estados, n_estados))
  plot.n_compartimentos(t, i_total, n_estados, resultados)


#sis()
#sins()
n_compartimentos()