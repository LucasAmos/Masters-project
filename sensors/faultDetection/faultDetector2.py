from datetime import  datetime

def correctfault2(readings):

    for idx, reading in enumerate(readings[4:-4]):

        index = idx+4

        if float(readings[idx+1]['dht22'] is not None):


            dht22mean = (float(readings[index-2]['dht22']) +
                    float(readings[index-1]['dht22']) +
                    float(readings[index]['dht22']) +
                    float(readings[index+1]['dht22']) +
                    float(readings[index+2]['dht22']))/5

            if dht22mean * 1.3 < float(readings[index]['dht22']) or float(readings[index]['dht22']) < dht22mean * 0.7:

                replace = (float(readings[index - 2]['dht22']) +
                           float(readings[index - 1]['dht22']) +
                           float(readings[index + 1]['dht22']) +
                           float(readings[index + 2]['dht22'])) / 4

                # print("**************")
                # print ("error temp: " + str(readings[index]['dht22']))
                # readings[index]['dht22'] = replace
                # print("replace: " + str(replace))
                # print("**************")

        if float(readings[idx+1]['humidity'] is not None):


            humiditymean = (float(readings[index - 2]['humidity']) +
                         float(readings[index - 1]['humidity']) +
                         float(readings[index]['humidity']) +
                         float(readings[index + 1]['humidity']) +
                         float(readings[index + 2]['humidity'])) / 5

            if humiditymean * 1.3 < float(readings[index]['humidity']) or float(readings[index]['humidity']) < humiditymean * 0.7:
                replace = (float(readings[index - 2]['humidity']) +
                           float(readings[index - 1]['humidity']) +
                           float(readings[index + 1]['humidity']) +
                           float(readings[index + 2]['humidity'])) / 4

                # print("**************")
                # print ("error humidity: " + str(readings[index]['humidity']))
                # readings[index]['humidity'] = replace
                # print("replace: " + str(replace))
                # print("**************")


        if float(readings[idx+1]['dht11'] is not None):


            dht22mean = (float(readings[index-2]['dht11']) +
                    float(readings[index-1]['dht11']) +
                    float(readings[index]['dht11']) +
                    float(readings[index+1]['dht11']) +
                    float(readings[index+2]['dht11']))/5

            if dht22mean * 1.3 < float(readings[index]['dht11']) or float(readings[index]['dht11']) < dht22mean * 0.7:

                replace = (float(readings[index - 2]['dht11']) +
                           float(readings[index - 1]['dht11']) +
                           float(readings[index + 1]['dht11']) +
                           float(readings[index + 2]['dht11'])) / 4

                # print("**************")
                # print ("error temp: " + str(readings[index]['dht11']))
                # print("replace: " + str(replace))
                # print("**************")


    return readings




