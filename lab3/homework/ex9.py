def get_even_list(a):
    if type(a) == list:
        evenl = []
        for i in a:
            if i % 2 == 0:
                evenl.append(i)
        return evenl
    else:
        print("wrong format")
    
    