possible_connections = [
    #0
    {
        "mothing":[0]
    },
    #1
    {
        "up": [5,6,10,11,14],
        "down" : [2,16,17,18],
        "left" : [1,8,19],
        "right" : [1,7,20]
    },
    #2
    {
        "up": [1,16,19,20],
        "down" : [7,8,10,12,15],
        "left" : [2,6,17],
        "right" : [2,5,18]
    },
    #3
    {
        "up": [3,7,17],
        "down" : [3,5,19],
        "left" : [4,16,18,20],
        "right" : [4,6,8,9,14,15]
    },
    #4
    {
        "up": [4,8,18],
        "down" : [4,6,20],
        "left" : [3,5,7,9,11,12],
        "right" : [3,16,17,19]
    },
    #5
    {
        "up": [3,7,17],
        "down" : [1,10,12,15],
        "left" : [2,6,17],
        "right" : [4,9,14,15]
    },
    #6
    {
        "up": [4,8,18],
        "down" : [1,10,12,15],
        "left" : [3,9,11,12],
        "right" : [2,5,18]
    },
    #7
    {
        "up": [2,10,11,14],
        "down" : [3,5,19],
        "left" : [1,8,19],
        "right" : [4,9,14,15]
    },
    #8
    {
        "up": [2,10,11,14],
        "down" : [4,6,20],
        "left" : [3,9,11,12],
        "right" : [1,7,20]
    },
    #9
    {
        "up": [9,12,13,15],
        "down" : [9,11,13,14],
        "left" : [3,5,7],
        "right" : [4,6,8]
    },
    #10
    {
        "up": [2,5,6],
        "down" : [1,7,8],
        "left" : [10,13,14,15],
        "right" : [10,11,12,13]
    },
    #11
    {
        "up": [9],
        "down" : [1,7,8],
        "left" : [10],
        "right" : [4,6,8]
    },
    #12
    {
        "up": [2,5,6],
        "down" : [9],
        "left" : [10],
        "right" : [4,6,8]
    },
    #13
    {
        "up": [9],
        "down" : [9],
        "left" : [10],
        "right" : [10]
    },
    #14
    {
        "up": [9],
        "down" : [1,7,8],
        "left" : [3,5,7],
        "right" : [10]
    },
    #15
    {
        "up": [2,5,6],
        "down" : [9],
        "left" : [3,5,7],
        "right" : [10]
    },
    #16
    {
        "up": [1,16,19,20],
        "down" : [2,16,17,18],
        "left" : [4,16,18,20],
        "right" : [3,16,17,19]
    },
    #17
    {
        "up": [1,16,19,20],
        "down" : [3,5,19],
        "left" : [4,16,18,20],
        "right" : [2,5,18]
    },
    #18
    {
        "up": [1,16,19,20],
        "down" : [4,6,20],
        "left" : [2,6,17],
        "right" : [3,16,17,19]
    },
    #19
    {
        "up": [3,7,17],
        "down" : [2,16,17,18],
        "left" : [4,16,18,20],
        "right" : [1,7,20]
    },
    #20
    {
        "up": [4,8,18],
        "down" : [2,16,17,18],
        "left" : [1,8,19],
        "right" : [3,16,17,19]
    }
]

weights = [0,3,3,3,3,2,2,2,2,2,2,0.5,0.5,1,0.5,0.5,1,0.5,0.5,0.5,0.5]

for i in range(1,21):
    up = possible_connections[i]["up"]
    down = possible_connections[i]["down"]
    left = possible_connections[i]["left"]
    right = possible_connections[i]["right"]

    up_inverse = []
    down_inverse = []
    left_inverse = []
    right_inverse = []

    for j in range(1,21):
        #if i != j:
        if i in possible_connections[j]["down"]:
            up_inverse += [j]
        if i in possible_connections[j]["up"]:
            down_inverse += [j]
        if i in possible_connections[j]["right"]:
            left_inverse += [j]
        if i in possible_connections[j]["left"]:
            right_inverse += [j]

    if up != up_inverse:
        print(i, "connects to ", up, " upwards and is connected to by", up_inverse)
    if down != down_inverse:
        print(i, "connects to ", down, " downwards and is connected to by", down_inverse)
    if left != left_inverse:
        print(i, "connects to ", left, " to the left and is connected to by", left_inverse)
    if right != right_inverse:
        print(i, "connects to ", right, " to the right and is connected to by", right_inverse)