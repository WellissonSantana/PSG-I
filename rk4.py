def rk4(l, k, i0, n_estados, u, t, h):

    S = [1 - i0]  # suscetíveis
    i_estados = [ [i0] if i == 0 else [0] for i in range(n_estados) ]  # I1,...,In

    # Função para calcular as derivadas
    def df_dt(S, i_estados):
        i_total = sum(i_estados)
        dS_dt = -l * k * S * i_total + u * i_estados[-1]
        dI_dt = []
        for i in range(n_estados):
            if i == 0:
                dI = l * k * S * i_total - u * i_estados[0]
            elif i == n_estados - 1:
                dI = u * i_estados[i - 1] - u * i_estados[i]
            else:
                dI = u * i_estados[i - 1] - u * i_estados[i]
            dI_dt.append(dI)

        return dS_dt, dI_dt

    # Método de Runge-Kutta 4 para o sistema
    for ti in t[1:]:
        S_atual = S[-1]
        i_atual = [state[-1] for state in i_estados]

        # k1
        dS1, dI1 = df_dt(S_atual, i_atual)
        
        # k2
        S_k2 = S_atual + 0.5 * h * dS1
        I_k2 = [i + 0.5 * h * di for i, di in zip(i_atual, dI1)]
        dS2, dI2 = df_dt(S_k2, I_k2)
        
        # k3
        S_k3 = S_atual + 0.5 * h * dS2
        I_k3 = [i + 0.5 * h * di for i, di in zip(i_atual, dI2)]
        dS3, dI3 = df_dt(S_k3, I_k3)
        
        # k4
        S_k4 = S_atual + h * dS3
        I_k4 = [i + h * di for i, di in zip(i_atual, dI3)]
        dS4, dI4 = df_dt(S_k4, I_k4)

        # Atualizar S
        S_next = S_atual + (h / 6) * (dS1 + 2 * dS2 + 2 * dS3 + dS4)
        S.append(S_next)

        # Atualizar cada estado de infecção
        for i in range(n_estados):
            i_proximo = i_atual[i] + (h / 6) * (dI1[i] + 2 * dI2[i] + 2 * dI3[i] + dI4[i])
            i_estados[i].append(i_proximo)


    I_total = [sum(states_at_time) for states_at_time in zip(*i_estados)]
    
    return S, I_total, i_estados