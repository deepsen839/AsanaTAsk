import sys
import os
import json
import asana
def user_select_option(message, options):
    option_lst = list(options)
    print(message)
    for i, val in enumerate(option_lst):
        print(i, ': ' + val['name'])
    index = int(input("Enter choice (default 0): ") or 0)
    return option_lst[index]
params = {
    'project': '1201821606208506',
}

client = asana.Client.access_token('1/1201821606208506:4ab76f8873e4e4c04fc9cece4fbe6b1b')
#tasks = [x for x in client.tasks.find_all(params)]
#print(tasks)
result = client.tasks.create_task({'name': 'Buy catnip','notes': 'Mittens really likes the stuff from Humboldt.',"projects":['1201799999322388']},opt_pretty=True)

print(json.dumps(result, indent=4))
