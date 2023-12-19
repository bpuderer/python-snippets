from itertools import zip_longest
import operator


# is valid rgb
data = (0, 243, 50)
data = (0, -243, 50)
print(all(0 <= val <= 255 for val in data))


# str contain any digits
data = 'aadfasdfasf'
#data = '345'
print(any(char.isdigit() for char in data))


#enumerate and zip
#itertools.zip_longest
countries = ['Sweden', 'Finland', 'Norway']
capitals = ['Stockholm', 'Helsinki']

for country, capital in zip(countries, capitals):
    print(f'The capital of {country} is {capital}')

for country, capital in zip_longest(countries, capitals, fillvalue='Unknown'):
    print(f'The capital of {country} is {capital}')


for index, (country, capital) in enumerate(zip(countries, capitals), start=1):
    print(f'{index} The capital of {country} is {capital}')

print(list(zip(countries, capitals)))



def annual_population_average(years, pops):
    '''
        (year, pop, running_average)
    '''
    result = []
    total = 0
    for i, (year, pop) in enumerate(zip(years, pops), start=1):
        total += pop
        result.append((year, pop, round(total/i)))
    return result

years = [2019, 2020, 2021, 2022]
pops = [100, 200, 300, 400]
print(annual_population_average(years, pops))


# reverse, [::-1], reversed()


# country with the lowest population
countries = ['Sweden', 'Finland', 'Norway']
pops = [789, 123, 456]

temp = list(zip(pops, countries))
# first item in tuple used for comparison
print(f'country with lowest pop: {min(temp)}')
# if didn't know that
temp = list(zip(countries, pops))
print(f'country with lowest pop: {min(temp, key=lambda x: x[1])}')
# ...and also wanted to avoid lambda
print(f'country with lowest pop: {min(temp, key=operator.itemgetter(1))}')
