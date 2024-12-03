# 332p, 치킨 배달
# www.acmicpc.net/problem/15686

from itertools import combinations

def findChickenDistance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

def getLocations(city):
    chicken_locations = []
    house_locations = []
    for i in range(len(city)):
        for j in range(len(city[i])):
            if city[i][j] == 0: continue
            elif city[i][j] == 2:
                chicken_locations.append((i, j))
            elif city[i][j] == 1:
                house_locations.append((i, j))

    return chicken_locations, house_locations

def getCityChickenDistance(house_locations, chicken_locations):
    city_chicken_distance = 0
    for house in house_locations:
        house_chicken_distance = 0
        for chicken in chicken_locations:
            if house_chicken_distance == 0:
                house_chicken_distance = findChickenDistance(house, chicken)
            else:
                house_chicken_distance = min(house_chicken_distance, findChickenDistance(house, chicken))
        city_chicken_distance += house_chicken_distance
    return city_chicken_distance

def solution(city, m):
    city_chicken_distance = 0
    chicken_locations, house_locations = getLocations(city)

    chicken_combinations = list(combinations(chicken_locations, m))

    for i in range(len(chicken_combinations)):
        chicken_combi = chicken_combinations[i]
        if city_chicken_distance == 0:
            city_chicken_distance = getCityChickenDistance(house_locations, chicken_combi)
        else:
            city_chicken_distance = min(city_chicken_distance, getCityChickenDistance(house_locations, chicken_combi))

    return city_chicken_distance

if __name__ == "__main__":
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    print(solution(city, m))