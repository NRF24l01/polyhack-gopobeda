from datetime import datetime, timedelta
import pytz


def convert_to_utc_plus_11(input_time: str, input_format: str = "%Y-%m-%d %H:%M"):
    """
    Converts the given time to UTC+11.

    :param input_time: Time to be converted (string format).
    :param input_format: The format of the input time string (default is "%Y-%m-%d %H:%M:%S").
    :return: Time converted to UTC+11 in the same format.
    """

    # Parse the input time string to a datetime object
    local_time = datetime.strptime(input_time, input_format)

    # Set the local time timezone to UTC (assuming input time is in UTC)
    utc_time = local_time.replace(tzinfo=pytz.utc)

    # Add 11 hours to convert to UTC+11
    utc_plus_11_time = utc_time + timedelta(hours=11)

    # Return the result in the desired format
    return utc_plus_11_time.strftime(input_format)


# Example usage
input_time = "2025-04-15 23:00"
converted_time = convert_to_utc_plus_11(input_time)
print("Converted time:", converted_time)
