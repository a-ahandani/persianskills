<div dir="rtl" align="center">

# 🇮🇷 مهارت جامع نگارش فارسی و راست‌چین برای هوش مصنوعی
### Persian Typography, Natural Voice (De-AI) & Universal RTL Skill for AI Agents

**یک مهارت جامع، چندسکویی و استاندارد برای دستیارهای کدنویسی و مدل‌های زبانی:**  
Google Antigravity | Claude Code | Cursor | GitHub Copilot | Windsurf | ChatGPT

[![English Version](https://img.shields.io/badge/Language-English-blue.svg)](README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/PouyaRN/persian-formatting-skill/pulls)
[![RTL Supported](https://img.shields.io/badge/RTL-100%25-orange.svg)](#)

[English Documentation](README.md) • **[مستندات فارسی](README.fa.md)**

</div>

---

<div dir="rtl">

## 🎯 چرا این مهارت لازم است؟

مدل‌های هوش مصنوعی (مانند GPT-4، Claude 3.7، Gemini 2.5) با وجود قدرت بالا در درک زبان فارسی، هنگام تولید متن، کد فرانت‌اند و مستندات دچار مشکلات زیر می‌شوند:
1. **لحن رباتیک و ترجمه‌ای:** استفاده مکرر از افعال مرده مثل «می‌باشد»، «لازم به ذکر است» و مقدمه‌چینی‌های کلیشه‌ای.
2. **به‌هم‌ریختگی ترکیبی (BiDi):** جابجا شدن پرانتزها، کلمات انگلیسی و علائم نگارشی حین خروجی در چت یا مارک‌داون.
3. **تخریب کلمات با `letter-spacing`:** هوش مصنوعی در کدهای CSS برای زیبایی به تیترها فاصله بین حروف می‌دهد که حروف متصل فارسی را متلاشی می‌کند.
4. **خرابی متون فارسی در مایکروسافت اکسل:** فایل‌های CSV که علامت‌سؤال (`????`) می‌شوند.
5. **مشکل فونت در سیستم کاربران:** نبود فونت محلی استاندارد و به‌هم‌ریختگی چاپ و تبدیل PDF.

این مهارت با مجموعه‌ای از قوانین مهندسی‌شده و دقیق، خروجی تمامی دستیارها را در تولید محتوا، کد و سند به بالاترین استاندارد ارتقا می‌دهد.

---

## ⚡ نصب و استفاده سریع بر اساس پلتفرم

| پلتفرم شما | نحوه راه‌اندازی |
| :--- | :--- |
| **Google Antigravity** | فایل `SKILL.md` را در مسیر `~/.gemini/config/skills/persian-formatting/SKILL.md` کپی کنید. |
| **Cursor IDE** | فایل `rules/persian.mdc` را در پوشه `.cursor/rules/` قرار دهید یا متن آن را در `.cursorrules` بگذارید. |
| **Claude Code (CLI)** | فایل `SKILL.md` را در `.claude/skills/persian-formatting/SKILL.md` کپی کرده یا محتوای `rules/CLAUDE.md` را در ریشه پروژه قرار دهید. |
| **GitHub Copilot** | محتوای `rules/copilot-instructions.md` را در ریشه پروژه داخل مسیر `.github/copilot-instructions.md` بگذارید. |
| **Windsurf** | فایل `rules/windsurfrules` را در ریشه پروژه قرار دهید. |
| **ChatGPT / Claude Web** | بخش‌های ۱ تا ۴ فایل `SKILL.md` را در بخش **Custom Instructions** جای‌گذاری کنید. |

---

## 🌟 قابلیت‌های کلیدی

### ۱. لحن طبیعی و انسانی (De-AI-ing)
* جایگزینی ۹۵٪ فعل‌های «می‌باشد» با افعال طبیعی و روان «است» و «هست».
* حذف عبارات پرکننده و ترجمه‌ای مانند «در دنیای پرشتاب امروزی...» و «شایان ذکر است...».
* اصلاح خودکار حروف عربی (`ي` و `ك`) به حروف اصیل فارسی (`ی` و `ک`).

### ۲. استانداردهای حیاتی فرانت‌اند و CSS
* **ممنوعیت `letter-spacing`:** اجبار به حفظ اتصال طبیعی حروف الفبای فارسی.
* **فیلدهای ورودی حساس:** تنظیم خودکار `dir="ltr"` برای موبایل، کد ملی، کارت بانکی، ایمیل و پسورد.
* **ویژگی‌های منطقی (Logical Properties):** جایگزینی خودکار `margin-left` با `margin-inline-start` برای پشتیبانی کامل از دوزبانه بودن.
* **فونت وب استاندارد (CDN Fallback):** لود خودکار فونت Sahel از CDN jsDelivr در خروجی‌های وب تا حتی روی سیستم‌های فاقد فونت محلی، متون چشم‌نواز باشند.

### ۳. ایزولاسیون کامل در چت و مارک‌داون
* کپسوله‌سازی خروجی با استایل RTL در اینترفیس‌های وب.
* استفاده از برچسب `<bdi>` و بک‌تیک برای ایزوله کردن کلمات و اصطلاحات انگلیسی وسط متن.
* رعایت نیم‌فاصله‌های استاندارد (ZWNJ)، گیومه‌های فارسی (« ») و ممیز فارسی (`٫`).

### ۴. اسناد اداری، اکسل و خروجی PDF
* انکودینگ **UTF-8 with BOM** برای جلوگیری از خرابی فایل‌های CSV در Excel.
* دستورات دقیق و آزمایش‌شده Chrome Headless برای تولید فایل PDF در سه سیستم‌عامل Windows، macOS و Linux.

---

## 📂 ساختار فایل‌های مخزن

```text
├── SKILL.md                  # فایل کامل اسکیل و استاندارد اصلی
├── README.md                 # راهنمای انگلیسی پروژه
├── README.fa.md              # راهنمای فارسی پروژه
├── LICENSE                   # پروانه متن‌باز MIT
└── rules/                    # تنظیمات آماده کپی در ابزارهای مختلف
    ├── persian.mdc           # ویژه Cursor IDE
    ├── CLAUDE.md             # ویژه Claude Code
    ├── copilot-instructions.md # ویژه GitHub Copilot
    └── windsurfrules         # ویژه Windsurf
```

---

## 🤝 مشارکت و بهبود (Contributing)

پیشنهادات، اصلاح قوانین نگارشی و افزودن تمپلیت برای ابزارهای جدید با استقبال کامل پذیرفته می‌شود. لطفاً یک Issue یا Pull Request ثبت کنید!

## 📜 پروانه (License)

این پروژه تحت پروانه [MIT](LICENSE) منتشر شده است و استفاده از آن برای مقاصد شخصی و تجاری کاملاً آزاد و رایگان است.

</div>
