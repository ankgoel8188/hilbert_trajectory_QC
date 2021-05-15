# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 04:41:17 2021

@author: erina
"""
coordinates = open('positions.txt', 'r')
lines = coordinates.read().split('\n') 
x_coord = lines[0].split(',')
y_coord = lines[1].split(',')
file = open('flightpath.plan', 'w')
size = len(x_coord)
file.write('{\n    "fileType": "Plan",\n    "geoFence": {\n        "circles": [\n        ],\n        "polygons": [\n        ],\n        "version": 2\n    },\n    "groundStation": "QGroundControl",\n    "mission": {\n        "cruiseSpeed": 2,\n        "firmwareType": 12,\n        "globalPlanAltitudeMode": 0,\n        "hoverSpeed": 2,\n        "items": [')

jumpID = str(1)
long = str(x_coord[0])
lat = str(y_coord[0])
file.write('            {\n                "AMSLAltAboveTerrain": null,\n                "Altitude": 5,\n                "AltitudeMode": 1,\n                "autoContinue": true,\n                "command": 22,\n                "doJumpId": ' + jumpID + ',\n                "frame": 2,\n                "params": [\n                    0,\n                    0,\n                    0,\n                    null,\n                    '+long+',\n                    '+lat+',\n                    5\n                ],\n                "type": "SimpleItem"\n            },\n')



for i in range(1, size-1):
    jumpID = str(i+1)
    long = str(x_coord[i])
    lat = str(y_coord[i])
    file.write('            {\n                "AMSLAltAboveTerrain": null,\n                "Altitude": 5,\n                "AltitudeMode": 1,\n                "autoContinue": true,\n                "command": 16,\n                "doJumpId": ' + jumpID + ',\n                "frame": 2,\n                "params": [\n                    0,\n                    0,\n                    0,\n                    null,\n                    '+long+',\n                    '+lat+',\n                    5\n                ],\n                "type": "SimpleItem"\n            },\n')

jumpID = str(i+1)
long = str(x_coord[i])
lat = str(y_coord[i])
file.write('            {\n                "AMSLAltAboveTerrain": null,\n                "Altitude": 5,\n                "AltitudeMode": 1,\n                "autoContinue": true,\n                "command": 16,\n                "doJumpId": ' + jumpID + ',\n                "frame": 2,\n                "params": [\n                    0,\n                    0,\n                    0,\n                    null,\n                    '+long+',\n                    '+lat+',\n                    0\n                ],\n                "type": "SimpleItem"\n            }\n')
x = x_coord[-1];
y = y_coord[-1];
x_i = x_coord[0];
y_i = y_coord[0];


# file.write('            {\n                "altitudesAreRelative": true,\n                "complexItemType": "fwLandingPattern",\n                "landCoordinate": [\n                    '+str(x_i)+',\n                    '+str(y_i)+',\n                    0\n                ],\n                "loiterClockwise": true,\n                "loiterCoordinate": [\n                    '+x+',\n                    '+y+',\n                    5\n                ],')
# file.write('                "loiterRadius": 75,\n                "stopTakingPhotos": true,\n                "stopVideoPhotos": true,\n                "type": "ComplexItem",\n                "valueSetIsDistance": false,\n                "version": 2\n            }\n        ],')
# file.write('            {\n                "altitudesAreRelative": true,\n                "landCoordinate": [\n                    '+str(x_i)+',\n                    '+str(y_i)+',\n                    0\n                ],\n                ')
# file.write('                "type": "ComplexItem",\n                "valueSetIsDistance": false,\n                "version": 2\n            }\n        ],')
file.write('        ],\n        "plannedHomePosition": [\n            '+x_i+',\n            '+y_i+',\n            472\n        ],\n        "vehicleType": 2,\n        "version": 2\n    },\n    "rallyPoints": {\n        "points": [\n        ],\n        "version": 2\n    },\n    "version": 1\n}')
file.close()
coordinates.close()