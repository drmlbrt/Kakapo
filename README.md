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
- install the scripts modules (readable on the top)
- Needed modules:
    Connecting to Devices: NetMiko and Napalm
- I use PyCharm for scripting

Testing:
Please use your development LAB environment prior real cfg pushing.

Sincerely yours, 

SSDD
