import math


def correctfault2(readings):

    dhtcount =0
    humiditycount = 0


    for reading in readings:

        dhtcount += float(reading['dht22'])
        humiditycount += float(reading['humidity'])


    dhtmean = dhtcount / len(readings)
    humiditymean = humiditycount / len(readings)

    dht22variance = 0
    humidityvariance = 0

    for reading in readings:
        dht22variance += (float(reading['dht22']) - dhtmean) ** 2
        humidityvariance += (float(reading['humidity']) - humiditymean) ** 2



    dht22variance = dht22variance / (len(readings) -1)
    dht22variance = math.sqrt(dht22variance)
    humidityvariance = humidityvariance / (len(readings) - 1)
    humidityvariance = math.sqrt(humidityvariance)


    for idx, reading in enumerate(readings[4:-4]):

        dht22mean = (float(readings[idx + 2]['dht22']) +
                     float(readings[idx + 3]['dht22']) +
                     float(readings[idx + 5]['dht22']) +
                     float(readings[idx + 6]['dht22'])) / 4


        if (float(readings[idx+4]['dht22']) > (dhtmean + (dht22variance *1.5)) or float(readings[idx+4]['dht22']) <(dhtmean - (dht22variance *1.5)) ) :
            #
            # print("loop 2")
            # print(idx+4)
            # print(readings[idx + 4]['dht22'])

            readings[idx + 4]['dht22'] = dht22mean

        humiditymean = (float(readings[idx + 2]['humidity']) +
                        float(readings[idx + 3]['humidity']) +
                        float(readings[idx + 5]['humidity']) +
                        float(readings[idx + 6]['humidity'])) / 4


        if (float(readings[idx + 4]['humidity']) > (humiditymean + (humidityvariance * 1.5)) or float(readings[idx + 4]['humidity']) < (humiditymean - (humidityvariance * 1.5))  ):
            # print("loop 2")
            # print(idx + 4)
            # print(readings[idx + 4]['humidity'])

            readings[idx + 4]['humidity'] = humiditymean

    print ("dht22 mean: " + str(dhtmean))
    print ("dht22 variance: " + str(dht22variance))

    print ("humidity mean: " + str(humiditymean))
    print ("humidity variance: " + str(humidityvariance))


















        # if (readings[idx]['dht22'] > 5000):
        #     print("")
        #     print("yep")
        #     print(idx)
        #     print(readings[idx]['date'] )




        #
        # if float(readings[idx]['dht22'] is not None):
        #
        #     dht22mean = (float(readings[idx-2]['dht22']) +
        #             float(readings[idx-1]['dht22']) +
        #             float(readings[idx]['dht22']) +
        #             float(readings[idx+1]['dht22']) +
        #             float(readings[idx+2]['dht22']))/5
        #
        #     if dht22mean * 1.3 < float(readings[idx]['dht22']) or float(readings[idx]['dht22']) < dht22mean * 0.7:
        #
        #         replace = (float(readings[idx - 2]['dht22']) +
        #                    float(readings[idx - 1]['dht22']) +
        #                    float(readings[idx + 1]['dht22']) +
        #                    float(readings[idx + 2]['dht22'])) / 4
        #
        #         readings[idx]['dht22'] = replace
        #
        #         print("**************")
        #         print ("error temp: " + str(readings[idx]['dht22']))
        #         print("replace: " + str(replace))
        #         print("**************")





    return readings




