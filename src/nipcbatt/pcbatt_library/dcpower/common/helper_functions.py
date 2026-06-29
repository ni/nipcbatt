import math


def generate_pulse_current_sequence(
    start_current,
    end_current,
    step_size,
    source_delay,
    max_points=10000
):
    """
    Replicates the LabVIEW sequence generation logic.
    """

    # Protect against zero step
    if step_size == 0:
        raise ValueError("Step size cannot be zero")

    # Allow reverse sweeps
    if end_current < start_current:
        step = -abs(step_size)
    else:
        step = abs(step_size)

    # Calculate number of points
    num_points = int(
        math.floor(abs(end_current - start_current) / abs(step))
    ) + 1

    # Limit for SMU
    num_points = min(num_points, max_points)

    # Generate sequence
    pulse_current_sequence = [
        start_current + i * step
        for i in range(num_points)
    ]

    # Protect against overshoot
    if step > 0:
        pulse_current_sequence = [
            min(v, end_current)
            for v in pulse_current_sequence
        ]
    else:
        pulse_current_sequence = [
            max(v, end_current)
            for v in pulse_current_sequence
        ]

    last_point_current = pulse_current_sequence[-1]

    # Create delay array
    source_delays = [source_delay] * num_points

    return {
        "source_delays": source_delays,
        "number_of_points": num_points,
        "pulse_current_sequence": pulse_current_sequence,
        "last_point_current": last_point_current,
    }


# Example
result = generate_pulse_current_sequence(
    start_current=0.0,
    end_current=1.0,
    step_size=0.2,
    source_delay=0.1
)

print("Number of Points:", result["number_of_points"])
print("Sequence:", result["pulse_current_sequence"])
print("Last Point:", result["last_point_current"])