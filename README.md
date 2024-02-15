
## Requerimentos

## Instalação

### Ambiente virtual

#### Virtual Enviroment

Rodar o comando ```sudo apt install python3.10-venv```

Esse comando irá instalar o pacote para criarmos um ambiente virtual. Serve pra instalar pacotes sem impactar o user e que facilite a instalação em outros PCs.

```
~/user ❯ sudo apt install python310-venv       at 20:24:57
[sudo] password for ubuntu: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  python3-pip-whl python3-setuptools-whl
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.10-venv
0 upgraded, 3 newly installed, 0 to remove and 10 not upgraded.
Need to get 2.473 kB of archives.
After this operation, 2.884 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

Rodar o comando ```python3 -m venv .venv```

![venv](python-virtual-envs1.webp)

https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/


Rodar o comando ``` source .venv/bin/activate ``` para ativar o ambiente virtual.

Rodar o comando ```pip install -r requirements.txt``` para instalar todos os pacotes necessários para rodar o projeto.

