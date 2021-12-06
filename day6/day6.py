from pathlib import Path

input = Path(__file__).with_name('day6.txt')
input = input.open('r').read()

def process_input(input):
    x = input.strip().split(',')
    for i in range(0,len(x)):
        x[i] = int(x[i])
    
    return x

def create_population(population):
    new_pop = [0] * 9

    for age in population:
        new_pop[age] += 1

    return new_pop

def pass_n_days(population, days):
    for day in range(1, days + 1):
        newborns = population[0]

        population = population[1:] + [newborns]
        population[6] += newborns

    return population

pop_init_state = process_input(input)
population = create_population(pop_init_state)
print(f'Population starts of with: {sum(population)} individuals')
days = [80,256]

for d in days:
    pop_aged = pass_n_days(population, d)
    print(f'After {d} days there are {sum(pop_aged)} individuals')
