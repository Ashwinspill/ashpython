test_list = [{'ford': 'GT', 'bmw':'M3', 'merc': 'E3'},
             {'ford': 'MUSTANG'}, {'bmw': 'M3', 'ford': 'F-series'}]

print("The original list is : " + str(test_list))

res = [sub['ford'] for sub in test_list]

print("The values corresponding to key : " + str(res))