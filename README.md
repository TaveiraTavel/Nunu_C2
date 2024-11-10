---

# Nunu C2

Nunu C2 é um projeto de segurança voltado ao estudo e entendimento do funcionamento de um Command and Control (C2). Através deste projeto, é possível observar como um C2 opera, desde o controle remoto de agentes até a execução de comandos neles.

O Nunu C2 está usando o protocolo ICMP para comunicação entre o servidor e os agentes, mas construído de forma escalável, para futuras implementações de outros protocolos, como DNS, HTTP, HTTPS, SMTP...

Algumas outas adições válidas: Criptografia Assimétrica, Proccess Injection, Persistência...

## Funcionalidades

- **Modo de Infecção**:
  - Permite a configuração de parâmetros do payload, como LHOST, LPORT, RHOST e CHANNEL.
  - Geração de payloads personalizados.

- **Modo de Controle**:
  - Controle de agentes infectados através do envio de comandos.
  - Listagem de agentes ativos.
  - Execução de comandos remotos em sistemas comprometidos.

- **Comunicação via ICMP**:
  - O Nunu C2 utiliza pacotes ICMP (ping) para comunicação entre o servidor e os agentes.
  - A comunicação é discreta e pode passar por filtros de firewall.
  
- **Persistência de Sessões**:
  - As configurações e estados dos agentes são salvos em arquivos JSON, permitindo que as sessões sejam recuperadas a qualquer momento.

## Estrutura do Projeto

- **`auxiliary/`**: Contém módulos auxiliares, como comandos, opções e interface de usuário.
- **`channels/`**: Implementações dos canais de comunicação, incluindo ICMP.
- **`main/`**: Contém os módulos principais, como controle de agentes e payloads.
- **`stagers/`**: Scripts responsáveis pela inicialização da infecção nos sistemas alvo.

## Instalação

Para executar o Nunu C2, é necessário ter o Python e algumas dependências instaladas.

### Requisitos

- Python 3.x
- Scapy (biblioteca para manipulação de pacotes de rede)

### Instalação de Dependências

```bash
pip install scapy
```

### Rodando o Projeto

1. **Modo de Infecção**:
   - No modo de infecção, configure o servidor e o alvo, definindo os parâmetros `LHOST`, `LPORT`, `RHOST` e o canal de comunicação (ICMP).
   - Gere o payload e aguarde a infecção do sistema alvo.

2. **Modo de Controle**:
   - Após a infecção do sistema, você pode alternar para o modo de controle para gerenciar os agentes infectados.
   - Liste os agentes ativos, envie comandos ou finalize sessões.

3. **Comunicação via ICMP**:
   - O agente utiliza pacotes ICMP para se comunicar com o servidor, enviando e recebendo comandos via "ping".

## Comandos

### Comandos Gerais

- **`help`**: Exibe o menu de ajuda.
- **`mode <infection|control>`**: Alterna entre os modos de Infecção e Controle.
- **`exit`**: Encerra o programa.

### Comandos de Infecção

- **`set <option> <value>`**: Define as variáveis do payload. Exemplo: `set LHOST 192.168.1.1`.
- **`unset <option>`**: Remove uma variável do payload.
- **`options`**: Exibe as opções do payload.
- **`make`**: Gera um payload para infectar o alvo.
- **`wait`**: Aguarda a infecção do sistema alvo.

### Comandos de Controle

- **`agents`**: Lista os agentes ativos.
- **`use <ip> <channel>`**: Seleciona um agente para controle.
- **`cmd <command>`**: Executa um comando no agente selecionado.
- **`kill`**: Finaliza o agente atual.

## Exemplo de Uso

1. Inicie o Nunu C2 no modo de infecção:

```bash
sudo python3 nunu.py
```

2. Defina as configurações do payload:

```bash
Nunu> help
Nunu> options
Nunu> set LHOST 192.168.1.100
Nunu> set RHOST 192.168.1.200
Nunu> set CHANNEL ICMP
```

3. Gere o payload:

```bash
Nunu> make
```

4. Aguarde a infecção:

```bash
Nunu> wait
```

5. No modo de controle, gerencie os agentes:

```bash
Nunu> mode control
Nunu> agents
Nunu> use 192.168.1.200 ICMP
Nunu> cmd whoami
Nunu> cmd dir C:\
```

## Contribuindo

Este é um projeto de estudo e pesquisa em segurança cibernética. Se você encontrar algum bug ou tiver sugestões para melhorias, fique à vontade para abrir um issue ou enviar um pull request.

## Aviso Legal

Este projeto é destinado apenas para fins educacionais. O uso deste código para realizar atividades ilegais é estritamente proibido. A responsabilidade pelo uso do código é de quem o utilizar.
