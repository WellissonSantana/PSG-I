import numpy as np
import matplotlib.pyplot as plt

def sis(t, S, i_total):

    plt.figure(figsize=(18, 9))

    plt.plot(t, i_total, label='Infectados', linewidth=5, color= 'red'),
    plt.plot(t, S, label='Suscetíveis', linewidth=5, color='blue')

    plt.xlabel('Tempo (t)', fontsize=28)
    plt.ylabel('Fração da população', fontsize=28)
    plt.title('Evolução da população ao longo do tempo', fontsize=28)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.legend(fontsize=18, loc='lower right')
    plt.grid(True, alpha=0.8)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig('sis.png', dpi=300, bbox_inches='tight')
    plt.show()


def sins(S1, S_total, i1, i_total, t):

    plt.figure(figsize=(18, 9))

    plt.plot(t, S1, label='Suscetíveis SIS', linewidth=5, color='blue')
    plt.plot(t, i1, label='Infectados SIS', linewidth=5, color= 'red')

    plt.plot(t, S_total, label='Suscetíveis SInS', linewidth=5, color='purple')
    plt.plot(t, i_total, label='Infectados SInS', linewidth=5, color='orange')

    plt.xlabel('Tempo (t)', fontsize=28)
    plt.ylabel('Fração da população', fontsize=28)
    plt.title('Evolução da população ao longo do tempo', fontsize=28)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.legend(fontsize=18, loc='lower right')
    plt.grid(True, alpha=0.8)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig('comparação sis x sins.png', dpi=300, bbox_inches='tight')
    plt.show()

    
def n_compartimentos(t, i_total, n_estados, resultados):
    
    colors = plt.cm.Reds(np.linspace(0.3, 1, n_estados))

    plt.figure(figsize=(18, 9))

    for _, i_total, _, n_estados in resultados:
        plt.plot(t, i_total, label=f' (n={n_estados}) compartimentos', linewidth=5, color=colors[n_estados - 1])

    plt.xlabel('Tempo (t)', fontsize=28)
    plt.ylabel('Fração da população infectada', fontsize=28)
    plt.title('Comparação para diferentes números de compartimentos de infecção (n)', fontsize=28)
    plt.xticks(fontsize=24)
    plt.yticks(fontsize=24)
    plt.legend(fontsize=18, loc='lower right')
    plt.grid(True, alpha=0.8)
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig('comparação_n_compartimentos.png', dpi=300, bbox_inches='tight') 
    plt.show()