# rust_webrcon Package

## Install
`pip install rust_webrcon`<br>
or<br>
`pip install https://github.com/thegreatstorm/rust_webrcon/archive/master.zip`

## Docs

#### Base Dictionary (server_info)
Gather Base Information for server connection<br>
* `hostname: <str>` - The IP/hostname of the Rust server accepting Web Rcon<br>
* `rcon_port: <str>` - The rcon port for the Rust Server<br>
* `rcon_password: <str>` - The rcon password used to connect over Web Rcon<br>
* `enable_trace: <boolean>` - If you want to debug the websocket<br>
* Example:
*     server_info = {}
      server_info["hostname"] = ""
      server_info["rcon_port"] = ""
      server_info["rcon_password"] = ""
      server_info["enable_trace"] = False

- - -
##### <b>Connect Test:</b> connect_test.connection_status(server_info)
Verify if you can receive server data.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.
- - -
##### <b>Server Info:</b> server_info.get_players_list(server_info)
Gets a list of players in string based.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.