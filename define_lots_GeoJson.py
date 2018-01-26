import json


class Point(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def getLat(self):
        return self.latitude

    def getLong(self):
        return self.longitude

#*****************************************

# polygon coordinates of first space in bolin which is top left handicapped spot
startingPoint = Point(33.873432, -98.520179)
secondPoint = Point(33.873432, -98.520146)
thirdPoint = Point(33.873386, -98.520146)
fouthPoint = Point(33.873386, -98.520179)
latDiff = 0.000046
longDiff = 0.000036

# startingPoint = Point(33.873312, -98.520100)
# secondPoint = Point(33.873312, -98.520072)
# thirdPoint = Point(33.873266, -98.520072)
# fouthPoint = Point(33.873266, -98.520100)
spaceId = 1
roundby = 7

data = {
    'type': 'FeatureCollection',
    'name': 'bolin',
}
data['features'] = []

# 32 per middle row
for x in range(0, 197):
    

    data['features'].append({
        'type': 'Feature',
        'properties': {
            'spaceNum': spaceId
        },
        'geometry': {
            "type": "Polygon",
            "coordinates": [
                [
                    [round(startingPoint.longitude, roundby), round(startingPoint.latitude, roundby)],
                    [round(secondPoint.longitude, roundby), round(secondPoint.latitude, roundby)],
                    [round(thirdPoint.longitude, roundby), round(thirdPoint.latitude, roundby)],
                    [round(fouthPoint.longitude, roundby), round(fouthPoint.latitude, roundby)],
                    [round(startingPoint.longitude, roundby), round(startingPoint.latitude, roundby)]
                ]
            ]
        }
    })

 
    # start at 2nd middle row 
    if x == 0:
        startingPoint = Point(33.873432, -98.520131)
    elif x == 1:
        longDiff = 0.0000296
        startingPoint = Point(secondPoint.latitude, secondPoint.longitude)
    elif x == 22:
        startingPoint = Point(33.873432, -98.519412)
    elif x == 33:
        startingPoint = Point(33.873312, -98.520100)
    elif x == 65:
        startingPoint = Point(33.873245, -98.520100)
    # start at 3rd middle row
    elif x == 97:
        startingPoint = Point(33.873135, -98.520100)
    # start at 4th middle row
    elif x == 129:
        startingPoint = Point(33.873068, -98.520100)
    elif x == 161:
        startingPoint = Point(33.872951, -98.520182)
    else:
        startingPoint = Point(secondPoint.latitude, secondPoint.longitude)

    secondPoint = Point(startingPoint.latitude, startingPoint.longitude + longDiff)
    thirdPoint = Point(secondPoint.latitude - latDiff, secondPoint.longitude)
    fouthPoint = Point(startingPoint.latitude - latDiff, startingPoint.longitude)

    spaceId += 1


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# latDiff normal 0.000046
# longDiff normal 0.0000296