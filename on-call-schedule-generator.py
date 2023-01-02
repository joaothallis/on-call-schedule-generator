import random


def generate_on_call_schedule(names, num_sprints, start_sprint):
    random.shuffle(names)
    schedule = []
    for i in range(num_sprints):
        schedule.append((names[(i + start_sprint - 1) % len(names)], i + 1))
    return schedule


names = ["Alice", "Bob", "Charlie"]
num_sprints = 10
start_sprint = 0
schedule = generate_on_call_schedule(names, num_sprints, start_sprint)
print(schedule)
