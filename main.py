# Constants
MIN_DURATION = 60
YELLOW_DURATION = 5
TIMESTEP = 1
TOTAL_TIME = 200
PEDESTRIAN_ARRIVAL_TIME = 70

# Variables
traffic_light_color = None
count = 0

while count <= TOTAL_TIME:
    print(f"Time: {count} Seconds")

    if count < MIN_DURATION:
        traffic_light_color = "red"
    elif count < MIN_DURATION + MIN_DURATION:
        if count < PEDESTRIAN_ARRIVAL_TIME:
            traffic_light_color = "green"
            print("Output: sigG\n")
        else:
            traffic_light_color = "pending"
            print("Input: pedestrian\n")
    elif count < MIN_DURATION + MIN_DURATION + YELLOW_DURATION:
        traffic_light_color = "yellow"
        print("Output: sigY\n")
    elif count < MIN_DURATION + MIN_DURATION + YELLOW_DURATION + MIN_DURATION:
        traffic_light_color = "red"
        print("Output: sigR\n")
    else:
        traffic_light_color = "green"
        print("Output: sigG\n")

    print(f"System State: {traffic_light_color}\n")
    count += TIMESTEP
