import matplotlib.pyplot as plt
import numpy as np


def NRZI(array, lenght):
    nrzi = []
    aux = 0  # houve mudança
    for i in range(lenght):
        if array[i] == 1:
            if aux == 1:
                aux = 0
            else:
                aux = 1
        nrzi.append(aux)
    # nrzi.append(1)
    return nrzi, 0, "NRZI"


def NRZL(array, lenght):
    nrzl = []
    aux = 0
    for i in range(lenght):
        if(array[i] == 1):
            aux = 0
        else:
            aux = 1
        nrzl.append(aux)
    # nrzl.append(0)
    return nrzl, 0, "NRZL"


def AMI(array, lenght):
    ami = []
    aux = -1
    for i in range(lenght):
        if(array[i] == 1):
            aux = aux * -1
            ami.append(aux)
        else:
            ami.append(0)
    # ami.append(1)
    return ami, 0, "AML"


def PSEUDO(array, lenght):
    pseudo = []
    aux = 1
    for i in range(lenght):
        if(array[i] == 1):
            pseudo.append(0)
        else:
            pseudo.append(aux)
            aux = aux * -1
    return pseudo, 0, "PSEUDO"


def MANCHESTER(array, lenght):
    manchester = []
    for i in range(lenght):
        if(array[i] == 0):
            manchester.append(1)
            manchester.append(0)
        else:
            manchester.append(0)
            manchester.append(1)
    return manchester, 1, "MANCHESTER"


def DIFMANCHESTER(array, lenght):
    difmanchester = []
    aux = 1
    difmanchester.append(aux)
    for i in range(lenght):
        if(array[i] == 0):
            if(aux == 1):
                difmanchester.append(0)
                difmanchester.append(1)
            else:
                difmanchester.append(1)
                difmanchester.append(0)
                aux = 0
        else:
            if(aux == 1):
                difmanchester.append(1)
                difmanchester.append(0)
                aux = 0
            else:
                difmanchester.append(0)
                difmanchester.append(1)
                aux = 1
    return difmanchester, 1, "DIFMANCHESTER"

def MLT3(array, lenght):
    mlt3 = []
    ult1 = -1
    aux = 0
    mlt3.append(aux)
    for i in range(lenght):
        if array[i] == 1:
            if aux == 1:
                aux = 0
                ult1 = 1
            elif aux == -1:
                aux = 0
                ult1 = -1
            else: # aux == 0
                if ult1 == 1:
                    aux = -1
                    ult1 = -1
                else: #ult1 == -1
                    aux = 1
                    ult1 = 1
        mlt3.append(aux)
    mlt3.append(0)
    return mlt3, 1, "MLT3"

def BINDIF(array, lenght):
    bindif = []
    aux = array[0]
    bindif.append(aux)
    for i in range(lenght - 2): 
        bindif.append(aux)
        aux = array[i+2] - array[i+1]

    bindif.append(aux)
    bindif.append(aux)
    return bindif, 1, "BINDIF"


ex = [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1]
#bitstream = [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]
bitstream = [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0]

array, opcode, text = BINDIF(bitstream, len(bitstream))
#array, opcode, text = BINDIF(ex, len(ex))

#nrzi.insert(0, 0)

# Criar os eixos de tempo e amplitude
t = list(range(len(array)))

t = np.arange(1, len(array) + 1)

amplitude = array

if(opcode == 1):
    plt.xticks(np.arange(0, len(array), 2))
else:
    plt.xticks(np.arange(0, len(array), 1))

# Plotar o sinal NRZ-I
plt.step(t, amplitude, where='post', color='red')

# Configurar os rótulos dos eixos e o título do gráfico
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.title('Representação de código de linha '+ text)
plt.grid(axis = 'x')

# Exibir o gráfico
plt.show()
