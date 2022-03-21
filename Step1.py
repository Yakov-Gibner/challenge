import json
import csv
from datetime import datetime

# list ids of Black MERCEDES-BENZ
black_Merc = []

# list time of views (ids of Black MERCEDES-BENZ)
event_time = []


# open ads.json
with open('ads.json', 'r') as json_file:
    json_list = list(json_file)


# open views.json as list
with open('views.json', 'r') as json_file_views:
    json_list_views = list(json_file_views)


# looking for ids of Black MERCEDES-BENZ and write them to the list "black_Merc"
for json_str in json_list:
    result = json.loads(json_str)
    if result["make"] == 'MERCEDES-BENZ' and result["attributes"]['exteriorColor'] == 'BLACK':
        black_Merc.append(result["id"])


# looking for time of views (ids of Black MERCEDES-BENZ) and write them to the list "event_time"
for json_str in json_list_views:
    result_views = json.loads(json_str)
    if result_views['ad']['id'] in black_Merc:
        event_time.append(result_views['ad']['id'])
        event_time.append(datetime.utcfromtimestamp(result_views['event']['time']).strftime('%Y-%m-%dT%H:%M:%SZ'))
        event_time.append('\n')


# writing output of ids and time to csv-file
with open('step1.csv', mode='w', newline='') as csv_file:
    ads_writer = csv.writer(csv_file)
    ads_writer.writerow(event_time)


print(event_time)