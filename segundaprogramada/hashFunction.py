def customHash(dateObj, quarter, homeTeam):
    """
    Hash function to map (date, quarter, homeTeam) to an integer [0..749].
    Adjust this logic as you wish, but remember to document how it works.
    """

    if dateObj is None:
        year = month = day = 0
    else:
        year = dateObj.year
        month = dateObj.month
        day = dateObj.day

    baseValue = year + month + day + quarter + len(homeTeam or "")
    return baseValue % 750
