def player_category(age):
    if (10<age<14):
        return 'infantil'
    elif (15<age<17):
        return 'juvenil'
    elif (18<age<32):
        return 'profesional'
    elif (age>33):
        return 'veterano'
    else:
        return 'Not valid'

def custom_function(age, weeks, quantity, gender):
    if (weeks >=250):
        if (gender=='f'):
            if ( age >= 58):            
                return f'La persona se pensiona con: COP {0.9*quantity}'
            else:
                return ('Invalid age')
        else:
            if (age >= 63 ):
                return f'La persona se pensiona con: COP {0.9*quantity}'
            else:
                return ('Invalid age')
    else:
        return ('Minimum week number is 250')           

if __name__ == '__main__':
    print(custom_function(58, 250, 3000000, 'f'))