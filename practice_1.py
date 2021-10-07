import datetime

def twelveto24(s):
    twelve_hr_format = '%-I:%M%p'
    twentyfour_hr_format = '%H:%M'
    s.strftime(twentyfour_hr_format)
    print(s)
    
twelveto24('10:10am')