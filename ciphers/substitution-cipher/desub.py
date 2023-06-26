key = {
	"q":"a",
	"h":"b",
	"o":"c",
	"z":"d",
	"s":"e",
	"m":"f",
	"p":"g",
	"e":"h",
	"d":"i",
	"g":"j",
	"t":"k",
	"f":"l",
	"c":"m",
	"a":"n",
	"u":"o",
	"k":"p",
	"n":"q",
	"i":"r",
	"y":"s",
	"r":"t",
	"j":"u",
	"b":"v",
	"x":"w",
	"v":"x",
	"w":"y",
	"l":"z"
}
with open('decrypted.txt', "w") as o:
    with open('encrypted.txt', mode='r') as f:
        contents = f.read()
        for char in contents:
            cryptchar = key.get(char.lower())
            if cryptchar:
                print(cryptchar, file=o, end='')
            else:
                print(char, file=o, end='')
    f.close()
o.close()

