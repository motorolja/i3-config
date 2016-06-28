#!/usr/bin/env python3
# coding = utf-8
import subprocess
import netifaces
import os
from i3pystatus import Status

os.system('/home/knase/.config/i3/addstatus-icons&')

status = Status(standalone=True)
status.register('pulseaudio')

status.register('clock', format='%Y-%m-%d %H:%M:%S', interval=1)

status.register('temp', format='{temp:.0f}°C',)

status.register("battery",format="{status}/{consumption:.2f}W {percentage:.2f}% {remaining:%E%hh:%Mm}",
alert=True,
alert_percentage=10,
status={
"DIS": "↓",
"CHR": "↑",
"FULL": "=",
},)

status.register('load', format='{avg1}')

# status.register('disk', path='/', format='{free}GiB')

interfaces = list(filter(lambda x: x != 'lo', netifaces.interfaces()))
for i in interfaces:
    status.register('network', interface=i, format_up='{v6}')
    status.register('network', interface=i, format_up='{v4}')

#status.register('mpd', host='mpd.mydomain.com', format='[{artist} - ]{album}[ - {title}][ ({song_elapsed}/{song_length})] {status}')
status.run()
