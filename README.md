# Práctica 6: Generación de sonido con ESP32-C3 y buzzer pasivo mediante PWM

## Descripción

Esta práctica utiliza un ESP32-C3 programado en MicroPython para generar sonido con un buzzer piezoeléctrico pasivo mediante PWM. El programa reproduce una versión simplificada de la melodía de Super Mario Bros modificando la frecuencia de la señal PWM.

## Materiales

- ESP32-C3
- Buzzer piezoeléctrico pasivo
- Cables Dupont
- Cable USB
- MicroPython
- Thonny o terminal serial

## Conexión

| Buzzer | ESP32-C3 |
|--------|----------|
| Positivo | GPIO1 o GPIO2 |
| Negativo | GND |

## Funcionamiento

El buzzer pasivo necesita una señal oscilante para generar sonido. El ESP32-C3 produce esta señal mediante PWM. Al cambiar la frecuencia del PWM, el buzzer genera diferentes tonos. El programa usa una lista de notas y duraciones para reproducir una melodía.

## Ejecución

1. Cargar MicroPython en el ESP32-C3.
2. Abrir `main.py` en Thonny.
3. Verificar el pin usado en la variable `BUZZER_PIN`.
4. Ejecutar el programa.
5. El buzzer reproducirá la melodía de Super Mario Bros.

## Cambio de pin

Si el buzzer está conectado al GPIO1:

```python
BUZZER_PIN = 1
