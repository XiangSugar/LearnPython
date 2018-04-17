from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

# 用指定日期时间创建datetime
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
print(now.timestamp())

t = 1429417200.0
# timestamp 转化为 datetime(本地时间)
print(datetime.fromtimestamp(t))  
# 准化为格林威治标准时间
print(datetime.utcfromtimestamp(t))

# str 转化为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime 转化为str
print(now.strftime('%a, %b %d %H:%M'))

# datetime 加减
fut1 = now + timedelta(hours=10)
fut2 = now + timedelta(days=1)
fut3 = now - timedelta(days=1, hours=5)
print(fut1, fut2, fut3)

# 创建时区UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))
# 强制设置为UTC+8:00
dt2 = now.replace(tzinfo=tz_utc_8)
print(dt2)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone将转换时区为北京时间：
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，
# 然后强制设置时区，作为基准时间。

# 利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

# 注：不是必须从 UTC+0:00 时区转换到其他时区，任何带时区的datetime都可以正确转换，
# 例如上述bj_dt到tokyo_dt的转换。