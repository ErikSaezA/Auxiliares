import matplotlib.pyplot as plt
import csv

# Definir las listas para almacenar los datos del E-plane
theta_eplane_03 = []
gain_eplane_03 = []
theta_eplane_04 = []
gain_eplane_04 = []
theta_eplane_05 = []
gain_eplane_05 = []

# Definir las listas para almacenar los datos del H-plane
theta_hplane_03 = []
gain_hplane_03 = []
theta_hplane_04 = []
gain_hplane_04 = []
theta_hplane_05 = []
gain_hplane_05 = []

# Ruta de los archivos CSV para el E-plane
archivo_csv_eplane_03 = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/Gain_plot_0.3_base.csv"
archivo_csv_eplane_04 = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/Gain_plot_0.4_base.csv"
archivo_csv_eplane_05 = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/Gain_plot_0.5_base.csv"

# Ruta de los archivos CSV para el H-plane
archivo_csv_hplane_03 = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/Gain_Plot_0.3_hplane.csv"
archivo_csv_hplane_04 = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/Gain_Plot_0.4_hplane.csv"
archivo_csv_hplane_05 = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/Gain_Plot_0.5_hplane.csv"

# Leer el archivo CSV 0.3 GHz del E-plane
with open(archivo_csv_eplane_03, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Para omitir la primera fila (encabezado)
    for row in reader:
        theta_eplane_03.append(float(row[0]))  # Columna 0: Theta
        gain_eplane_03.append(float(row[1]))   # Columna 1: Ganancia

# Leer el archivo CSV 0.4 GHz del E-plane
with open(archivo_csv_eplane_04, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Para omitir la primera fila (encabezado)
    for row in reader:
        theta_eplane_04.append(float(row[0]))  # Columna 0: Theta
        gain_eplane_04.append(float(row[1]))   # Columna 1: Ganancia

# Leer el archivo CSV 0.5 GHz del E-plane
with open(archivo_csv_eplane_05, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Para omitir la primera fila (encabezado)
    for row in reader:
        theta_eplane_05.append(float(row[0]))  # Columna 0: Theta
        gain_eplane_05.append(float(row[1]))   # Columna 1: Ganancia

# Leer el archivo CSV 0.3 GHz del H-plane
with open(archivo_csv_hplane_03, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Para omitir la primera fila (encabezado)
    for row in reader:
        theta_hplane_03.append(float(row[0]))  # Columna 0: Theta
        gain_hplane_03.append(float(row[1]))   # Columna 1: Ganancia

# Leer el archivo CSV 0.4 GHz del H-plane
with open(archivo_csv_hplane_04, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Para omitir la primera fila (encabezado)
    for row in reader:
        theta_hplane_04.append(float(row[0]))  # Columna 0: Theta
        gain_hplane_04.append(float(row[1]))   # Columna 1: Ganancia

# Leer el archivo CSV 0.5 GHz del H-plane
with open(archivo_csv_hplane_05, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Para omitir la primera fila (encabezado)
    for row in reader:
        theta_hplane_05.append(float(row[0]))  # Columna 0: Theta
        gain_hplane_05.append(float(row[1]))   # Columna 1: Ganancia

# Crear los gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico del E-plane
ax1.plot(theta_eplane_03, gain_eplane_03, label='0.3 GHz', color='blue', linestyle='solid', linewidth=1.5)
ax1.plot(theta_eplane_04, gain_eplane_04, label='0.4 GHz', color='red', linestyle='dashed', linewidth=1.5)
ax1.plot(theta_eplane_05, gain_eplane_05, label='0.5 GHz', color='green', linestyle='dashdot', linewidth=1.5)
ax1.axhline(y=-3, color='black', linestyle='dotted', label='-3 dB')  # Línea punteada en -3 dB
ax1.set_title('E-Plane')
ax1.set_xlabel('Theta [deg]', fontsize=14)  # Establecer el tamaño de la fuente
ax1.set_ylabel('dB10normalize(GainTotal)', fontsize=14)  # Establecer el tamaño de la fuente
ax1.grid(True)
ax1.legend()

# Gráfico del H-plane
ax2.plot(theta_hplane_03, gain_hplane_03, label='0.3 GHz', color='blue', linestyle='solid', linewidth=1.5)
ax2.plot(theta_hplane_04, gain_hplane_04, label='0.4 GHz', color='red', linestyle='dashed', linewidth=1.5)
ax2.plot(theta_hplane_05, gain_hplane_05, label='0.5 GHz', color='green', linestyle='dashdot', linewidth=1.5)
ax2.axhline(y=-3, color='black', linestyle='dotted', label='-3 dB')  # Línea punteada en -3 dB
ax2.set_title('H-Plane')
ax2.set_xlabel('Theta [deg]', fontsize=14)  # Establecer el tamaño de la fuente
ax2.set_ylabel('dB10normalize(GainTotal)', fontsize=14)  # Establecer el tamaño de la fuente
ax2.grid(True)
ax2.legend()


plt.tight_layout()  # Ajustar el diseño para que no se superpongan los gráficos

# Mostrar el gráfico
plt.show()


# Definir las listas para almacenar los datos del S11 Parameter base
frecuencia_s11_base = []
dB_s11_base = []

# Definir las listas para almacenar los datos del S11 Parameter optimizado
frecuencia_s11_optimizado = []
dB_s11_optimizado = []

# Ruta del archivo CSV del S11 Parameter base
archivo_csv_s11_base = "C:/Users/eriks/OneDrive/Escritorio/Presentacion practica/Datos_para_Plotear/S11_base.csv"

# Leer el archivo CSV del S11 Parameter base
with open(archivo_csv_s11_base, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la primera fila (encabezado)
    for row in reader:
        frecuencia_s11_base.append(float(row[0]))  # Convertir la frecuencia a flotante
        dB_s11_base.append(float(row[1]))  # Convertir el valor dB a flotante



# Graficar los datos del S11 Parameter
plt.figure(figsize=(10, 6))

# Graficar el S11 Parameter base (más opaco)
plt.plot(frecuencia_s11_base, dB_s11_base, linestyle='-', label='S11 Parameter', color='red')

plt.title('S11 Parameter ')  # Ajustar el tamaño del título
plt.xlabel('Frequency (MHz)')  # Ajustar el tamaño de la etiqueta del eje x
plt.ylabel('dB(S11)')  # Ajustar el tamaño de la etiqueta del eje y

plt.grid(True)


# Agregar líneas verticales en 300 y 500 MHz
plt.axvline(x=300, color='g', linestyle='--', label='300 MHz')
plt.axvline(x=500, color='g', linestyle='--', label='500 MHz')
plt.axhline(y=-15, color='r', linestyle='--', label='-15 dB')  # Línea punteada en -10 dB
plt.legend(fontsize=12)  # Ajustar el tamaño de la leyenda
plt.show()