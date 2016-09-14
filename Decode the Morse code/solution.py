'''
Best practice:

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
'''

def decodeMorse(morseCode):
    code = morseCode.strip()
    s = list()
    w = list()
    for word in code.split('   '):
        for char in word.split(' '):
            w.append(MORSE_CODE[char])
        s.append(''.join(w))
        del w[:]
    return ' '.join(s)