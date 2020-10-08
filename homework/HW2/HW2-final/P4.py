import numpy as np
import matplotlib.pyplot as plt
import datetime


def clockhand(rhand):
    def clocktime(theta_time):
        theta_time_rad=theta_time*np.pi/180
        x_time=rhand*np.cos(theta_time_rad)
        y_time=rhand*np.sin(theta_time_rad)
        return x_time,y_time
    return clocktime
        

### Closure defined up here


# Specify the length of hour, minute and second hands
rhour=4
rminute=5
rsecond=6
hour_hand = clockhand(rhour)
minute_hand = clockhand(rminute)
second_hand = clockhand(rsecond)
#########################

# Plot the clock
fig = plt.figure(figsize=(6,6))
currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand
theta_hour=90-30*hour-minute/2
theta_minute=90-6*minute
theta_second=90-6*second


x_hour, y_hour = hour_hand(theta_hour)
x_minute, y_minute = minute_hand(theta_minute)
x_second, y_second = second_hand(theta_second)

#plt.cla()
plt.plot([0,x_hour],[0,y_hour],linewidth=4)
plt.plot([0,x_minute],[0,y_minute],linewidth=3)
plt.plot([0,x_second],[0,y_second],linewidth=2)
plt.axis([-7, 7, -7, 7])
plt.axis('off')
plt.show()
