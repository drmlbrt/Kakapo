# Kakapo project - EoIP automation & Monitoring

## EOIP AUTOMATION 

This project is created as a starter to automate changes to the deployed sites. 
The DEV is development and should not be used for configuration changes. I only addedd the DEV so you can view running changes.
The PROD is PRODUCTION -> this you should be able to use.

The project runs on a Python 3+ platform. It is not intended to run on earlier versions. If it does, good for you and yeay for me.


It is the intention to Finalise the KAKAPO project as such:
- Push cfg to different cisco platforms
- Recognize the platform and differentiate in the used push method (Newer IOS Xe shall use RESTCONF and a candidate dB)
- Working with YANG files -> BABY STEPS
- Visualize in a Webpage environment -> BABY STEPS

## EOIP MONITORING

Project idea : using telemetry data on the routers and integrating scripting in the Linux Shell of the 4K9K infrastructure.
TBD


## Platform requirements:
- python 3+
- pip3
- Install the scripts modules (readable on the top)
- Needed modules:
    Connecting to Devices: NetMiko and Napalm
- I use PyCharm for scripting

Testing:
Please use your development LAB environment prior real cfg pushing.

## PCN RESTCONF SERVER

Ok: Added or started on the next journey. 
For PCN (CWIX) purpose we should be able to build a RESTCONF server that should deliver:
-   Yang Structured data
-   Respond to a request
-   Have something of minimum security

####Requirements:

-   YANG datamodel knowledge
-   Abuse some GitHub respository that allows Python/Restconf calls (JETCONF is a valuable candidate, but hey this is already old?Not?)
-   Be able to translate the YANG into JSON -> data validation
-   Be able to store JSON information, after validation, into a database
-   Visualize the requested information
-   Telemetry

####Used tools:

-   Python,
-   Flask,
-   Flask-Sqlalchemy,
-   ... will add stuff along the way

#####Installation in the terminal:

Speed up the process with the 'prepare workstation in the tecex folder'!
   -  sudo apt-get install gcc make perl
   -  sudo apt-get install python3-pip
   -  sudo apt-get install nodejs
   -  sudo apt-get install git
   -  sudo apt-get install ./google-chrome-stable_current_amd64.deb (download the latest version)[not mandatory]
   -  sudo pip3 install flask
   -  sudo pip3 install flask-sqlalchemy
   -  sudo pip3 install net-tools
   -  sudo pip3 install sqlite3
   -  sudo pip3 install tabulate
   -  sudo pip3 install python-arptable
   -  sudo pip3 install flask-cors
   -  sudo pip3 install napalm
   -  sudo pip3 install ntplib
   -  sudo pip3 install psycopg2-binary


####Learning Track:

-   Read the introduction on the Flask web page. It sets up quickly a RESTFUL server.

Sincerely yours, 

SSDD
