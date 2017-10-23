JSON_1_DICT = {
   "coreData": {  
      "msgCnt":102,
      "id":"BEA10000",
      "secMark":36799,
      "position": {  
         "latitude":41.1641851,
         "longitude":-104.8434230,
         "elevation":1896.9
      },
      "accelSet":{  
         "accelYaw":0.00
      },
      "accuracy":{  

      },
      "speed":22.00,
      "heading":321.0125,
      "brakes":{  
         "wheelBrakes":{  
            "leftFront":False,
            "rightFront":False,
            "unavailable":False,
            "leftRear":False,
            "rightRear":True
         },
         "traction":"unavailable",
         "abs":"unavailable",
         "scs":"unavailable",
         "brakeBoost":"unavailable",
         "auxBrakes":"unavailable"
      },
      "size":{  
      }
   },
   "partII": [  
      {  
         "id":"vehicleSafetyExt",
         "value":{  
            "pathHistory":{  
               "crumbData":[  
                  {  
                     "elevationOffset":9.5,
                     "latOffset":0.0000035,
                     "lonOffset":0.0131071,
                     "timeOffset":33.20
                  },
                  {  
                     "elevationOffset":4.6,
                     "latOffset":0.0000740,
                     "lonOffset":0.0131071,
                     "timeOffset":44.60
                  },
                  {  
                     "elevationOffset":3.5,
                     "latOffset":0.0000944,
                     "lonOffset":0.0000051,
                     "timeOffset":49.30
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001826,
                     "lonOffset":0.0000637,
                     "timeOffset":71.70
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001313,
                     "lonOffset":0.0000606,
                     "timeOffset":80.20
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001535,
                     "lonOffset":0.0000748,
                     "timeOffset":92.90
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001650,
                     "lonOffset":0.0001171,
                     "timeOffset":126.40
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001363,
                     "lonOffset":0.0001000,
                     "timeOffset":136.10
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001196,
                     "lonOffset":0.0001028,
                     "timeOffset":141.90
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0001111,
                     "lonOffset":0.0000980,
                     "timeOffset":143.00
                  },
                  {  
                     "elevationOffset":204.7,
                     "latOffset":0.0131071,
                     "lonOffset":0.0000095,
                     "timeOffset":348.00
                  },
                  {  
                     "elevationOffset":12.6,
                     "latOffset":0.0131071,
                     "lonOffset":0.0131071,
                     "timeOffset":437.80
                  },
                  {  
                     "elevationOffset":11.5,
                     "latOffset":0.0131071,
                     "lonOffset":0.0131071,
                     "timeOffset":468.20
                  },
                  {  
                     "elevationOffset":10.0,
                     "latOffset":0.0131071,
                     "lonOffset":0.0131071,
                     "timeOffset":474.00
                  },
                  {  
                     "elevationOffset":10.2,
                     "latOffset":0.0131071,
                     "lonOffset":0.0000070,
                     "timeOffset":481.30
                  }
               ]
            },
            "pathPrediction":{  
               "confidence":0.0,
               "radiusOfCurve":0.0
            }
         }
      }
   ]
}

JSON_2_DICT = {
    "schemaVersion": 3,
    "metadata": {
        "schemaVersion":3,
        "recordGeneratedBy": "OBU",
        "recrodGeneratedAt": "2016-08-10T16:35:45.138Z[UTC]", 
        "logFileName": "bsm.uper",
        "payloadType": "us.dot.its.jpo.ode.model.OdeBsmPayload",
        "recordType": "bsmRxRecord",
        "serialId": {
            "streamId": "f9c7635a-7763-4e21-bece-cb1104f143b9",
            "bundleSize": 1,
            "bundleId": 12,
            "recordId": 5,
            "serialNumber": 0
        },
        "odeReceivedAt": "2017-09-26T20:00:08.48Z[UTC]",
        "sanitized": False,
        "validSignature": True
    },
    "payload": {
        "dataType": "us.dot.its.jpo.ode.plugin.j2735.J2735Bsm",
        "data": {
            "coreData": {
                "msgCnt": 102,
                "id": "BEA10000",
                "secMark": 36799,
                "position": {
                    "latitude": 41.3015058,
                    "longitude": -105.6155548,
                    "elevation": 1896.9
                },
                "accelSet": {
                    "accelYaw": 0.00
                },
                "accuracy": {},
                "speed": 0.00,
                "heading": 321.0125,
                "brakes": {
                    "wheelBrakes": {
                        "leftFront": False,
                        "rightFront": False,
                        "unavailable": True,
                        "leftRear": False,
                        "rightRear": False
                    },
                    "traction": "unavailable",
                    "abs": "unavailable",
                    "scs": "unavailable",
                    "brakeBoost": "unavailable",
                    "auxBrakes": "unavailable"
                },
                "size": {}
            },
            "partII": [
                {
                    "id": "VEHICLESAFETYEXT",
                    "value": {
                    "pathHistory": {
                        "crumbData": [
                            {
                                "elevationOffset": 9.5,
                                "latOffset": 0.0000035,
                                "lonOffset": 0.0131071,
                                "timeOffset": 33.20
                            },    
                            {
                              "elevationOffset": 4.6,
                              "latOffset": 0.0000740,
                              "lonOffset": 0.0131071,
                              "timeOffset": 44.60
                            },
                            {
                              "elevationOffset": 3.5,
                              "latOffset": 0.0000944,
                              "lonOffset": 0.0000051,
                              "timeOffset": 49.30
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001826,
                              "lonOffset": 0.0000637,
                              "timeOffset": 71.70
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001313,
                              "lonOffset": 0.0000606,
                              "timeOffset": 80.20
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001535,
                              "lonOffset": 0.0000748,
                              "timeOffset": 92.90
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001650,
                              "lonOffset": 0.0001171,
                              "timeOffset": 126.40
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001363,
                              "lonOffset": 0.0001000,
                              "timeOffset": 136.10
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001196,
                              "lonOffset": 0.0001028,
                              "timeOffset": 141.90
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0001111,
                              "lonOffset": 0.0000980,
                              "timeOffset": 143.00
                            },
                            {
                              "elevationOffset": 204.7,
                              "latOffset": 0.0131071,
                              "lonOffset": 0.0000095,
                              "timeOffset": 348.00
                            },
                            {
                              "elevationOffset": 12.6,
                              "latOffset": 0.0131071,
                              "lonOffset": 0.0131071,
                              "timeOffset": 437.80
                            },
                            {
                              "elevationOffset": 11.5,
                              "latOffset": 0.0131071,
                              "lonOffset": 0.0131071,
                              "timeOffset": 468.20
                            },
                            {
                              "elevationOffset": 10.0,
                              "latOffset": 0.0131071,
                              "lonOffset": 0.0131071,
                              "timeOffset": 474.00
                            },
                            {
                              "elevationOffset": 10.2,
                              "latOffset": 0.0131071,
                              "lonOffset": 0.0000070,
                              "timeOffset": 481.30
                            }
                        ]
                },
                "pathPrediction": {
                    "confidence": 0.0,
                    "radiusOfCurve": 0.0
                }
            }
        }
      ]
    }
  }
}

from json import dumps, loads

import sys

def json1toJson2(json_str_in):
    json_in = loads(json_str_in)

    json_out = JSON_2_DICT

    # Core data itself remained unchanged; just copy
    json_out['payload']['data']['coreData'] = json_in['coreData']

    return json_out    
    
def csvBSMLineToJson(bsm_line):
    fields = bsm_line.strip().split(',')

    try: 
        ID = hex(abs(int(fields[4]))).split('x')[1].upper()
        msgCount = int(fields[5])
        dseconds = int(fields[6])
        lat = float(fields[7])
        lng = float(fields[8])
        elevation = float(fields[9])
        speed = float(fields[10])
        heading = float(fields[11])
        # TODO rest fo the fields 
    except Exception:
        return None
    
    json_ret = JSON_1_DICT

    json_ret['coreData']['msgCnt'] = msgCount  
    json_ret['coreData']['id'] = ID
    json_ret['coreData']['secMark'] = dseconds
    json_ret['coreData']['position']['latitude'] = lat
    json_ret['coreData']['position']['longitude'] = lng
    json_ret['coreData']['position']['elevation'] = elevation
    json_ret['coreData']['speed'] = speed
    json_ret['coreData']['heading'] = heading
    
    return json_ret

for line in sys.stdin:
    #json_ret = csvBSMLineToJson(line)
    json_ret = json1toJson2(line)

    if not json_ret:
        # Invalid line.
        continue

    print(dumps(json_ret, sort_keys=True))
