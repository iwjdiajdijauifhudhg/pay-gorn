def cntAccel(vel0, vel1, time):
    global acc
    acc = abs(vel1 - vel0)/time
    return acc

def decorator(func):
    def cntDist():
        print(func)
        print(vel0*time + acc*time*time/2)
    return cntDist()

try:
    vel0 = int(input())
    vel1 = int(input())
    time = int(input())
    cntAccel = decorator(cntAccel(vel0, vel1, time))
except(ZeroDivisionError):
    print('Ты еще не дорос до деления на ноль, сынок')
except(ValueError):
    print('А теперь запусти заново и введи числа.')
