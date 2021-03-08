# Automation IOS
## Introduction.

I'll be frankly, automation is not achieved in one day. I mean, in this lesson, you will achieve some automation. 
But, automation is much more than this introduction. 
In the near future you will come in contact with the new Cisco DNA development in our corporation.

###### What is the learning trajectory

I suggest finding a course that explains practical network automation. 
This course will bring you in contact with Linux and Python scripting. Google is probably your best friend. 
My advice: start small, and that is what we will do today.

## Napalm
For deployed networks automation at you local 'LAN' level automation is probably not a big issue. From the moment that you want to manage more than 10 devices, then automation is your friend.
But, what can it do for you? 

First, there is a big difference between IOS 15+ and IOS XE. 
The latter is more equipped and is focused upon automation. So, the first, IOS 15 is less performant. 
However, there are some small gains to achieve though! 

This small introduction is the perfect playground.

NAPALM!
Start SMALL :-)
NAPALM is a collection of ready-made solutions. You just need to know how to use that NAPALM solution. So RTM (read-the-manual).


#####First step: boot up you Virtual Machine (Ubuntu 20.04 and your PyCharm)

######Open a new python file.
Write the following code:

`install python package NAPALM & json & pprint`


Start with:

`from napalm import get_network_driver`

`import json`

`driver = get_network_driver('ios')`

this request to use the IOS configuration to talk to your EoIP 3.03 routers.
Then fill in the parameters:

`device = driver(hostname='IPADDRESS', username = 'username' , password ='password')`

`device.open()`

`device.get_interfaces()`

-> this command plots a non human readable result. 
therefore, we would like a more presentable format.

`print(json.dumps(device.get_interfaces(), sort_keys=True, indent=4))`

Here we dump the result/**s**tring in a json parser. This prints out in a JSON format the result of the command get_interfaces.
end with:

`device.close()`

What can our device deliver with NAPALM? 

`get_method = dir(device)`
`print(json.dumps(get_method, sort_keys=True, indent= 4))`

add this above you 'close' statement. 
It shall print out all the options. 
Is get_config one of them? 
If so, try to manipulate the above code and see the running config. 
Did it take a lot of time? 

###Remember:
Napalm does the SSH for you, so you do not need to logon to the device and work inside the CLI to retreive the information you seek. 
Python scripting is able to parse the information to a readible format. It is now up to you to go and discover more. 

###References:

https://github.com/napalm-automation/napalm

https://napalm.readthedocs.io/en/latest