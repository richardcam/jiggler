import pyautogui
import time

def main():
    """
    Función principal que controla el movimiento del ratón.
    Si no hay actividad durante 60 segundos, mueve el ratón 25 píxeles a la derecha y luego regresa a su posición original.
    """
    last_position = pyautogui.position()  # Posición inicial del ratón
    idle_time = 0  # Contador de tiempo de inactividad en segundos

    print("Jiggler iniciado. Presiona Ctrl+C para detener.")

    try:
        while True:
            current_position = pyautogui.position()  # Posición actual del ratón

            if current_position == last_position:
                # Incrementar contador si no hay movimiento
                idle_time += 1
            else:
                # Reiniciar contador si detecta movimiento
                idle_time = 0
                last_position = current_position

            if idle_time >= 60:  # Si han pasado 60 segundos sin movimiento
                pyautogui.move(25, 0)  # Mover el ratón 25 píxeles a la derecha
                print("Ratón movido 25 píxeles a la derecha.")
                time.sleep(0.5)  # Breve pausa para simular el movimiento
                pyautogui.move(-25, 0)  # Mover el ratón de regreso a su posición original
                print("Ratón regresó a la posición original.")
                idle_time = 0  # Reiniciar contador tras el movimiento

            time.sleep(1)  # Esperar un segundo antes de volver a comprobar
    except KeyboardInterrupt:
        print("\nJiggler detenido.")

if __name__ == "__main__":
    main()

