
"""
            MULTIDIMENSIONAL KNAPSACK    ->  TWO CONSTRAINS KNAPSACK
"""

def chek_negative(num):
    if num <= 0:
        return 0


def three_dimension_knapsack(n, cost_limit, radiation_limit, priorities, costs, radiation):

    table = [[[0] * (cost_limit + 1) for _ in range(radiation_limit + 1)] for _ in range(n + 1)]

    for item in range(1, n + 1):  # number of items
        for rad in range(1, radiation_limit + 1):  # for limited expected radiation
            for cost in range(1, cost_limit + 1):  # for limited expected cost
                if costs[item - 1] <= cost and radiation[item-1] <= rad:   # chek if pair (cost, radiation)
                    # is smaller than the iterators  (rad, cost)


                    if (rad - radiation[item-1]) >= 0 and (cost - costs[item-1]) >= 0:
                        table[item][rad][cost] = max(table[item-1][rad][cost],
                                                      table[item][rad-1][cost],
                                                      table[item][rad][cost-1],
                                                      table[item-1][rad - radiation[item-1]][cost - costs[item-1]] +
                                                      priorities[item - 1])

                    else:
                        table[item][rad][cost] = max(table[item - 1][rad][cost],
                                                     table[item][rad - 1][cost],
                                                     table[item][rad][cost - 1])

                else:

                    table[item][rad][cost] = max(table[item][rad-1][cost], table[item][rad][cost-1],  table[item-1][rad][cost])

    for x in table:
        print("x-----------------------------------")
        for t in x:
            print(t)

    return table[-1][-1][-1], table





def get_selected_items_list2(number_of_itmes, cost_limit, radiation_limit, priorities, items_name, table):
    table1= table[1]
    result = table[0]
    add_items=[]
    add_items_name=[]
    r_limit = radiation_limit
    c_limit = cost_limit

    # iteration through ITEM
    for item in range(number_of_itmes, 0, -1):
        if result == table1[item][r_limit][c_limit] and table1[item][r_limit][c_limit] != table1[item-1][r_limit][c_limit]:
            add_items.append(item)
            add_items_name.append(items_name[item-1])
            r_limit = r_limit-1
            c_limit = c_limit-1
            result= result - priorities[item-1]
            continue

        else:
            next_iterator = 0

            # iteration through ROW
            for rad in range(r_limit, 0, -1):
                if next_iterator == 1:
                    break

                else:

                    # iteration through COLUMN
                    for cost in range(cost_limit, 0, -1):
                        if table1[item][rad][cost] == table1[item][rad][cost-1]:
                            continue

                        else:
                            if result == table1[item][rad][cost] and table1[item][rad][cost] == table1[item][rad-1][cost]:
                                # r_limit = r_limit - 1
                                # c_limit = c_limit - cost + 1
                                break

                            elif result == table1[item][rad][cost] and table1[item][rad][cost] == table1[item-1][rad][cost]:
                                # r_limit = r_limit - rad + 1
                                # c_limit = c_limit - cost + 1
                                next_iterator = 1
                                break

                            elif result == table1[item][rad][cost]:
                                add_items.append(item)
                                add_items_name.append(items_name[item-1])
                                # r_limit = r_limit - rad + 1
                                # c_limit = c_limit - cost + 1
                                next_iterator = 1
                                result = result - priorities[item - 1]
                                break

    return add_items, add_items_name


def check_chosen_itmes_sum(items, prioriteis, result):
    print("items", items)
    print("prioristes", prioriteis)
    add_items=0
    for x in items:
        add_items=add_items + prioriteis[x-1]

    if add_items == result:
        return "True! Result is : " + str(result) + "  Sum of items is : " + str(add_items)

    else:
        return "Result doesn't mach the item's sum.  Result is: " + str(result) + " Sum of items is : " + str(add_items)


def check_chosen_itmes_cost(items, costs, limit):
    print("items", items)
    print("prioristes", costs)
    add_items = 0
    for x in items:
        add_items = add_items + costs[x-1]

    if add_items <= limit:
        return "True! Cost limit is : " + str(limit) + ", calculated limit is : " + str(add_items)

    else:
        return "Result doesn't mach the limit.  Result is: " + str(limit) + ", calculated limit is : " + str(add_items)


def check_chosen_itmes_radiation(items, radiation, limit):
    print("items", items)
    print("prioristes", radiation)
    add_items = 0
    for x in items:
        add_items = add_items + radiation[x-1]

    if add_items <= limit:
        return "True! Radiation limit is : " + str(limit) + ",  calculated limit is : " + str(add_items)

    else:
        return "Result doesn't mach the limit.  Result is: " + str(limit) + ",  calculated limit is : " + str(add_items)


"""                             
            DEMO                                            
"""

cost_limit = 29   # max for cost limit
radiation_limit = 59
items_name = ["radi0", "tv", "phone", "lamp", "teapot1", "teapot2", "teapot3", "teapot4", "teapot5"]
priorities = [10, 90, 40, 50, 80, 44, 55, 78, 51]  # priority values
costs = [1, 2, 3, 4, 5, 6, 8, 10, 12]   # cost values 5+10 =15
radiation = [1, 2, 3, 3, 10, 11, 32, 34, 37]   # radiation values 34+10=44

# cost_limit = 7   # max for cost limit
# radiation_limit = 10
# items_name = ["radi0", "tv", "phone", "new"]
# priorities = [20, 90, 160, 100]  # priority values
# costs = [1, 2, 3, 4]   # cost values
# radiation = [1, 2, 3, 7]  # radiation values
n = len(priorities)
table1 = three_dimension_knapsack(n, cost_limit, radiation_limit, priorities, costs, radiation)

print(three_dimension_knapsack(n, cost_limit, radiation_limit, priorities, costs, radiation))



# lista= get_selected_items_list(n, cost_limit, radiation_limit, priorities, costs, items_name, table1)

items = get_selected_items_list2(n, cost_limit, radiation_limit, priorities, items_name, table1)[0]
result = three_dimension_knapsack(n, cost_limit, radiation_limit, priorities, costs, radiation)[0]

print(check_chosen_itmes_sum(items, priorities, result))
print(check_chosen_itmes_cost(items, costs, cost_limit))
print(check_chosen_itmes_radiation(items, radiation, radiation_limit))

print(get_selected_items_list2(n, cost_limit, radiation_limit, priorities,  items_name, table1))