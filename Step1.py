import json
from datetime import datetime


black_Merc = []
events_time = []


with open('ads.json', 'r') as json_file:
    for json_str in json_file:
        result_ads = json.loads(json_str)
        if result_ads["make"] == 'MERCEDES-BENZ' and result_ads["attributes"]['exteriorColor'] == 'BLACK':
            black_Merc.append(result_ads["id"])


with open('views.json', 'r') as json_file_views:
    for json_str in json_file_views:
        result_views = json.loads(json_str)
        event_t = datetime.utcfromtimestamp(result_views['event']['time']).strftime('%Y-%m-%dT%H:%M:%SZ')
        if result_views['ad']['id'] in black_Merc:
            events_time.append(f"{result_views['ad']['id']}, {event_t} \n")


with open('step1_output.csv', mode='w') as csv_file:
    csv_file.writelines(events_time)
