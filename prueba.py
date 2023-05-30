import matplotlib.pyplot as plt

class Calentadorh2o:
    def __init__(self):
        self.parametros()
        self.x = 0
        self.tiempos = []
        self.temperaturas = []

    def parametros(self):
        self.radio = 0.0535
        self.altura = 0.15
        self.espesor = [0.01, 0.005, 0.05]
        self.qent = 909
        self.qesph2o = 4184
        self.tiempo_max = 400
        self.ti = 25  # Temperatura inicial
        self.te = 20  # Temperatura externa
        self.k = 0.4

    def sin_perdidas(self):
        self.tiempos = []
        self.temperaturas = []

        for tiempo in range(self.tiempo_max):
            # Actualiza la temperatura final
            tf = self.ti + (self.qent / self.qesph2o)
            # Agrega los valores actuales de temperatura y tiempo a las listas
            self.temperaturas.append(tf)
            self.tiempos.append(tiempo)
            # Actualiza la temperatura inicial para la siguiente iteración
            self.ti = tf
            # Imprime la temperatura en base a cada segundo
            # if tiempo == 0 or tiempo == 1 or tiempo == 399:
            print(f"Tiempo: {tiempo+1} s, Temperatura: {tf} °C")
        self.x = 1
        self.grafico_tiempo_temp()

    def con_perdidas(self):
        self.tiempos = []
        self.temperaturas = []

        for i in range(3):
            self.ti = 25  # Reinicia la temperatura inicial para cada espesor
            for tiempo in range(self.tiempo_max):
                perdida_calor = (self.k * 2 * 3.1416 * self.altura * self.radio * (self.ti - self.te)) / self.espesor[i]
                self.temperaturas.append(self.ti)
                self.tiempos.append(tiempo)
                self.ti += (self.qent - perdida_calor) / self.qesph2o
                # Imprime la temperatura en base a cada segundo
                if tiempo == 0 or tiempo == 1 or tiempo == 399:
                    print(f"Tiempo: {tiempo+1} s, Temperatura: {self.ti} °C")
        self.x = 3
        self.grafico_tiempo_temp()

    # Genera un gráfico de la temperatura en función del tiempo
    def grafico_tiempo_temp(self):
        if self.x == 1:
            label = 'Sin pérdidas'
            color = 'red'
        elif self.x == 2:
            label = 'Espesor 0.005'
            color = 'green'
        elif self.x == 3:
            label = 'Espesor 0.05'
            color = 'blue'

        plt.plot(self.tiempos, self.temperaturas, color=color, label=label)

        if self.x == 3:
            x_label = 'Tiempo (s)'
            y_label = 'Temperatura (°C)'
            title = 'Gráfico de Temperatura vs. Tiempo'
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.legend()
            plt.show()


if __name__ == "__main__":
    g = Calentadorh2o()
    stop = False
    while not stop:
        election = int(input("Ingresar 1 para cálculo sin pérdidas\nIngresar 2 para cálculo con pérdidas\n"))
        if election == 1:
            g.sin_perdidas()
            stop = True
        elif election == 2:
            g.con_perdidas()
            stop = True
