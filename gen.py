from random import choice as random
from random import shuffle as shuffle
import numpy as np

day_start = int(input("What is the start day (of the month)? "))
month = int(input("What is the month? "))

activities = [
"running up/down stairs",
"running up/down stairs",
"running in place",
"jogging in place",
"jumping jacks",
"walking back and forth in hall",
"running back and forth in hall",
"lifting weights 10 pounds",
"lifting weights 15 pounds"]


nums = np.random.multinomial(90, np.ones(6)/8, size=1)[0]
nums = list(nums)
nums.append(0)
shuffle(nums)

counter = 0

def get_activity(count):
	if nums[count] == 0:
		return "rest day"
	else:
		return random(activities)

print("\n\n")
for day in range(day_start,day_start+7):
	print(f"{month}/{day} - {nums[counter]} minutes - {get_activity(counter)}")
	counter += 1

while True:
	pass


