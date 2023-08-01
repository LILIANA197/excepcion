
# resultado=None
# numerador=0
# denominador=0

try:
    #SE ABRE UNA CONEXION A BBDD
    numerador= float(input('Ingrese el numerador (Ingrese numeros): '))
    denominador= float(input('Ingrese el denominador (Ingrese numeros): '))
    resultado= numerador/denominador

    archivo= open('archivo.txt', mode='a')
    #archivo.write('Hola\n')
    archivo.write(str(resultado))

except ZeroDivisionError as e:
    print('Excepcion especifica - SE dividio para 0')
except ValueError as e:
    print('Excepcion especifica - Se ingreso un valor no numerico')
except TypeError as e:
    print('Excepcion especifica - No se pudo convertir a numero lo ingresado')
except PermissionError as e:
    print('Excepcion especifica - No se tiene permiso para ejecutar el archivo')
except Exception as e:
    print(type(e))
    print('Excepcion general')
    # print(f'{e}')
    #print(f'No se puede dividir para 0 por siguiente error:{e}')
    #resultado='Error por division para 0'
else:  #NO es obligatorio
    print(resultado)
    archivo.close()
    print('Se ejecuta codigo del Else porque no hubo excepcion')
finally:
    #CIERRO la conexion de BBDD
    print('Se ejecuta siempre el codigo del bloqueo Finally')


#ZeroDivision Error
#ValueError
#TypeError
