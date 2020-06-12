import socket
from termcolor import colored

print('\nWelcome to My Chat Room\n')
print('Trying to creating connection...')
try:
    connect_tool = socket.socket()
    print(colored('Connection successfully created.', 'green'))
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    port = 8585
    connect_tool.bind((server_host, port))
    print('Socket binded to %s (%s)\n' % (server_host, ip))
    name = input(str('Enter your name : '))
    connect_tool.listen(3)
    print(colored('\nWait for someone to come and connect...\n', 'cyan'))
    connection, adr = connect_tool.accept()
    print('Got connection from %s (%s)\n' % (adr[0], adr[1]))
    client = connection.recv(1024).decode()
    print(colored(client, 'yellow'), 'has connected to this room\n \nEnter --exit to Exit\n')
    connection.send(name.encode())
    while True:
        message = input(str(colored('\nMe : ', 'green')))
        if message == '--exit':
            message = '--exit'
            connection.send(message.encode())
            print('\n')
            break
        connection.send(message.encode())
        message = connection.recv(1024).decode()
        if message == '--exit':
            print('\n', colored(client, 'yellow'), ' left the room\n\n',
                  colored('And you exiting out', 'red'), '\n\nBye.\n')
            break
        elif message == 'None':
            print(colored('\n%s : ', 'yellow') % client, colored(message, 'red'))
        else:
            print(colored('\n%s : ', 'yellow') % client, message)
except socket.error as err:
    print(colored('connection creation failed with error :\n', 'red'), err)
