
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
# creating the table and


def dynamic_programming_solution(cost_limit, cost, priority):
    number_items = len(cost)
    # build the table
    table = [[0 for x in range(cost_limit + 1)] for x in range(number_items + 1)]
    # Assign the result in table
    for row in range(number_items + 1):
        for column in range(cost_limit + 1):
            if row == 0 or column == 0:
                table[row][column] = 0
            elif cost[row-1] <= column:
                table[row][column] = max(priority[row-1] + table[row-1][column-cost[row-1]], table[row-1][column])

            else:
                table[row][column] = table[row-1][column]

    return table   # k[number_items][cost_limit],


# table = dynamic_programming_solution(cost_limit, appliances)

def get_selected_items_list(cost_limit, table, cost, priority, appliances_dictionary):

    number_items = len(cost)
    result1 = table[number_items][cost_limit]
    result = table[number_items][cost_limit]
    total_cost = 0
    items_list = []
    # backtracking and finding items, and it's costs and priority
    for i in range(number_items, 0, -1):
        if result <= 0:
            break
        if result == table[i - 1][cost_limit]:
            continue
        else:
            items_list.append((cost[i - 1], priority[i - 1]))
            total_cost += cost[i - 1]
            result -= priority[i - 1]
            cost_limit -= cost[i - 1]

    selected_stuff = []
    for search in items_list:
        list1 = []
        for key, value in appliances_dictionary.items():
            if tuple(value[0:2]) == search:
                list1.append(key)
                list1.append(value)
                tuple1 = tuple(list1)
                selected_stuff.append(tuple1)

    result = table[number_items][cost_limit]
    return total_cost, result1, sorted(selected_stuff)


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