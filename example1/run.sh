#!/bin/bash
python ../vcopernicus/manager.py start
sleep 3
python ../vcopernicus/manager.py start_node NODE01
echo "Environment has been started. You may now interact with devices."
echo "To stop this example, exit this shell by typing exit or pressing Ctrl-D."
NODE01/home/code.py &
bash
python ../vcopernicus/manager.py stop_node NODE01
python ../vcopernicus/manager.py stop
