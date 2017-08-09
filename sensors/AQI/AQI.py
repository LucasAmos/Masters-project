from flask import jsonify
def ratings(locationreadings):

    for reading in locationreadings:

        id = locationreadings[reading]['deviceid']
        voc = locationreadings[reading]['voc']
        humidity = locationreadings[reading]['humidity']
        temperature = locationreadings[reading]['dht11'] if locationreadings[reading]['dht11'] != None else locationreadings[reading]['dht22']
        locationreadings[reading]['temperature'] = temperature

        metric = calculateMetric(temperature, humidity, voc)

        metric = round((metric[0] + metric[1] + metric[2])/3, 2)

        locationreadings[reading]['AQI'] = metric

    return locationreadings



def calculateMetric(temperature, humidity, voc):

    temperature = float(temperature)
    humidity = float(humidity)
    voc = float(voc)
    temperaturerating = 0
    humidityrating = 0
    vocrating = 0

    #good range
    if (temperature >= 23 and temperature <=25):
        temperaturerating = 1

    #medium range
    elif temperature >= 21 and temperature <23:
        temperaturerating = (temperature -21) /2

    elif(temperature > 25 and temperature <=27):
        temperaturerating = (27 - temperature) / 2

    # bad range
    elif temperature >= 20 and temperature < 21:
        temperaturerating = (temperature - 20) -1

    elif temperature > 27 and temperature <= 28:
        temperaturerating = (27 - temperature)

    else:
        temperaturerating = -1


    if (humidity >=40 and humidity <=60):
        humidityrating = 1

    elif (humidity >= 30 and humidity <40):
        humidityrating = (humidity - 30) /10

    elif (humidity > 60 and humidity <= 70):
        humidityrating = (70 - humidity) / 10

    elif (humidity >= 20 and humidity <30):
        humidityrating = ((humidity - 20) /10) -1

    elif (humidity > 70 and humidity <80):
        humidityrating = ((70 - humidity) /10)

    else:
        humidityrating = -1



    if (voc < 200):
        vocrating = 1

    elif (voc <= 400):
        vocrating = (400 - voc) /200

    elif (voc<= 600):
        vocrating = (400 - voc) /200

    else:
        vocrating = -1


    return [round(temperaturerating, 2), round(humidityrating, 2), float(vocrating)]


