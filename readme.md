### Comandos basicos

pipenv shell < --- cria o ambiente virtual <br/>
pipenv install  < --- instala as dependencias <br/>
pipenv install --dev < --- instala as dependencias de dev <br/>
pipenv graph < --- Mostra o arquivo pipfile <br/>
pipenv check < --- Verifica se há vulnerabilidade de segurança <br/>


----------------------------------------------------------
### Podemos instalar versões especificas de libs com pipenv, e multiplos pacotes de uma vez exemplo:

Selecionando versão: <br/>
> pipenv install requests==2.13.0 <br/>

Instalando multiplos pacotes: <br/>
> pipenv install requests django pytest <br/>

----------------------------------------------------------
### Desinstalando pacotes com pipenv:

> pipenv unistall requests <br/>

> pipent unistall  --all <br/>

> pipent unistall  --all-dev <br/>

----------------------------------------------------------
### É possivel rodar comandos pelo pipenv exemplo:

> pipenv run django-admin <br/>

----------------------------------------------------------
### Escolhendo versão do python

instale o pyenv para ele orquestrar as versoes do python e por fim rode os comandos: <br/>

> pipenv --two <--- comando passando a flag para trocar a versão do python <br/>
> pipenv --python 2.0.1 <--- comando passando a flag para trocar a versão do python <br/>

----------------------------------------------------------
### Pesquisar:

* poetry <br/>
* hatch <br/>