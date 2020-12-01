import Markov as mk
weather_today = mk.Markov()
weather_today.load_data(file_path='./weather.csv')
print(weather_today.get_prob('windy', 'cloudy')) # This line should print 0.2