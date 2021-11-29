MARKET_WEEK = 5
SEPARATOR_LENGTH = 50


def get_investment_data():
    ''' asks user for initial details '''
    initial = float(input('Initial Investment: $'))
    growth = float(input('growth rate %: ')) / 100  # convert to decimal
    interval = int(input('Days: '))
    print('\n', '=' * SEPARATOR_LENGTH, sep='')
    return initial, interval, growth


def compute_daily_values(value=0, growth=0, day=0):
    ''' compute daily values based on growth rate '''
    todays_growth = value * growth
    result = value + todays_growth
    return result, todays_growth, day + 1


def daily_report(result=0, todays_growth=0, day=0):
    print(
        f'Day {day}\t Current: ${formatter(result)} |',
        f'Previous: ${formatter(result - todays_growth)} |',
        f'Today\'s growth: ${formatter(todays_growth)}'
    )


def weekly_report(initial=0, result=0, weekly_gain=0, day=0):
    ''' Outputs the weekly report of gains since original investment '''
    # print('\n', '=' * SEPARATOR_LENGTH, sep='')
    print(f'\nWEEK {day // MARKET_WEEK}')
    print(f'WEEKLY GAIN: ${formatter(result - initial - weekly_gain)}')
    print(f'TOTAL GAINS: ${formatter(result - initial)}')
    input('\nPRESS ENTER TO CONTINUE . . .')
    print('=' * SEPARATOR_LENGTH, end="\n")


def final_report(initial, result, interval):
    ''' Outputs final investment results '''
    print('\n', '*' * SEPARATOR_LENGTH, sep='')
    print(
        f'FINAL REPORT DAY {interval}\n',
        f'Initial:\t${formatter(initial)}',
        f'Result:\t${formatter(result)}',
        f'Total Gains:\t${formatter(result - initial)}',
        sep='\n'
    )
    print('*' * SEPARATOR_LENGTH)


def compute_growth(initial, interval, growth):
    ''' compute investment growth simulation within given time interval '''
    result = initial
    weekly_gain = 0
    for i in range(0, interval):
        result, todays_growth, day = compute_daily_values(result, growth, i)
        daily_report(result, todays_growth, day)

        if day % MARKET_WEEK == 0:
            weekly_report(initial, result, weekly_gain, day)
            weekly_gain = result - initial
    return result


def formatter(value):
    ''' formats values with commas and rounds to the 4 decimal point '''
    return '{:,.4f}'.format(value)

