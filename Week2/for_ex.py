devs = {
    0:'Victor',
    1:'Christian',
    2:'Ignacio',
    3:'Daniel',
    4:'Sendy',
    5:'Fernanda',
    6:'Daniela'
}

for key, dev in devs.items():
    for key2, dev2 in devs.items():
        if dev[-1]==dev2[-1] and key!=key2:
            print(dev)
        