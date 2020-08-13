from rust_webrcon.utils.connection import connect_rust_rcon


def get_server_info(server_info):
    command = 'global.serverinfo'
    response = connect_rust_rcon(server_info, command)
    return response


def get_players_list(server_info):
    command = 'playerlist'
    response = connect_rust_rcon(server_info, command)
    return response


def banlist(server_info):
    command = 'global.banlist'
    response = connect_rust_rcon(server_info, command)
    return response


def find_command(server_info, search_command):
    command = 'find {}'.format(search_command)
    response = connect_rust_rcon(server_info, command)
    return response


def users_sleeping(server_info):
    command = 'global.sleepingusers'
    response = connect_rust_rcon(server_info, command)
    return response


