# utils

## Testing Connection
* connection_status(server_info&lt;dict&gt;)
*     The command is global.serverinfo. Its to allow you to identify if you made proper connection.
        In order to go through that json your going to have to use a json.loads(response). 
        To cipher through that.
        
        Example:
        server_info = {}
        server_info["hostname"] = ""
        server_info["rcon_port"] = ""
        server_info["rcon_password"] = ""
        server_info["enable_trace"] = False/True


## server_info Connection
* get_players_list(server_info)
* kick_player(server_info, steam_id)
* ban_player(server_info, username, reason, duration)
* banid_player(server_info, steam_id, username, reason, duration)
* banlist(server_info, steam_id, reason, duration)
* find_command(server_info, search_command="")
* custom_command(server_info, command="")