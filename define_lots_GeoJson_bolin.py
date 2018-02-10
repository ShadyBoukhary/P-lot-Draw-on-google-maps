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

spaceId = 1
roundby = 7

data = {
    'type': 'FeatureCollection',
    'name': 'bolin',
}
data['features'] = []

# 34 spaces top row
# 4 middle rows
# 32 per middle row
# 34 spaces last row
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

    # first spot, handicapped, larger than others
    if x == 0:
        startingPoint = Point(33.873432, -98.520131)
    # another handicapped spot, same row
    # change size to normal after drawing handicapped spots
    elif x == 1:
        longDiff = 0.0000296
        startingPoint = Point(secondPoint.latitude, secondPoint.longitude)
    elif x == 22:
        startingPoint = Point(33.873432, -98.519412)
    elif x == 33:
        startingPoint = Point(33.873312, -98.520100)
    # start of 2nd row
    elif x == 65:
        startingPoint = Point(33.873245, -98.520100)
    # start of 3rd row
    elif x == 97:
        startingPoint = Point(33.873135, -98.520100)
    # start of 4th row
    elif x == 129:
        startingPoint = Point(33.873068, -98.520100)
    # start of last row
    elif x == 161:
        startingPoint = Point(33.872951, -98.520182)
    # continue on same row
    else:
        startingPoint = Point(secondPoint.latitude, secondPoint.longitude)

    # calculate the rest of the points of the polygon using the first point
    secondPoint = Point(startingPoint.latitude, startingPoint.longitude + longDiff)
    thirdPoint = Point(secondPoint.latitude - latDiff, secondPoint.longitude)
    fouthPoint = Point(startingPoint.latitude - latDiff, startingPoint.longitude)

    spaceId += 1


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

# latDiff normal 0.000046
# longDiff normal 0.0000296