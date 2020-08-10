import websocket
import json


def get_players_list(server_info):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'playerlist', 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))


def kick_player(server_info, steam_id):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'global.kick {}'.format(steam_id), 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))


def ban_player(server_info, username, reason, duration):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'global.ban {} {} {}'.format(username, reason, duration), 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))


def banid_player(server_info, steam_id, username, reason, duration):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'global.banid {} {} {} {}'.format(steam_id, username, reason, duration), 'Name': 'WebRcon'})

    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))


def banlist(server_info, steam_id, reason, duration):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'global.ban {} {} {}'.format(steam_id, reason, duration), 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))


def find_command(server_info, search_command):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'find {}'.format(search_command), 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))


def custom_command(server_info, command):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': '{}'.format(command), 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))

