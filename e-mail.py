from mailthon.postman import Postman
from mailthon.middleware import TLS, Auth
from mailthon import email
while(True):
    postman = Postman(
        host='smtp-mail.outlook.com',
        port=587,
        middlewares=[
            TLS(force=True),
            Auth(username='thiagofelicio@hotmail.com', password='')
        ],
    )

    envelope = email(
        sender='sender <thiagofelicio@hotmail.com>',
        receivers=['thiagofelicio@hotmail.com'],
        subject='Manutenção/Suporte',
        content='Hi',
    )
    response = postman.send(envelope)
    print(response.message)
    print(response.status_code)

    if response.ok:
        print("OK! :)")