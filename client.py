import socket
from termcolor import colored

print('\nWelcome to My Chat Room\n')
print('Trying to creating connection...')

try:
    connect_tool = socket.socket()
    client_host = socket.gethostname()
    ip = socket.gethostbyname(client_host)
    print(colored('%s (%s)\n', 'blue') % (client_host, ip))
    other_side_host = input(str('Enter server address that you want to connect to : '))
    name = input(str('\nEnter your name : '))
    port = 8585
    print(colored('\nTrying to connect to %s (%s) please wait...\n', 'cyan') % (other_side_host, port))
    connect_tool.connect((other_side_host, port))
    connect_tool.send(name.encode())
    server = connect_tool.recv(1024).decode()
    print(colored(server, 'yellow'), 'has joined to this room\n \nEnter --exit to Exit\n')
    print('Okay, You connected\nWait for receive message...\n')
    while True:
        message = connect_tool.recv(1024).decode()
        if message == '--exit':
            print('\n', colored(server, 'yellow'), ' left the room\n\n',
                  colored('And you exiting out', 'red'), '\n\nBye.\n')
            break
        elif message == 'None':
            print(colored('\n%s : ', 'yellow') % server, colored(message, 'red'))
        else:
            print(colored('\n%s : ', 'yellow') % server, message)
        message = input(str(colored('\nMe : ', 'green')))
        if message == '--exit':
            message = '--exit'
            connect_tool.send(message.encode())
            print('\n')
            break
        connect_tool.send(message.encode())
except socket.error as err:
    print(colored('connection creation failed with error :\n', 'red'), err)
