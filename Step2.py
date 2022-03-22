import json
import jsonlines
from collections import Counter


views_counter = {}
views_list = []


with open('views.json', 'r') as json_file_views:
    for json_str in json_file_views:
        result_views = json.loads(json_str)
        for i in result_views:
            views_list.append(result_views['ad']['id'])


views_counter = Counter(views_list)
views_dict = dict(views_counter)

array = [{'adId': i, 'views': views_dict[i]} for i in views_dict]


with jsonlines.open('step2_output.jsonl', 'w') as writer:
    writer.write_all(array)
