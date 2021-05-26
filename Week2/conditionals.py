import dictionaries as dct 

def max_price_car1(dct):
    max_price = 0
    for key,val in dct['modelos'].items():
        car = dct['modelos'][key]
        price = car['precio']
        if price > max_price:
            max_price = price
            car_key = key
    return dct['modelos'][car_key]

def car_max_colors(dct):
   sandero = dct['modelos'][1]
   kwid = dct['modelos'][2]
   duster = dct['modelos'][3]
   megan = dct['modelos'][4]
   sandero_colours = len(sandero['colores'])
   kwid_colours = len(sandero['colores'])
   duster_colours = len(sandero['colores'])
   megan_colours = len(sandero['colores'])
   
   if (sandero_colours >= kwid_colours >= duster_colours >= megan_colours):
       return sandero
   elif ( kwid_colours >= duster_colours >= megan_colours):
        return kwid
   elif ( duster_colours >= megan_colours):
        return duster
   else:
        return megan
print(car_max_colors(dct.carro))