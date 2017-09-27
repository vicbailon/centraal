#dir() para ver las propiedades
#reverse
#sort ---modifica la lista
#copy --- clonar por inmutables, asignar nueva
#sorted ordena y --- no modifica
#---- Parametros

#--MAP aplica una funcion a cada elemento de una busqueda
#--FILTER
#--REDUCE

"""lista=[1,2,5,6,7,8]
def add_by(value , number):
    return value * number

a= add_by(10,3);
print(a)

#list(map(add_by(20,3)))

e=list(map(add_by , lista , lista))
print (e)"""


#--- EXCEPTION

def add_by(number):
    '''this function return number by number'''
    try:
        if number >=5:
            raise ValueError("El número debe ser menor que 5");
        return  number / number
    except TypeError as err:
        print("Necesito un numero"+str(err))
    except ZeroDivisionError as err:
        print(str(err))
    except:
        "todos los demas"
    finally:
        print(1)

a= add_by(0);

print(a);