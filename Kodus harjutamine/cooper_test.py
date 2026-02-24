def grade(distance, gender):
    if gender == 'M':
        if distance >= 2800:
            return 'väga hea'
        elif distance < 2000:
            missing = 2000 - distance
            return f'nõrk, järgmisest hindest puudu {missing} m'
        else:
            missing = 2800 - distance
            return f'rahuldav, järgmisest hindest puudu {missing} m'
    elif gender == 'N':
        if distance >= 2600:
            return 'väga hea'
        elif distance < 1800:
            missing = 1800 - distance
            return f'nõrk, järgmisest hindest puudu {missing} m'
        else:
            missing = 2600 - distance
            return f'rahuldav, järgmisest hindest puudu {missing} m'


filename = input('Sisestage failinimi: ')
results = []
with open(filename, 'r') as f:
    for line in f:
        parts = line.strip().split()
        distance = int(parts[0])
        gender = parts[1]
        results.append((gender, distance))


for gender, distance in results:
    result = grade(distance, gender)
    print(f'{gender} {distance} m, {result}')


male_distances = [d for g, d in results if g == 'M']
female_distances = [d for g, d in results if g == 'N']

avg_male = round(sum(male_distances)/len(male_distances))
avg_female = round(sum(female_distances)/len(female_distances))

print('Keskmised:')
print(f'M {avg_male} m, {grade(avg_male, "M")}')
print(f'N {avg_female} m, {grade(avg_female, "N")}')