import websocket
import json


def connection_status(server_info):
    websocket.enableTrace(server_info["enable_trace"])
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    websocket.WebSocketClientProtocol = None

    ws = websocket.WebSocket()

    message= json.dumps({'Identifier': 1, 'Message': 'global.serverinfo', 'Name': 'WebRcon'})
    try:
        ws.connect(server_uri)
        ws.send(message)
        response = ws.recv()
        ws.close()
        response = json.loads(response)
        return response["Message"]
    except Exception as e:
        print(str(e))
