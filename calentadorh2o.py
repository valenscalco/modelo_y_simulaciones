import matplotlib.pyplot as plt


class Calentadorh2o:
    def __init__(self):
        self.parametros()

    def parametros(self):
        self.radio = 0.0535
        self.altura = 0.15
        self.espesor = 0.01
        self.qent = 909
        self.qesph2o = 4184
        self.tiempo_max = 400
        self.ti = 25  # Temperatura inicial
        self.te = 20  # Temperatura externa
        self.k = 0.4

    def sin_perdidas(self):
        temperaturas = []
        tiempos = []

        for tiempo in range(self.tiempo_max):
            # Actualiza la temperatura final
            tf = self.ti + (self.qent / self.qesph2o)
            # Agrega los valores actuales de temperatura y tiempo a las listas
            temperaturas.append(tf)
            tiempos.append(tiempo)
            # Actualiza la temperatura inicial para la siguiente iteración
            self.ti = tf
            # Imprime la temperatura en base a cada segundo
            # if tiempo == 0 or tiempo == 1 or tiempo == 399:
            print(f"Tiempo: {tiempo+1} s, Temperatura: {tf} °C")
        g.grafico_tiempo_temp(tiempos, temperaturas)

    def con_perdidas(self):
        # Calcula la temperatura interna de un objeto en un tiempo dado.
        area = 2 * 3.1416 * self.altura * self.radio + 2 * 3.1416 * self.radio**2
        temperaturas = []
        tiempos = []

        for tiempo in range(self.tiempo_max):
            perdida_calor = (self.k * area * (self.ti - self.te)) / self.espesor
            temperaturas.append(self.ti)
            tiempos.append(tiempo)
            self.ti += (self.qent - perdida_calor) / self.qesph2o
            # Imprime la temperatura en base a cada segundo
            # if tiempo == 0 or tiempo == 1 or tiempo == 399:
            print(f"Tiempo: {tiempo+1} s, Temperatura: {self.ti} °C")
        g.grafico_tiempo_temp(tiempos, temperaturas)

    # Genera un gráfico de la temperatura en función del tiempo
    def grafico_tiempo_temp(self, tiempos, temperaturas):
        x_label = 'Tiempo'
        y_label = 'Temperatura'
        title = 'Gráfico de Temperatura vs. Tiempo'
        plt.plot(tiempos, temperaturas)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()


if __name__ == "__main__":
    g = Calentadorh2o()
    stop = False
    while not stop:
        election = int(input("Ingresar 1 para calculo sin perdidas \nIngresar 2 para calculo con perdidas\n"))
        if election == 1:
            g.sin_perdidas()
            stop = True
        elif election == 2:
            g.con_perdidas()
            stop = True
