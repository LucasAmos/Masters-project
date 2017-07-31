import math


def correctfault2(readings):
    dht22count= 0
    humiditycount = 0

    for reading in readings:

        dht22count += float(reading['dht22'])
        humiditycount += float(reading['humidity'])

    dht22mean = dht22count / len(readings)
    humiditymean = humiditycount / len(readings)


    dht22variance = 0
    humidityvariance = 0

    for reading in readings:
        dht22variance += (float(reading['dht22']) - dht22mean) ** 2
        humidityvariance += (float(reading['dht22']) - humiditymean) ** 2

    dht22variance = dht22variance / (len(readings) - 1)
    dht22variance = math.sqrt(dht22variance)

    humidityvariance = humidityvariance / (len(readings) - 1)
    humidityvariance = math.sqrt(humidityvariance)

    print("")
    print ("dht22 variance: " + str(dht22variance))
    print ("humidity variance: " + str(humidityvariance))



    # do not iterate over the first and last elements
    for idx, reading in enumerate(readings[1:-1]):
        if float(readings[idx+1]['dht22'] is not None):

            # assumes that the first reading is not an error. If the element is a clear error:
            if float(readings[idx+1]['dht22']) > 50 or float(readings[idx+1]['dht22']) < 10:

                # replace the element with the previous element (this is why it's import first element is not an error
                readings[idx + 1]['dht22'] = float(readings[idx]['dht22'])

            # if the the difference between an element and its preceding element is greater than 5:
            elif (float(readings[idx + 1]['dht22']) - float(readings[idx]['dht22'])) > dht22variance:

                readings[idx ]['dht22'] = float(readings[idx-1]['dht22'])

            # if the the difference between an element and its next element is greater than 5:
            elif (float(readings[idx ]['dht22']) - float(readings[idx + 1]['dht22'])) > dht22variance:

                readings[idx+1]['dht22'] = float(readings[idx]['dht22'])




        if float(readings[idx + 1]['humidity'] is not None):
            # assumes that the first reading is not an error. If the element is a clear error:
            if float(readings[idx + 1]['humidity']) > 70 or float(readings[idx + 1]['humidity']) < 10:

                            # replace the element with the previous element (this is why it's import first element is not an error
                readings[idx + 1]['humidity'] = float(readings[idx]['humidity'])

                        # if the the difference between an element and its preceding element is greater than 5:
            elif (float(readings[idx + 1]['humidity']) - float(readings[idx]['humidity'])) > 5:

                            # replace the element with the preceding element
                readings[idx]['humidity'] = float(readings[idx - 1]['humidity'])


        if float(readings[idx+1]['dht11'] is not None):

            # assumes that the first reading is not an error. If the element is a clear error:
            if float(readings[idx+1]['dht11']) > 50 or float(readings[idx+1]['dht11']) < 10:

                # replace the element with the previous element (this is why it's import first element is not an error
                readings[idx + 1]['dht11'] = float(readings[idx]['dht11'])

            # if the the difference between an element and its preceding element is greater than 5:
            elif (float(readings[idx + 1]['dht11']) - float(readings[idx]['dht11'])) > 3:

                readings[idx ]['dht11'] = float(readings[idx-1]['dht11'])

            # if the the difference between an element and its next element is greater than 5:
            elif (float(readings[idx ]['dht11']) - float(readings[idx + 1]['dht11'])) > 3:

                readings[idx+1]['dht11'] = float(readings[idx]['dht11'])



    return readings




