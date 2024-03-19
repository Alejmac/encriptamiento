import Encriptar

#se genera la clase
clave_secreta = Encriptar.generar_clave()
#el texto a encriptar es
texto = "todo lo bueno pasa por algo"
#encriptar texto
texto_encriptado = Encriptar.encriptar_texto(texto,clave_secreta)

print("*"*50)
print(f"texto a encriptar \t {texto} \n")
print(f"texto encriptado \t {texto_encriptado}")
print("*"*50)

# para desencriptar
texto_desencriptado = Encriptar.desencriptar_texto(texto_encriptado,clave_secreta)
print(f"El texto desencriptado es \t{texto_desencriptado}")
print("*"*30)