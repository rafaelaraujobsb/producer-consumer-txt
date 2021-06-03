<div align="center"><h1>Producer Consumer Text</h1></div>


## ✒️ Introdução
N/A
## 🔌 Instalação da Aplicação
N/A
## ⚙️ Variáveis de ambiente
| Nome | Descrição | Default |
|-|-|-|
|None|None|None|
## 📀 Iniciar Aplicação
**Geração do certificado SSL**

O arquivo [gerar_ssl.sh](./ssl/gerar_ssl.sh) faz a varificação se existe os arquivos `server.key` e `server.cert` dentro do container, se não existir, esses arquivos serão gerados de forma automática. Caso já tenha um certificado SSL adicione eles na pasta [ssl](./ssl) e eles serão utilizado pelo container.

**Atenção:** esses arquivos devem ser adicionados manualmente no servidor de execução e não devem ir para o git, como forma de evitar acidentes no [.gitignore](.gitignore) foi adicionado a remoção de arquivos com `.key` e `.cert`

## 🧪 Executar Testes
N/A
## 🛠️ Ferramentas Utilizadas
<a href="https://docs.python.org/3.8/">Python3.8</a><br>
<a href="https://fastapi.tiangolo.com/">FastAPI</a><br>
<a href="https://gunicorn.org/">Gunicorn</a><br>
<a href="https://github.com/Delgan/loguru">Loguru</a><br>
<a href="https://pylama.readthedocs.io/en/latest/">Pylama</a><br>

## 🧔 Responsáveis pelo projeto
<p><a href="mailto:EMAIL_DEV@automatizai.com.br">NOME DESENVOLVEDOR</a></p>
<div align="center"><img width="500" alt="Logo automatizAI" src="https://automatizai.com.br/assets/img/automatizai-logo.svg"></div>