# bounce.py
#
# Exercise 1.5
# 3/5 = 3 divided by 5 = 0.6
# 100/0.6 = 60 or 3/5 the first height the ball fell

max_bounce_height = 0.6
current_height = 100
bounce_height = 0
bounces = 0

while current_height > 1:
    print(bounces, round(current_height * max_bounce_height, 4))
    current_height = current_height * max_bounce_height
    bounces += 1

print('Number of bounces: ', bounces) 

# simpler way
height = 100
bounce = 1
while bounce <= 10:
    height = height * (3/5)
    print(bounce, round(height, 4))
    bounce += 1