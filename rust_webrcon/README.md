# Docs of library
How to use!

## server_info
##### <b><u>get_server_info(server_info)</u></b> 
Verify if you can receive server data json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.

##### <b><u>get_players_list(server_info)</u></b> 
Gets a list of players in string based json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.

##### <b><u>banlist(server_info)</u></b> 
Gets a list of ban users in string based json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.

##### <b><u>find_command(server_info, search_command)</u></b> 
Gets results for searching command in string based.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
* `search_command` - an string value of command your searching for<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.

##### <b><u>users_sleeping(server_info)</u></b> 
Gets results of sleeping users command in string json.<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads and a index list.
- - -

## oxide_commands
##### <b><u>oxide_version(server_info)</u></b> 
Get the version of oxide you have installed<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.

##### <b><u>oxide_plugin_list(server_info)</u></b> 
Get all the plugins listed installed<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.


##### <b><u>oxide_get_user_info(server_info, user)</u></b> 
Get user information, such as groups, and permissions<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
* `user` - an string declaring the user name<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.

##### <b><u>oxide_create_group(server_info, group)</u></b> 
Get group information, such as users, and permissions associated to the group<br>
<b>Arguments:</b>
* `server_info` - an dictionary array to transfer information to the function.<br>
* `group` - an string declaring the group name<br>
<b>Return Value:</b>
* `message <str_json>` - an json formated as a string given back from server connection. This will require a json.loads without index.


- - -