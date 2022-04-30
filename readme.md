# Welcome to PyNetS - Python Network Scanner 🚀

PyNetS is a Port Scanner script developed using python that can be used for provide agility in obtaining verifications related a services (and ports detection) running on servers.

Note: Please don't use this script on servers that you don't have permissions for (and if you do this it is just your responsibility).

## Author:

- [Sérgio Corrêa](https://github.com/correa-sergio)


## How to Run:

- Clone the project

```bash
git clone https://github.com/correa-sergio/PyNetS
```
- Go to the project directory

```bash
cd PyNetS
```

## Install the Requirements

- create a virtual environment (Optional)
```bash
python3 -m venv venv
```

- Activate the Environment (Optional)

```bash
source venv/bin/activate
```

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.

```bash
pip install -r requirements.txt
```
- Input

```python
python3 pynets.py -h
```

```python 

Usage example: 

Ex: python3 pynets.py -i 192.168.0.6 -p 22 (Only one port scan)

Ex: python3 pynets.py -i 192.168.0.6 -p 22 80 443 8080 (multiple ports scan)

PyNetS - Python Network Scanner 1.0

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        The address reflected to the target
  -p [PORT [PORT ...]], --port [PORT [PORT ...]]
                        The port reflected to the target
  -v, --version         show program's version number and exit

```

- Output Example:

```
[√] IP address '192.168.0.7' is valid
[√] Found Port: 8080
[√] Total of 1 port(s) opened

[√] Processing Time: 0.0006721019744873047
[√] PyNetS - Python Network Scanner v.1.0
```


## License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Contribution:

Suggestions and issues are welcome (Feel free to send me an e-mail). ✉️

Made with love. By me. To the community ♥️