import math


def correctfault(readings, sensorid):
    humiditycount = 0

    for reading in readings:
        humiditycount += float(reading['humidity'])

    humiditymean = humiditycount / len(readings)
    humidityvariance = 0

    for reading in readings:

        if float(reading['humidity']) < 100:

            humidityvariance += (float(reading['humidity']) - humiditymean) ** 2

    humidityvariance = humidityvariance / (len(readings) - 1)
    humidityvariance = math.sqrt(humidityvariance)



    # do not iterate over the first and last elements
    for idx, reading in enumerate(readings[1:-1]):

        if float(readings[idx + 1]['humidity'] is not None):

            if (float(readings[idx + 1]['humidity']) - float(readings[idx]['humidity'])) > humidityvariance / 2:
                readings[idx+1]['humidity'] = float(readings[idx]['humidity'])

            elif (float(readings[idx]['humidity']) - float(readings[idx + 1]['humidity'])) > humidityvariance / 2:
                readings[idx + 1]['humidity'] = float(readings[idx]['humidity'])



    if sensorid == 22:

        dht22count = 0
        dht22variance = 0

        for reading in readings:
            dht22count += float(reading['dht22'])

        dht22mean = dht22count / len(readings)

        for reading in readings:
            dht22variance += (float(reading['dht22']) - dht22mean) ** 2

        dht22variance = dht22variance / (len(readings) - 1)
        dht22variance = math.sqrt(dht22variance)

        for idx, reading in enumerate(readings[1:-1]):


            if float(readings[idx+1]['dht22'] is not None):

                if (float(readings[idx + 1]['dht22']) - float(readings[idx]['dht22'])) > dht22variance/2:

                    readings[idx +1]['dht22'] = float(readings[idx]['dht22'])

                elif (float(readings[idx ]['dht22']) - float(readings[idx + 1]['dht22'])) > dht22variance/2:

                    readings[idx+1]['dht22'] = float(readings[idx]['dht22'])

    elif sensorid == 11:

        dht11count = 0
        dht11variance = 0

        for reading in readings:
            dht11count += float(reading['dht11'])

        dht11mean = dht11count / len(readings)

        for reading in readings:
            dht11variance += (float(reading['dht11']) - dht11mean) ** 2

        dht11variance = dht11variance / (len(readings) - 1)
        dht11variance = math.sqrt(dht11variance)



        for idx, reading in enumerate(readings[1:-1]):

            if float(readings[idx + 1]['dht11'] is not None):

                if (float(readings[idx + 1]['dht11']) - float(readings[idx]['dht11'])) > dht11variance *2:

                    readings[idx +1]['dht11'] = float(readings[idx ]['dht11'])

                elif (float(readings[idx]['dht11']) - float(readings[idx + 1]['dht11'])) > dht11variance *2:

                    readings[idx + 1]['dht11'] = float(readings[idx]['dht11'])

    return readings