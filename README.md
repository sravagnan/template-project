# TEMPLATE PROJECT

<div align="center">
  <a href="https://www.enyr.eu/">
    <img src="" alt="Logo" width="220">
  </a>

  <h3 align="center"> TEMPLATE PROJECT</h3>

  <p align="center">
    <a href="https://github.com/energiacollettiva/MVP/issues">Report Bug/Request Feature</a>
  </p>
</div>

This repository contains ...

### Prerequisites

This repository will not work without the following external dependencies:

* [docker ](https://docs.docker.com/engine/install/)
* [traefik](https://traefik.io/), following the [dockerswarm.rocks](https://dockerswarm.rocks/traefik/) instructions

<p align="right">(<a href="#top">back to top</a>)</p>

### Structure

The project structure follows the structure below:

- **deploy.sh**: this bash file contains the deployment steps to create a Docker Swarm Stack based on the `.env` file.
- **app**: this directory contains the Django application.
    - **apps**: this directory contains all the reusable apps.
    - **config**: this directory stores the project configuration files:
        - **.env**: contains environment variables
        - **config.ini**: contains logger configuration
        - **environment.py**: contains pydantic environment model
    - **tools**: this directory stores reusable tools:

<p align="right">(<a href="#top">back to top</a>)</p>

### Getting Started

Create a new environment file `.env` and place it in the `src/configs` directory, then add the follow environment variables:

```sh
### GENERAL
DEBUG=True
```

Create a new virtual environment by running the command below:

```sh
python -m venv .venv
```

Activate it in a Linux enviroment by running:

```sh
source .venv/bin/activate
```

or in a Windows enviroment by running:

```sh
.\.venv\Scripts\activate
```

Install the dependencies by running:

```sh
pip install -r requirements.txt
```

### Run the App

In order to run the app localy you need to locate in root dir and run:

```sh
python src/main.py
```

If you are developing with vscode, the `.vscode` folder contains the `launch.json` to be able to run the app in debugging mode.

### Deploy the App

If you want to deploy the app into a Docker container using Docker Swarm as a container orchertrator you can simply run:

```sh
./deploy.sh
```

The script builds a container image with the source code, then it creates a stack with some container repliacas, a network and a Swarm service.

Enjoy!

<p align="right">(<a href="#top">back to top</a>)</p>

### Requirements

#### Compile dependencies

Run the following command to install pip-tools that is required to compile the requirements.txt

```shell
pip install pip-tools
```

In order to compile the requirements.txt file based on a pyproject.toml file, run the following command:

```shell
pip-compile --resolver=backtracking --output-file=requirements.txt pyproject.toml
```

### Setup pre-commit

In order to initialize the environment for pre-commit-hooks run the following command:

```shell
pre-commit install
```

### Contact

Stefano Ravagnan - stefano.ravagnan@outlook.com

Project Link: [https://github.com/energiacollettiva/MVP](https://github.com/energiacollettiva/MVP)

<p align="right">(<a href="#top">back to top</a>)</p>
