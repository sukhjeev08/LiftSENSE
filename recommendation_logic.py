def get_workout_focus(fat_pct, experience):
    if fat_pct >= 25:
        return "Cardio-focused"
    elif fat_pct <= 18 and experience >= 2:
        return "Strength-focused"
    else:
        return "Balanced"


def get_calorie_goal(fat_pct, days, experience):
    if fat_pct >= 25:
        return "Deficit"
    elif fat_pct <= 18 and days >= 4 and experience >= 2:
        return "Bulk"
    else:
        return "Maintenance"