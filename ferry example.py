# leer el número de casos de prueba
c = int(input())

# bucle a través de cada caso de prueba
results = []
for i in range(c):
    # leer la entrada para el caso de prueba actual
    n, t, m = map(int, input().split())
    arr_times = [int(input()) for j in range(m)]
    
    # ajustar cross_time si el primer auto llega antes del ferry
    if arr_times[0] < cross_time:
        cross_time = arr_times[0]
    
    # calcular el tiempo más temprano en que se pueden transportar todos los autos al otro lado del río
    cross_time = 0
    trips = 0
    while len(arr_times) > 0:
       
