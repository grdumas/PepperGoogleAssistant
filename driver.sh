#!/bin/bash

# an implementation of Google Assistant on Pepper Robot

# SSH to robot
ssh nao@192.168.1.140 'bash -s' <<'ENDSSH'
  # record the audio request on Pepper
  echo "recording"
  arecord -d 5 -f S16_LE -c 1 -r 16000 -t wav query.wav &
  wait
  # close SSH connection
  exit
ENDSSH

# copy audio input to host system
scp nao@192.168.1.140:/home/nao/query.wav /home/gdumas/env/pga-test_v3/
wait

# process through GA
source /home/gdumas/env/bin/activate
googlesamples-assistant-pushtotalk --device-id pepper-f12d8 --device-model-id pepper-f12d8-pepper-puku14 -i query.wav -o syn.wav
wait

# copy GA response back to Pepper
scp /home/gdumas/env/pga-test_v3/syn.wav nao@192.168.1.140:/home/nao
wait

# play response through Pepper's speakers
python play_response.py
