import websocket
import json


def connect_rust_rcon(server_info, command):
    # If you want to enable websocket for debugging.
    websocket.enableTrace(server_info["enable_trace"])

    # Generates a server_uri needed for connecting via rcon
    server_uri = 'ws://{0}:{1}/{2}'.format(server_info["hostname"],server_info["rcon_port"],server_info["rcon_password"])

    # Default
    websocket.WebSocketClientProtocol = None

    # Create the object
    ws = websocket.WebSocket()

    # Standard format for connection. Used dict to make it easier to modify and read.
    command_json = {}
    command_json["Identifier"] = 1
    command_json["Message"] = command
    command_json["Name"] = "WebRcon"

    # It takes string json in the websocket call. Convert to string json using json.dumps
    command_json = json.dumps(command_json)

    # If connection fails for whatever reason
    try:
        # Tries to connect to rust rcon server
        ws.connect(server_uri)

        # Tries to send command to rcon server
        ws.send(command_json)

        # Retrieve the response from rcon call
        response = ws.recv()

        # Close connection, connection not needed all the time.
        ws.close()

        # Convert it to readable json object.
        response = json.loads(response)

        # Return back to who ever called function
        return response["Message"]

    except Exception as e:
        # Inform the user it was a failure to connect. provide Exception string for further diagnostics.
        response = "Failed to connect. {}".format(str(e))
        return response