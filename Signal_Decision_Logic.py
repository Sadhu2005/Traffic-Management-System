def calculate_signal_times(vehicle_counts, total_cycle_time=120, min_green_time=20):
    num_directions = len(vehicle_counts)
    remaining_time = total_cycle_time - (num_directions * min_green_time)

    if remaining_time < 0:
        raise ValueError("Total cycle time is too short to allocate minimum green time.")

    # Calculate proportional additional time
    total_vehicles = sum(vehicle_counts)
    additional_times = [
        (count / total_vehicles) * remaining_time if total_vehicles > 0 else 0
        for count in vehicle_counts
    ]

    # Combine minimum green time with proportional additional time
    green_times = [min_green_time + extra_time for extra_time in additional_times]

    return green_times


# Example vehicle counts from 4 directions
vehicle_counts = [20, 15, 30, 25]

# Calculate green signal times
green_times = calculate_signal_times(vehicle_counts)
print("Green Signal Times (in seconds):", green_times)
