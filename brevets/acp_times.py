"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading. You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#
VALID_BREVETS = [200, 300, 400, 600, 1000]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km: number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    #Open time = Distance ÷ Max Speed (fastest possible)
    
    ranges = [(200, 34), (200, 32), (200, 30), (400, 28), (300, 26)]
    if brevet_dist_km not in VALID_BREVETS:
      raise ValueError("Invalid brevet distance")
    if control_dist_km < 0:
      raise ValueError("Invalid control distance")
    remaining = min(control_dist_km, brevet_dist_km)
    hours = 0
    
    for size, speed in ranges:
      chunk = min(remaining, size)
      hours = hours + chunk/speed
      remaining = remaining - chunk
    start = arrow.get(brevet_start_time)
    return start.shift(minutes= round(hours *60)).isoformat()
    



def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    #closing time = Distance ÷ min Speed (slowest possible)
        
    ranges = [(200, 15), (200, 15), (200, 15), (400,11.428 ), (300, 13.333)]
    
    
    if brevet_dist_km not in VALID_BREVETS:
      raise ValueError("Invalid brevet distance")
    if control_dist_km < 0:
       raise ValueError("Invalid control distance")
    remaining = min(control_dist_km, brevet_dist_km)
    hours = 0
   
   #200km finish: Closing time is 13:30 (not 13:20 from formula)
    if remaining == 200 and brevet_dist_km == 200:
       start = arrow.get(brevet_start_time)
       return start.shift(minutes=810).isoformat() #13:30 = 810 min
    
   #400km finish: Closing time is 27:00 (not 26:40)
    if remaining == 400 and brevet_dist_km == 400:
       start = arrow.get(brevet_start_time)
       return start.shift(minutes=1620).isoformat() #27:00 = 1620 min
   
   #Controls < 60km: Closing time = distance/20 + 1 hour
    if control_dist_km < 60:
       start = arrow.get(brevet_start_time)
       hours = control_dist_km/20 +1
       return start.shift(minutes= round(hours*60)).isoformat() 
   
    for size, speed in ranges:
      chunk = min(remaining, size)
      hours = hours + chunk/speed
      remaining = remaining - chunk
      start = arrow.get(brevet_start_time)

    return start.shift(minutes= round(hours *60)).isoformat()
        
