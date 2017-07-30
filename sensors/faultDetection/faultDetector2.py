import math
def correctfault2(readings):

    count =0

    for reading in readings:

        count += float(reading['dht22'])

    mean = count/ len(readings)


    squares = 0

    for reading in readings:

        squares += (float(reading['dht22']) - mean) ** 2

    squares = squares / (len(readings) -1)
    print ("dht22 variance: " + str(math.sqrt(squares)))





    #
    #
    # for idx, reading in enumerate(readings[4:-4]):
    #
    #     dht22mean = (float(readings[idx + 2]['dht22']) +
    #                  float(readings[idx + 3]['dht22']) +
    #                  float(readings[idx + 5]['dht22']) +
    #                  float(readings[idx + 6]['dht22'])) / 4
    #
    #     if (float(readings[idx+4]['dht22']) > 50):
    #         print(str(idx+4) + " "+str(readings[idx+4]['dht22']))
    #
    #         readings[idx + 4]['dht22'] = dht22mean
    #
    #     elif dht22mean * 1.3 < float(readings[idx+4]['dht22']) or float(readings[idx+4]['dht22']) < dht22mean * 0.7:
    #
    #         print("loop 2")
    #         print(idx+4)
    #         print(readings[idx + 4]['dht22'])
    #
    #         readings[idx + 4]['dht22'] = dht22mean









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




