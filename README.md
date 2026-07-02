# intro-good-practices
 
This repository is designed as a learning space where we will practice and apply software development best practices, including the use of Git, GitHub, Issues, Pull Requests, documentation, and collaborative work.
 
## Table of Contents
 
- [intro-good-practices](#intro-good-practices)
  - [Table of Contents](#table-of-contents)
  - [Tool Set](#tool-set)
  - [Setting up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Create the virtual environment](#create-the-virtual-environment)
  - [Running the application with Docker](#running-the-application-with-docker)
 
## Tool Set
 
The following external tools are used to initialize and manage the project:
 
| Name   | Version   |
| ------ | --------- |
| Python | >= 3.13   |
| Poetry | >= 2.4.1  |
| pyenv  | >= v2.7.2 |
 
## Setting up a Virtual Environment
 
This project uses a local Python virtual environment to keep dependencies isolated from the global system installation.
 
> [!NOTE]
> Please be sure that you have the tool set suggested already installed on your local.
 
## Create the virtual environment
 
First, make sure Python 3.13 is selected for this project:
 
```powershell
pyenv local 3.13
```
 
Validate that it is 3.13.x
 
```powershell
python -V
```
 
This creates a local folder called .venv, which is ignored by .gitignore
 
```powershell
python -m venv .venv
```
 
Activates the virtual environment on Windows:
 
```powershell
.venv\Scripts\Activate.ps1
```
 
Install Poetry:
 
```powershell
pip install poetry
```
 
Install dependencies, including `dev` dependencies:
 
```powershell
poetry install --with=dev
```
 
Check the `pre-commit` configuration:
 
```powershell
pre-commit validate-config
pre-commit install --hook-type commit-msg --hook-type pre-push
pre-commit run
```
 
> [!NOTE]
> Any hook type configured in `.pre-commit-config.yaml` must also be installed locally. Otherwise, the hook will not run automatically during the Git workflow.
 
## Running the application with Docker
 
This project can also be executed inside a Docker container.
 
The `Dockerfile` is located in the root directory of the project. Even though the FastAPI application is inside the `src` folder, the Docker build context is the whole project, so Docker can access the dependency files and the source code.
 
### Build the Docker image
 
From the root directory of the project, run:
 
```powershell
docker build -t myimage .
```
 
This command builds a Docker image named `myimage`.
 
### Run the Docker container
 
Run the application container with:
 
```powershell
docker run -d --name mycontainer -p 80:80 myimage
```
 
This command starts a container named `mycontainer` in detached mode and maps port `80` from the container to port `80` on the local machine.
 
### Access the application
 
Open the following URL in your browser:
 
```text
http://localhost
```
 
You can also access the automatic FastAPI documentation at:
 
```text
http://localhost/docs
```
 
### Stop and remove the container
 
To stop the container:
 
```powershell
docker stop mycontainer
```
 
To remove the container:
 
```powershell
docker rm mycontainer
```
