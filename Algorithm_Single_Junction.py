def calculate_signal_times(vehicle_counts, max_cycle_time=120, min_green_time=20):
    num_directions = len(vehicle_counts)
    remaining_time = max_cycle_time - (num_directions * min_green_time)

    total_vehicles = sum(vehicle_counts)
    additional_times = [
        (count / total_vehicles) * remaining_time if total_vehicles > 0 else 0
        for count in vehicle_counts
    ]

    green_times = [min_green_time + extra_time for extra_time in additional_times]
    return green_times
