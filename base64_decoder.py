import base64
from time import sleep

coded_string = 'aHNSdW5QeXRob24='
decoded = base64.b64decode(coded_string)

print('=========================')
sleep(5)
print('HACKERSEC DECODING . . .')
sleep(5)
print('Flag: ',decoded)
sleep(5)
print('Programa finalizado.')