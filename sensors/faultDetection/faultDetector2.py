from datetime import  datetime

def correctfault2(readings):

    for idx, reading in enumerate(readings[4:-4]):

        index = idx+4

        mean = (float(readings[index-2]['dht22']) +
                float(readings[index-1]['dht22']) +
                float(readings[index]['dht22']) +
                float(readings[index+1]['dht22']) +
                float(readings[index+2]['dht22']))/5

        if mean * 1.5 < float(readings[index]['dht22']) or float(readings[index]['dht22']) < mean * 0.5:

            replace = (float(readings[index - 2]['dht22']) +
                       float(readings[index - 1]['dht22']) +
                       float(readings[index + 1]['dht22']) +
                       float(readings[index + 2]['dht22'])) / 4

            print("**************")
            print ("error: " + str(readings[index]['dht22']))
            readings[index]['dht22'] = replace
            print("replace: " + str(replace))
            print("**************")





    return readings




