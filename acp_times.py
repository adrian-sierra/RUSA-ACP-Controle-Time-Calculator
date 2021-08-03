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
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    control = float(control_dist_km)
  
    time = 0.0

    if brevet_dist_km == 200:
        if control <= 200:
            time += control/34
        if control > 200 and control <= 240:
            time += 200/34

    if brevet_dist_km == 300:
        if control <= 200:
            time += control/34
        elif control > 200 and control <= 300:
            time += 200/34
            control -= 200
 
            time += control/32
        elif control > 300 and control <= 360:
            time += (200/34 + 100/32)

    if brevet_dist_km == 400:
        if control <= 200:
            time += control/34
        elif control > 200 and control <= 400:
            time += 200/34
            control -= 200
 
            time += control/32
        elif control > 400 and control <= 480:
            time += (200/34 + 200/32)
     
    if brevet_dist_km == 600:
       if control <= 200:
           time += control/34
       elif control > 200 and control <= 400:
           time += 200/34
           control -= 200
 
           time += control/32
       elif control > 400 and control <= 600:
           time += 200/34
           control -= 200

           time += 200/32
           control -= 200

           time += control/30
       elif control > 600 and control <= 720:
           time += (200/34 + 200/32 + 200/30)

    if brevet_dist_km == 1000:
       if control <= 200:
           time += control/34
       elif control > 200 and control <= 400:
           time += 200/34
           control -= 200

           time += control/32
       elif control > 400 and control <= 600:
           time += 200/34
           control -= 200

           time += 200/32
           control -= 200

           time += control/30
       elif control > 600 and control <= 1000:
           time += 200/34
           control -= 200

           time += 200/32
           control -= 200
 
           time += 200/30
           control -= 200

           time += control/28
       elif control > 1000 and control <= 1200:
           time += (200/34 + 200/32 + 200/30 + 400/28)
       elif control > 1200 and control <= 1300:
           time += 200/34
           control -= 200

           time += 200/32
           control -= 200
 
           time += 200/30
           control -= 200

           time += 400/28
           control -= 400

           time += control/26

    hrs = int(time)
    mins = (time * 60) % 60
    sec = (time * 3600) % 60
    
    date_arrow = arrow.get(brevet_start_time, 'YYYY-MM-DD HH:mm:ss')

    start = date_arrow.shift(hours=hrs, minutes=mins, seconds=sec).isoformat()

    return start

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
    control = float(control_dist_km)

    time = 0.0
   
    if brevet_dist_km == 200:
        if (control >= 200 and control <= 240):
            time = 13.5
        elif control <= 60:
            time = (control/20 + 1)
        elif control > 60 and control < 200:
            time += ( (60/20) + 1)
            control -= 60

            time += control/15

    if brevet_dist_km == 300:
        if (control >= 300 and control <= 360):
            time = 20
        elif control <= 60:
            time = ((control/20) + 1)
        elif control > 60 and control < 300:
            time += ( (60/20) + 1)
            control -= 60

            time += control/15

    if brevet_dist_km == 400:
        if (control >= 400 and control <= 480):
            time = 27
        elif control <= 60:
            time = (control/20 + 1)
        elif control > 60 and control < 400:
            time += ( (60/20) + 1)
            control -= 60

            time += control/15

    if brevet_dist_km == 600:
        if (control >= 600 and control <= 720):
            time = 40
        elif control <= 60:
            time = (control/20 + 1)
        elif control > 60 and control < 600:
            time += ( (60/20) + 1)
            control -= 60

            time += control/15

    if brevet_dist_km == 1000:
        if (control >= 1000 and control <= 1200):
            time = 75
        elif control <= 60:
            time = (control/20 + 1)
        elif control > 60 and control <= 600:
            time += ( (60/20) + 1)
            control -= 60

            time += control/15
        elif control > 600 and control < 1000:
            time += ( (60/20) + 1)
            control -= 60
    
            time += 540/15
            control -= 540

            time += control/11.428
        elif control > 1200 and control <= 1300:
            time += ( (60/20) + 1)
            control -= 60
         
            time += 540/15
            control -= 540

            time += 400/11.428
            control -= 400

            time += control/13.333

    hrs = int(time)
    mins = (time * 60) % 60
    sec = (time * 3600) % 60

    date_arrow = arrow.get(brevet_start_time, 'YYYY-MM-DD HH:mm:ss')

    start = date_arrow.shift(hours=hrs, minutes=mins, seconds=sec).isoformat()

    return start


































