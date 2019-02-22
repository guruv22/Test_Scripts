def get_total_fine(actual_return, exp_return):
    actual_return_list = actual_return.split(" ")
    act_date, act_month, act_year = int(actual_return_list[0]), int(actual_return_list[1]), int(actual_return_list[2])

    exp_return_list = exp_return.split(" ")
    exp_date, exp_month, exp_year = int(exp_return_list[0]), int(exp_return_list[1]), int(exp_return_list[2])

    total_fine = 0
    if (act_year < exp_year):
        return 0
    elif (act_year > exp_year):
        return 10000
    else:
        if (act_month > exp_month):
            total_fine = total_fine + (500 * (act_month - exp_month))
        else:
            if (act_date > exp_date):
                total_fine = total_fine + (15*(act_date - exp_date))
            else:
                return 0
    return (total_fine)

actual_return = input()
exp_return = input()

print(get_total_fine(actual_return, exp_return))
