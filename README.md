# rust_webrcon Package
Information can be found for libraries in rust_webrcon folder

## Install
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


# More Docs coming soon!