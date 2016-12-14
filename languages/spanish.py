no_autoplaylist = "Advertencia: La lista de reproducción automática está vacía, deshabilitando."

autosummon_attempt = "Intentando convocar automáticamente."

autosummon_found_owner = "Encontré el dueño en \"%s\", intentando juntar."

owner_only_cmd = "solamente el propietario puede usar este commando"

already_autojoined = "Ya junta un canal en %s, saltando"

attempt_autojoin = "Intento a juntar %s en %s"

no_channel_permission = "No puede junta un canal \"%s\". No tiene permiso."

no_speak_permission = "No junto canal \"%s\". No tiene permiso a hablar."

failed_join = "Fallo a juntar"

not_text_channel = "No junto %s en %s. Es un canel de texto."

invalid_voice_channel = "Canal inválido: "

not_in_voice = "debes estar en un canal de voz a usas este commando (%s)"

not_voice_channel = "Canal dado tiene que ser un canal de voz"

attempt_voice_connection = "Intentando conectar..."

voice_connection_successful = "Conexión satisfactoria."

voice_connection_failed = "Fallo a juntar. Reintentar (%s/%s)..."

# ------END OF CURRENT TRANSLATIONS------
# - Leave this for me later. (~MattBSG) -
# ---------------------------------------

voice_connection_error = ("Cannot establish connection to voice chat.  "
                          "Something may be blocking outgoing UDP connections.",

                          "This may be an issue with a firewall blocking UDP.  "
                          "Figure out what is blocking UDP and disable it.  "
                          "It's most likely a system firewall or overbearing anti-virus firewall.  ")

error_disconnecting = "Error disconnecting during reconnect"

bot_not_in_voice = ('The bot is not in a voice channel.  '
                    'Use %ssummon to summon it to your voice channel.')

now_playing_mention = "%s - your song **%s** is now playing in %s!"

now_playing = "Now playing in %s: **%s**"

ap_unplayable = "[Info] Removing unplayable song from autoplaylist: %s"

ap_error_adding = "Error adding song from autoplaylist:"

ap_no_playable = "[Warning] No playable songs in the autoplaylist, disabling."

user_playing_on = "music on %s servers"

no_text_send_permission = "Warning: Cannot send message to %s, no permission"

invalid_text_channel = "Warning: Cannot send message to %s, invalid channel?"

no_text_delete_permission = "Warning: Cannot delete message \"%s\", no permission"

message_already_deleted = "Warning: Cannot delete message \"%s\", message not found"

cannot_edit_message = "Warning: Cannot edit message \"%s\", message not found"

send_instead = "Sending instead"

cannot_send_typing = "Could not send typing to %s, no permssion"

bad_credentials = ("Bot cannot login, bad credentials.",
                   "Fix your Email or Password or Token in the options file.  "
                   "Remember that each field should be on their own line.")

cleanup_error = "Error in cleanup:"

exception_in = "Exception in"

bad_owner_id = ("Your OwnerID is incorrect or you've used the wrong credentials.",

                "The bot needs its own account to function.  "
                "The OwnerID is the id of the owner, not the bot.  "
                "Figure out which one is which and use the correct information.")

bot_connected = "\rConnected!    "

bot_name = "Bot:  %s/%s#%s"

owner_name = "Owner: %s/%s#%s\n"

server_list = "Server List:"

owner_not_found = "Owner could not be found on any server (id: %s)\n"

owner_unknown = "Owner unknown, bot is not on any servers."

bot_invite_link_help = ("\nTo make the bot join a server, paste this link in your browser."
                        "Note: You should be logged into your main account and have \n"
                        "manage server permissions on the server you want the bot to join.\n")

bound_to_channels = "Bound to text channels:"
bound_to_voice_error = "\nNot binding to voice channels:"
not_bound_error = "Not bound to any text channels"

autojoin_channels = "Autojoining voice chanels:"
autojoin_text_error = "\nCannot join text channels:"
not_autojoin_error = "Not autojoining any voice channels"

# CONFIG OPTIONS - op_
op_options = "Options:"
op_command_prefix = "  Command prefix: "
op_default_volume = "  Default volume: %s%%"
op_skip_threshold = "  Skip threshold: %s votes or %s%%"
op_now_playing_mentions = "  Now Playing @mentions: "
op_autosummom = "  Auto-Summon: "
op_autoplaylist = "  Auto-Playlist: "
op_autopause = "  Auto-Pause: "
op_delete_messages = "  Delete Messages: "
op_delete_invoking = "  Delete Invoking: "
op_debug_mode = "  Debug Mode: "
op_downloaded_songs = "  Downloaded songs will be %s"

op_disabled = "Disabled"
op_enabled = "Enabled"
op_deleted = "Deleted"
op_saved = "Saved"
# ===== END CONFIG OPTIONS

delete_audiocache = "Deleting old audio cache"
delete_audiocache_error = "Could not delete old audio cache, moving on."

done = "Done!"

ap_start_autoplaylist = "Starting auto-playlist"

owner_not_in_voice = "Owner not found in a voice channel, could not autosummon."

# BOT COMMANDS

# TODO EXPERIMENT using similer concept for CMD_COMMAND
# IF it works, implement changes similer to this
# may break a mod API i was working on but meh, we shall see

# ===== END BOT COMMANDS =====
