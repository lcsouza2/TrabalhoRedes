import ipaddress

#Nomes do grupo: Luiz Carlos, Elias Batista, Luiz Eduardo, Gabriel Miranda

def ObterIpDestino():
    global ip_destino
    ip_destino = input("Digite o endereço IP de destino: ")
    print("Endereço recebido")
    return int(ip_destino.replace(".",""))

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
            print("Endereços carregados com sucesso")
            return enderecos
    except FileNotFoundError:
        print(f"O arquivo {arquivo} não foi encontrado.")
        return {}

def calc_checksum():
    with open('arquivos/hexapacket.sem.cks.txt','r') as file:
        frame = file.read()

    number = frame[:-1]
    soma=i=0
    j=4
    while (i < len(number)):
        soma += int(number[i:j], base=16)
        i+=4
        j+=4
    print("Checksum calculado")
    return hex(soma%65536) #Retorna o valor do cálculo em hexadecimal para a função 

def checar_subrede(ip1, ip2, mascara_subrede):
    rede = ipaddress.ip_network(f'{ip1}/{mascara_subrede}', strict=False)
    return ipaddress.ip_address(ip2) in rede

def gravar_pacote():
    ip_destino_bruto = ObterIpDestino()
    ip_destino_processado = hex(ip_destino_bruto).split("x")

    with open("arquivos/netsettings.host.txt", "r") as file:
        dados_endereco = file.readlines()
        for i in dados_endereco:
            if "address 192.168.5.100" in i: 
                ip_origem = i.split()[1]
            if "netmask 255.255.255.0" in i:
                netmask = i.split()[1]    

    if checar_subrede(ip_origem, ip_destino, netmask) is True:
        print("Os IPs estão na mesma subrede!")
    else:
        print("Os IPs não estão na mesma subrede!")

    pacote_gravar = ""

    with open("arquivos/packet.txt", "r") as dados_pct:
        dados_arquivo = dados_pct.readlines()
    
    for i in dados_arquivo:
        lista_dados = i.split(":")
        pacote_gravar += lista_dados[1][2:].strip()

        if lista_dados[0] == "CHECKSUM":
            pacote_gravar += calc_checksum()[2:]
    
        if lista_dados[0] == "IP DESTINO":
            pacote_gravar += ip_destino_processado[1]
    print("Pacote gravado, cheque a pasta ethernet")
    with open("ethernet/spacket.txt", "w") as pct_gravar:
        pct_gravar.write(pacote_gravar.upper())
    
    global continuar
    continuar = input("Deseja gravar mais um pacote? Digite S para sim e qualquer coisa para não: ").upper()
gravar_pacote()

while continuar == "S":
    print("\n")
    gravar_pacote()