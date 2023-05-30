import matplotlib.pyplot as plt


class Calentadorh2o:
    def __init__(self):
        self.parametros()

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
        g.grafico_tiempo_temp_sin_perdidas(tiempos, temperaturas)

    def con_perdidas(self):
        # Calcula la temperatura interna de un objeto en un tiempo dado.
        area = 2 * 3.1416 * self.altura * self.radio + 2 * 3.1416 * self.radio**2
        temperaturas1 = []
        tiempos1 = []
        temperaturas2 = []
        tiempos2 = []

        for i in range(3):
            temperaturas = []
            tiempos = []
            for tiempo in range(self.tiempo_max):
                perdida_calor = (self.k * area * (self.ti - self.te)) / self.espesor[i]
                temperaturas.append(self.ti)
                tiempos.append(tiempo)
                self.ti += (self.qent - perdida_calor) / self.qesph2o
                # Imprime la temperatura en base a cada segundo
                if tiempo == 0 or tiempo == 1 or tiempo == 399:
                    print(f"Tiempo: {tiempo+1} s, Temperatura: {self.ti} °C")
            self.ti = 25
            if i == 0:
                temperaturas1 = temperaturas
                tiempos1 = tiempos
            elif i == 1:
                temperaturas2 = temperaturas
                tiempos2 = tiempos
        g.grafico_tiempo_temp(tiempos, temperaturas, tiempos2, temperaturas2, tiempos1, temperaturas1)

    # Genera un gráfico de la temperatura en función del tiempo
    def grafico_tiempo_temp(self, tiempos, temperaturas, tiempos2, temperaturas2, tiempos1, temperaturas1):
        plt.plot(tiempos1, temperaturas1, label="Espesor = 0.01")
        plt.plot(tiempos2, temperaturas2, label="Espesor = 0.005")
        plt.plot(tiempos, temperaturas, label="Espesor = 0.05")
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Temperatura (C)')
        plt.title('Gráfico de Temperatura vs. Tiempo')
        plt.legend()
        plt.show()

    # Genera un gráfico de la temperatura en función del tiempo
    def grafico_tiempo_temp_sin_perdidas(self, tiempos, temperaturas):
        plt.plot(tiempos, temperaturas)
        plt.xlabel('Tiempo')
        plt.ylabel('Temperatura')
        plt.title('Gráfico de Temperatura vs. Tiempo')
        plt.show()
        plt.close()


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
