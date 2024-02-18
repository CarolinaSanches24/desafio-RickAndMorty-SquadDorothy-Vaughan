Criando o ambiente
terminal: py -3 -m venv .venv

Ativar o ambiente virtual
terminal: .venv\scripts\activate (pode usar tab pra completar o caminho)
Se rolar erro de bloqueio de excecução: Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser

Instalar o Flask
terminal: pip install flask
Se rolar erro: pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Flask -vvv
** Com o ambiente virtual ativo

Consultar a api criada
terminal: flask --app app run
