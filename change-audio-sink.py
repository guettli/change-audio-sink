#!/usr/bin/env python3

import subprocess

result = subprocess.run(['pactl', 'list', 'short', 'sinks'], stdout=subprocess.PIPE)
running = None
sinks = dict()
for line in result.stdout.splitlines():
    line = line.decode('utf8').split('\t')
    line[0] = int(line[0])
    if 'RUNNING' in line:
        running = line
    sinks[line[0]] = line

next_sink = None

sink_ids = sorted(sinks.keys())
if running:
    cur_index = sink_ids.index(running[0])
    next_index = cur_index + 1
    if next_index == len(sink_ids):
        next_sink = sink_ids[0]
    else:
        next_sink = sink_ids[next_index]
else:
    next_sink = sink_ids[0]

subprocess.run(['pacmd', 'set-default-sink', str(next_sink)])
