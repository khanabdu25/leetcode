from moving_average import MovingAverage

m = MovingAverage(3)

print(m.next(1))   # 1.0
print(m.next(10))  # 5.5
print(m.next(3))   # 4.6666666667
print(m.next(5))   # 6.0