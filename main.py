#Recebe o Ip de destino e o armazena {

def ObterIpDestino():
  IpDestino = input("Digite o endereço IP de destino: ")
  return IpDestino

# Exemplo de uso
IpDestino = ObterIpDestino()
print("Endereço IP de destino digitado:", IpDestino)

# }

ip = """
VERSÃO DO IP: 0x4
TAMANHO DO CABEÇALHO: 0x5
SERVIÇOS DIFERENCIADOS: 0x00
TAMANHO TOTAL: 0x002E 
IDENTIFICAÇÃO, FLAGS E OFFSET: 0x00000000
TTL: 0x00
PROTOCOLO: 0x11
CHECKSUM: 0xD0E7
IP ORIGEM: 0xC0A80501 (192.168.5.1)
IP DESTINO: 0xC0A80564 (192.168.5.100)
DADOS: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
"""
with open("packet.txt","w") as a:
    a.write(ip)

def carregar_enderecos(arquivo):
    try:
        with open(arquivo, 'w+') as f:
            linhas = f.readlines()
            enderecos = {}
            for linha in linhas:
                if linha.strip():  # Ignora linhas em branco
                    partes = linha.split('=')
                    if len(partes) == 2:
                        chave, valor = partes[0].strip(), partes[1].strip()
                        enderecos[chave] = valor
            return enderecos
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return {}

# Exemplo de uso
arquivo = "netsettings.host.txt"
enderecos = carregar_enderecos(arquivo)
print("Endereços carregados:")
for chave, valor in enderecos.items():
    print(f"{chave}: {valor}")


#Calcular checksum {

def CalcChecksum():
  with open('hexapacket.sem.cks.txt','w') as arquivos:
    arquivos.write("4500002E0000000000110000C0A80501C0A80564FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
  
  with open('hexapacket.sem.cks.txt','r') as file:
      frame = file.read()
  number = frame[:-1]
  soma=i=0
  j=4
  while (i < len(number)):
     soma += int(number[i:j], base=16)
     i+=4
     j+=4
  return hex(soma%65536) #Retorna o valor do cálculo em hexadecimal para a função 

#}