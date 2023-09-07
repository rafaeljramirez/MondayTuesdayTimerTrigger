import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:

        # Get the current UTC time
    utc_timestamp = datetime.date.today()


    # Check if it's Monday and not the last day of the month current this is running for wednesday
    if utc_timestamp.weekday() == 2 and not is_last_day_of_month(utc_timestamp):
        # Execute logic for Monday
        logging.info('Today is Wednesday!')
        pass
    
    # Check if it's Tuesday and the first day of the month this is running for Thursday. Change to fit schedule
    elif utc_timestamp.weekday() == 3 and utc_timestamp.day == 1:
        # Execute logic for Tuesday
        logging.info('Today is Thursday!')
        pass
    
    # Exit the function for all other cases
    return

def is_last_day_of_month(date):
    next_month = date.replace(day=28) + datetime.timedelta(days=4)  # Move to next month
    last_day = next_month - datetime.timedelta(days=next_month.day)
    return date.day == last_day.day

