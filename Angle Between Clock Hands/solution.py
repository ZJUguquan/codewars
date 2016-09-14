'''
Best practice:

import math
def handAngle(hours, minutes):
    degrees = abs(.5 * (60 * hours + minutes) - 6 * minutes)
    if degrees > 180:
        degrees = 360 - degrees
    return (math.pi / 180) * degrees
'''

import math
def degToRad(n):
    return n * math.pi / 180;

def handAngle(hours, minutes):
    clockDegs = 360
    minsPerHour = 60
    hoursPerClock = 12
    degPerMin = (clockDegs / minsPerHour)
    degPerHour = (clockDegs / hoursPerClock / minsPerHour)
    hourAngle = degPerHour * (hours * minsPerHour + minutes);
    minuteAngle = degPerMin * minutes;
    angle = math.fabs(hourAngle - minuteAngle);
    return degToRad( min(clockDegs-angle, angle) )