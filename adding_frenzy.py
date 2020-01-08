

"""
                                                pierwsza -> druga -> trzecia -> czwarta
                           druga -> pierwsza -> /\
     czwarta -> trzecia -> /\
                           pierwsza -> czwarta -> druga -> pierwsza -> /\
"""

def add(a, b):

    mapper = {
        'o̵̶': 'o̶̵',  # 1 -> 2
        'o̶̵': 'o̵̶',  # 2 -> 1
        'o̶': 'o̵',  # 3 -> 4
        'o̵': 'o̶',  # 4 -> 3
    }

    def o̵̶(a, b):
        print('pierwsza')
        return o̶̵(a, b)

    def o̶̵(a, b):
        print('druga')
        return a + b

    def o̶(a, b):
        print('trzecia')
        return a + b

    def o̵(a, b):
        print('czwarta')
        return a + b

    o̵̶(a, b)  # 1
    o̶̵(a, b)  # 2
    o̶(a, b)  # 3
    o̵(a, b)  # 4
    # return o̶̵(a, b)
