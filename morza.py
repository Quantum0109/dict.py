morse_dict = {
	"а" : ".-",
	"б" : "-...",
	"в" : ".--",
	"г" : "--.",
	"д" : "-..",
	"е" : ".",
	"ж" : "...-",
	"з" : "--..",
	"и" : "..",
	"й" : ".---",
	"к" : "-.-",
	"л" : ".-..",
	"м" : "--",
	"н" : "-.",
	"о" : "---",
	"п" : ".--.",
	"р" : ".-.",
	"с" : "...",
	"т" : "- ",
	"у" : "..-",
	"ф" : "..-.",
	"х" : "....",
	"ц" : "-.-.",
	"ч" : "---.",
	"ш" : "----",
	"щ" : "--.-",
	"ъ" : "--.--",
	"ы" : "-.--",
	"ь" : "-..-",
	"э" : "..-..",
	"ю" : "..--",
	"я" : ".-.-",
	" " : " "
}



text = "Привет"
def morse_encode(text: str) -> str:
	text = text.lower()
	encoded_text = []
	for letter in text:
		encoded_text.append(morse_dict[letter])

	return " ".join(encoded_text)


print(morse_encode(text))
assert list (morse_encode(' ')) == [' ']
assert list (morse_encode('питон')) == ['.--. .. - --- -.']
assert list (morse_encode('при вет')) == ['.--. .-. ..   .-- . - ']