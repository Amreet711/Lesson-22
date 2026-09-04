habit_info=("Writing",False,7,3)
print(habit_info)
weekly_habits=(1,0,1,1,0,1,1,1,0,1)
print(weekly_habits)
print("TOTAL DAYS TRACKED: ",len(weekly_habits))
print("DAY 1: ",weekly_habits[0])
print("DAY 4: ",weekly_habits[3])
print("DAY 1-4: ",weekly_habits[0:3])
print("DAY 6-8: ",weekly_habits[6:8])
tuple1=(12,13,14)
print(tuple1)
tuple1=tuple1+(15,)
print(weekly_habits.count(1))
print(weekly_habits.count(0))
done=0
not_done=0
for i in weekly_habits:
    if weekly_habits[i]==0:
        done+=1
    else:
        not_done+=1
if not_done>done:
    print("Very COnsistant!")
else:
    print("Very Inconsistant!")
print()
print("WEEKLY HABIT TRACKER")
print("HABIT NAME:", habit_info[0])
print("WEEKLY RECORD:",weekly_habits)
print("DAYS COMPLETED:",done)
print("DAYS NOT COMPLETED:", not_done)