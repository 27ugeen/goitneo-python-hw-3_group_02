from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    weekend_days = ["Saturday", "Sunday"]
    work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    def get_birthday_this_year(birthday, today):
        birthday_this_year = birthday.replace(year=today.year)
        return birthday_this_year if birthday_this_year >= today else birthday_this_year.replace(year=today.year + 1)

    def get_weekday_name(date):
        return date.strftime("%A")

    birthday_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user.name.value
        birthday = datetime.strptime(user.birthday.value, '%d.%m.%Y').date() if user.birthday else None

        if birthday is not None:
            birthday_this_year = get_birthday_this_year(birthday, today)
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                weekday = get_weekday_name(today + timedelta(days=delta_days))
                weekday = "Monday" if weekday in weekend_days else weekday
                birthday_dict[weekday].append(name)

    all_names=[]
    for day in work_days:
        names = birthday_dict.get(day, [])
        if names:
            print(f"{day}: {', '.join(names)}")
            all_names.append(names)
    
    if not all_names:
        print("No Upcoming Birthdays found.")