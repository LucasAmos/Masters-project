import math


def correctfault2(readings, sensorid):
    humiditycount = 0

    for reading in readings:
        humiditycount += float(reading['humidity'])

    humiditymean = humiditycount / len(readings)
    humidityvariance = 0

    for reading in readings:
        humidityvariance += (float(reading['humidity']) - humiditymean) ** 2

    humidityvariance = humidityvariance / (len(readings) - 1)
    humidityvariance = math.sqrt(humidityvariance)




    # do not iterate over the first and last elements
    for idx, reading in enumerate(readings[1:-2]):

        if float(readings[idx + 1]['humidity'] is not None):

            # # assumes that the first reading is not an error. If the element is a clear error:
            # if float(readings[idx + 1]['humidity']) > 70 or float(readings[idx + 1]['humidity']) < humidityvariance*2:
            #
            #     # replace the element with the previous element (this is why it's import first element is not an error
            #     readings[idx + 1]['humidity'] = float(readings[idx]['humidity'])

            # if the the difference between an element and its preceding element is greater than 5:
            if (float(readings[idx + 1]['humidity']) - float(readings[idx]['humidity'])) > humidityvariance / 2:
                readings[idx+1]['humidity'] = float(readings[idx]['humidity']) + float(readings[idx+2]['humidity'])/2


            # if the the difference between an element and its preceding element is greater than 5:
            elif (float(readings[idx]['humidity']) - float(readings[idx + 1]['humidity'])) > humidityvariance / 2:

                # replace the element with the preceding element
                readings[idx + 1]['humidity'] = float(readings[idx]['humidity'] + float(readings[idx+2]['humidity'])/2)


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

                # # assumes that the first reading is not an error. If the element is a clear error:
                # if float(readings[idx+1]['dht22']) > (dht22mean + (dht22variance * 2)) or float(readings[idx+1]['dht22']) < (dht22mean - (dht22variance * 2)):
                #
                #     # replace the element with the previous element (this is why it's import first element is not an error
                #     readings[idx + 1]['dht22'] = float(readings[idx]['dht22'])

                # if the the difference between an element and its preceding element is greater than 5:
                if (float(readings[idx + 1]['dht22']) - float(readings[idx]['dht22'])) > dht22variance/2:

                    readings[idx +1]['dht22'] = float(readings[idx]['dht22'])

                # if the the difference between an element and its next element is greater than 5:
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

                # # assumes that the first reading is not an error. If the element is a clear error:
                # if float(readings[idx + 1]['dht11']) > (dht11mean + (dht11variance * 2)) or float(
                #         readings[idx + 1]['dht11']) < (dht11mean - (dht11variance * 2)):
                #
                #     # replace the element with the previous element (this is why it's import first element is not an error
                #     readings[idx + 1]['dht11'] = float(readings[idx]['dht11'])

                # if the the difference between an element and its preceding element is greater than half the variance:
                if (float(readings[idx + 1]['dht11']) - float(readings[idx]['dht11'])) > dht11variance :

                    readings[idx +1]['dht11'] = float(readings[idx ]['dht11'])

                # if the the difference between an element and its next element is greater than half the variance:
                elif (float(readings[idx]['dht11']) - float(readings[idx + 1]['dht11'])) > dht11variance :

                    readings[idx + 1]['dht11'] = float(readings[idx]['dht11'])


    return readings




