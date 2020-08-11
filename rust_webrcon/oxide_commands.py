from rust_webrcon.utils.connection import connect_rust_rcon


def oxide_version(server_info):
    command = 'oxide.version'
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_plugin_list(server_info):
    command = 'oxide.version'
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_get_user_info(server_info, user):
    command = 'oxide.show user {}'.format(user)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_get_group_info(server_info, group):
    command = 'oxide.show group {}'.format(group)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_create_group(server_info, group):
    command = 'oxide.group add {}'.format(group)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_remove_group(server_info, group):
    command = 'oxide.group remove {}'.format(group)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_add_user_group(server_info, steam_id, group):
    command = 'oxide.usergroup add {} {}'.format(steam_id,group)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_remove_user_group(server_info, steam_id, group):
    command = 'oxide.usergroup remove {} {}'.format(steam_id,group)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_load_plugin(server_info, plugin_name):
    command = 'oxide.load {}'.format(plugin_name)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_unload_plugin(server_info, plugin_name):
    command = 'oxide.unload {}'.format(plugin_name)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_reload_plugin(server_info, plugin_name):
    command = 'oxide.reload {}'.format(plugin_name)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_reload_all_plugins(server_info):
    command = 'oxide.reload *'
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_grant_user_perm(server_info, steam_id, permission):
    command = 'oxide.grant user {} {}'.format(steam_id, permission)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_revoke_user_perm(server_info, steam_id, permission):
    command = 'oxide.revoke user {} {}'.format(steam_id, permission)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_grant_group_perm(server_info, steam_id, permission):
    command = 'oxide.grant group {} {}'.format(steam_id, permission)
    response = connect_rust_rcon(server_info, command)
    return response


def oxide_revoke_group_perm(server_info, steam_id, permission):
    command = 'oxide.revoke group {} {}'.format(steam_id, permission)
    response = connect_rust_rcon(server_info, command)
    return response