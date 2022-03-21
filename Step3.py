import json
from collections import Counter
from statistics import mean

views_count = {}
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
views_count = Counter(views_list)

views_dict = dict(views_count)


#10 adId with max views
max_views_ids = sorted(views_count, key=views_count.get, reverse=True)[:10]

#saving data as JSON
with open('ads.json', 'r') as json_file:
    json_list = list(json_file)

# list of car price
price_gross = []

for json_str in json_list:
    result = json.loads(json_str)
    if result["id"] in max_views_ids:
        if result["price"]["consumerValue"]['gross'] not in price_gross:
            price_gross.append(result["price"]["consumerValue"]['gross'])
        else:
            continue

# list of car price (float)
price_gross_fl = []

# convert str values in list to float
for item in price_gross:
    price_gross_fl.append(float(item))

# find average value of top 10
avg_price_top10 = mean(price_gross_fl)

# output results of average price of top 10 views ads
print(avg_price_top10)
