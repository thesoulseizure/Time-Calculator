def add_time(start_time, duration, start_day=None):
    # Parse start time
    time, period = start_time.split()
    start_hours, start_minutes = map(int, time.split(':'))
    
    # Convert to 24-hour format for easier calculation
    if period == 'PM' and start_hours != 12:
        start_hours += 12
    elif period == 'AM' and start_hours == 12:
        start_hours = 0
    
    # Parse duration
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60
    
    # Calculate total hours
    total_hours = start_hours + duration_hours + extra_hours
    days_later = total_hours // 24
    final_hours = total_hours % 24
    
    # Convert back to 12-hour format
    if final_hours == 0:
        display_hours = 12
        period = 'AM'
    elif final_hours == 12:
        display_hours = 12
        period = 'PM'
    elif final_hours > 12:
        display_hours = final_hours - 12
        period = 'PM'
    else:
        display_hours = final_hours
        period = 'AM'
    
    # Format time string
    time_str = f"{display_hours}:{final_minutes:02d} {period}"
    
    # Handle day of week if provided
    if start_day:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 
                'friday', 'saturday', 'sunday']
        start_day = start_day.lower()
        day_index = days.index(start_day)
        final_day_index = (day_index + days_later) % 7
        time_str += f", {days[final_day_index].capitalize()}"
    
    # Add days later information
    if days_later == 1:
        time_str += " (next day)"
    elif days_later > 1:
        time_str += f" ({days_later} days later)"
    
    return time_str