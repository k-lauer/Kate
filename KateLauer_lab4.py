def get_shift():
    try:
        shift = int(input('Enter a number to shift by: '))
        if shift in range (1, 27)
            return shift
        else: 
            print('Invalid Number')
            return get_shift()
    except: 
        print('Invalid Number')
        return get_shift()

file1 = open('KateLauer_original.txt')
read_file1 = file1.read()

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)