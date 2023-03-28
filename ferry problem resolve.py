def ferry_problem(n, t, m, cars):
    trips = 0
    time = 0
    i = 0

    while i < len(cars):
        # Wait for the next available car
        next_car = cars[i]
        if next_car > time:
            time = next_car

        # Load the ferry with as many cars as possible
        loaded_cars = 0
        while i < len(cars) and cars[i] <= time and loaded_cars < n:
            i += 1
            loaded_cars += 1

        # Cross the river and return
        time += t
        trips += 1

    # The last return trip is not counted in the number of trips
    time -= t

    return time, trips


# Read the number of test cases
num_cases = int(input())

# Process each test case
for i in range(num_cases):
    n, t, m = map(int, input().split())
    cars = []
    for j in range(m):
        cars.append(int(input()))

    # Solve the ferry problem for this test case
    time, trips = ferry_problem(n, t, m, cars)

    # Print the solution
    print(time, trips)
