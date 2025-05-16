from http import HTTPStatus


def test_hello_word(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test',
            'email': 'test@example.com',
            'password': 'test'
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test',
        'email': 'test@example.com',
        'id': 1
    }


def test_update_invalid_user(client):
    response = client.put(
        '/users/999',
        json={
            "username": "test",
            "email": "test@example.com",
            "password": "test"
        }
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        "detail": "User not found!"
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test',
        'email': 'test@example.com',
        "id": 1
    }


def test_delete_invalid_user(client):
    response = client.delete('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        "detail": "User not found!"
    }
