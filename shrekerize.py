def St(value, format):
    if format == 's':
        time = int(value) / 5400
    elif format == "m:s":
        form = str(value).split(':')
        time = (int(form[0])*60 + int(form[1])) / 5400
    elif format == "h:m:s":
        form = str(value).split(':')
        time = (int(form[0])*60**2 + int(form[1])*60 + int(form[2])) / 5400

    return time


def Sl(value, format):
    if format == 'm':
        length = value/2.44
    elif format == "ft":
        length = (value*0.3048)/2.44
    elif format == "mi":
        length = (value*1609.344)/2.44
    

    return length

print(Sl(8, 'mi'))