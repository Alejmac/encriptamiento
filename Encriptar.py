from cryptography.fernet  import Fernet

# vamo hacer unprograma en python para hacer un cifrado simetrito
#fernet garatiza el cifrado , con e no podra ser manipuado sin tener la clave
#fernet es una implementacion de criptografia autenticada simetrica
#tambien conocida como clave secreta
def generar_clave ():
    return Fernet.generate_key()

#clave de 32 bytes codificada a base de 64
def encriptar_texto(texto,clave):
    f = Fernet(clave)
    texto_encriptado= f.encrypt(texto.encode())
    return texto_encriptado

def desencriptar_texto(texto,clave):
    f= Fernet(clave)
    texto= f.decrypt(texto).decode()
    return texto
