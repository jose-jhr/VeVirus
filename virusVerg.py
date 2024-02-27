import threading

from pynput.mouse import Listener
import tkinter as tk
from PIL import Image, ImageTk
import keyboard

# Crear la ventana principal de Tkinter
root = tk.Tk()
# Ocultar bordes y barra de título de la ventana
root.overrideredirect(True)


# Definir una función llamada startVirus que toma la ruta de una imagen como parámetro
def startVirus(image_path):
    # Cargar la imagen desde la ruta proporcionada
    image = Image.open(image_path)

    # Convertir la imagen a un formato compatible con Tkinter
    tk_image = ImageTk.PhotoImage(image)

    # Crear un widget de etiqueta para mostrar la imagen en la ventana
    label = tk.Label(root, image=tk_image)
    label.pack()

    # Definir la función on_click para manejar clics del ratón
    def on_click(x, y, button, pressed):
        if pressed:
            # Actualizar la posición de la ventana en cada clic
            root.geometry(f"{image.width}x{image.height}+{x}+{y}")
            # Hacer la ventana superior sobre todas las demás
            root.attributes('-topmost', True)
            print("click")

    def check_key():
        # Verificar periódicamente si la tecla 'e' ha sido presionada
        if keyboard.is_pressed('e'):
            root.destroy()  # Cerrar la ventana si 'e' está presionada
        else:
            # Programar la verificación nuevamente después de 100 milisegundos
            root.after(100, check_key)

    # Iniciar el listener para el clic del ratón
    with Listener(on_click=on_click) as listener:
        #hilo para verificar si se presiona e
        threading.Thread(target=check_key).start()
        # Mostrar la ventana y esperar a que el usuario interactúe con ella
        root.mainloop()

# Llamar a la función startVirus con la ruta de la imagen como argumento
startVirus("img/pene.png")