<div align="center">
<img align="center" width="260rem" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/main/docs/logo-github.png">
</div>

# Greetings! ⚜

The Filebrax Hub (which doesn't share any similarity with my nickname) is a fully functional project for handling file uploads and downloads on a server. It has been developed using Flask as its Micro Framework, with the goal of providing an efficient internal environment. Moreover, thanks to its well-structured architecture using Blueprints, it allows for easy integration of additional backend modules (e.g., [Tracker Tickets](https://github.com/victorbrax/TrackerG), a tracking and management application that I plan to release soon).
</br>
</br>
[![Python](https://img.shields.io/badge/Python-green.svg)](https://shields.io/)
[![Flask Application](https://img.shields.io/badge/Flask-gray.svg)](https://shields.io/)
[![Bootstrap Framework](https://img.shields.io/badge/Bootstrap-red.svg)](https://shields.io/)
[![Blueprints Routes](https://img.shields.io/badge/Blueprints-blue.svg)](https://shields.io/)
[![Jinja2](https://img.shields.io/badge/Jinja2-gray.svg)](https://shields.io/)
[![Javascript](https://img.shields.io/badge/Javascript-yellow.svg)](https://shields.io/)


## Demo 🖼️

Soon, I will make available the main pages of the application in a non-functional way using the GitHub Pages feature for non-experienced programming users.
</br>

<div align="center">
<img height="220vh" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/main/docs/presentation.gif">
<img height="220vh" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/main/docs/not_found.gif">
</div>
<div align="center">
<img height="220vh" src="https://raw.githubusercontent.com/victorbrax/filebrax-hub/main/docs/download.gif">
</div>

## Run Project Locally 🏠

Assumes local installation of [Python](https://python.org)
To run the project locally:

* Clone or fork this repository.
* Create a virtual environment. You can do this by using `python -m venv venv` in the terminal.
* Install the necessary libraries. If you use pip to manage your packages, use `pip install -r requirements.txt`.
* Run `python app.py`
* By default, the application will run on the following address: `127.0.0.1:8000`, with the debug mode enabled.

## Technologies Used 🖥️
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Bootstrap](http://getbootstrap.com)
* [Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)
* [Jinja2](https://palletsprojects.com/p/jinja/)
* [JavaScript](https://js.org)


## Considerations 📝

* The system doesn't have an authentication module, but I believe that due to the modular architecture of Blueprints, it wouldn't be difficult to implement. If you feel comfortable, you can send me a pull request for the project.
* There is a deliberate project called "FORCE404"; you can try accessing it to test if the Flask error handler redirection is working correctly.
* The Uploads environment has validation for "port users" with JavaScript, Jinja2 and Flash Messages.

### Warning ⚠️
If the user tries to upload a project that already exists in the directory, the existing project **will be replaced** by the new one and a message will be displayed.

## License 📜

The code in this project is licensed under the MIT License. See [LICENSE](LICENSE) for details.</br>
Note: My intention is simply to help people who are also studying web development with Python. :)

> Thank you for the prestige. 🐍
</br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

