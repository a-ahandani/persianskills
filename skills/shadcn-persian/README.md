<div align="center">

# 🇮🇷 PersianLabs/ui (shadcn-persian) AI Agent Skill

**The ultimate, production-grade, 100% offline agent skill for building Persian & RTL-first React, Next.js, and Vite applications with shadcn/ui and PersianLabs/ui.**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Abulfadl-Ahmadi/shadcn-persian?style=social)](https://github.com/Abulfadl-Ahmadi/shadcn-persian)
[![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-compatible-black)](https://ui.shadcn.com)
[![PersianLabs UI](https://img.shields.io/badge/PersianLabs-UI-006fee)](https://ui.persian-labs.ir)

</div>

---

## 📖 معرفی (Introduction)

این ریپازیتوری شامل **اسکیل جامع و رسمی `shadcn-persian`** برای دستیارهای هوش مصنوعی (مانند Hermes Agent, Claude Code, Cursor, Windsurf و OpenClaw) است.

تمامی مستندات، راهنماها، نمونهکدها، قوانین استایلینگ مدرن shadcn v4، توابع اعتبارسنجی ایرانی و سورسکدهای TypeScript به صورت **کاملاً آفلاین** در این مجموعه بستهبندی شدهاند تا هوش مصنوعی بدون نیاز به بازنویسی از صفر یا جستجوی اینترنت، حرفهایترین رابطهای کاربری فارسی را بسازد.

---

## ⚡ نحوه نصب در دستیارهای هوش مصنوعی (Installation)

### ۱. نصب در Hermes Agent
```bash
# نصب مستقیم از گیتهاب
hermes skill install Abulfadl-Ahmadi/shadcn-persian

# یا کلون دستی در پوشه اسکیلها:
git clone https://github.com/Abulfadl-Ahmadi/shadcn-persian.git ~/.hermes/skills/shadcn-persian
```

### ۲. نصب در Claude Code
```bash
# در پوشه کاربری Claude
git clone https://github.com/Abulfadl-Ahmadi/shadcn-persian.git ~/.claude/skills/shadcn-persian

# یا به عنوان اسکیل پروژه در ریپوی فعلی:
git clone https://github.com/Abulfadl-Ahmadi/shadcn-persian.git .claude/skills/shadcn-persian
```

### ۳. نصب در Cursor / Windsurf / VSCode
پوشه را داخل مسیر اسکیلهای پروژه قرار دهید:
```bash
git clone https://github.com/Abulfadl-Ahmadi/shadcn-persian.git .agents/skills/shadcn-persian
```

---

## 📦 محتویات بسته (Package Contents)

```text
shadcn-persian/
├── SKILL.md                  # راهنمای اصلی دستیار هوش مصنوعی و جدول دستورات سریع
├── README.md                 # توضیحات و مستندات پروژه
├── getting-started/          # ۹ راهنمای کلیدی (نصب، تم، RTL، فونت، قراردادها، آیکونها، CLI)
├── rules/                    # ۶ قانون طراحی مدرن shadcn (استایلینگ، فرمها، چت و ترکیببندی)
├── components/               # ۸۹ فایل مستندات کامل کامپوننتها با پروپها و الگوهای Zod
├── utilities/                # ۲۰ فایل مستندات توابع اعتبارسنجی و الگوریتمهای بومی
├── source-code/              # ۱۳۱ فایل سورس TypeScript کامل و آفلاین:
│   ├── components/*.tsx      # ۸۷ کامپوننت آماده
│   ├── hooks/*.ts            # ۱۳ کاستوم هوک (useCountdown, usePersianDate, ...)
│   ├── lib/*.ts              # ۲۹ الگوریتم محاسباتی (کد ملی، بانکها، پلاک، ...)
│   └── styles/globals.css    # متغیرهای کامل تم و CSS Variables
├── registry-json/            # ۱۰۶ فایل JSON رسمی رجیستری shadcn
└── examples/                 # ۴۸۲ مثال و دموی آماده با کد کامل TSX
```

---

## 🇮🇷 کامپوننتهای بومی و اختصاصی فارسی (Persian Components)

| ویژگی | نام کامپوننت / هوک | دستور ترمینال CLI |
| :--- | :--- | :--- |
| **کارت بانکی و شبا** | `BankInput`, `CardNumberInput`, `ShabaInput` | `npx shadcn@latest add @persianlabsui/bank-input` |
| **کد ملی با اعتبارسنجی** | `NationalIdInput`, `isValidNationalId` | `npx shadcn@latest add @persianlabsui/national-id-input` |
| **شماره موبایل ایران** | `MobileNumberInput` | `npx shadcn@latest add @persianlabsui/mobile-number-input` |
| **پلاک خودرو ملی** | `PlateInput` | `npx shadcn@latest add @persianlabsui/plate-input` |
| **انتخاب استان و شهر** | `CitySelector` | `npx shadcn@latest add @persianlabsui/city-selector` |
| **نقشه تعاملی ایران** | `IranMapPicker` | `npx shadcn@latest add @persianlabsui/iran-map-picker` |
| **تقویم کامل شمسی** | `Calendar` | `npx shadcn@latest add @persianlabsui/calendar` |
| **انتخابگر تاریخ شمسی** | `DatePicker` | `npx shadcn@latest add @persianlabsui/date-picker` |
| **دیتپیکر چرخشی موبایل** | `DateWheelPicker`, `WheelPicker` | `npx shadcn@latest add @persianlabsui/date-wheel-picker` |
| **انتخابگر ساعت و زمان** | `TimePicker`, `DurationPicker` | `npx shadcn@latest add @persianlabsui/time-picker` |
| **ورودی مبلغ با حروف** | `PriceInput` | `npx shadcn@latest add @persianlabsui/price-input` |
| **نماد وکتور تومان** | `TomanIcon` | `npx shadcn@latest add @persianlabsui/toman-icon` |
| **چاپ فاکتور و رسید حرارتی** | `ReceiptPrinter` | `npx shadcn@latest add @persianlabsui/receipt-printer` |
| **لوگوی بانکها و برندها** | `@persianlabs/icons` (۸۲۰+ لوگو) | `npm install @persianlabs/icons` |
| **ورودی رمز یکبار مصرف OTP**| `InputOtp`, `useCountdown` | `npx shadcn@latest add @persianlabsui/input-otp` |
| **پیامرسان و چت روم** | `MessageScroller`, `Message`, `Bubble` | `npx shadcn@latest add @persianlabsui/message-scroller` |

---

## 🧮 توابع اعتبارسنجی و الگوریتمهای بومی (Utilities)

| تابع کمکی | کاربرد | دستور نصب |
| :--- | :--- | :--- |
| `national-id` | فرمول چکسام اعتبارسنجی کد ملی ۱۰ رقمی | `npx shadcn@latest add @persianlabsui/national-id` |
| `iranian-bank` | تشخیص نام و لوگوی بانک از شماره کارت و شبا | `npx shadcn@latest add @persianlabsui/iranian-bank` |
| `normalize-persian-digits` | تبدیل ارقام انگلیسی/عربی به فارسی و بالعکس | `npx shadcn@latest add @persianlabsui/normalize-persian-digits` |
| `normalize-persian-text` | استانداردسازی حروف ی، ک و نیمفاصلهها | `npx shadcn@latest add @persianlabsui/normalize-persian-text` |
| `number-to-persian-words` | تبدیل اعداد به حروف فارسی (تومان / ریال) | `npx shadcn@latest add @persianlabsui/number-to-persian-words` |
| `persian-date` | تبدیل و قالببندی تاریخهای شمسی / میلادی | `npx shadcn@latest add @persianlabsui/persian-date` |
| `persian-date-zod` | اعتبارسنجی تاریخ شمسی در اسکیماهای Zod | `npx shadcn@latest add @persianlabsui/persian-date-zod` |
| `postal-code` | اعتبارسنجی کد پستی ۱۰ رقمی ایران | `npx shadcn@latest add @persianlabsui/postal-code` |
| `use-countdown` | هوک تایمر شمارش معکوس ارسال مجدد پیامک OTP | `npx shadcn@latest add @persianlabsui/use-countdown` |

---

## 📜 لایسنس (License)

این پروژه تحت لایسنس [MIT](LICENSE) منتشر شده است.
با تشکر ویژه از تیم [PersianLabs](https://ui.persian-labs.ir) و سازندگان [shadcn/ui](https://ui.shadcn.com).
