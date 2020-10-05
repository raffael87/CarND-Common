# Localization algorithm
# Udacity Nanodegree
# step 1: Sense = product + normalization (measurement)
#   penalty if the measurement is not equal what we saw
# step 2: Move = convolution


world = ['green', 'red', 'red', 'green', 'green']

probabilities = [0.0, 1, 0.0, 0.0, 0.0]
measurements = ['red', 'green']
motions = [1,1]

p_hit = 0.6
p_miss = 0.2

p_exact = 0.8
p_undershoot = 0.1
p_overshoot = 0.1

#measurement
def Sense(p, m):
    q = []
    for index in range(len(world)):
        is_hit =  (world[index] == m)
        p_value =  (is_hit * p_hit + (1 - is_hit) * p_miss)
        q.append(p[index] * p_value)

# normalize with sum of q
    s = sum(q)
    q = [x / s for x in q]

    return q

# motion
def Move(p, shift):
    q = []
    for i in range(len(p)):
        s = p_exact * p[(i - shift) % len(p)]
        s += p_undershoot * p[(i - shift-1) % len(p)]
        s += p_overshoot * p[(i - shift + 1) % len(p)]
        q.append(s)

    return q

for measurement, motion in zip(measurements, motions):
    probabilities = Sense(probabilities, measurement)
    probabilities = Move(probabilities, motion)

print probabilities
