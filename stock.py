from stock_helpers import get_investment_data, compute_growth, final_report


def main():
    initial_value, time_interval, growth_rate = get_investment_data()
    result = compute_growth(initial_value, time_interval, growth_rate)
    final_report(initial_value, result, time_interval)


if __name__ == '__main__':
    main()

