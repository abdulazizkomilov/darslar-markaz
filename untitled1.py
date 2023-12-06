from datetime import datetime, timedelta

class UserLimit:
    def __init__(self):
        self.usage_count = 0
        self.last_reset_date = datetime.now()

    def reset_daily_limit(self):
        if datetime.now().date() > self.last_reset_date.date():
            self.usage_count = 0
            self.last_reset_date = datetime.now()
            
    def get_current_usage(self):
        return self.usage_count

    def increment_usage(self):
        self.usage_count += 1

    def has_daily_limit_exceeded(self, limit):
        self.reset_daily_limit()
        return self.usage_count > limit


user_limits = {}

daily_limit = 5

def handle_user(user_id):
    user_limit = user_limits.get(user_id, UserLimit())
    user_limits[user_id] = user_limit

    if user_limit.has_daily_limit_exceeded(daily_limit):
        return "Sizning kunlik limitlariniz tugadi. Yangi limit ertaga belgilandi."
        user_limit.reset_daily_limit()
    else:
        user_limit.increment_usage()


def get_user_usage(user_id):
    user_limit = user_limits.get(user_id, UserLimit())
    user_limits[user_id] = user_limit

    if user_limit.has_daily_limit_exceeded(daily_limit):
        user_limit.reset_daily_limit()

    return user_limit.get_current_usage()


test_user_id = 123456789
handle_user(test_user_id)