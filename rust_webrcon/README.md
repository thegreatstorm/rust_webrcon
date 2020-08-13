# Docs of library
How to use!
## server_info
##### <b>Connect Test:</b> server_info.get_server_info(server_info)
Verify if you can receive server data json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.
- - -
##### <b>Server Info:</b> server_info.get_players_list(server_info)
Gets a list of players in string based json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.
- - -
##### <b>Server Info:</b> server_info.banlist(server_info)
Gets a list of ban users in string based json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.
- - -
##### <b>Server Info:</b> server_info.find_command(server_info)
Gets results for searching command in string based.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
* `search_command` - an string value of command your searching for<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.
- - -
##### <b>Server Info:</b> server_info.users_sleeping(server_info)
Gets results of sleeping users command in string json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.
