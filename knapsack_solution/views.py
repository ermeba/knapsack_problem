from django.shortcuts import render

# Create your views here.
from .forms import Predict_Form
from client.models import UserProfileInfo
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .knapsack_functions import *


@login_required(login_url='/')
def PredictRisk(request, pk):

    predicted = False
    predictions = {}
    list_of_sums = []

    # predictions = {
    #     'SVC': '1',
    #     'LogisticRegression': '1',
    #     'NaiveBayes': '1',
    #     'DecisionTree': '0',
    # }

    appliances = {
        'Coffee maker': 1200,
        'Clothes washer': 500,
        'Clothes dryer': 5000,
        'Dishwasher': 2400,
        'Hair dryer': 1875,
        'Heater': 1500,
        'Clothes iron': 1800,
        'Water pump': 1100,
        'Laptop': 50,
        'Radio': 400,
        'Refrigerator': 725,
        'Television': 110,
        'Vacuum cleaner': 1440,
        'Microwave oven': 1100,
        'Toaster': 1400,
        'Ceiling Fans': 110
    }



    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)

        if form.is_valid():
            features = [[form.cleaned_data['appliance1'], form.cleaned_data['appliance2'],
                         form.cleaned_data['appliance3'], form.cleaned_data['appliance4'],
                         form.cleaned_data['appliance5'], form.cleaned_data['appliance6'],
                         form.cleaned_data['appliance7'], form.cleaned_data['appliance8'],
                         form.cleaned_data['appliance9'], form.cleaned_data['appliance10'],
                         form.cleaned_data['priority1'], form.cleaned_data['priority2'],
                         form.cleaned_data['priority3'], form.cleaned_data['priority4'],
                         form.cleaned_data['priority5'], form.cleaned_data['priority6'],
                         form.cleaned_data['priority7'], form.cleaned_data['priority8'],
                         form.cleaned_data['priority9'], form.cleaned_data['priority10'],
                         form.cleaned_data['time1'],  form.cleaned_data['time2'],
                         form.cleaned_data['time3'],  form.cleaned_data['time4'],
                         form.cleaned_data['time5'],  form.cleaned_data['time6'],
                         form.cleaned_data['time7'],  form.cleaned_data['time8'],
                         form.cleaned_data['time9'],  form.cleaned_data['time10'],
                         form.cleaned_data['price_of_electricity'], form.cleaned_data['price_of_high_tariffs'],
                         form.cleaned_data['limit_of_time_hours']]]

            # return HttpResponse(features)
            main_list = features[0]                 # list of all elements retrieved from the user
            list_names = main_list[0:10]            # list of names of items chosen from user
            list_priorities = main_list[10:20]      # list of the priorities chosen from user
            list_time = main_list[20:30]            # list of time for each appliance chosen from use
            length = len(main_list)                 # len of list

            price_in_kwh = main_list[30]            # price of electricity dollar per kilowatt per hours
            increase_in_percent = main_list[31]     # percent increase of price for high tariffs
            limit_of_time_in_hours = main_list[32]  # if the client want to limit time of all appliances' operations


            print(list_names)
            print(list_priorities)
            print(list_time)
            print(price_in_kwh)
            print(increase_in_percent)
            print(limit_of_time_in_hours)
            print(length)

            # return HttpResponse(main_list)

            dictionary_of_items = {}
            list_watts = []                        # watts for each appliance
            list_watts_multiply_hours = []         # multiply watts per hour with number of hours of appliance usage
            list_price_for_all_watts_spend = []    # multiply amount of watts used with price (kilo watts per hours)
            list_after_increased_prices = []       # multiply amount of watts with price of high tariffs
            iterator = 0

            for x in list_names:
                if x in appliances.keys():
                    lista = []
                    list_watts.append(appliances[x])                          # list of watts per hour by appliance

                    hours_watts = int(appliances[x]) * int(list_time[iterator])  # multiply watts by time spend
                    list_watts_multiply_hours.append(hours_watts)                # get the results in a list

                    price_of_used_watts = int(hours_watts * int(price_in_kwh) /1000)  # multiply all watts and the price
                    list_price_for_all_watts_spend.append(price_of_used_watts)        # get the results in a list

                    high_tariffs = (int(price_in_kwh) * int(increase_in_percent))/100
                    price_of_used_watts_high_tariffs = int(hours_watts * (int(price_in_kwh) + high_tariffs)/1000)
                    list_after_increased_prices.append(price_of_used_watts_high_tariffs)

                    lista.append(price_of_used_watts_high_tariffs)
                    lista.append(list_priorities[iterator])
                    lista.append(appliances[x])
                    lista.append(list_time[iterator])


                    dictionary_of_items[x] = lista

                    iterator = iterator + 1

            price_limit = sum(list_price_for_all_watts_spend)
            price_limit1 = sum(list_after_increased_prices)

            print(list_watts)
            print(list_watts_multiply_hours)
            print(list_price_for_all_watts_spend)
            print(list_after_increased_prices)
            print("first price", price_limit)
            print("second price", price_limit1)
            print("my dictionary", dictionary_of_items)

            # return HttpResponse(features)

            """                             
                        DYNAMIC PROGRAMING => using Knapsack to give the optimal solution of appliances                                               
            """

            table = dynamic_programming_solution(price_limit, list_after_increased_prices, list_priorities)
            optimal_solution = get_selected_items_list(price_limit, table, list_after_increased_prices,
                                                       list_priorities, dictionary_of_items)

            predictions = dict(optimal_solution[2])

            print('this is the solution isheAllah', optimal_solution)
            print('this is the new dictionary insheAllah', predictions)

            sum1 = 0
            sum2 = 0
            sum3 = 0
            sum4 = 0



            for key, values in predictions.items():
                sum1 = sum1 + values[0]
                sum2 = sum2 + values[1]
                sum3 = sum3 + values[2]
                sum4 = sum4 + values[3]

            list_of_sums.append(sum1)
            list_of_sums.append(sum2)
            list_of_sums.append(sum3)
            list_of_sums.append(sum4)


            pred = form.save(commit=False)

            # l = [predictions['SVC'],
            #      predictions['LogisticRegression'],
            #      predictions['NaiveBayes'],
            #      predictions['DecisionTree']]
            #
            # count = l.count('1')
            #
            # result = False
            #
            # if count >= 2:
            #     result = True
            #     pred.num = 1
            # else:
            #     pred.num = 0

            pred.profile = profile

            pred.save()
            predicted = True

            # colors = {}
            #
            # if predictions['SVC'] == '0':
            #     colors['SVC'] = "table-success"
            # elif predictions['SVC'] == '1':
            #     colors['SVC'] = "table-danger"
            #
            # if predictions['LogisticRegression'] == '0':
            #     colors['LR'] = "table-success"
            # else:
            #     colors['LR'] = "table-danger"
            #
            # if predictions['NaiveBayes'] == '0':
            #     colors['NB'] = "table-success"
            # else:
            #     colors['NB'] = "table-danger"
            #
            # if predictions['DecisionTree'] == '0':
            #     colors['DT'] = "table-success"
            # else:
            #     colors['DT'] = "table-danger"

    if predicted:
        return render(request, 'solution.html',
                      {'form': form, 'predicted': predicted, 'user_id': u_id, 'list_of_sums': list_of_sums,
                          'predictions': predictions})

    else:
        form = Predict_Form()

        return render(request, 'solution.html',
                      {'form': form, 'predicted': predicted, 'user_id': u_id, 'list_of_sums': list_of_sums,
                       'predictions': predictions})
