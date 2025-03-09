import os

# Nome do arquivo de entrada
arquivo_fasta = "arquivos_fasta.fa"

# Pasta onde os arquivos serão salvos
pasta_saida = "PaVE_Download"
os.makedirs(pasta_saida, exist_ok=True)  # Criar a pasta se não existir

# Ler o arquivo e dividir pelo ">"
with open(arquivo_fasta, "r") as f:
    conteudo = f.read().strip().split(">")  # Divide pelo ">"

# Salvar cada sequência em um arquivo separado dentro da pasta de destino
for seq in conteudo:
    if seq.strip():  # Ignorar sequências vazias
        linhas = seq.split("\n")  # Divide o identificador e a sequência
        identificador = linhas[0].strip().split()[0]  # Pega o primeiro termo do identificador
        sequencia = "".join(linhas[1:]).replace("\n", "")  # Junta todas as linhas da sequência

        # Criar o nome do arquivo dentro da pasta correta
        nome_arquivo = f"{identificador}.fasta"

        # Garantir que o nome seja válido (removendo caracteres indesejados)
        nome_arquivo = "".join(c for c in nome_arquivo if c.isalnum() or c in "._-")

        # Caminho final do arquivo dentro da pasta correta
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)

        # Escrever o arquivo na pasta correta
        with open(caminho_completo, "w") as f_out:
            f_out.write(f">{linhas[0].strip()}\n{sequencia}\n")  # Mantém o identificador e coloca a sequência em uma única linha

        print(f"Arquivo salvo: {caminho_completo}")  # Debug para confirmar o salvamento

print(f"\nTodos os arquivos foram movidos para '{pasta_saida}'.")
