import time
import pigpio

import Rpi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

from time import sleep
import pygame.mixer
import sys
pygame.mixer.init(44100,-16,2,4096)

class flabianos:
	def __init__(self):
		self.invitados=['ojos abiertos']

	def TuSiTuNo(self, EllosSi):
		if EllosSi in self.Invitados:

			print('Estado Normal')

		else:
			print('alerta ojos cerrados ESTORNUDO')
			segundos_d=3
			inicio=time.time()
			final=time.time()+segundos_d
			GPIO.output(18, True)
			while inicio<=final:
				inicio=time.time()

			else:
				GPIO.output(18, False)
			sonido = pygame.mixer.Sound("audio_alarma.wav")
			sonido,set_volume(1,0)
			sonido.play()
			sleep(10)
			sonido.stop()