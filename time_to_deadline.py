import datetime

# ask the user for thier goal and a deadline, then store it in a variable
user_input = input(
    "Please enter your goals with a deadline,seperated by a colon \n")
input_list = user_input.split(":")

# set them to variable
goal = input_list[0]
deadline = input_list[1]

# format the datetime
deadline_formarted = datetime.datetime.strptime(deadline, "%d.%m.%Y")
todays_date = datetime.datetime.today()

# calculate how many days left
# deadline date - todays date
remaining_days = todays_date - deadline_formarted

# inform the user
print(f"you have {remaining_days.days} days to complete your goal of {goal}")
