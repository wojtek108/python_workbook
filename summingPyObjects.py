def isint(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

def sum_int(lista):
    output = sum(item for item in lista if isint(item))
    return output

print(sum_int([1, 2, 3, 4, 5, 'Wojtek']))
    
