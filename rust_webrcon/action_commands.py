from rust_webrcon.utils.connection import connect_rust_rcon


def custom_command(server_info, command):
    command = '{}'.format(command)
    response = connect_rust_rcon(server_info, command)
    return response


def set_hostname(server_info, hostname):
    command = 'server.hostname "{}"'.format(hostname)
    response = connect_rust_rcon(server_info, command)
    return response


def set_description(server_info, description):
    command = 'server.description "{}"'.format(description)
    response = connect_rust_rcon(server_info, command)
    return response


def stop_server(server_info):
    command = 'server.stop'
    response = connect_rust_rcon(server_info, command)
    return response


def set_max_players(server_info, max_players):
    command = 'server.maxplayers "{}"'.format(max_players)
    response = connect_rust_rcon(server_info, command)
    return response


def kick_player(server_info, steam_id):
    command = 'global.kick {}'.format(steam_id)
    response = connect_rust_rcon(server_info, command)
    return response


def ban_player(server_info, username, reason, duration):
    command = 'global.ban {} {} {}'.format(username, reason, duration)
    response = connect_rust_rcon(server_info, command)
    return response


def banid_player(server_info, steam_id, username, reason, duration):
    command = 'global.banid {} {} {} {}'.format(steam_id, username, reason, duration)
    response = connect_rust_rcon(server_info, command)
    return response


def send_chat_message(server_info, chat_message):
    command = 'global.say {}'.format(chat_message)
    response = connect_rust_rcon(server_info, command)
    return response