"""
Author: Rasul Dadashbayli
Assignment: #1
"""

# Step b: Create 4 variables

gym_member = "Alex Alliton"            # str
preferred_weight_kg = 20.5             # float
highest_reps = 25                      # int
membership_active = True               # bool


# Step c: Create a dictionary named workout_stats
# workout_stats is a dictionary (dict)

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (40, 35, 30),
    "Taylor": (25, 50, 10),
    "Morgan": (35, 30, 60),
}


# Step d: Calculate total workout minutes using a loop

for friend, minutes in list(workout_stats.items()):
    workout_stats[f"{friend}_Total"] = sum(minutes)


# Step e: Create a 2D nested list called workout_list
# workout_list is a 2D list (list of lists)

friends = ["Alex", "Jamie", "Taylor", "Morgan"]
workout_list = [list(workout_stats[friend]) for friend in friends]


# Step f: Slice the workout_list

yoga_running_all = [row[0:2] for row in workout_list]
print("Yoga & Running minutes:", yoga_running_all)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting (last two friends):", weightlifting_last_two)


# Step g: Check if total >= 120

for friend in friends:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")


# Step h: User input

name = input("Enter a friend's name: ").strip()

if name in workout_stats and isinstance(workout_stats[name], tuple):
    yoga, running, weightlifting = workout_stats[name]
    total = workout_stats[f"{name}_Total"]

    print("Yoga:", yoga)
    print("Running:", running)
    print("Weightlifting:", weightlifting)
    print("Total:", total)
else:
    print(f"Friend {name} not found in the records.")


# Step i: Highest and lowest total

totals = {friend: workout_stats[f"{friend}_Total"] for friend in friends}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Highest total:", highest_friend, totals[highest_friend])
print("Lowest total:", lowest_friend, totals[lowest_friend])
