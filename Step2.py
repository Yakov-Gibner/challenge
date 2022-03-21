import json
import jsonlines
from collections import Counter

# counter of views ads (from collections)
views_counter = {}

# list of all ad views
views_list = []


#open views.json as list
with open('views.json', 'r') as json_file_views:
    json_list_views = list(json_file_views)


#looping each line and add each id of view ad to list "views_list"
for json_str in json_list_views:
    result_views = json.loads(json_str)
    for key in result_views:
        views_list.append(result_views['ad']['id'])


#counting amount of each view per ad
views_counter = Counter(views_list)

views_dict = dict(views_counter)

#rename keys and values
array = [{'adId': i, 'views': views_dict[i]} for i in views_dict]

#save as JSON
with jsonlines.open('output.jsonl', mode='w') as writer:
    writer.write(array)


print(views_counter)

