# mouse-test-click
# Explicación del código

Este programa es una aplicación en Python que prueba la velocidad de respuesta del usuario al hacer clic en puntos rojos que aparecen en pantalla. La aplicación se ejecuta en una ventana de pantalla completa y mide el tiempo de reacción de cada clic.

## Características principales:
- La ventana se abre en modo de pantalla completa.
- Un botón de inicio permite comenzar la prueba.
- Aparece un punto rojo en una ubicación aleatoria y se mantiene en pantalla hasta que el usuario haga clic en él.
- Al hacer clic en el punto, este desaparece y reaparece en otra ubicación.
- Un temporizador cuenta regresivamente el tiempo de la prueba.
- Al finalizar, se muestra el total de clics realizados y el tiempo promedio de reacción.
- Se puede salir del modo de pantalla completa presionando la tecla `Escape`.
- Se puede reiniciar la prueba después de completarla.

---

## Explicación del código:

### 1. **Importación de librerías**
```python
import tkinter as tk
import random
import time
```
Se importan las librerías necesarias:
- `tkinter` para crear la interfaz gráfica.
- `random` para generar posiciones aleatorias.
- `time` para medir los tiempos de reacción.

### 2. **Inicialización de la aplicación**
```python
class ClickTestApp:
    def __init__(self, root, duration=10):
```
Se define una clase `ClickTestApp` que representa la aplicación. Recibe `root` (la ventana principal) y `duration` (duración de la prueba en segundos, por defecto 10).

### 3. **Configuración de la ventana**
```python
self.root.attributes('-fullscreen', True)
self.root.configure(bg="white")
```
La ventana se abre en modo pantalla completa y con fondo blanco.

### 4. **Temporizador y contador**
```python
self.label_timer = tk.Label(root, text=f"Time: {self.duration}s", font=("Arial", 14), bg="white")
self.label_timer.pack()
```
Se muestra una etiqueta con el tiempo restante.

### 5. **Área de juego (Canvas)**
```python
self.canvas = tk.Canvas(root, bg="white", highlightthickness=0)
self.canvas.pack(fill=tk.BOTH, expand=True)
```
Se crea un `Canvas` que cubre toda la pantalla para mostrar los puntos rojos.

### 6. **Inicio de la prueba**
```python
self.start_button = tk.Button(root, text="Start", command=self.start_test)
self.start_button.pack()
```
El botón "Start" inicia la prueba cuando se presiona.

### 7. **Aparición de los puntos rojos**
```python
x, y = random.randint(20, width - 20), random.randint(20, height - 20)
self.point = self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="red", outline="red")
```
Cada punto aparece en una posición aleatoria dentro de la ventana.

### 8. **Detección de clics**
```python
def click_point(self, event):
    reaction_time = time.time() - self.start_time - sum(self.click_times)
    self.click_times.append(reaction_time)
    self.points_clicked += 1
    self.spawn_point()
```
Cuando el usuario hace clic en el punto rojo, se calcula el tiempo de reacción y se genera un nuevo punto en otra ubicación.

### 9. **Finalización de la prueba**
```python
avg_time = sum(self.click_times) / len(self.click_times) if self.click_times else 0
result_text = f"Test Completed!\nTotal Clicks: {self.points_clicked}\nAverage Reaction Time: {avg_time:.2f} sec"
```
Cuando el tiempo de la prueba se agota, se calcula el tiempo promedio de reacción y se muestra un mensaje con los resultados.

### 10. **Salir de pantalla completa**
```python
def exit_fullscreen(self, event=None):
    self.root.attributes('-fullscreen', False)
```
El usuario puede salir del modo de pantalla completa presionando `Escape`.

---

## Cómo ejecutar el programa en Windows y Linux

### **Requisitos previos**
1. Tener Python instalado (versión 3.x).
2. Asegurarse de que `tkinter` esté disponible (viene incluido en la mayoría de las instalaciones de Python).

### **Ejecución en Windows**
1. Abrir una terminal (cmd o PowerShell).
2. Navegar hasta la carpeta donde se encuentra el archivo `click_test.py`.
3. Ejecutar el siguiente comando:
   ```sh
   python click_test.py
   ```

### **Ejecución en Linux**
1. Abrir una terminal.
2. Navegar hasta la carpeta donde está el archivo.
3. Ejecutar:
   ```sh
   python3 click_test.py
   ```

Si `tkinter` no está instalado, puedes instalarlo con:
```sh
sudo apt-get install python3-tk  # Para distribuciones basadas en Debian (Ubuntu)
```

