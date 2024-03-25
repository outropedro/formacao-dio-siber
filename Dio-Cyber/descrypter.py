import os 
import pyaes

#abre o arquivo criptografado
file_name = "teste.txt.ransomwaretroll"
fie = open(file_name, "rb")
file_data = file.read()
file.close()

#chave de descoptografia
 
key = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# remover arquivo criptografado

os.remove(file_name)

#criar arquivo descriptografado

new_file = "teste.txt"
new_file = open(f"{new_file}", "wb")
new_file.write(decrypt_data)
new_file.close()