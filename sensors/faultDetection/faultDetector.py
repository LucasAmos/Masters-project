
def correctfault(readings):




    # do not iterate over the first and last elements
    for idx, reading in enumerate(readings[1:-1]):

        if float(readings[idx+1]['dht22'] is not None):

            # assumes that the first reading is not an error. If the element is a clear error:
            if float(readings[idx+1]['dht22']) > 50 or float(readings[idx+1]['dht22']) < 10:

                # replace the element with the previous element (this is why it's import first element is not an error
                readings[idx + 1]['dht22'] = float(readings[idx]['dht22'])

            # if the the difference between an element and its preceding element is greater than 5:
            elif (float(readings[idx + 1]['dht22']) - float(readings[idx]['dht22'])) > 5:

                # replace the element with the preceding element
                readings[idx + 1]['dht22'] = float(readings[idx]['dht22'])




            # elif (float(readings[idx + 1]['dht22']) - float(readings[idx + 2]['dht22'])) > 5:
            #     print ("idx :" + readings[idx + 1]['dht22'] + "  " + "idx+1 " + readings[idx + 2]['dht22'])
            #
            #     readings[idx + 1]['dht22'] = float(readings[idx + 2]['dht22'])

    for idx, reading in enumerate(readings[1:-1]):

        if float(readings[idx]['dht11'] is not None):

            if float(readings[idx+1]['dht11']) > 50 or float(readings[idx+1]['dht11']) < 10:
                readings[idx + 1]['dht11'] = float(readings[idx]['dht11'])

            elif 50 < float(readings[idx + 1]['dht11']) - float(readings[idx + 2]['dht11']) > 5:
                readings[idx + 2]['dht11'] = float(readings[idx + 1]['dht11'])



    return readings