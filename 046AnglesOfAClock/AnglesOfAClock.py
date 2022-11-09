def get_legs_angle(curTime):
    hours, minutes = curTime.split(":")
    minuteLegAngle = int(minutes) * 6    # minutes / 60 * 360 (in degrees)
    hourLegAngle = (int(hours) + int(minutes) / 60) * 30       # hours / 12 * 360 + minutes / (12 * 60) * 360 (in degrees)
    
    resAngle = abs(hourLegAngle - minuteLegAngle)
    return min(resAngle, 360 - resAngle)     # scaled to [0, 180]
