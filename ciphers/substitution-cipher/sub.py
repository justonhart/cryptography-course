key = {
	"a":"q",
	"b":"h",
	"c":"o",
	"d":"z",
	"e":"s",
	"f":"m",
	"g":"p",
	"h":"e",
	"i":"d",
	"j":"g",
	"k":"t",
	"l":"f",
	"m":"c",
	"n":"a",
	"o":"u",
	"p":"k",
	"q":"n",
	"r":"i",
	"s":"y",
	"t":"r",
	"u":"j",
	"v":"b",
	"w":"x",
	"x":"v",
	"y":"w",
	"z":"l"
}
with open('encrypted.txt', "w") as o:
    with open('message.txt', mode='r') as f:
        contents = f.read()
        for char in contents:
            cryptchar = key.get(char.lower())
            if cryptchar:
                print(cryptchar, file=o, end='')
            else:
                print(char, file=o, end='')
    f.close()
o.close()

