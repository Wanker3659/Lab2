def display_main_menu():
    print("display_main_menu")

def get_user_input():
    return 1.1,2.2,3.3;

def calc_average(list):
    num1 = sum(list) #find the average of the list
    num2 = len(list)
    return [num1/num2]

def min_max(temp_list):
    min_temp = min(temp_list) #find min and max of the list
    max_temp = max(temp_list)
    return [min_temp, max_temp]

def sort_temperature(list):
    return sorted(list);

def calc_median_average(list):
    median_list = sorted(list) #find the median of the list
    average_list = len(median_list)
    if average_list % 2 == 0:
        median = (median_list[average_list//2 - 1] + median_list[average_list//2]) / 2
    else:
        median = median_list[average_list//2]
    return [median]