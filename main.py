from machine import Pin, PWM
from time import sleep_ms

BUZZER_PIN = 1

buzzer = PWM(Pin(BUZZER_PIN))
buzzer.duty_u16(0)

NOTE_E4  = 330
NOTE_G4  = 392
NOTE_A4  = 440
NOTE_AS4 = 466
NOTE_B4  = 494
NOTE_C5  = 523
NOTE_D5  = 587
NOTE_E5  = 659
NOTE_F5  = 698
NOTE_G5  = 784
NOTE_A5  = 880
REST = 0

melody = [
    (NOTE_E5, 125), (NOTE_E5, 125), (REST, 125),
    (NOTE_E5, 125), (REST, 125), (NOTE_C5, 125),
    (NOTE_E5, 125), (REST, 125), (NOTE_G5, 125),
    (REST, 375), (NOTE_G4, 125), (REST, 375),

    (NOTE_C5, 125), (REST, 250), (NOTE_G4, 125),
    (REST, 250), (NOTE_E4, 125), (REST, 250),
    (NOTE_A4, 125), (REST, 125), (NOTE_B4, 125),
    (REST, 125), (NOTE_AS4, 125), (NOTE_A4, 125),

    (NOTE_G4, 170), (NOTE_E5, 170), (NOTE_G5, 170),
    (NOTE_A5, 125), (REST, 125), (NOTE_F5, 125),
    (NOTE_G5, 125), (REST, 125), (NOTE_E5, 125),
    (REST, 125), (NOTE_C5, 125), (NOTE_D5, 125),
    (NOTE_B4, 125), (REST, 250),

    (NOTE_C5, 125), (REST, 250), (NOTE_G4, 125),
    (REST, 250), (NOTE_E4, 125), (REST, 250),
    (NOTE_A4, 125), (REST, 125), (NOTE_B4, 125),
    (REST, 125), (NOTE_AS4, 125), (NOTE_A4, 125),

    (NOTE_G4, 170), (NOTE_E5, 170), (NOTE_G5, 170),
    (NOTE_A5, 125), (REST, 125), (NOTE_F5, 125),
    (NOTE_G5, 125), (REST, 125), (NOTE_E5, 125),
    (REST, 125), (NOTE_C5, 125), (NOTE_D5, 125),
    (NOTE_B4, 125), (REST, 250),
]

def play_tone(freq, duration):
    if freq == REST:
        buzzer.duty_u16(0)
        sleep_ms(duration)
    else:
        buzzer.freq(freq)
        buzzer.duty_u16(32768)
        sleep_ms(duration)
        buzzer.duty_u16(0)
        sleep_ms(25)

while True:
    for note, duration in melody:
        play_tone(note, duration)
    sleep_ms(1500)
