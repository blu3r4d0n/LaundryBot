import xmltodict
import requests
import tweepy




def getData(room):
    data=requests.get(room)
    parsed = xmltodict.parse(data.content)
    return parsed
def getWashers(laundryroomData):
    availWash=0
    for appliance in laundryroomData['laundry_room']['appliances']['appliance']:
        if appliance['appliance_type'] == 'WASHER':
            if appliance['status'] == 'Available':
                availWash=availWash+1
#            if appliance['out_of_service']=='1':
#                print("Yep")
    return availWash
def getDryers(laundryroomData):
    availDry=0
    for appliance in laundryroomData['laundry_room']['appliances']['appliance']:
        if appliance['appliance_type'] == 'DRYER':
            if appliance['status'] == 'Available':
                availDry=availDry+1
            
    return availDry
#if  availWash == 0

def Phelps():
    laundryRooms = {
        "Phelps 1st Floor":'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=1946215',
        "Phelps 2nd Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=1946216',
        "Phelps Basement": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194625',
        "Richardson": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194629',
        "Roddey 1st Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194621',
        "Roddey 2nd Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194622',
        "Roddey 3rd Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194623',
        "Thomson East": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194627',
        "Thomson West": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194628',
        "Wofford":'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=1946210',
        }
    for key, value in laundryRooms.items():
        altText="Currently, there are " + str(getWashers(getData(value))) + " washers and "+ str(getDryers(getData(value))) + " dryers available in the "+ key +" laundry room."
        tweet= key +": "+ str(getWashers(getData(value))) +  " W / " + str(getDryers(getData(value))) + " D"
        print(tweet)
Phelps()
