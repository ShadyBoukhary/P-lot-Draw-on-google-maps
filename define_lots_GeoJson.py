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


startingPoint = Point(33.873312, -98.520100)
secondPoint = Point(33.873312, -98.520072)
thirdPoint = Point(33.873266, -98.520072)
fouthPoint = Point(33.873266, -98.520100)
spaceId = 1
roundby = 7

data = {
    'type': 'FeatureCollection',
    'name': 'bolin',
}
data['features'] = []

for x in range(0, 31):

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

    startingPoint = Point(secondPoint.latitude, secondPoint.longitude)
    secondPoint = Point(startingPoint.latitude, startingPoint.longitude + 0.0000297)
    thirdPoint = Point(secondPoint.latitude - 0.000046, secondPoint.longitude)
    fouthPoint = Point(startingPoint.latitude - 0.000046, startingPoint.longitude)

    spaceId += 1


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
