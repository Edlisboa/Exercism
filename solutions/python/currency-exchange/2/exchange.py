def exchange_money(budget, exchange_rate):
    convertation = float(budget) / float(exchange_rate)
    return convertation
    
    pass


def get_change(budget, exchanging_value):
    return float(budget - exchanging_value)
    
    pass


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    
    pass


def get_number_of_bills(amount, denomination):
    return int(amount / denomination)
    
    pass


def get_leftover_of_bills(amount, denomination):
    return amount % denomination
    
    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    budget = budget
    exchange_rate = exchange_rate
    spread = spread
    real_rate = exchange_rate + (exchange_rate * spread / 100)
    total_value = int(budget / real_rate)
    return (total_value // denomination) * denomination
    
    pass
