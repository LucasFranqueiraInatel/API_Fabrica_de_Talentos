# API realizada durante a fabrica de Talestos

## Professor>
 https://github.com/flaviobergamini

 ## Novas Futuras
caso queira criar um ambiente virtual, siga os passoas:
 ### Entre na pasta do projeto da API, ou onde está o requirements.txt: 
 cd Vendas

 ### Crie um ambiente virtual: 
 python -m venv venv

 ### Ative seu ambiente virtual, para o Windows, o comando é: 
 venv\Scripts\activate
 ### Se tiver no Linux ou mac: 
 source venv\bin\activate

 ### Instale as dependências do arquivo requirements.txt: 
 pip install -r requirements.txt

 ### Faça a migração para construir o banco de dados se for relacional, como o nosso caso: 
 python manage.py migrate

 ### Se der tudo certo na migração, o processo está concluído, basta executar o comando: 
 python manage.py runserver

 ### Para atualizar(caso queira) o arquivo requirements.txt:
 pip freeze > requirements.txt
