import AutoNaviAPI.main as AutoNaviAPI

print(AutoNaviAPI.get_location("cbf50c4fd937fd427bffafa8700615a6", "沈阳市", "利生丽园东区", "base")["geocodes"][0]["location"])
print(AutoNaviAPI.unget_location(KEY="cbf50c4fd937fd427bffafa8700615a6", LOCATION=AutoNaviAPI.get_location("cbf50c4fd937fd427bffafa8700615a6", "沈阳市", "利生丽园东区", "base")["geocodes"][0]["location"], OUTPUT="json")["regeocode"]["formatted_address"])
