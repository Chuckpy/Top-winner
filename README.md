# Sistema de Armazenamento, Compra e Venda


## História e Objetivo : 
O projeto  tem como objetivo ser uma aplicação para gestão de produtos, venda e compra de produtos e serviços, bem como a inteligência de armazenamento. A aplicação hoje é feito em Django e segue os principios [REST](https://www.infoq.com/br/articles/rest-introduction/) para que possa ter um front-end agradável futuramente.
## Principais Caracteristicas :
- Design Responsivo 
- Fácil Entendimento e Adaptação
- Fácil Escalabilidade 
## Principais Funcionalidades :
- Administração Personalizada (Filtros, Aparência, ações e etc personalizáveis)
- Registro, organização e controle de armazenamento dos produtos
- Registro e controle de serviços
- Controle e registro de vendas de serviços e produtos (Por diversos tipos de usuários)
- Controle e registro de compras de produtos (Somente com autorização prévia)
- Dashboard para controle e análise de dados
- Controle de divulgação externa da plataforma

## Em construção :

O projeto iniciou sendo uma maneira de estudos, e hoje esta tomando novas proporções, por isso esta sendo revisto as bases e refatorado para que possa ser usado em diferentes plataformas, por isso ***não esta em processo de produção***

## Como Inicializar :

Caso você não tenha o repositório em seu computador, basta clona-lo na pasta que deseja :
```bash
git clone https://github.com/Chuckpy/Management-Sistem.git
```
Feito isso, basta acessar contruir os container com o docker-compose:
```bash
docker-compose up -build
```
Se tudo deu certo até aqui, você pode subir os containers e ver o servidor funcionando com :
```bash
docker-compose up -d
```
### Parabéns  !
Se chegou até aqui, ***parabéns*** ! Veja em seu servidor local que ele esta funcionando normalmente, clique aqui para ver ele funcionando  => [AQUI](http://0.0.0.0:8000/) : 

### Vamos rodar as migrações :

Feito tudo de acordo, vamos dar continuidade no projeto fazendo as migrações (sempre lembando que o nome dos containers pode ser diferente, caso você tenha alterado manualmente)

```bash
docker exec open-rest-app_web_1 python3 manage.py makemigrations
docker exec open-rest-app_web_1 python3 manage.py migrate
```
E da mesma maneira você pode acessar o sistema administrativo com um "superusuario", criado facilmente com o comando :

```bash
docker exec open-rest-app_web_1 python3 manage.py createsuperuser
```
E finalmente, derrubar os containers, com o comando :
```bash
docker-compose down
```

## Como contribuir com o projeto :

O projeto foi imaginado inicialmente para ser open source, portanto, caso queira apoiar o projeto codando conosco, sinta-se a vontade.
Veja os relatórios e onde pode ajudar em [Questões]('')

### Apoia-se :
Se gostou do que viu até aqui, você pode apoiar com qualquer valor [AQUI](https://apoia.se/gestaopen)
