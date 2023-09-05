"""

    SOLVING 0/1 KNAPSACK USING THREE METHODS:

                            1.BRUTE FORCE
                            2.GREEDY ALGORITHM
                            3.DYNAMIC PROGRAMMING

    Finds the optimal value possible from a combination of Items, given a cost constraint.
    PARAMETERS: items, a list of Items to consider, max_cost, the cost/priority constraint
    RETURNS: the list of optimal Items and the total value attained


"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time


# a dictionary of HOUSEHOLDS APPLIANCES, cost and priority for usage
APPLIANCE_POWER_USAGE = {
    'Television': [493, 2],
    'Dishwasher': [603, 7],
    'Home_computer': [13, 6],
    'Vacuum_cleaner': [93, 5],
    'Hair_dryer': [88, 4],
    'Iron': [93, 3],
    'Lamp': [21, 15],
    'Iron1': [9, 16],
    'Lamp2': [22, 18],
    'Washing_machine1': [201, 10],
    'Washing_machine2': [73, 11],
    'Washing_machine3': [54, 12],
    'Washing_machine4': [94, 13],
    'Washing_machine5': [145, 14],
}

APPLIANCE_POWER_USAGE1 = {
    'Television': [493, 2],
    'Dishwasher': [373, 7],
    'Home_computer': [13, 6],
    'Vacuum_cleaner': [93, 5],
    'Hair_dryer': [88, 4],
    'Iron': [93, 3],
    'Lamp': [20, 8],
    'Washing_machine': [200, 2],
}


max_cost = 700
# max_cost = 600
dictionary_length = len(APPLIANCE_POWER_USAGE)

"""                             
            BRUTE FORCE                                                
"""


def create_lists(appliances):
    list = [(k, v[0], v[1]) for k, v in appliances.items()]
    return list


def powerset(items):
    res = [[]]
    for item in items:
        newset = [r+[item] for r in res]
        res.extend(newset)
    return res


def knapsack_brute_force(max_weight, items):
    knapsack = []
    best_weight = 0
    best_value = 0
    for item_set in powerset(create_lists(items)):
        set_weight = sum(map(weight, item_set))
        set_value = sum(map(value, item_set))
        if set_value > best_value and set_weight <= max_weight:
            best_weight = set_weight
            best_value = set_value
            knapsack = item_set


    return best_weight, best_value, sorted(knapsack)


def weight(item):
    return item[1]


def value(item):
    return item[2]

# print("BRUTE FORCE")
# print( knapsack_brute_force(APPLIANCE_POWER_USAGE, max_cost))


"""                             
            GREEDY ALGORITHM                                                 
"""


# Finding density: priority/cost
def find_density(appliances):
    density_appliance = {}
    for key, value in appliances.items():
        list1 = []
        density = float(value[1] / value[0])
        list1.append(round(density, 3))
        list1.append(value[0])
        list1.append(value[1])
        density_appliance[key] = list1
    return density_appliance


# Getting the optimized results using greedy algorithm:
def greedy_solution(max_cost, appliances):
    density_appliance = find_density(appliances)
    # sorting the dictionary of appliances and density
    sorted_items = sorted(density_appliance.items(), key=lambda x: x[1], reverse=True)
    # Make an empty list to hold results
    result = []
    # Initialize total value and total cost at 0
    total_value, total_cost = 0, 0
    # Iterate through sorted items
    for item in sorted_items:
        # If we can "afford" the next item, add it to the list
        if (total_cost + item[1][1]) <= max_cost:
            result.append(item)
            total_cost += item[1][1]
            total_value += item[1][2]
    # Return the result and total value of it
    return total_cost, total_value, sorted(result)


# print("GREEDY ALGORITHM")
# print(greedy_solution(max_cost, APPLIANCE_POWER_USAGE))


"""                             
            DYNAMIC PROGRAMING                                                
"""


# creating the table and
def dynamic_programming_solution(max_value, appliances):
    cost = get_cost_and_priority(appliances)[0]
    priority = get_cost_and_priority(appliances)[1]
    number_items = len(cost)
    # build the table
    table = [[0 for x in range(max_value + 1)] for x in range(number_items + 1)]
    # Assign the result in table
    for row in range(number_items + 1):
        for column in range(max_value + 1):
            if row == 0 or column == 0:
                table[row][column] = 0
            elif cost[row-1] <= column:
                table[row][column] = max(priority[row-1] + table[row-1][column-cost[row-1]], table[row-1][column])

            else:
                table[row][column] = table[row-1][column]

    return table   # k[number_items][max_value],


def get_selected_items_list(max_value, appliances):
    table = dynamic_programming_solution(max_value, appliances)
    cost = get_cost_and_priority(appliances)[0]
    priority = get_cost_and_priority(appliances)[1]
    number_items = len(cost)
    result1 = table[number_items][max_value]
    result = table[number_items][max_value]
    total_cost = 0
    items_list = []
    # backtracking and finding items, and it's costs and priority
    for i in range(number_items, 0, -1):
        if result <= 0:
            break
        if result == table[i - 1][max_value]:
            continue
        else:
            items_list.append((cost[i - 1], priority[i - 1]))
            total_cost += cost[i - 1]
            result -= priority[i - 1]
            max_value -= cost[i - 1]

    selected_stuff = []
    for search in items_list:
        list1 = []
        for key, value in appliances.items():
            if tuple(value) == search:
                list1.append(key)
                list1.append(value)
                tuple1 = tuple(list1)
                selected_stuff.append(tuple1)

    result = table[number_items][max_value]
    return  total_cost, result1, sorted(selected_stuff)


#   getting values, and cost from dictionary
def get_cost_and_priority(appliances):
    cost = []
    priority = []

    for item in appliances:
        cost.append(appliances[item][0])
        priority.append(appliances[item][1])

    return cost, priority
#
# print("DYNAMIC PROGRAMMING")
# print(get_selected_items_list(max_cost, APPLIANCE_POWER_USAGE))


"""                             
            MEASURE TIME                                              
"""


print("BRUTE FORCE")
start1:float = time.time()
knapsack_brute_force(max_cost, APPLIANCE_POWER_USAGE)
end1:float = time.time()
print("TIME FOR THE BRUTE FORCE")
print(f"time:{end1 - start1}s")


print("GREEDY ALGORITHM")
start2:float = time.time()
greedy_solution(max_cost, APPLIANCE_POWER_USAGE)
end2:float = time.time()
print("TIME FOR THE GREEDY ALGORITHM")
print(f"time:{end2 - start2}s")


print("DYNAMIC PROGRAMMING")
start3:float = time.time()
get_selected_items_list(max_cost, APPLIANCE_POWER_USAGE)
end3:float = time.time()
print("TIME FOR THE DYNAMIC PROGRAMMING")
print(f"time:{end3 - start3}s")





# making dictionary

print("RESUTLS---------------------------")
print("BRUTE FORCE")
print(knapsack_brute_force(max_cost,APPLIANCE_POWER_USAGE))
print("GREEDY ALGORITHM")
print(greedy_solution(max_cost, APPLIANCE_POWER_USAGE))
print("DYNAMIC PROGRAMMING")
print(get_selected_items_list(max_cost, APPLIANCE_POWER_USAGE))

brute = knapsack_brute_force(max_cost,APPLIANCE_POWER_USAGE)[2]
greedy = greedy_solution(max_cost, APPLIANCE_POWER_USAGE)[2]
dynamic = get_selected_items_list(max_cost, APPLIANCE_POWER_USAGE)[2]

list2 = []
for y in brute:
    dictionary_1 = {}
    dictionary_1['algorithm'] = 'brute'
    dictionary_1['item'] = y[0]
    dictionary_1['cost'] = y[1]
    dictionary_1['priority'] = y[2]
    list2.append(dictionary_1)

# print(list2)


for y in greedy:
    dictionary_1 = {}
    dictionary_1['algorithm'] = 'greedy'
    dictionary_1['item'] = y[0]
    dictionary_1['cost'] = y[1][1]
    dictionary_1['priority'] = y[1][2]
    list2.append(dictionary_1)


for y in dynamic:
    dictionary_1 = {}
    dictionary_1['algorithm'] = 'dynamic'
    dictionary_1['item'] = y[0]
    dictionary_1['cost'] = y[1][0]
    dictionary_1['priority'] = y[1][1]
    list2.append(dictionary_1)


"""                             
            VISUALIZATION                                            
"""

max_list = max(len(brute), len(greedy), len(dynamic))
df = pd.DataFrame(list2)
colors = [plt.cm.Spectral(i/float(max_list+1.5)) for i in range(max_list+1)]
ax = df.groupby(['algorithm', 'item']).sum().unstack().plot(kind='barh', y='cost', stacked=True, color=colors,
                                                            figsize=(16, 9))

ax.set_alpha(0.8)
ax.set_title("Three solution for 0/1 Knapsack", fontsize=20)
ax.set_xlabel("Cost of items", fontsize=18)
ax.set_ylabel("", fontsize=18)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x+width/2, y+height/2, '{:.0f}'.format(width), horizontalalignment='center', verticalalignment='center',
            color='black', fontsize=13)


plt.show()

df.groupby(['item']).sum().plot(kind='pie', subplots=True, shadow=True, colors=colors,
                                startangle=90, figsize=(15, 10), autopct='%1.1f%%')
# plt.show()