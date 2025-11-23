def display_average_hours(weekly_hours_table: list):
    gemiddelden= []
    index= 1
    for n in weekly_hours_table:
        gem= sum(n)/ len(n)
        gemiddelden.append((gem, index))
        index+=1
    sorted_gemiddelden = sorted(gemiddelden, reverse=True)
    print("Employee, Average Daily Hours")
    print("-"*33)
    lang= len(weekly_hours_table)
    for l in range(lang):
        y, w= sorted_gemiddelden[l]
        print(f"Employee {w}\t{y:.2f} hours")