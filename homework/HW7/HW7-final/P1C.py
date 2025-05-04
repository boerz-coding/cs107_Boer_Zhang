##P1C.py
from Markov import *
city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}
city_maxweather={}
for city in city_weather:
    weather_today=Markov(city_weather[city])
    prediction=weather_today.get_weather_for_day(7, 100)
    result_dic={}
    for weather_k in weather_array:
        result_dic[weather_k]=0
    for result_k in prediction:
        result_dic[result_k]+=1
    print(city+":",result_dic)
    weather_maxday=-1;
    weather_maxweather=None
    for weather_k in weather_array:
        if result_dic[weather_k]>weather_maxday:
            weather_maxweather=weather_k
            weather_maxday=result_dic[weather_k]
    city_maxweather[city]=weather_maxweather
        
    
print("\nMost likely weather in seven days")
print("----------------------------------")
for city in city_weather:
    print(city+":",city_maxweather[city])
