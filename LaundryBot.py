import xmltodict
import requests
import tweepy



from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth)


def getData(room):
    data=requests.get(room)
    parsed = xmltodict.parse(data.content)
    return parsed
def getWashers(laundryroomData):  ##May merge getWashers and getDryers at some point
    availWash=0
    for appliance in laundryroomData['laundry_room']['appliances']['appliance']: 
        if appliance['appliance_type'] == 'WASHER':
            if appliance['status'] == 'Available':
                availWash=availWash+1
    return availWash
def getDryers(laundryroomData):
    availDry=0
    for appliance in laundryroomData['laundry_room']['appliances']['appliance']:
        if appliance['appliance_type'] == 'DRYER':
            if appliance['status'] == 'Available':
                availDry=availDry+1
            
    return availDry
def listMaker():
    listData=[]
    laundryRooms = {
        "Phelps 1st Floor":'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=1946215', ############################
        "Phelps 2nd Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=1946216',############################
        "Phelps Basement": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194625',  ############################
        "Richardson": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194629',       # This API is publicly known
        "Roddey 1st Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194621', # so I don't feel it's      
        "Roddey 2nd Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194622', # dangerous to put on GitHub
        "Roddey 3rd Floor": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194623', # (It's alright :) ) 
        "Thomson East": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194627',     ############################
        "Thomson West": 'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=194628',     ############################
        "Wofford":'http://api.laundryview.com/room/?api_key=8c31a4878805ea4fe690e48fddbfffe1&method=getAppliances&location=1946210',          ############################
        }
    for key, value in laundryRooms.items():
        #altText="Currently, there are " + str(getWashers(getData(value))) + " washers and "+ str(getDryers(getData(value))) + " dryers available in the "+ key +" laundry room."      
        listData.append (key +": "+ str(getWashers(getData(value))) +  " W / " + str(getDryers(getData(value))) + " D")
    return listData
tweet="\n".join(listMaker())
api.update_status(tweet)
