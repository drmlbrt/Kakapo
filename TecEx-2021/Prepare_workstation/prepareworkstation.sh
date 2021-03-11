#!/bin/bash
echo "==========================================================="
echo "===Starting the workstation setup answer when needed to===="
echo "==========================================================="
sudo apt-get install
sudo apt-get install gcc make perl
sudo apt-get install python3-pip
sudo apt-get install nodejs
sudo apt-get install git
sudo pip3 install flask
sudo pip3 install flask-sqlalchemy
sudo pip3 install net-tools
sudo pip3 install sqlite3
sudo pip3 install tabulate
sudo pip3 install python-arptable
sudo pip3 install flask-cors
sudo pip3 install napalm
sudo pip3 install ntplib
sudo pip3 install psycopg2-binary
echo "==========================================================="
echo "===Preparing workstation for scripting                 ===="
echo "==========================================================="
#Snap prepare workstation
sudo snap install pycharm-community --classic
sudo snap install postman
echo "==========================================================="
echo "===Preparing Telemetry workstation for monitoring      ===="
echo "==========================================================="
#preparing TIG stack
sudo snap install grafana
sudo snap install influxdb --edge
#preparing the sources for telegraf
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update
sudo apt-get install telegraf
sudo systemctl start telegraf