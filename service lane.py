#input first
N, T =input().split()
N = int(N)
T = int(T)
# the number
width = map(int, input().split())

for i, road_width in enumerate(width):
    last_car = -1
    last_truck = -1
    if road_width > 1:
        last_car = i
        # it can pass
        if len(last) > 0 and last
