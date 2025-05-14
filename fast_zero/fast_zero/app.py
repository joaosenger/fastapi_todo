from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(title='Minha API TOP')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello, World!'}


@app.get('/hello_html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_html():
    return """
    <h1>Hello, World!</h1>
    """
