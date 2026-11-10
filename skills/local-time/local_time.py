#!/usr/bin/env python3
"""
Local Time Skill for Claude Code
دریافت زمان و تاریخ فعلی سیستم با دقت
"""

import sys
import io
import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

# Fix Windows console encoding for Persian characters
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    import jdatetime
    HAS_JDATETIME = True
except ImportError:
    HAS_JDATETIME = False

# Persian day names
PERSIAN_DAYS = {
    0: "دوشنبه", 1: "سه‌شنبه", 2: "چهارشنبه",
    3: "پنج‌شنبه", 4: "جمعه", 5: "شنبه", 6: "یکشنبه",
}

ENGLISH_DAYS = {
    0: "Monday", 1: "Tuesday", 2: "Wednesday",
    3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday",
}

JALALI_MONTHS = {
    1: "فروردین", 2: "اردیبهشت", 3: "خرداد", 4: "تیر",
    5: "مرداد", 6: "شهریور", 7: "مهر", 8: "آبان",
    9: "آذر", 10: "دی", 11: "بهمن", 12: "اسفند",
}

COMMON_TIMEZONES = [
    "UTC", "Asia/Tehran", "Europe/Berlin", "America/New_York",
    "America/Los_Angeles", "Asia/Tokyo", "Europe/London",
    "Asia/Dubai", "Asia/Kolkata", "Australia/Sydney",
]


def get_now(tz_name=None):
    """Get current datetime for timezone."""
    now_utc = datetime.now(timezone.utc)

    if tz_name:
        try:
            target_tz = ZoneInfo(tz_name)
        except (ZoneInfoNotFoundError, KeyError, OSError):
            return {"error": f"Invalid timezone: {tz_name}"}
    else:
        now_local = datetime.now().astimezone()
        target_tz = now_local.tzinfo
        if hasattr(target_tz, "key"):
            tz_name = target_tz.key
        else:
            tz_name = "Local"

    now = now_utc.astimezone(target_tz)
    offset = now.utcoffset()
    total_seconds = int(offset.total_seconds())
    sign = "+" if total_seconds >= 0 else "-"
    hours = abs(total_seconds) // 3600
    minutes = (abs(total_seconds) % 3600) // 60

    day_num = now.weekday()
    result = {
        "datetime": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day_of_week": ENGLISH_DAYS[day_num],
        "day_of_week_fa": PERSIAN_DAYS[day_num],
        "timezone": tz_name,
        "utc_offset": f"{sign}{hours:02d}:{minutes:02d}",
        "unix_timestamp": int(now.timestamp()),
    }

    if HAS_JDATETIME:
        jalali = jdatetime.date.fromgregorian(year=now.year, month=now.month, day=now.day)
        result["jalali_date"] = f"{jalali.year}/{jalali.month:02d}/{jalali.day:02d}"
        result["jalali_date_fa"] = f"{jalali.day} {JALALI_MONTHS[jalali.month]} {jalali.year}"
        result["jalali_year"] = jalali.year
        result["jalali_month"] = jalali.month
        result["jalali_month_name"] = JALALI_MONTHS[jalali.month]
        result["jalali_day"] = jalali.day

    return result


def cmd_now(args):
    """Get current datetime."""
    result = get_now(args.tz)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if "error" not in result else 1


def cmd_jalali(args):
    """Get current Jalali date."""
    result = get_now(args.tz)
    if "error" in result:
        print(json.dumps(result, ensure_ascii=False))
        return 1
    jalali = {
        "jalali_date": result.get("jalali_date"),
        "jalali_date_fa": result.get("jalali_date_fa"),
        "jalali_year": result.get("jalali_year"),
        "jalali_month": result.get("jalali_month"),
        "jalali_month_name": result.get("jalali_month_name"),
        "jalali_day": result.get("jalali_day"),
        "gregorian_date": result["date"],
        "timezone": result["timezone"],
    }
    print(json.dumps(jalali, ensure_ascii=False))
    return 0


def cmd_weekday(args):
    """Get current day of week."""
    result = get_now(args.tz)
    if "error" in result:
        print(json.dumps(result, ensure_ascii=False))
        return 1
    weekday = {
        "day_of_week": result["day_of_week"],
        "day_of_week_fa": result["day_of_week_fa"],
        "date": result["date"],
        "timezone": result["timezone"],
    }
    print(json.dumps(weekday, ensure_ascii=False))
    return 0


def cmd_to_jalali(args):
    """Convert Gregorian date to Jalali."""
    if not HAS_JDATETIME:
        print(json.dumps({"error": "jdatetime not installed. Run: pip install jdatetime"}))
        return 1

    date_str = args.date.replace("-", "/").replace(".", "/")
    parts = date_str.split("/")
    if len(parts) != 3:
        print(json.dumps({"error": "Invalid date format. Use YYYY-MM-DD or YYYY/MM/DD"}))
        return 1

    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        jalali = jdatetime.date.fromgregorian(year=year, month=month, day=day)
        result = {
            "gregorian": f"{year:04d}-{month:02d}-{day:02d}",
            "jalali": f"{jalali.year}/{jalali.month:02d}/{jalali.day:02d}",
            "jalali_fa": f"{jalali.day} {JALALI_MONTHS[jalali.month]} {jalali.year}",
            "jalali_year": jalali.year,
            "jalali_month": jalali.month,
            "jalali_month_name": JALALI_MONTHS[jalali.month],
            "jalali_day": jalali.day,
        }
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (ValueError, OverflowError) as e:
        print(json.dumps({"error": f"Invalid date: {e}"}))
        return 1


def cmd_to_gregorian(args):
    """Convert Jalali date to Gregorian."""
    if not HAS_JDATETIME:
        print(json.dumps({"error": "jdatetime not installed. Run: pip install jdatetime"}))
        return 1

    date_str = args.date.replace("-", "/")
    parts = date_str.split("/")
    if len(parts) != 3:
        print(json.dumps({"error": "Invalid date format. Use YYYY/MM/DD or YYYY-MM-DD"}))
        return 1

    try:
        jy, jm, jd = int(parts[0]), int(parts[1]), int(parts[2])
        gregorian = jdatetime.date(jy, jm, jd).togregorian()
        result = {
            "jalali": f"{jy}/{jm:02d}/{jd:02d}",
            "gregorian": f"{gregorian.year}-{gregorian.month:02d}-{gregorian.day:02d}",
            "gregorian_year": gregorian.year,
            "gregorian_month": gregorian.month,
            "gregorian_day": gregorian.day,
        }
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (ValueError, OverflowError) as e:
        print(json.dumps({"error": f"Invalid Jalali date: {e}"}))
        return 1


def cmd_timestamp(args):
    """Get current Unix timestamp."""
    result = get_now(args.tz if hasattr(args, 'tz') else None)
    if "error" in result:
        print(json.dumps(result))
        return 1
    print(json.dumps({
        "unix_timestamp": result["unix_timestamp"],
        "datetime": result["datetime"],
        "timezone": result["timezone"],
    }))
    return 0


def cmd_timezones(args):
    """List common timezones."""
    print(json.dumps({
        "common_timezones": COMMON_TIMEZONES,
        "note": "Any IANA timezone name is supported. These are just common examples.",
    }))
    return 0


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Local Time Skill for Claude Code")
    subparsers = parser.add_subparsers(dest="command")

    # now
    p_now = subparsers.add_parser("now", help="Get current datetime")
    p_now.add_argument("--tz", help="Timezone (e.g. Asia/Tehran, UTC)")
    p_now.set_defaults(func=cmd_now)

    # jalali
    p_jalali = subparsers.add_parser("jalali", help="Get current Jalali date")
    p_jalali.add_argument("--tz", help="Timezone")
    p_jalali.set_defaults(func=cmd_jalali)

    # weekday
    p_weekday = subparsers.add_parser("weekday", help="Get current day of week")
    p_weekday.add_argument("--tz", help="Timezone")
    p_weekday.set_defaults(func=cmd_weekday)

    # to-jalali
    p_to_jalali = subparsers.add_parser("to-jalali", help="Convert Gregorian to Jalali")
    p_to_jalali.add_argument("date", help="Gregorian date (YYYY-MM-DD)")
    p_to_jalali.set_defaults(func=cmd_to_jalali)

    # to-gregorian
    p_to_gregorian = subparsers.add_parser("to-gregorian", help="Convert Jalali to Gregorian")
    p_to_gregorian.add_argument("date", help="Jalali date (YYYY/MM/DD)")
    p_to_gregorian.set_defaults(func=cmd_to_gregorian)

    # timestamp
    p_ts = subparsers.add_parser("timestamp", help="Get Unix timestamp")
    p_ts.add_argument("--tz", help="Timezone")
    p_ts.set_defaults(func=cmd_timestamp)

    # timezones
    p_tz = subparsers.add_parser("timezones", help="List common timezones")
    p_tz.set_defaults(func=cmd_timezones)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
