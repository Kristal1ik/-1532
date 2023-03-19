import math
from get_data import get_data

class Status:
    no_move = False
    distance = 21
    day = 0
    SH = 8
    location = 0
    fuel = 0
    fuel_use = 0
    energy = 0
    credits = 0
    T = 10
    M = 192
    speed = 2
    W = 0
    V_max = 2
    Oxi = 0
    E = 0
    next_sh = 248
    total_fuel = 0
    total_oxi = 0


def oxiuse():
    if Status.SH < Status.next_sh + 8:
        Status.Oxi = 60
        Status.T = 10
    else:
        Status.T = 0
        Status.Oxi = 40


def setW():
    Status.energy = math.ceil(Status.E / 11)
    Status.fuel_use = math.ceil(Status.W + Status.energy)
    Status.W = 80


def autoclaveStatus(n):
    if n == Status.T:
        return Status.T
    else:
        return 0


def day_tick():
    autoclaveStatus(Status.T)
    Status.location += Status.speed
    Status.distance -= Status.speed
    oxiuse()
    Status.E = sum([i for i in range(Status.T + 1)])

    Status.speed = Status.V_max * (Status.W / 80) * (200 / (Status.M + Status.SH))
    if Status.distance - Status.speed < 0:
        temp_w = Status.distance * 80 * (Status.M + Status.SH) / (2 * 200)
        Status.speed = Status.V_max * (Status.W / 80) * (200 / (Status.M + Status.SH))
    setW()
    # if Status.SH + Status.SH * math.sin(
    #         -math.pi / 2 + (math.pi * (Status.T + 0.5 * Status.Oxi)) / 40) > Status.next_sh + 8:
    #     temp_o = 0
    #     temp_t = 0
    #     temp = math.ceil((math.asin((Status.next_sh - Status.SH) / Status.SH) + math.pi / 2) * 40 / math.pi)
    #     if temp > 30:
    #         temp_o = 60
    #         temp_t = temp - 30
    #     else:
    #         temp_o = math.ceil(temp)
    #     Status.Oxi = temp_o
    #     Status.fuel_use = math.ceil(sum([i for i in range(temp_t + 1)]) / 11)
    #     Status.SH = math.ceil(Status.SH + Status.SH * math.sin(-math.pi / 2 + (math.pi * (temp_t + 0.5 * temp_o)) / 40))
    # else:
    Status.SH = Status.SH + Status.SH * math.sin(-math.pi / 2 + (math.pi * (Status.T + 0.5 * Status.Oxi)) / 40)
    Status.total_oxi += Status.Oxi + Status.SH
    Status.total_fuel += Status.fuel_use


if __name__ == "__main__":
    points = get_data()
    for i in points:
        Status.distance = i[1]
        Status.next_sh = i[0]
        while Status.distance > 0:
            day_tick()
            Status.day += 1
        Status.no_move = True
        while Status.SH < Status.next_sh + 8 and Status.distance <= 0.002:
            day_tick()
        Status.no_move = False
        Status.SH = 8

    print(Status.day)
    print(Status.total_fuel)
    print(Status.total_oxi)
    print(f"Всего кредитов: {Status.total_fuel * 10 + Status.total_oxi * 7}")
    pass
