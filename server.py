import socket
import re ## why not response? 


## create a socket instance
## AF_INET: use IP protocol v 4
## SOCK_STREAM: full duplex byte stream (?) (google it)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## it reminds me java

## allow resuse of addresses (?)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

## Bind the socket to any address, port 8080, and listen 
s.bind(('', 8080))
s.listen()


HEAD_200 ="HTTP/1.1 200 OK\n\n" 
HEAD_404 ="HTTP/1.1 404 Not Found\n\n" 

## serve forever you slave socket
while True: ## and that is final the usefulness of such weird capabilities of languages 
    # accept the connection, accept your fate
    conn, addr = s.accept() ## this is i suppose something list() on php, google it (?)

    # receive data from this socket using a bugger of 1024 bytes
    data = conn.recv(1024)

    # print out then the data nicely decoded
    request = data.decode('utf-8')

    #print(request)
    print(request)
    resource = re.match(r'GET /(.*) HTTP', request).group(1) # group (?)
    try:
        with open(resource, 'r') as f:
            content = HEAD_200 + f.read()
        print('Resource {} correctly served'.format(resource))
    except FileNotFoundError:
        content = HEAD_404 + 'Resource {} cannot be found'.format(resource)
        print('Resource {} cannot be loaded'.format(resource))

    print('--------------------------------') # do not forget to be artistic

    #we have content now to send
    conn.sendall(bytes(content, 'utf-8'))

    # close the connection but why closing since it has to run forever, but a suppose the 
    # essence of the server is the socket, connections we can have many, so it will wait until 
    # receiving data and then be closed again, Lets test it
    conn.close()

