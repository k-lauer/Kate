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

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)

if __name__ == "__main__"
    file1 = open('KateLauer_original.txt')
    read_file1 = file1.readlines()

    for line in file1:
        words = line.split()
        encrypted_line = []
        for word in words:
            encrypted_word = ""
            for char in word.lower()
                encrypted_word += chr((ord(letter)+shift -97))%26+97

            enctrypted_line.append

        encrypted_file.write(' ',join(encrypted_line))


