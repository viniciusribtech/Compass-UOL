import hashlib
while True: 
    entrada = input("Texto a ser mascarado: ")
    hash = hashlib.sha1(entrada.encode()).hexdigest()
    # "entrada.encode" converte a string em Bytes, pq sha1() usa Bytes
    print("SHA-1: ", hash)
    # Usando "Ctrl+C" termina o loop criado