from datetime import  datetime

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

                readings[idx + 1]['dht22'] = float(readings[idx]['dht22'])


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
            elif (float(readings[idx + 1]['dht11']) - float(readings[idx]['dht11'])) > 5:

                readings[idx ]['dht11'] = float(readings[idx-1]['dht11'])


    return readings