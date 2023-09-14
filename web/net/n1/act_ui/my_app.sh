#!/usr/bin/env bash


#pid=$(sudo netstat -tulpn | grep 5000 | awk '{print $7}' | cut -d/ -f1)
pid=$(netstat -nlp | grep 5000 | awk '{print $7}' | cut -d/ -f1)
if [ -n "$pid"]; then
  sudo kill -9 $pid
fi


# flask run --host=0.0.0.0 --port=50001
# flask run --host=0.0.0.0
# flask run

nohup flask run --host=0.0.0.0 --port=50001 1>my_app.std.out 2>my_app.std.err &
