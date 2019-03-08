import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
import pygal_maps_world.maps

filename = 'population_data.json'


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code


with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name+": "+ str(population))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010,by Country'
wm.add('2010', cc_populations)
wm.render_to_file('world_population.svg')

print('countof items = ' + str(len(pop_data)))
