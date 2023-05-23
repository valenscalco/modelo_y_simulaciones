import matplotlib.pyplot as plt
# Aumento de temperatura

# Sin tener en cuenta la perdida de calor
m = 1 #Kg, masa del agua
c = 4186 #J, calor especifico del agua
Q = 1000 #J, calor entregado por segundo
temperaturas = [293.15, ] # temperatura inicial 293.15K

while temperaturas[-1] < 373.15:
    temperaturas.append((Q/(m*c)) + temperaturas[-1])

print(f"Temperatura final: {temperaturas[-1]}K = {temperaturas[-1] - 273.15}°C")
print(f"Demora: {len(temperaturas)}s")

eje_x = [segundo for segundo in range(0, len(temperaturas))]
plt.scatter(eje_x, temperaturas)
plt.title("Aumento de temperatura sin tener en cuenta la perdida de calor")
plt.show()

## Teniendo en cuenta la perdida de calor
Q_resistencia = 1000 #J, calor entregado por segundo por la resistencia
t_env = 293.15 # kelvin
k = 0.0004
A = 0.06845754 # m**2
d = 0.01 # m

temperaturas = [293.15, ] # temperatura inicial 293.15K

while temperaturas[-1] < 373.15 and temperaturas[-1] >= temperaturas[0]:
    Q_perdido = (k*A*(temperaturas[-1] - t_env)) / d
    Q_real = Q_resistencia - Q_perdido

    temperaturas.append((Q_real/(m*c)) + temperaturas[-1])

print(f"Temperatura final: {temperaturas[-1]}K = {temperaturas[-1] - 273.15}°C")
print(f"Demora: {len(temperaturas)}s")

eje_x = [segundo for segundo in range(0, len(temperaturas))]
plt.scatter(eje_x, temperaturas)
plt.title("Aumento de temperatura")
plt.show()