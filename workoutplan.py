import random
# ARRAY OF WORKOUT PLANS

#chest & arms
home_chest_workout = ["Regular Push Ups", "Incline Push Ups", "Decline Push Ups", "Wide Push Up", "Narrrow Push Ups" "Diamond Push Ups", "Shoulder Taps"]
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

quotes = ["Of course it's hard. It's supposed to be hard. If it were easy, everybody would do it. Hard is what makes it great!" ,
            "Your body can stand almost anything. It’s your mind that you have to convince!", 
            "Hustle for that muscle!", "It comes down to one simple thing: how bad do you want it?", 
            "Making excuses burns zero calories per hour!", 
            "Obstacles can’t stop you. Problems can’t stop you. People can’t stop you. Only you can stop you!",
            "Exercise is like telling your body “you’re gonna hate me for this, but you’ll thank me later!",
            "The pain you feel today, will be the strength you feel tomorrow!"]


#combine workout into nested array

combined_home_workouts =[home_chest_workout], [home_abs_workout], [home_back_workout], [home_full_workout]

combined_gym_workouts = [gym_chest_workout, gym_abs_workout, gym_back_workout, gym_full_workout]


print(combined_gym_workouts[0][0])
print(random.choice(combined_gym_workouts[0]))


