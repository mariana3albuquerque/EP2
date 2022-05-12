import random 
def sorteia_letra(s, l):
    ac = ['.', ',', '-', ';', ' ']
    s = s.lower()
    for e in (ac + l):
        s = s.replace(e, '')
    if len(s) == 0:
        return ''
    return random.choice(s)
    