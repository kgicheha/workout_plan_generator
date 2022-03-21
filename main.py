from workoutplan import quotes, home_chest_workout, gym_chest_workout, home_abs_workout, gym_abs_workout, home_back_workout, gym_back_workout, home_leg_workout, gym_leg_workout, home_full_workout, gym_full_workout 
import random
import colorama
from colorama import Fore



# USER INPUT

user_workout_choice = int(input("What type of workout would you like today? Type '0' for Chest & Arms, '1' for Abs, '2' for Back, '3' for Legs, '4' for Full Body \n"));

#While loops 

while (user_workout_choice < 0) or (user_workout_choice > 4):
    print("Invalid option, please select from the given options")
    user_workout_choice = int(input("What type of workout would you like today? Type '0' for Chest & Arms, '1' for Abs, '2' for Back, '3' for Legs, '4' for Full Body \n"));
    

user_location = int(input("Is your workout at home or at the gym? Type '0' for at Home or '1' for at the gym \n"))

while (user_location > 1) or (user_location < 0):
    print("Invalid option, please select from the given options")
    user_location = int(input("Is your workout at home or at the gym? Type '0' for at Home or '1' for at the gym \n"))

workout_time = int(input("How many minutes do you plan on working out today? 30, 45, 60 \n"));

while workout_time < 30:
    print("Not adequate time to get the best results. Increase workout to 30 minutes. It'll be worth it!")
    workout_time = int(input("How many minutes do you plan on working out today? 30, 45, 60 \n"));


#MOTIVATIONAL QUOTE

print("QUOTE OF THE DAY: " + Fore.GREEN + random.choice(quotes).capitalize())

#removes the color that was set prior to this line. Resets the color back to default
print ('\033[39m')


#WORKOUT PLAN

#create function that generates workout routine


#at home 
if user_location == 0:
    #at home 
    if user_workout_choice == 0:
        # chest & arm workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(home_chest_workout) + ", " + random.choice(home_chest_workout) + ", & " + random.choice(home_chest_workout))
    elif user_workout_choice == 1:
        # Abs workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(home_abs_workout) + ", " + random.choice(home_abs_workout) + ", & " + random.choice(home_abs_workout))
    elif user_workout_choice == 2:
        # Back workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(home_back_workout) + ", " + random.choice(home_back_workout) + ", & " + random.choice(home_back_workout))
    elif user_workout_choice == 3:
        # Legs workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(home_leg_workout) + ", " + random.choice(home_leg_workout) + ", & " + random.choice(home_leg_workout))
    else:
        # Full body workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(home_full_workout) + ", " + random.choice(home_full_workout) + ", & " + random.choice(home_full_workout))
else:
    #at the gym
    if user_workout_choice == 0:
        # chest & arm workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(gym_chest_workout) + ", " + random.choice(gym_chest_workout) + ", & " + random.choice(gym_chest_workout))
    elif user_workout_choice == 1:
        # Abs workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(gym_abs_workout) + ", " + random.choice(gym_abs_workout) + ", & " + random.choice(gym_abs_workout))
    elif user_workout_choice == 2:
        # Back workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(gym_back_workout) + ", " + random.choice(gym_back_workout) + ", & " + random.choice(gym_back_workout))
    elif user_workout_choice == 3:
        # Legs workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(gym_leg_workout) + ", " + random.choice(gym_leg_workout) + ", & " + random.choice(gym_leg_workout))
    else:
        # Full body workout plan
        print("TODAY'S WORKOUT PLAN: " + Fore.LIGHTBLUE_EX + random.choice(gym_full_workout) + ", " + random.choice(gym_full_workout) + ", & " + random.choice(gym_full_workout))

print ('\033[39m')

#WORKOUT BREAKDOWN

# if workout is at home -- jump rope as warm up
# if workout is at the gym -- treadmill as warm up
# the more workout time, more minutes on warmup, and more sets and reps

if user_location == 0:
    if workout_time < 45:
        print("Warm up: " + Fore.LIGHTYELLOW_EX + "15 minutes jumprope. ")
        print ('\033[39m')
        print("Sets and reps: " + Fore.LIGHTYELLOW_EX + "3 sets, 15 reps each." )
        print ('\033[39m')
        print("Break in between each exercise: " + Fore.LIGHTYELLOW_EX + "1 minute")
        print ('\033[39m')
    elif workout_time >= 45 and workout_time < 60:
        print("Warm up: " + Fore.LIGHTYELLOW_EX + "20 minutes jumprope. ")
        print ('\033[39m')
        print("Sets and reps: " + Fore.LIGHTYELLOW_EX + "4 sets, 15 reps each. ")
        print ('\033[39m')
        print("Break in between each exercise: " + Fore.LIGHTYELLOW_EX + "2 minute")
        print ('\033[39m')
    else :
        print("Warm up: " + Fore.LIGHTYELLOW_EX + "20 minutes jumprope.")
        print ('\033[39m')
        print("Sets and reps: " + Fore.LIGHTYELLOW_EX + " 5 sets, 20 reps each.")
        print ('\033[39m')
        print("Break in between each exercise: " + Fore.LIGHTYELLOW_EX + "2 minute")
        print ('\033[39m')
else:
    if workout_time <= 45:
        print("Warm up: " + Fore.LIGHTYELLOW_EX + "15 minutes treadmill.")
        print ('\033[39m')
        print("Sets and reps: " + Fore.LIGHTYELLOW_EX + "3 sets, 15 reps.")
        print ('\033[39m')
        print("Break in between each exercise: " + Fore.LIGHTYELLOW_EX + "1 minute")
        print ('\033[39m')
    elif workout_time >= 45 and workout_time < 60:
        print("Warm up: " + Fore.LIGHTYELLOW_EX + "20 minutes jumprope.")
        print ('\033[39m')
        print("Sets and reps: " + Fore.LIGHTYELLOW_EX + " 4 sets, 15 reps each.")
        print ('\033[39m')
        print("Break in between each exercise: " + Fore.LIGHTYELLOW_EX + "2 minute")
        print ('\033[39m')
    else:
        print("Warm up: " + Fore.LIGHTYELLOW_EX + "20 minutes treadmill.")
        print ('\033[39m')
        print("Sets and reps: " + Fore.LIGHTYELLOW_EX + "3 sets, 20 reps.")
        print ('\033[39m')
        print("Break in between each exercise: " + Fore.LIGHTYELLOW_EX + "2 minute")


