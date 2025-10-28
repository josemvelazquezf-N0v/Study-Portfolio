# ==========================
# PROBABILIDAD E INCERTIDUMBRE EN GRAFOS
# Ejemplo: localización de un robot con ruido (modelo bayesiano simple)
# ==========================

# Estados posibles (nodos)
estados = ['A', 'B', 'C']

# Creencia inicial (distribución de probabilidad)
P = {'A': 0.2, 'B': 0.5, 'C': 0.3}

# Modelo de sensor:
# P(ruido_fuerte | estado)
P_ruido_dado_estado = {
    'A': 0.3,   # en A es poco probable oír ruido
    'B': 0.8,   # en B el ruido es fuerte (hay maquinaria)
    'C': 0.6    # en C ruido medio
}

# Evidencia observada: "ruido fuerte"
evidencia = "ruido_fuerte"

# Calculamos P(evidencia) (normalización)
P_evidencia = 0.0
for s in estados:
    P_evidencia += P_ruido_dado_estado[s] * P[s]

# Actualizamos las probabilidades con Bayes:
P_posterior = {}
for s in estados:
    P_posterior[s] = (P_ruido_dado_estado[s] * P[s]) / P_evidencia

# Mostramos resultados
print("Creencia inicial:")
for s in estados:
    print(f"  P({s}) = {P[s]:.2f}")

print("\nDespués de observar 'ruido fuerte':")
for s in estados:
    print(f"  P({s} | ruido) = {P_posterior[s]:.3f}")

# Mostramos el estado más probable
mejor_estado = max(P_posterior, key=P_posterior.get)
print(f"\n→ El robot cree que está en '{mejor_estado}' (máxima probabilidad).")


# Creencia inicial:
#   P(A) = 0.20
#   P(B) = 0.50
#   P(C) = 0.30

# Después de observar 'ruido fuerte': Prueba de testeo
#   P(A | ruido) = 0.118
#   P(B | ruido) = 0.471
#   P(C | ruido) = 0.412

# → El robot cree que está en 'B' (máxima probabilidad).
