# Usando a imagem base do Python
FROM python:3.12-slim

# Definindo o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiando o arquivo de dependências
COPY requirements.txt .

# Instalando as dependências
RUN pip install -r requirements.txt

# Copiando o código da aplicação para o contêiner
COPY . /app

# Adicionando o diretório /app/src ao PYTHONPATH
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Comando para rodar a aplicação
CMD ["python", "src/index.py"]
