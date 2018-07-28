import socket

def enviarMsg():
    porta = 9100
    ip = '10.125.229.195'
    endereco = (ip, porta)
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(endereco)
    mensagem = raw_input('Digite uma mensagem: ')
    if(mensagem == ''): return False
    cliente_socket.send(str.encode(mensagem))
    cliente_socket.close()

    return True;

def enviar():
    if enviarMsg():
        enviar()

if __name__ == '__main__':
    enviar()