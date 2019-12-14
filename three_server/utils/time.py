import datetime as base_datetime
from datetime import datetime, timedelta, timezone as timezone


def get_now():
    """
    获取今日范围
    :return:
    """
    now = datetime.now()
    init_date = now - timedelta(hours=now.hour, minutes=now.minute, seconds=now.second,
                                microseconds=now.microsecond)
    # 今日数据时间范围
    start_date = (init_date - timedelta(hours=8)).replace(tzinfo=timezone.utc)
    end_date = (init_date + timedelta(hours=23, minutes=59, seconds=59)).replace(tzinfo=timezone.utc)
    return [init_date.strftime("%F %H:%M:%S"), end_date.strftime("%F %H:%M:%S")]


def get_current_week():
    """
    获取本周范围
    :return:
    """
    monday, sunday = base_datetime.date.today(), base_datetime.date.today()
    one_day = base_datetime.timedelta(days=1)
    while monday.weekday() != 0:
        monday -= one_day
    while sunday.weekday() != 6:
        sunday += one_day
    # 返回当前的星期一和星期天的日期
    return int(monday.strftime("%Y%m%d")), int(sunday.strftime("%Y%m%d"))
