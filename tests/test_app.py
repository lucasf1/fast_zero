from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    # act
    response = client.get('/')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


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
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'alice@example.com',
        'username': 'alice',
    }


def test_read_user_with_user_inexistent(client):
    response = client.get('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'email': 'alice@example.com',
                'username': 'alice',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'email': 'bob@example.com',
            'username': 'bob',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_update_user_with_user_inexistent(client):
    response = client.put(
        '/users/10',
        json={
            'email': 'bob@example.com',
            'username': 'bob',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user_with_user_inexistent(client):
    response = client.delete('/users/10')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_ola_mundo_html(client):
    response = client.get('/ola-mundo')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo!</h1>
      </body>
    </html>"""
    )
