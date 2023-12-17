def water_jug_problem(jug1_capacity, jug2_capacity, target_capacity):
    jug1_current = 0  # current water level in jug 1
    jug2_current = 0  # current water level in jug 2

    while jug1_current != target_capacity and jug2_current != target_capacity:
        print(f"Jug 1: {jug1_current}L\tJug 2: {jug2_current}L")

        # Fill jug 1 to its maximum capacity
        jug1_current = jug1_capacity

        print(f"Jug 1 filled:\tJug 1: {jug1_current}L\tJug 2: {jug2_current}L")

        # Transfer water from jug 1 to jug 2
        transfer_amount = min(jug1_current, jug2_capacity - jug2_current)
        jug1_current -= transfer_amount
        jug2_current += transfer_amount

        print(f"Transfer Jug 1 to Jug 2:\tJug 1: {jug1_current}L\tJug 2: {jug2_current}L")

        if jug1_current == target_capacity or jug2_current == target_capacity:
            break

        # If jug 2 is full, empty it
        if jug2_current == jug2_capacity:
            jug2_current = 0

            print(f"Jug 2 emptied:\tJug 1: {jug1_current}L\tJug 2: {jug2_current}L")

    print(f"Target capacity of {target_capacity}L achieved!")
    print(f"Jug 1: {jug1_current}L\tJug 2: {jug2_current}L")


# Example usage:
water_jug_problem(8, 5, 1)
