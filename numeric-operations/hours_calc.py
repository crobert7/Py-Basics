hour = int(input('Hora de inicio:')) 
min = int(input('Minuto de inicio:'))
dura = int(input('Duración del evento:'))

hours = (hour + (min + dura) // 60) % 24
minutes = (min + dura) % 60

print(f'{hours}:{minutes}') 