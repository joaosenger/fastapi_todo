# FastAPI

## Comandos para iniciar um projeto com Pipx e Poetry

```bash
pip install pipx
pipx install poetry
pipx inject poetry poetry-plugin-shell
poetry shell
poetry new --flat nome_projeto # cria um projeto
poetry use 3.13 # baixa a versão 3.13 do Python
poetry env use 3.13 # usa a versão 3.13 no projeto, após isso, atualizar
# o pyproject.toml com a versão que vc deseja
poetry install # é o comando que instala todas as dependências do projeto, igual npm i
poetry add 'fastapi[standard]' # instala o fastapi
poetry shell # ativa o .venv 
fastapi dev fast_zero/app.py
```