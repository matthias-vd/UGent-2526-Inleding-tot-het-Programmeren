import calendar

def print_month_title(jaar, maand):
    x = calendar.month_name[maand]
    print("         ", x, " ", str(jaar))
    print("-----------------------------")
    print(" Mon Tue Wed Thu Fri Sat Sun")


def print_month_body(jaar, maand):
    calendar.setfirstweekday(calendar.MONDAY)
    weeks = calendar.monthcalendar(jaar, maand)
    for week in weeks:
        cols = []
        for day in week:
            if day == 0:
                cols.append("   ")
            else:
                cols.append(f"{day:>3}")
        line = " ".join(cols)
        print(" " + line)


def print_month(jaar, maand):
    print_month_title(jaar, maand)
    print_month_body(jaar, maand)