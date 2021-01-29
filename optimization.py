portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route,ports):
    if not ports:
        print(' '.join([portnames[i] for i in route]))
    for index, element in enumerate(ports):
        permutations(route + [element],ports[:index] + ports[index+1:])

def main():
    permutations([0],list(range(1, len(portnames))))