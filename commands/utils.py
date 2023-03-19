def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def remove_mentions(mesaj):
    start = mesaj.find('<')
    end = mesaj.find('>')
            
    while (start>-1 and end>-1):
        lun = len(mesaj)
        mesaj = mesaj[0: start] + mesaj[end+1: lun]
        start = mesaj.find('<')
        end = mesaj.find('>')
            
    while mesaj.startswith(" "):
        mesaj = mesaj[1:]
        
    while "  " in mesaj:
        mesaj = mesaj.replace("  ", " ")
        
    return mesaj