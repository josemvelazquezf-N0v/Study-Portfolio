import random

# Urna: lista con pelotas de colores
urna = ['Roja'] * 4 + ['Azul'] * 3 + ['Verde'] * 3
total = len(urna)

# ======================
# Probabilidades teóricas
# ======================
P_roja = 4 / total
P_azul = 3 / total
P_verde = 3 / total

P_roja_o_azul = (4 + 3) / total     # suma de casos favorables
P_roja_y_luego_azul = (4/total) * (3/(total-1))  # sin reemplazo

print("Probabilidades teóricas:")
print(f"  P(Roja) = {P_roja:.2f}")
print(f"  P(Azul) = {P_azul:.2f}")
print(f"  P(Verde) = {P_verde:.2f}")
print(f"  P(Roja o Azul) = {P_roja_o_azul:.2f}")
print(f"  P(Roja y luego Azul sin reemplazo) = {P_roja_y_luego_azul:.3f}")

# ======================
# Simulación (Monte Carlo)
# ======================
n_experimentos = 100000
roja = 0
roja_o_azul = 0
roja_y_luego_azul = 0

for _ in range(n_experimentos):
    # sacar 1 pelota al azar
    p1 = random.choice(urna)
    if p1 == 'Roja':
        roja += 1
    if p1 in ('Roja', 'Azul'):
        roja_o_azul += 1

    # sacar 2 pelotas sin reemplazo
    muestra = random.sample(urna, 2)
    if muestra[0] == 'Roja' and muestra[1] == 'Azul':
        roja_y_luego_azul += 1

print("\nResultados simulados (frecuencia relativa):")
print(f"  P(Roja) ≈ {roja / n_experimentos:.2f}")
print(f"  P(Roja o Azul) ≈ {roja_o_azul / n_experimentos:.2f}")
print(f"  P(Roja y luego Azul) ≈ {roja_y_luego_azul / n_experimentos:.3f}")


