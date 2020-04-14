def ex(args, message, client, invoke):
    if len(args) == 0:
     yield from client.send_message(message.channel, "Pong!")
    else:
     yield from client.send_message(message.channel, "Ping!")
