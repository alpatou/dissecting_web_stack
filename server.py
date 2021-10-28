import socket


## create a socket instance
## AF_INET: use IP protocol v 4
## SOCK_STREAM: full duplex byte stream (?) (google it)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## it reminds me java

## allow resuse of addresses (?)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

## Bind the socket to any address, port 8080, and listen 
s.bind(('', 8080))
s.listen()


## serve forever you slave socket
while True: ## and that is final the usefulness of such weird capabilities of languages 
    # accept the connection, accept your fate
    conn, addr = s.accept() ## this is i suppose something list() on php, google it (?)

    # re

