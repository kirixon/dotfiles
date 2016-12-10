from i3pystatus import Status
status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%H:%M",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format="♪ {volume}",)


# Shows disk usage of /
# Format:
# 42/128G [86G]
status.register("disk",
    path="/home",
    format="{avail}G",)

# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{status} {artist} - {title}",
    status={
        "pause": "",
        "play": "▶",
        "stop": "◾",
    },)

status.run()
