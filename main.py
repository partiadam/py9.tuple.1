'''
1. Feladat
Hozz létre egy tuple-t! Írasd ki a képernyőre az egyik elemét! 
Próbáld meg módosítani az egyik elemét! 
Milyen hibaüzenetet eredményez ez?
'''

szavak = ('kutya', 'macska')

szavak[0]='béka'

'''
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    szavak[0]='béka'
TypeError: 'tuple' object does not support item assignment
'''