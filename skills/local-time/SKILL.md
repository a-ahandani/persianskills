---
name: local-time
description: "دریافت زمان و تاریخ فعلی سیستم. برای get time, get date, تاریخ جلالی، روز هفته، و time-sensitive reasoning استفاده کن."
allowed-tools: Bash(python *local_time.py*)
---

# 🕐 Local Time Skill

یک ابزار خط فرمان برای دریافت دقیق زمان و تاریخ سیستم — شامل تقویم جلالی (هجری شمسی).

## 📋 فهرست

- [پیش‌نیازها](#پیش‌نیازها)
- [نصب](#نصب)
- [دستورات](#دستورات)
  - [now — زمان فعلی](#now--زمان-فعلی)
  - [jalali — تاریخ جلالی](#jalali--تاریخ-جلالی)
  - [weekday — روز هفته](#weekday--روز-هفته)
  - [to-jalali — تبدیل میلادی به جلالی](#to-jalali--تبدیل-میلادی-به-جلالی)
  - [to-gregorian — تبدیل جلالی به میلادی](#to-gregorian--تبدیل-جلالی-به-میلادی)
  - [timestamp — Unix timestamp](#timestamp--unix-timestamp)
  - [timezones — لیست timezoneها](#timezones--لیست-timezoneها)
- [ساختار خروجی JSON](#ساختار-خروجی-json)
- [timezoneهای پشتیبانی شده](#timezoneهای-پشتیبانی-شده)
- [نکات مهم](#نکات-مهم)
- [عیب‌یابی](#عیب‌یابی)

---

## پیش‌نیازها

- Python 3.11+
- کتابخانه `jdatetime` برای پشتیبانی از تاریخ جلالی

```bash
pip install jdatetime
```

## نصب

```bash
# کپی فایل‌ها به دایرکتوری skills
cp -r skill/ ~/.claude/skills/local-time/

# یا به صورت دستی
mkdir -p ~/.claude/skills/local-time/
cp skill/SKILL.md skill/local_time.py ~/.claude/skills/local-time/
```

---

## دستورات

### `now` — زمان فعلی

زمان و تاریخ کامل فعلی رو برمی‌گردونه (میلادی + جلالی).

**نحوه استفاده:**

```bash
# زمان محلی سیستم
python ~/.claude/skills/local-time/local_time.py now

# زمان با timezone مشخص
python ~/.claude/skills/local-time/local_time.py now --tz Asia/Tehran
python ~/.claude/skills/local-time/local_time.py now --tz UTC
python ~/.claude/skills/local-time/local_time.py now --tz Europe/Berlin
python ~/.claude/skills/local-time/local_time.py now --tz America/New_York
```

**پارامترها:**

| پارامتر | نوع | ضروری | پیش‌فرض | توضیح |
|----------|------|--------|----------|-------|
| `--tz` | `string` | ❌ | ساعت محلی | نام timezone IANA |

**نمونه خروجی:**

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

---

### `jalali` — تاریخ جلالی

فقط تاریخ جلالی فعلی رو برمی‌گردونه.

**نحوه استفاده:**

```bash
python ~/.claude/skills/local-time/local_time.py jalali
python ~/.claude/skills/local-time/local_time.py jalali --tz Asia/Tehran
```

**نمونه خروجی:**

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

---

### `weekday` — روز هفته

روز هفته رو به انگلیسی و فارسی برمی‌گردونه.

**نحوه استفاده:**

```bash
python ~/.claude/skills/local-time/local_time.py weekday
python ~/.claude/skills/local-time/local_time.py weekday --tz Asia/Tehran
```

**نمونه خروجی:**

```json
{
  "day_of_week": "Tuesday",
  "day_of_week_fa": "سه‌شنبه",
  "date": "2026-08-11",
  "timezone": "Asia/Tehran"
}
```

---

### `to-jalali` — تبدیل میلادی به جلالی

یک تاریخ میلادی رو به جلالی تبدیل می‌کنه.

**نحوه استفاده:**

```bash
python ~/.claude/skills/local-time/local_time.py to-jalali 2026-08-10
python ~/.claude/skills/local-time/local_time.py to-jalali 2026/08/10
python ~/.claude/skills/local-time/local_time.py to-jalali 2026.08.10
```

**ورودی:** تاریخ میلادی با فرمت `YYYY-MM-DD` یا `YYYY/MM/DD` یا `YYYY.MM.DD`

**نمونه خروجی:**

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

**نمونه برای نوروز:**

```bash
python ~/.claude/skills/local-time/local_time.py to-jalali 2026-03-21
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

---

### `to-gregorian` — تبدیل جلالی به میلادی

یک تاریخ جلالی رو به میلادی تبدیل می‌کنه.

**نحوه استفاده:**

```bash
python ~/.claude/skills/local-time/local_time.py to-gregorian 1405/05/19
python ~/.claude/skills/local-time/local_time.py to-gregorian 1405-05-19
```

**ورودی:** تاریخ جلالی با فرمت `YYYY/MM/DD` یا `YYYY-MM-DD`

**نمونه خروجی:**

```json
{
  "jalali": "1405/05/19",
  "gregorian": "2026-08-10",
  "gregorian_year": 2026,
  "gregorian_month": 8,
  "gregorian_day": 10
}
```

---

### `timestamp` — Unix timestamp

Unix timestamp فعلی رو برمی‌گردونه.

**نحوه استفاده:**

```bash
python ~/.claude/skills/local-time/local_time.py timestamp
python ~/.claude/skills/local-time/local_time.py timestamp --tz UTC
```

**نمونه خروجی:**

```json
{
  "unix_timestamp": 1786446271,
  "datetime": "2026-08-11T14:34:31+03:30",
  "timezone": "Asia/Tehran"
}
```

---

### `timezones` — لیست timezoneها

لیست timezoneهای رایج رو نمایش میده.

**نحوه استفاده:**

```bash
python ~/.claude/skills/local-time/local_time.py timezones
```

**نمونه خروجی:**

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

---

## ساختار خروجی JSON

تمام دستورات خروجی JSON تولید می‌کنن. فیلدهای اصلی:

| فیلد | نوع | توضیح |
|------|------|-------|
| `datetime` | `string` | تاریخ و ساعت ISO 8601 با offset |
| `date` | `string` | تاریخ میلادی (YYYY-MM-DD) |
| `time` | `string` | ساعت (HH:MM:SS) |
| `day_of_week` | `string` | نام روز به انگلیسی |
| `day_of_week_fa` | `string` | نام روز به فارسی |
| `timezone` | `string` | نام timezone IANA |
| `utc_offset` | `string` | اختلاف با UTC (±HH:MM) |
| `unix_timestamp` | `integer` | Unix epoch timestamp |
| `jalali_date` | `string` | تاریخ جلالی عددی (YYYY/MM/DD) |
| `jalali_date_fa` | `string` | تاریخ جلالی به فارسی |
| `jalali_year` | `integer` | سال جلالی |
| `jalali_month` | `integer` | ماه جلالی (1-12) |
| `jalali_month_name` | `string` | نام ماه فارسی |
| `jalali_day` | `integer` | روز جلالی (1-31) |

---

## timezoneهای پشتیبانی شده

هر نام timezone IANA معتبر کار می‌کنه:

| Timezone | شهر | UTC Offset |
|----------|------|------------|
| `UTC` | جهانی | +00:00 |
| `Asia/Tehran` | تهران | +03:30 |
| `Europe/Berlin` | برلین | +01:00 / +02:00 (DST) |
| `America/New_York` | نیویورک | -05:00 / -04:00 (DST) |
| `America/Los_Angeles` | لس‌آنجلس | -08:00 / -07:00 (DST) |
| `Asia/Tokyo` | توکیو | +09:00 |
| `Europe/London` | لندن | +00:00 / +01:00 (DST) |
| `Asia/Dubai` | دبی | +04:00 |
| `Asia/Kolkata` | هند | +05:30 |
| `Australia/Sydney` | سیدنی | +10:00 / +11:00 (DST) |

---

## نکات مهم

- ⏰ **زمان لحظه‌ای**: هر بار که دستور اجرا میشه، زمان دقیق اون لحظه برگردونده میشه
- 🌍 **DST خودکار**: Daylight Saving Time به صورت خودکار مدیریت میشه
- 📅 **تقویم جلالی**: از کتابخانه `jdatetime` استفاده میشه
- 🔌 **آفلاین**: فقط از ساعت سیستم استفاده میشه، بدون اتصال اینترنت
- 📄 **خروجی JSON**: تمام خروجی‌ها JSON هستن برای پردازش خودکار
- 🪟 **ویندوز**: رمزگذاری UTF-8 به صورت خودکار تنظیم میشه

---

## عیب‌یابی

### خطای `jdatetime not installed`

```bash
pip install jdatetime
```

### خطای `Invalid timezone`

از نام‌های timezone IANA معتبر استفاده کنید:

| ❌ غلط | ✅ درست |
|--------|---------|
| `Tehran` | `Asia/Tehran` |
| `CET` | `Europe/Berlin` |
| `EST` | `America/New_York` |
| `GMT` | `UTC` |

### خطای `Invalid date format`

فرمت تاریخ رو چک کنید:

- میلادی: `YYYY-MM-DD` یا `YYYY/MM/DD`
- جلالی: `YYYY/MM/DD` یا `YYYY-MM-DD`

### مشکل رمزگذاری فارسی در ویندوز

اسکریپت به صورت خودکار UTF-8 رو تنظیم می‌کنه. اگه مشکل داشتید:

```bash
# تنظیم متغیر محیطی
set PYTHONIOENCODING=utf-8
python ~/.claude/skills/local-time/local_time.py now
```

---

## مثال‌های کاربردی

### پرسیدن زمان فعلی

```
کاربر: ساعت چنده؟
Claude: python local_time.py now --tz Asia/Tehran
```

### پرسیدن تاریخ جلالی

```
کاربر: امروز چندمه به تقویم جلالی؟
Claude: python local_time.py jalali
```

### پرسیدن روز هفته

```
کاربر: امروز چه روزیه؟
Claude: python local_time.py weekday
```

### تبدیل تاریخ

```
کاربر: ۱۰ آگوست ۲۰۲۶ چندمه به جلالی؟
Claude: python local_time.py to-jalali 2026-08-10
```

### محاسبه روز باقی‌مانده

```
کاربر: چند روز تا جمعه مونده؟
Claude: python local_time.py weekday → سه‌شنبه → ۳ روز
```
