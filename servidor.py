# Servidor web simples, trabalho de redes

from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM) 
#AF_INET é para endereços do tipo IPv4
#Sock_STREAM só ta falando que a conexão é TCP



dataPayLoad = 2048
# máximo de dados que vai poder receber 



serverAddress = ('127.0.0.1', 6789)


serverSocket.bind(serverAddress)
# vincula o socket que eu criei na porta 6789

serverSocket.listen(1)
#definindo número de conexões pendentes para eté 1
try:
    while(True):
        print("Começando a rodar o servidor")

        (connectionSocket, addr) = serverSocket.accept()
        # Essa parada de accept manda uma tupla quando a conexão é liberada


        try:
            message = connectionSocket.recv(dataPayLoad).decode()
            filename = message.split()[1]


            f = open(filename[1:]) # abre o arquivo html requisitado
            outputdata = f.read() # lê o arquivo

            print(f"Message: {message}")

            data    =   "HTTP/1.1 200 OK\r\n"
            data    +=  "Content-Type: text/html; charset = utf-8\r\n"
            data    +=  "\r\n"
            data    +=  outputdata
            connectionSocket.sendall(data.encode())

        except IOError:
            error   =   "HTTP/1.1 404 Not Found\r\n\r\n"
            error   +=  "<html><body><h1>404 Not Found</h1></body></html>"

            connectionSocket.sendall(error.encode())
        
        finally:
            connectionSocket.close()

except KeyboardInterrupt:
    print("\nFechando servidor pelo teclado: CTRL + C")

finally:
    serverSocket.close()
    sys.exit()