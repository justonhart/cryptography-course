key = "ourfatherwhoartinheaven"

alphamap = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}

with open('decrypted.txt', "w") as o:
    with open('encrypted.txt', mode='r') as f:
        contents = f.read()
        for idx, char in enumerate(contents):
            if char.isalpha():
                keyVal = alphamap[key[idx % len(key)]] 
                cryptVal = alphamap[char.lower()] 
                decryptVal = (cryptVal - keyVal) + 26 if cryptVal - keyVal <= 0 else cryptVal - keyVal
                decryptChar = list(alphamap.keys())[list(alphamap.values()).index(decryptVal)]
                print(decryptChar, file=o, end='')
            else:
                print(char, file=o, end='')
    f.close()
o.close()

