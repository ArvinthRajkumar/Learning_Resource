def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:                 # cannot start from any station up to i
            start, tank = i + 1, 0
    return start
