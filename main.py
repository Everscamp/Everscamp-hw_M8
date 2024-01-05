from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    CURDATE = date.today()
    birthdayDays = defaultdict(list)
    week_interval = timedelta(days=7)
    
    if not users:
            return birthdayDays

    else:
        for user in users:
            modified_date = user.get("birthday").replace(year=CURDATE.year + 1) \
            if user.get("birthday").month == 1 \
            else user.get("birthday").replace(year=CURDATE.year)

            if CURDATE > modified_date:
                continue

            if modified_date >= CURDATE and (modified_date - CURDATE) <= week_interval:
                if modified_date.isoweekday() not in (6, 7):
                    birthdayDays[modified_date.strftime("%A")].append(user.get("name"))
                else:
                    birthdayDays["Monday"].append(user.get("name"))


        return birthdayDays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 3).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
