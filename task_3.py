def cumulative_sum(o_list):
    lst=[];                              #final list
    total=0;                             #total
    for item in o_list:                  #loop
        total += item;                   #box
        lst.append(total);               #add box
    return lst                           #return


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