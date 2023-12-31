def client(env, client_sock):
    message = Message(env, client_sock)
    reply = yield env.process(message.send('ohai'))
    print(reply)

def server(env, server_sock):
    # Accept new connection
    sock = yield env.process(server_sock.accept())
    message = Message(env, PacketUTF8(sock))

    # Get message and send reply
    request = yield env.process(message.recv())
    print(request.content)
    yield env.process(request.succeed('cya'))
