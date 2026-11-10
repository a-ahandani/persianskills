---
name: local-time
description: >-
  Returns the current system date and time as JSON from a local Python
  script, including the Jalali (Solar Hijri) date, the weekday in English
  and Persian, Unix timestamps, any IANA timezone, and Gregorian to Jalali
  conversion both ways. Use before any time-sensitive reasoning, when the
  user asks for the time, today's date, the Jalali date or the day of the
  week, or writes «ساعت چنده», «امروز چندمه», «تاریخ جلالی» or «روز هفته».
license: MIT
compatibility: Python 3.11+; the Jalali fields need the jdatetime package.
allowed-tools: Bash(python *local_time.py*)
metadata:
  author: karimi-mohammad
  source: https://github.com/karimi-mohammad/local-time-mcp
  upstream-commit: 821afce
  changes: Only the skill/ folder copied, without the MCP server; instructions translated from Persian to English, emoji removed, and local_time.py moved into scripts/.
---

# Local Time

A command-line tool that returns the exact system date and time, including
the Jalali (Solar Hijri) calendar. Run it instead of guessing the date from
memory. Paths below are relative to this skill's folder.

## Prerequisites

- Python 3.11+
- The `jdatetime` package for Jalali dates. Without it `now` leaves out the
  Jalali fields, `jalali` returns them as `null`, and `to-jalali` and
  `to-gregorian` return an error.

```bash
pip install jdatetime
```

## Commands

### `now`: current time

Returns the full current date and time, Gregorian and Jalali.

Usage:

```bash
# system local time
python scripts/local_time.py now

# a given timezone
python scripts/local_time.py now --tz Asia/Tehran
python scripts/local_time.py now --tz UTC
python scripts/local_time.py now --tz Europe/Berlin
python scripts/local_time.py now --tz America/New_York
```

Parameters:

| Parameter | Type | Required | Default | Description |
|----------|------|--------|----------|-------|
| `--tz` | `string` | No | System local time | IANA timezone name |

Sample output:

```json
{
  "datetime": "2026-08-11T14:34:31.893922+03:30",
  "date": "2026-08-11",
  "time": "14:34:31",
  "day_of_week": "Tuesday",
  "day_of_week_fa": "سه‌شنبه",
  "timezone": "Asia/Tehran",
  "utc_offset": "+03:30",
  "unix_timestamp": 1786446271,
  "jalali_date": "1405/05/20",
  "jalali_date_fa": "20 مرداد 1405",
  "jalali_year": 1405,
  "jalali_month": 5,
  "jalali_month_name": "مرداد",
  "jalali_day": 20
}
```

### `jalali`: Jalali date

Returns only the current Jalali date.

Usage:

```bash
python scripts/local_time.py jalali
python scripts/local_time.py jalali --tz Asia/Tehran
```

Sample output:

```json
{
  "jalali_date": "1405/05/20",
  "jalali_date_fa": "20 مرداد 1405",
  "jalali_year": 1405,
  "jalali_month": 5,
  "jalali_month_name": "مرداد",
  "jalali_day": 20,
  "gregorian_date": "2026-08-11",
  "timezone": "Asia/Tehran"
}
```

### `weekday`: day of the week

Returns the day of the week in English and Persian.

Usage:

```bash
python scripts/local_time.py weekday
python scripts/local_time.py weekday --tz Asia/Tehran
```

Sample output:

```json
{
  "day_of_week": "Tuesday",
  "day_of_week_fa": "سه‌شنبه",
  "date": "2026-08-11",
  "timezone": "Asia/Tehran"
}
```

### `to-jalali`: Gregorian to Jalali

Converts a Gregorian date to Jalali.

Usage:

```bash
python scripts/local_time.py to-jalali 2026-08-10
python scripts/local_time.py to-jalali 2026/08/10
python scripts/local_time.py to-jalali 2026.08.10
```

Input: a Gregorian date as `YYYY-MM-DD`, `YYYY/MM/DD` or `YYYY.MM.DD`.

Sample output:

```json
{
  "gregorian": "2026-08-10",
  "jalali": "1405/05/19",
  "jalali_fa": "19 مرداد 1405",
  "jalali_year": 1405,
  "jalali_month": 5,
  "jalali_month_name": "مرداد",
  "jalali_day": 19
}
```

Nowruz example:

```bash
python scripts/local_time.py to-jalali 2026-03-21
```

```json
{
  "gregorian": "2026-03-21",
  "jalali": "1405/01/01",
  "jalali_fa": "1 فروردین 1405",
  "jalali_year": 1405,
  "jalali_month": 1,
  "jalali_month_name": "فروردین",
  "jalali_day": 1
}
```

### `to-gregorian`: Jalali to Gregorian

Converts a Jalali date to Gregorian.

Usage:

```bash
python scripts/local_time.py to-gregorian 1405/05/19
python scripts/local_time.py to-gregorian 1405-05-19
```

Input: a Jalali date as `YYYY/MM/DD` or `YYYY-MM-DD`.

Sample output:

```json
{
  "jalali": "1405/05/19",
  "gregorian": "2026-08-10",
  "gregorian_year": 2026,
  "gregorian_month": 8,
  "gregorian_day": 10
}
```

### `timestamp`: Unix timestamp

Returns the current Unix timestamp.

Usage:

```bash
python scripts/local_time.py timestamp
python scripts/local_time.py timestamp --tz UTC
```

Sample output:

```json
{
  "unix_timestamp": 1786446271,
  "datetime": "2026-08-11T14:34:31+03:30",
  "timezone": "Asia/Tehran"
}
```

### `timezones`: common timezones

Lists common timezones.

Usage:

```bash
python scripts/local_time.py timezones
```

Sample output:

```json
{
  "common_timezones": [
    "UTC",
    "Asia/Tehran",
    "Europe/Berlin",
    "America/New_York",
    "America/Los_Angeles",
    "Asia/Tokyo",
    "Europe/London",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Australia/Sydney"
  ],
  "note": "Any IANA timezone name is supported. These are just common examples."
}
```

## JSON output

Every command prints JSON. The main fields:

| Field | Type | Description |
|------|------|-------|
| `datetime` | `string` | ISO 8601 date and time with offset |
| `date` | `string` | Gregorian date (YYYY-MM-DD) |
| `time` | `string` | Time (HH:MM:SS) |
| `day_of_week` | `string` | Day name in English |
| `day_of_week_fa` | `string` | Day name in Persian |
| `timezone` | `string` | IANA timezone name |
| `utc_offset` | `string` | Offset from UTC (±HH:MM) |
| `unix_timestamp` | `integer` | Unix epoch timestamp |
| `jalali_date` | `string` | Numeric Jalali date (YYYY/MM/DD) |
| `jalali_date_fa` | `string` | Jalali date with the Persian month name |
| `jalali_year` | `integer` | Jalali year |
| `jalali_month` | `integer` | Jalali month (1-12) |
| `jalali_month_name` | `string` | Persian month name |
| `jalali_day` | `integer` | Jalali day (1-31) |

## Supported timezones

Any valid IANA timezone name works:

| Timezone | City | UTC Offset |
|----------|------|------------|
| `UTC` | Universal | +00:00 |
| `Asia/Tehran` | Tehran | +03:30 |
| `Europe/Berlin` | Berlin | +01:00 / +02:00 (DST) |
| `America/New_York` | New York | -05:00 / -04:00 (DST) |
| `America/Los_Angeles` | Los Angeles | -08:00 / -07:00 (DST) |
| `Asia/Tokyo` | Tokyo | +09:00 |
| `Europe/London` | London | +00:00 / +01:00 (DST) |
| `Asia/Dubai` | Dubai | +04:00 |
| `Asia/Kolkata` | India | +05:30 |
| `Australia/Sydney` | Sydney | +10:00 / +11:00 (DST) |

## Notes

- **Live time:** every run returns the exact time at that moment.
- **Automatic DST:** daylight saving time is handled automatically.
- **Jalali calendar:** computed with the `jdatetime` package.
- **Offline:** uses only the system clock, no internet connection.
- **JSON output:** all output is JSON, for automated processing.
- **Windows:** UTF-8 output encoding is set automatically.

## Troubleshooting

### `jdatetime not installed` error

```bash
pip install jdatetime
```

### `Invalid timezone` error

Use valid IANA timezone names:

| Wrong | Right |
|--------|---------|
| `Tehran` | `Asia/Tehran` |
| `CET` | `Europe/Berlin` |
| `EST` | `America/New_York` |
| `GMT` | `UTC` |

### `Invalid date format` error

Check the date format:

- Gregorian: `YYYY-MM-DD` or `YYYY/MM/DD`
- Jalali: `YYYY/MM/DD` or `YYYY-MM-DD`

### Persian text garbled on Windows

The script sets UTF-8 automatically. If the problem persists:

```bash
# set the environment variable
set PYTHONIOENCODING=utf-8
python scripts/local_time.py now
```

## Examples

### Asking the current time

```
User: ساعت چنده؟
Claude: python scripts/local_time.py now --tz Asia/Tehran
```

### Asking the Jalali date

```
User: امروز چندمه به تقویم جلالی؟
Claude: python scripts/local_time.py jalali
```

### Asking the day of the week

```
User: امروز چه روزیه؟
Claude: python scripts/local_time.py weekday
```

### Converting a date

```
User: ۱۰ آگوست ۲۰۲۶ چندمه به جلالی؟
Claude: python scripts/local_time.py to-jalali 2026-08-10
```

### Counting the days left

```
User: چند روز تا جمعه مونده؟
Claude: python scripts/local_time.py weekday → سه‌شنبه → ۳ روز
```
