import random


# Arrays of different workouts

#chest & arms
home_chest_workout = ["Regular Push Ups", "Incline Push Ups", "Decline Push Ups", "Wide Push Up", "Narrrow Push Up" "Diamond Push Ups", "Shoulder Taps"]
gym_chest_workout = ["Flat Bench Press", "Inclined Press", "Decline Press", "Dumbell Press", "Chest Dips"]

# abs
home_abs_workout = ["Sit Ups", "Crunches", "Knee to Elbow", "Leg Raises", "Elbow Plank", "Heel Touches", "Mountain Climbers"]
gym_abs_workout = ["Hanging Leg Cirles", "Hanging Bicyles", "Hanging side-to-side Knees", "Mountain Climbers", "Abs Roll with Side Rotation"]

# back
home_back_workout = ["Elbow Planks", "Superman", "Wide Grip Push Ups"]
gym_back_workout = ["Bent over Dumbbell Row", "Reverse Dumbbell Fly", "Deadlift", "Pull Up", "Chest Supported Dumbbell Row", "Lat Pulldown"]

# legs
home_leg_workout = ["Chair Dips", "Leg Raises", "Mountain Climbers", "Knees Pull-Ins", "Squats", "Side Leg Swings", "Forward Leg Swings"]
gym_leg_workout = ["Leg Press", "Walking Lunges with Dumbbells", "Squats with Weight Bar", "Hamstring Curls", "Leg Extensions", "Bulgarian Split Squats"]


# full body

home_full_workout = ["Jumping Jacks", "Mountain Climbers", "Lunges", "Squats", "Shoulder Taps", "Push Ups", "Burpees"]
gym_full_workout = ["Jumping Jacks", "Chest Press with Dumbbell", "Burpees", "Mountain Climbers", "Squat", "Walking Lunges with Dumbbells"]


# motivational quotes

quotes = ["Of course it's hard. It's supposed to be hard. If it were easy, everybody would do it. Hard is what makes it great." ,
            "Your body can stand almost anything. It’s your mind that you have to convince", 
            "Hustle for that muscle.", "It comes down to one simple thing: how bad do you want it?", 
            "Making excuses burns zero calories per hour.", "Obstacles can’t stop you. Problems can’t stop you. People can’t stop you. Only you can stop you."
            "Exercise is like telling your body “you’re gonna hate me for this, but you’ll thank me later."
            "The pain you feel today, will be the strength you feel tomorrow."]

# User Input

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


# if workout is at home -- jump rope as warm up
if user_location == 0:
    print("Your warm up: **mins jumprope")

# if workout is at the gym -- treadmill as warm up
if user_location == 1:
    print("Your warm up: **mins on the treadmill")



# the more workout time, more minutes on warmup, and more sets and reps



#print out results & motivational quotes

#at home chest & arm workout plan
if user_workout_choice == 0 and user_location == 1:
    print(random.choice(home_chest_workout))
    
#gym chest & arm workout plan

#at home Abs workout plan

#gym abs workout plan

#at home 

#gym

#at home

#gym

#at home

#gym

#at home

#gym