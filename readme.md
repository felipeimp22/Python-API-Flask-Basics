pipenv shell < --- cria o ambiente virtual
pipenv install  < --- instala as dependencias
pipenv install --dev < --- instala as dependencias de dev
pipenv graph < --- Mostra o arquivo pipfile
pipenv check < --- Verifica se há vulnerabilidade de segurança


----------------------------------------------------------
Podemos instalar versões especificas de libs com pipenv, e multiplos pacotes de uma vez exemplo:

Selecionando versão:
pipenv install requests==2.13.0

Instalando multiplos pacotes: 
pipenv install requests django pytest

----------------------------------------------------------
Desinstalando pacotes com pipenv:

pipenv unistall requests

pipent unistall  --all

pipent unistall  --all-dev

----------------------------------------------------------
é possivel rodar comandos pelo pipenv exemplo:

pipenv run django-admin

----------------------------------------------------------
escolhendo versão do python

instale o pyenv para ele orquestrar as versoes do python e por fim rode os comandos:

pipenv --two <--- comando passando a flag para trocar a versão do python
pipenv --python 2.0.1 <--- comando passando a flag para trocar a versão do python

----------------------------------------------------------
Pesquisar:

* poetry
* hatch