#!/usr/bin/env python3

import json, requests
import readline
url="https://translifeline.org/hiring_stats_sample"

debug=0

try:
    r = requests.get(url)
    if debug:
    	print ('Status code', r.status_code)
    r.raise_for_status() 
    json_data = r.json()
    if debug:
    	print (json_data)
    print ('Answered ', json_data['answered'])
    print ('Notes: ', json_data['notes'])
except ValueError:
    print ("Invald Json")
    # in reality log the error
#help(requests.get)
#help (requests.Response)

#import readline
#readline.write_history_file('get_json.py')
