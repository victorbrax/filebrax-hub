<div align="center">
  <table>
  <tr>
    <td><img height="24rem" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/0752b2c1c65a0862a346f7d0e93ca1a3fbd0447b/docs/us.svg" alt="euaflag"></td>
    <td>Do you speak English? Please, <a href="https://github.com/victorbrax/filebrax-hub">click here</a>.</td>
  </tr>
</table>
</div>




<div align="center">
  
[![Projeto](https://img.shields.io/badge/PROJETO_REAL-important.svg)]()
[![Python](https://img.shields.io/badge/Python-informational.svg)]()
[![Jinja2](https://img.shields.io/badge/Jinja2-green.svg)]()
[![Flask](https://img.shields.io/badge/Flask-gray.svg)]()
[![Bootstrap](https://img.shields.io/badge/Bootstrap-red.svg)]()
[![Blueprints](https://img.shields.io/badge/Blueprints-blue.svg)]()
[![Javascript](https://img.shields.io/badge/Javascript-yellow.svg)]()
</div>


<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/main/docs/logo-github-photo.png">
</div>
</div>
<p align="center">Por <strong>Víctor Gomes</strong></p>

# É um prazer ter você aqui! ⚜

O Filebrax Hub (que não tem nenhuma semelhança com o meu nickname) é um projeto totalmente funcional para lidar com uploads e downloads de arquivos em um servidor. Ele foi desenvolvido usando o Flask como seu Micro Framework, com o objetivo de fornecer um ambiente interno eficiente. Além disso, graças à sua arquitetura bem estruturada usando Blueprints, ele permite a fácil integração de módulos adicionais de backend (e. g., [Tracker Tickets](https://github.com/victorbrax/TrackerG), um aplicativo de rastreamento e gerenciamento que pretendo lançar em breve).
</br>
</br>

## Visualização 🖼️

Em breve, disponibilizarei as páginas principais do aplicativo de forma não funcional, utilizando a funcionalidade de páginas do GitHub para usuários inexperientes em programação.
</br>

<div align="center">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/navigation.gif?raw=true">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/validacao.gif?raw=true">
</div>
<div align="center">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/collapse.gif?raw=true">
<img height="220vh" src="https://github.com/victorbrax/filebrax-hub/blob/main/docs/gifs/404.gif?raw=true">
</div>

## Rode o projeto localmente 🏠

Garanta que você tenha o [Python](https://python.org/downloads) instalado para rodar o projeto da seguinte forma:

* Clone ou faça um Fork desse repositório.
* Crie um ambiente virtual. Você pode fazer isso usando `python -m venv venv no terminal`.
* Instale as bibliotecas necessárias. Se você utiliza o pip para gerenciar seus pacotes, utilize `pip install -r requirements.txt`.
* Execute `python app.py`
* Por padrão, o aplicativo será executado no seguinte endereço: `127.0.0.1:8000`, com o modo de depuração ativado.

## Tecnologias que foram usadas 🖥️
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Bootstrap](http://getbootstrap.com)
* [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
* [Jinja2](https://palletsprojects.com/p/jinja/)
* [JavaScript](https://js.org)


## Considerações 📝

* O sistema não possui um módulo de autenticação, mas acredito que devido à arquitetura modular dos Blueprints, não seria difícil de implementar. Se você se sentir confortável, pode me enviar uma solicitação de pull request para o projeto.
* Existe um projeto chamado "_FORCE404_" de propósito; você pode tentar acessá-lo para testar se o redirecionamento do manipulador de erros do Flask está funcionando corretamente.
* O ambiente de Uploads possui validação para "usuários portas" com JavaScript, Jinja2 e Flash Messages.

### Atenção! ⚠️
Se o usuário tentar fazer o upload de um projeto que já existe no diretório, o projeto existente será **substituído pelo novo** e uma mensagem será exibida.


## Licença 📜

O código neste projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.</br>
Observação: Minha intenção é simplesmente ajudar pessoas que também estão estudando desenvolvimento web com Python. :)

> Obrigado pelo prestígio. 🐍
