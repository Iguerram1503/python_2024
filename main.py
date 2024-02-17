import re

#Special sequences 

mensaje = 'A RegEx, or  Regular Expresions, is a sequence of characters that forms a search pattern'
patron= '\AA'

resultado = re.findall(patron, mensaje)