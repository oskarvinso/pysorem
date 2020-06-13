import socket #se importa la libreria socket
EncBuff = 10
#AF_INET hace referencia a IPv4 SOCK_STREAM es TCP/import ipdb; ipdb.set_trace()
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('localhost', 7777)) #se define el host y el puerto

while True:
    MensComp = ""
    MensNuevo = True
    while True:
        MensResp = s2.recv(16)#buffer cuantos datos va a recibir
        if MensNuevo:
            MensLarg = int(MensResp[:EncBuff])
            MensNuevo = False

        MensComp += MensResp.decode("utf-8")#se decodifica el mensaje por que viene en bytes

        if len(MensComp)-EncBuff == MensLarg:
            print(MensComp[EncBuff:])
            MensNuevo = True
            MensComp = ""

    print (MensComp)
