import numpy as np
import random as random

weather_array=np.array(['sunny','cloudy','rainy','snowy','windy','hailing'])

class Markov:
    def __init__(self,day_zero_weather=None): # You will need to modify this header line later in Part C
        #print("init")
        self.data = self.load_data()
        self.day_zero_weather=day_zero_weather
        self.day_zero_num =self.weather2num(day_zero_weather)
        #print("??",day_zero_weather,self.day_zero_num)
    @staticmethod
    def weather2num(weather_string):
        #print("weather2num")
        weather_num= -1
        for i in range(0,6):
            #print("weather_string:",weather_string)
            if(weather_string == weather_array[i]):
                weather_num=i
                
        if weather_num == -1:
            raise Exception('Weather not recognized')
            
        return weather_num
    def load_data(self, file_path='./weather.csv'):
        return np.genfromtxt(file_path,delimiter=",")
    
    
    def get_prob(self, current_day_weather, next_day_weather): 
                
        cweather_num=self.weather2num(current_day_weather)      
        nweather_num=self.weather2num(next_day_weather)
          
        
        return self.data[cweather_num,nweather_num]
    
    def __iter__(self):
        #print("day0num:",self.day_zero_num)
        if(self.day_zero_weather is None):
            raise Exception('No initial value')
        return MarkovIterator(self.day_zero_num,self.get_prob)
    
    def _simulate_weather_for_day(self,day):
        if(self.day_zero_weather is None):
            raise Exception('No initial value')
        if(day==0):
            return self.day_zero_weather
        
        
        it=self.__iter__()
        for i in range(0,day-1):
            next(it)
        return next(it)
        
    def get_weather_for_day(self,day, trials):
        wlist=[];
        for sid in range(0,trials):
            #wlist.append(weather_array[1])
            wlist.append(self._simulate_weather_for_day(day))
        return wlist
        
class MarkovIterator:
    def __init__(self,cweather_num,get_prob):
        self.cweather_num=cweather_num
        self.get_prob=get_prob
        self.nit=0
    def __iter__(self):
        return self
    def __next__(self):
        #print("cweather", self.cweather_num)
        if(self.nit>=9999):
            raise StopIteration()
        self.cweather_num=random.choices([0,1,2,3,4,5],weights=[self.get_prob(weather_array[self.cweather_num],weather_array[i]) for i in range(0,6)])[0] #[0]means converting single element list to a single number
        
        self.nit+=1
        
        return  weather_array[self.cweather_num]
        
