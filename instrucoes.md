**Para criar o ambiente Virtual**

```shell
py -3 -m venv .venv
```

**Para Ativar o ambiente virtual**

```shell
.venv\Scripts\activate
```

**Se rolar erro de bloqueio de excecução:**

```shell
Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser
```

**Instalação do Flask**

```shell
pip install Flask
```

**Se rolar erro na instalação do Flask**

```shell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Flask -vvv
```

**Baixar atualizações caso necessário**

```shell
python.exe -m pip install --upgrade pip
```

**Executar o programa**

```shell
flask --app app run
```
