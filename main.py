def txt_read1():
    encrypt = ''
    with open(filename1, 'r', encoding='utf-8') as f:
        encrypt = encrypt.join(f)
    return encrypt

def encryption(encrypt, key):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in encrypt.lower():
        if letter in alphabet:
            position = alphabet.find(letter)
            newPosition = (position + key) % len(alphabet)
            encrypted += alphabet[newPosition] 
        else:
            encrypted += letter
    return encrypted

def text_write(encrypted):
	with open(filename2, 'w', encoding='utf-8') as f:
		f.write(encrypted)

def txt_read2():
	encrypt = ''
	with open(filename2, 'r', encoding='utf-8') as f:
		encrypt = encrypt.join(f)
	return encrypt

def decryption(encrypt, key):
	encryptedd = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in encrypt.lower():
		if letter in alphabet:
			position = alphabet.index(letter)
			newPosition = (position - key) % len(alphabet)
			encryptedd += alphabet[newPosition]
		else:
			encryptedd += letter
	return encryptedd

def text_write2(encryptedd):
    with open(filename3, 'w', encoding='utf8') as f:
        f.write(encryptedd)


filename1 = input('Какой файл зашифровать?: ')
filename2 = input('В какой файл разместить зашифрованный текст?: ')
filename3 = input('В какой файл разместить расшифрованный текст?: ')
key = int(input('Введите ключ(от 1 до 25): ')) 

encrypt =  txt_read1()
encrypt = encryption(encrypt, key)
text_write(encrypt)

encrypt = txt_read2()
encrypt = decryption(encrypt, key)
text_write2(encrypt)
print("Операция произошла успешна!")
