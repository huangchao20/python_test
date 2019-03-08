import requests
import pygal
import os
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# import json
import simple_pickle.utils as spick

filename = 'my_save'

# 将请求的数据本地化存储
if os.path.exists(filename) == False:
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    spick.write_pickle(r, filename)
    print('First Request...')
else:
    r = spick.read_pickle(filename)
    print('Read from local.')

print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
# print(response_dict.keys())
print('Total repositories:', response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:',len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print('\nKeys:',len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# print('\nSelected information about first repository:')
# for repo_dict in repo_dicts:
#     print('Name:',repo_dict['name'])
#     print('Owner:',repo_dict['owner']['login'])
#     print('Stars:',repo_dict['stargazers_count'])
#     print('Repository:',repo_dict['html_url'])
#     print('Created:',repo_dict['created_at'])
#     print('Updated:',repo_dict['updated_at'])
#     print('Description:',repo_dict['description'])
#     print()

names, stars = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
