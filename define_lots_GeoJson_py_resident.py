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
longDiff = 0.000036 # difference in long in a handicapped space
maxSpaces = 0


def bolinSpaces():
    # first spot, handicapped, larger than others
    if x == 0:
        startingPoint = Point(33.873432, -98.520131)
    # another handicapped spot, same row
    # change size to normal after drawing handicapped spots
    elif x == 1:
        longDiff = 0.0000296    #difference in long between bolin spaces
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
    
    
def pyResidentSpaces():
    if x == 30:
        return Point(33.873332, -98.521760)
    elif x == 61:
        return Point(33.873206, -98.521760)
    elif x == 92:
        return Point(33.873159, -98.521760)
    elif x == 123:
        return Point(33.873038, -98.521763)
    else:
        return Point(secondPoint.latitude, secondPoint.longitude)



roundby = 7
run = True
lot = ''

print("Enter the number of the lot to define spots for:\n"
+ "1. Bolin\n2. PY Resident\n3. PY Reserved\n4. PY Commuter\n5. Library Commuter\n"
+ "6. Library Reserved\n0. Exit")

while run:
    spaceId = 1
    lotChoice = input()
    if lotChoice == 1:
        lot = 'bolin'
        longDiff = 0.000036
        maxSpaces = 197
    elif lotChoice == 2:
        lot = 'py-resident'
        longDiff = 0.0000276
        maxSpaces = 155
        startingPoint = Point(33.873379, -98.521760)
        secondPoint = Point(33.873379, -98.5217325)
        thirdPoint = Point(33.873333, -98.5217325)
        fouthPoint = Point(33.873333, -98.521760)
    elif lotChoice == 3:
        lot = 'py-reserved'
    elif lotChoice == 4:
        lot = 'py-commuter'
    elif lotChoice == 5:
        lot = 'library-commuter'
    elif lotChoice == 6:
        lot = 'library-reserved'
    elif lotChoice == 0:
        run = False
    else:
        print ("Try again.")
    
    if run:
        data = {
            'type': 'FeatureCollection',
            'name': lot,
        }
        data['features'] = []

        # 34 spaces top row
        # 4 middle rows
        # 32 per middle row
        # 34 spaces last row
        for x in range(0, maxSpaces):
    
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
            #print (str(lotChoice))
            if lotChoice == 2:
                startingPoint = pyResidentSpaces()
            elif lotChoice == 1:
                bolinSpaces()

            # calculate the rest of the points of the polygon using the first point
            secondPoint = Point(startingPoint.latitude, startingPoint.longitude + longDiff)
            thirdPoint = Point(secondPoint.latitude - latDiff, secondPoint.longitude)
            fouthPoint = Point(startingPoint.latitude - latDiff, startingPoint.longitude)

            spaceId += 1


        with open(lot + '_spaces.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)
        print ("\nDone...! Choose another lot\n")

# latDiff normal 0.000046
# longDiff normal 0.0000296



    
