import datetime


def main():
    print("Welcome to DVR Event Time calculator")
    current_real_time = input("Current real time in this format: 'YYYY-MM-DD HH:MM:SS':")
    current_dvr_system_time = input("Current DVR system time in this format: 'YYYY-MM-DD HH:MM:SS': ")
    event_time_in_real_time = input("Event time in real time in this format: 'YYYY-MM-DD HH:MM:SS':  ")

    event_time_in_dvr = calculate_event_time_in_dvr(current_real_time, current_dvr_system_time, event_time_in_real_time)

    if event_time_in_dvr.startswith("Error"):
        print(event_time_in_dvr)
    else:
        print(f"The event time in the DVR is: {event_time_in_dvr}")


def calculate_event_time_in_dvr(current_real_time, current_dvr_system_time, event_time_in_real_time):
    try:
        # Parse the current real-time string in the format 'YYYY-MM-DD HH:MM:SS'
        current_real_time = datetime.datetime.strptime(current_real_time, '%Y-%m-%d %H:%M:%S')

        # Parse the current DVR system time string in the format 'YYYY-MM-DD HH:MM:SS'
        current_dvr_system_time = datetime.datetime.strptime(current_dvr_system_time, '%Y-%m-%d %H:%M:%S')

        # Parse the event time in real-time string in the format 'YYYY-MM-DD HH:MM:SS'
        event_time_in_real_time = datetime.datetime.strptime(event_time_in_real_time, '%Y-%m-%d %H:%M:%S')

        # Calculate the time difference between the current real-time and current DVR system time
        time_difference = current_real_time - current_dvr_system_time

        # Calculate the event time in the DVR by adding the time difference to the event time in real-time
        event_time_in_dvr = event_time_in_real_time - time_difference

        return event_time_in_dvr.strftime('%Y-%m-%d %H:%M:%S')

    except ValueError as e:
        return f"Error: {e}"



if __name__ == '__main__':
    main()
