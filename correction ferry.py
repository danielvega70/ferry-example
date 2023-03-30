# read the number of test cases
c = int(input())

# loop through each test case
for i in range(c):
    # read the input for the current test case
    n, t, m = map(int, input().split())
    arr_times = [int(input()) for j in range(m)]
    
    # calculate the earliest time that all the cars can be transported across the river
    cross_time = 0
    trips = 0
    while len(arr_times) > 0:
        next_arrival = arr_times[0]
        if next_arrival >= cross_time:
            # if the next car arrives after the ferry crosses the river, 
            # wait for the next available time to cross
            cross_time = next_arrival + t
            trips += 1
        else:
            # if the next car arrives before the ferry crosses the river, 
            # load as many cars as possible and cross the river
            loaded_cars = 0
            while len(arr_times) > 0 and arr_times[0] <= cross_time and loaded_cars < n:
                loaded_cars += 1
                arr_times.pop(0)
            cross_time += t
            trips += 1
    
    # print the output for the current test case
    print(cross_time - t, trips)
