#!/bin/bash
CSV=${HOME}/rpz-sensor/history/rpz-sensor.csv
SHELL_DIR=${HOME}/rpz-sensor/shell

# get latest data
# rpz_sensor.pyは indoorcorgielec.com 様のサンプルを使用させていただきました
# (https://www.indoorcorgielec.com/products/rpz-ir-sensor/)
python3 /home/pi/rpz-sensor/python3/rpz_sensor.py -l $CSV

# create json from csv
# mapping.jq はrpz_sensor.pyが出力するCSVに応じて編集してください
tail -n 1 $CSV | jq -R -s -f ${SHELL_DIR}/mapping.jq \
               | jq 'del(.[][] | nulls)'| head -n -2 \
               | sed -e 1d -e 's/},/}/g' | jq . -c \
               | sed -r "s/([0-9]{4})\/([0-9]{2})\/([0-9]{2}) ([0-9]{2}:[0-9]{2})/\1-\2-\3T\4/g" \
               > ${SHELL_DIR}regist.json

# send post
URL="http://localhost:8000/posts/record/"
BODY=`cat ${SHELL_DIR}regist.json`

curl -XPOST -H "Content-Type: application/json" -d $BODY $URL
