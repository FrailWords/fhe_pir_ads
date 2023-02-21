## Pre-requisite

Install Poetry - https://python-poetry.org/docs/#installation

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

or for powershell -  

```shell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Steps to run 

1. Create _poetry_ virtualenv - 

```shell
poetry update
```

2. Run Server -

```shell
poetry run server
```

3. Run client - 

```shell
poetry run client
```
