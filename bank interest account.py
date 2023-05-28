def calc_bank_interest(initial_money, number_of_years, rate):

    current_money = initial_money

    for _ in range(number_of_years):
        current_money *= (1 + rate)

    return current_money

print(calc_bank_interest(1000, 1, 0.20))
