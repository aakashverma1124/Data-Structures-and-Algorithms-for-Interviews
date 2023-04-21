def findTrips(cabsTime, midTime):
    totalTrips = 0
    for cab in cabsTime:
        totalTrips += (midTime//cab)
    return totalTrips

def binarySearch(cabsTime, low, high, trips):
    while low != high:
        midTime = (low + high)//2
        totalTrips = findTrips(cabsTime, midTime)
        if totalTrips > trips:
            high = midTime
        else:
            low = midTime + 1
    return low

def findMinTime(cabsTime, trips):
    low = 1
    high = min(cabsTime) * trips
    return binarySearch(cabsTime, low, high, trips)

if __name__ == "__main__":
    cabsTime = [5, 1, 3, 7]
    trips = 10
    print(findMinTime(cabsTime, trips))