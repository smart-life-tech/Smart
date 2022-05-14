import requests
import time
all_properties = {}
feat_prop = {}
areas = {}
event = {}
urgency = {}
smoke_check = {}
act= True
found = 0
def main_loop():
    response_update = requests.get('https://api.thingspeak.com/update?api_key=X2MOYRYWKCENHEA4&field4=43201')
    print(response_update.text)
    smoke = requests.get('https://api.thingspeak.com/channels/1143907/feeds.json?results=2')
    # print(smoke.json())
    smoke_check = (smoke.json())
    smoke_checking = smoke_check['feeds']
    fields = smoke_checking[1]
    print(fields['field1'])
    room1 = fields['field1']
    room2 = fields['field2']
    room3 = fields['field3']
    room4 = fields['field4']
    room5 = fields['field5']

    line = fields['field4']
    state = ''
    global found
    global act

    headers = {
      "apikey": "2d18bdd0-88d8-11ec-8605-6d7ce1bd9204"}

    params = (
       ("codes",line),
       ("compare",line),
       ("country","us"),
    )

    county_response = requests.get('https://app.zipcodebase.com/api/v1/search', headers=headers, params=params)
    county_response = county_response.json()

    county_check = county_response['results']
    print(county_check)

    county_province = county_check[str(line)]
    # print(county_province)

    province = county_province[0]
    county = province['province']
    print(county)

    if int(line) >= 5 :
        num = int(line)
        if num in range(99501, 99951):
            state = "ak"
            print("Alaska")
        elif num in range(35004, 36926):
            state = "al"
            print("Alabama")
        elif num in range(71601, 72960):
            state = "ar"
            print("Arkansas")
        elif num in range(75502, 75503):
            state = "ar"
            print("Arkansas (Texarkana)")
        elif num in range(85001, 86557):
            state = "az"
            print("Arizona")
        elif num in range(90001, 96163):
            state = "ca"
            print("Calielifnia")
        elif num in range(80001, 81659):
            state = "co"
            print("Colorado")
        elif num in range(6001, 6390):
            state = "ct"
            print("Connecticut")
        elif num in range(6401, 6929):
            state = "ct"
            print("Connecticut")
        elif num in range(20001, 20040):
            state = "dc"
            print("Dist of Columbia")
        elif num in range(20042, 20600):
            state = "dc"
            print("Dist of Columbia")
        elif num in range(20799, 20800):
            state = "dc"
            print("Dist of Columbia")
        elif num in range(19701, 19981):
            state = "de"
            print("Delaware")
        elif num in range(32004, 34998):
            state = "fl"
            print("Florida")
        elif num in range(30001, 32000):
            state = "ga"
            print("Georgia")
        elif num in range(39901, 39902):
            state = "ga"
            print("Geogia (Atlanta)")
        elif num in range(96701, 96899):
            state = "hi"
            print("Hawaii")
        elif num in range(50001, 52810):
            state = "ia"
            print("Iowa")
        elif num in range(68119, 68121):
            state = "ia"
            print("Iowa (OMAHA)")
        elif num in range(83201, 83877):
            state = "id"
            print("Idaho")
        elif num in range(60001, 63000):
            state = "il"
            print("Illinois")
        elif num in range(46001, 47998):
            state = "in"
            print("Indiana")
        elif num in range(66002, 67955):
            state = "ks"
            print("Kansas")
        elif num in range(40003, 42789):
            state = "ky"
            print("Kentucky")
        elif num in range(70001, 71233):
            state = "la"
            print("Louisiana")
        elif num in range(71234, 71498):
            state = "la"
            print("Louisiana")
        elif num in range(1001, 2792):
            state = "ma"
            print("Massachusetts")
        elif num in range(5501, 5545):
            state = "ma"
            print("Massachusetts (Andover)")
        elif num in range(20331, 20332):
            state = "md"
            print("Maryland")
        elif num in range(20335, 20798):
            state = "md"
            print("Maryland")
        elif num in range(20812, 21931):
            state = "md"
            print("Maryland")
        elif num in range(3901, 4993):
            state = "me"
            print("Maine")
        elif num in range(48001, 49972):
            state = "mi"
            print("Michigan")
        elif num in range(55001, 56764):
            state = "mn"
            print("Minnesota")
        elif num in range(63001, 65900):
            state = "mo"
            print("kc96 DataMO")
        elif num in range(38601, 39777):
            state = "ms"
            print("Mississippi")
        elif num in range(71233, 71234):
            state = "ms"
            print("Mississippi(Warren)")
        elif num in range(59001, 59938):
            state = "mt"
            print("Montana")
        elif num in range(27006, 28910):
            state = "nc"
            print("North Carolina")
        elif num in range(58001, 58857):
            state = "nd"
            print("North Dakota")
        elif num in range(68001, 68119):
            state = "ne"
            print("Nebraska")
        elif num in range(68122, 69368):
            state = "ne"
            print("Nebraska")
        elif num in range(3031, 3898):
            state = "nh"
            print("New Hampshire")
        elif num in range(7001, 8990):
            state = "nj"
            print("New Jersey")
        elif num in range(87001, 88442):
            state = "nm"
            print("New Mexico")
        elif num in range(88901, 89884):
            state = "nv"
            print("Nevada")
        elif num in range(6390, 6391):
            state = "ny"
            print("New York (Fishers Is)")
        elif num in range(10001, 14976):
            state = "ny"
            print("New York")
        elif num in range(43001, 46000):
            state = "oh"
            print("Ohio")
        elif num in range(73001, 73200):
            state = "ok"
            print("Oklahoma")
        elif num in range(73401, 74967):
            state = "ok"
            print("Oklahoma")
        elif num in range(97001, 97921):
            state = "or"
            print("Oregon")
        elif num in range(15001, 19641):
            state = "pa"
            print("Pennsylvania")
        elif num in range(0, 1):
            state = "pr"
            print("Puerto Rico")
        elif num in range(2801, 2941):
            state = "ri"
            print("Rhode Island")
        elif num in range(29001, 29949):
            state = "sc"
            print("South Carolina")
        elif num in range(57001, 57800):
            state = "sd"
            print("South Dakota")
        elif num in range(37010, 38590):
            state = "tn"
            print("Tennessee")
        elif num in range(73301, 73302):
            state = "tx"
            print("Texas (Austin)")
        elif num in range(75001, 75502):
            state = "tx"
            print("Texas")
        elif num in range(75503, 80000):
            state = "tx"
            print("Texas")
        elif num in range(88510, 88590):
            state = "tx"
            print("Texas (El Paso)")
        elif num in range(84001, 84785):
            state = "ut"
            print("Utah")
        elif num in range(20040, 20042):
            state = "va"
            print("Virginia")
        elif num in range(20040, 20168):
            state = "va"
            print("Virginia")
        elif num in range(20042, 20043):
            state = "va"
            print("Virginia")
        elif num in range(22001, 24659):
            state = "va"
            print("Virginia")
        elif num in range(5001, 5496):
            state = "vt"
            print("Vermont")
        elif num in range(5601, 5908):
            state = "vt"
            print("Vermont")
        elif num in range(98001, 99404):
            state = "wa"
            print("Washington")
        elif num in range(53001, 54991):
            state = "wi"
            print("Wisconsin")
        elif num in range(24701, 26887):
            state = "wv"
            print("West Virginia")
        elif num in range(82001, 83129):
            state = "wy"
            print("Wyoming")
    state = state.upper()

    link = 'https://api.weather.gov/alerts/active/area/'+state
    response = requests.get(link)
    print(link)

    # print(response.text)

    r_dictionary = response.json()
    print(r_dictionary['title'])
    features = r_dictionary["features"]
    for i in range(len(r_dictionary["features"])):
        all_properties[i] = features[i]

    for i in range(len(r_dictionary["features"])):
        feat_prop[i] = all_properties[i]['properties']

    # print(feat_prop[0]['areaDesc'])
    for i in range(len(r_dictionary["features"])):
        areas[i] = feat_prop[i]['areaDesc']

    for i in range(len(r_dictionary["features"])):
        event[i] = feat_prop[i]['event']

    for i in range(len(r_dictionary["features"])):
        urgency[i] = feat_prop[i]['urgency']

    for j in range(len(areas)):
        if county in areas[j]:
            print(county)
            act = True
            found = i
            # print(i)
            break
        #else:
            #print('not found')
"""
features_0 = features[0]
features0_prop = features_0['properties']

# print(features0_prop ['areaDesc'])
area1 = features0_prop ['areaDesc']
event1 = features0_prop ['event']
urgency1= features0_prop ['urgency']
"""
# for i in range (1,7):

while True:
    main_loop()
    if act:
        try:
            print(areas[found])
            print(event[found])
        except IndexError:
            # pass
            print('list out of range')
            pass
        finally:
            #break
            print('done sleeping')
            response_update = requests.get('https://api.thingspeak.com/update?api_key=X2MOYRYWKCENHEA4&field1=200')
            print(response_update.text)
            res = int(response_update.text)
            if res <= 0:
                response_update = requests.get('https://api.thingspeak.com/update?api_key=X2MOYRYWKCENHEA4&field1=200')
                print(response_update.text)
        act = False
    time.sleep(9)

