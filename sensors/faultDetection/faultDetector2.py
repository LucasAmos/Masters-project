import math


def correctfault2(readings, tempsensorid):
    dht11count = 0
    dht22count= 0
    humiditycount = 0

    for reading in readings:


        dht22count += float(reading[tempsensorid])
        humiditycount += float(reading['humidity'])

    dht22mean = dht22count / len(readings)
    humiditymean = humiditycount / len(readings)


    dht22variance = 0
    humidityvariance = 0

    for reading in readings:
        dht22variance += (float(reading[tempsensorid]) - dht22mean) ** 2
        humidityvariance += (float(reading[tempsensorid]) - humiditymean) ** 2

    dht22variance = dht22variance / (len(readings) - 1)
    dht22variance = math.sqrt(dht22variance)

    humidityvariance = humidityvariance / (len(readings) - 1)
    humidityvariance = math.sqrt(humidityvariance)

    print("")
    print (tempsensorid + " mean: " + str(dht22mean))
    print (tempsensorid +" variance: " + str(dht22variance))
    print ("humidity mean: " + str(humiditymean))
    print ("humidity variance: " + str(humidityvariance))

    if tempsensorid == "dht22":

        # do not iterate over the first and last elements
        for idx, reading in enumerate(readings[1:-1]):
            if float(readings[idx+1][tempsensorid] is not None):

                # assumes that the first reading is not an error. If the element is a clear error:
                if float(readings[idx+1][tempsensorid]) > (dht22mean + (dht22variance * 2)) or float(readings[idx+1][tempsensorid]) < (dht22mean - (dht22variance * 2)):

                    # replace the element with the previous element (this is why it's import first element is not an error
                    readings[idx + 1][tempsensorid] = float(readings[idx][tempsensorid])

                # if the the difference between an element and its preceding element is greater than 5:
                if (float(readings[idx + 1][tempsensorid]) - float(readings[idx][tempsensorid])) > dht22variance * 2:

                    readings[idx ][tempsensorid] = float(readings[idx-1][tempsensorid])

                # if the the difference between an element and its next element is greater than 5:
                elif (float(readings[idx ][tempsensorid]) - float(readings[idx + 1][tempsensorid])) > dht22variance *2:

                    readings[idx+1][tempsensorid] = float(readings[idx][tempsensorid])

        if tempsensorid == "dht11":

            # do not iterate over the first and last elements
            for idx, reading in enumerate(readings[1:-1]):
                if float(readings[idx + 1][tempsensorid] is not None):

                    # assumes that the first reading is not an error. If the element is a clear error:
                    if float(readings[idx + 1][tempsensorid]) > (dht22mean + (dht22variance * 2)) or float(
                            readings[idx + 1][tempsensorid]) < (dht22mean - (dht22variance * 2)):
                        # replace the element with the previous element (this is why it's import first element is not an error
                        readings[idx + 1][tempsensorid] = float(readings[idx][tempsensorid])

                    # if the the difference between an element and its preceding element is greater than 5:
                    if (float(readings[idx + 1][tempsensorid]) - float(readings[idx][tempsensorid])) > dht22variance *4:

                        readings[idx][tempsensorid] = float(readings[idx - 1][tempsensorid])

                    # if the the difference between an element and its next element is greater than 5:
                    elif (float(readings[idx][tempsensorid]) - float(readings[idx + 1][tempsensorid])) > dht22variance *4:

                        readings[idx + 1][tempsensorid] = float(readings[idx][tempsensorid])




        if float(readings[idx + 1]['humidity'] is not None):
            # assumes that the first reading is not an error. If the element is a clear error:
            if float(readings[idx + 1]['humidity']) > (humiditymean + humidityvariance) or float(readings[idx + 1]['humidity']) < (humiditymean -humidityvariance):

                            # replace the element with the previous element (this is why it's import first element is not an error
                readings[idx + 1]['humidity'] = float(readings[idx]['humidity'])

                        # if the the difference between an element and its preceding element is greater than 5:
            elif (float(readings[idx + 1]['humidity']) - float(readings[idx]['humidity'])) > humidityvariance/2:

                            # replace the element with the preceding element
                readings[idx]['humidity'] = float(readings[idx - 1]['humidity'])



    print("fault detector 2")
    return readings




