def manage_junctions(junction_data, vip_path=None):
    """
    Manages multiple junctions dynamically based on traffic and VIP presence.

    Args:
        junction_data: Dictionary containing junction IDs and their vehicle counts.
        vip_path: List of junction IDs that form the path for a VIP/ambulance.

    Returns:
        signal_timings: Dict with updated signal timings for all junctions.
    """
    signal_timings = {}
    for junction_id, vehicle_counts in junction_data.items():
        if vip_path and junction_id in vip_path:
            # Clear VIP path: Full green for VIP direction, others red
            vip_direction = vip_path[junction_id]
            signal_timings[junction_id] = [120 if i == vip_direction else 0 for i in range(4)]
        else:
            # Normal operation
            signal_timings[junction_id] = calculate_signal_times(vehicle_counts)
    return signal_timings
