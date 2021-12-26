import time
start_time = time.time()

with open('input.txt','r') as f:
    data = f.read().strip()

def parse(data):
    data = [[int(i) for i in d] for d in [item.split('..') for item in data.replace('target area: ', '').replace('x=','').replace(' y=', '').split(',')]]
    return data[0], data[1]

x_limit, y_limit = parse(data)

# Target area limits
x_limit, y_limit = parse(data)
x_low = x_limit[0]
x_high = x_limit[1]
y_low = y_limit[0]
y_high = y_limit[1]
# Results
current_high = 0
distinct_values = 0

def x_towards_zero(number):
    # Positive number decreases, negative increases, 0 stays the same
    return (number/abs(number))*(abs(number)-1) if number != 0 else 0 

def x_towards_zero2(number):
    if number == 0:
        return number
    elif number > 0:
        return number -1
    else:
        return number+1

def within_area(x,y):
    if x_low <= x <= x_high and y_low <= y <= y_high:
        return True
    return False

def x_low_limit(x_low):
    limit = 0 
    i = 1
    while limit+i < x_low:
        limit += i
        i+=1
    return i

def launch(x_vel,y_vel):
    global current_high
    x_pos = 0
    y_pos = 0
    y_max = 0
    
    while(True):
        x_pos += x_vel
        y_pos += y_vel
        if y_max < y_pos:
            y_max += y_vel
        x_vel = x_towards_zero(x_vel)
        y_vel -= 1
        if within_area(x_pos, y_pos):
            if current_high < y_max:
                current_high = y_max
            return True
        if x_pos > x_high or y_pos < y_low:
            return False

    return False

# Part 1 and 2
def launch_probes():
    global distinct_values
    for x in range(x_low_limit(x_low),x_high+1):
        for y in range(-200,200):
            if launch(x,y):
                distinct_values += 1
                #print(f'Hit {x} {y}')

    print(f'Answer for Part 1 = {current_high}')
    print(f'Answer for Part 2 = {distinct_values}')


launch_probes()
print(f'Time was {time.time()-start_time}')



