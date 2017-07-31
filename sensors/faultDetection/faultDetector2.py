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


    for idx, reading in enumerate(readings[1:-1]):

        # compare to preceding value
        difference = float(readings[idx+1]['dht22']) - float(readings[idx]['dht22'])



        mean = (float(readings[idx+2]['dht22']) + float(readings[idx]['dht22']))/2

        if float(readings[idx + 1]['dht22']) - mean > (dht22variance *2 ):

            readings[idx + 1]['dht22'] = dht22mean;

            #print("Idx" + str(idx+1) +": " + str(float(readings[idx+1]['dht22']))+" Diff: " + str(difference)+ " " + " Mean: " + str(mean))










            #
        # if (float(readings[idx+4]['dht22']) > (dht22mean + (dht22variance *1.5)) or float(readings[idx+4]['dht22']) <(dht22mean - (dht22variance *1.5)) ) :
        #
        #     readings[idx + 4]['dht22'] = dht22mean







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



