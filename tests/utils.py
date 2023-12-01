def get_duration_string(duration: int):
    """Converts duration in seconds to string format

    Args:
        duration (int): duration in seconds

    Returns:
        str: duration in string format
    """
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
