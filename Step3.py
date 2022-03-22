import json
from collections import Counter
from statistics import mean

views_count = {}
views_list = []
price_gross = []
price_gross_fl = []


with open('views.json', 'r') as json_file_views:
    for json_str in json_file_views:
        result_views = json.loads(json_str)
        for i in result_views:
            views_list.append(result_views['ad']['id'])


views_count = Counter(views_list)
views_dict = dict(views_count)


max_views_ids = sorted(views_count, key=views_count.get, reverse=True)[:10]


with open('ads.json', 'r') as json_file:
    for json_str in json_file:
        result = json.loads(json_str)
        if result["id"] in max_views_ids:
            if result["price"]["consumerValue"]['gross'] not in price_gross:
                price_gross.append(result["price"]["consumerValue"]['gross'])
            else:
                continue


for item in price_gross:
    price_gross_fl.append(float(item))


avg_price_top10 = mean(price_gross_fl)


print(avg_price_top10)
