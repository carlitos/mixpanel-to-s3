import json

def fixkey(key):
    # toy implementation
    #print("fixing {}".format(key))
    return key.replace("&", "").replace("$", "")

def normalize(data):
    #print("normalizing {}".format(data))
    if isinstance(data, dict):
        data = {fixkey(key): normalize(value) 
        for key, value in data.items()}
    elif isinstance(data, list):
        data = [normalize(item) for item in data]
    return data

jsdata = """
{"event":"Search","properties":{"time":1648943376,"distinct_id":"17dcaa4436434-02bd394ab7be51-2d223624-5c094-17dcaa4436526","$browser":"Chrome","$browser_version":99,"$city":"Mexico City","$current_url":"https://viaje.greyhound.com.mx/search/t-monterrey/t-nuevo-laredo/02-abr-22/p/A1/departures","$device":"Android","$device_id":"17dcaa4436434-02bd394ab7be51-2d223624-5c094-17dcaa4436526","$initial_referrer":"https://www.google.com/","$initial_referring_domain":"www.google.com","$insert_id":"0m5q10ooiui3hwc2","$lib_version":"2.45.0","$mp_api_endpoint":"api-js.mixpanel.com","$mp_api_timestamp_ms":1648964977987,"$os":"Android","$referrer":"https://www.greyhound.com.mx/","$referring_domain":"www.greyhound.com.mx","$region":"Mexico City","$screen_height":915,"$screen_width":412,"$search_engine":"google","Departure":"2022-04-01T23:00:00","Departure Delta":-1,"Destination":"NUEVO LAREDO","Destination Terminal":"NUEVO LAREDO","Lodging Provider":"None","Origin":"MONTERREY","Origin Terminal":"MONTERREY Terminal de Greyhound","Passengers":1,"Route":"MONTERREY - NUEVO LAREDO","User Type":"Anonymous","from":"Home","mp_country_code":"MX","mp_lib":"web","mp_processing_time_ms":1648965007913,"product":"web-mobile"}}
"""

data = json.loads(jsdata)

data = normalize(data)

result = json.dumps(data, indent=2)
print(result)