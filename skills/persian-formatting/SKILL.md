---
name: persian-formatting
description: >-
  Comprehensive standards, natural Persian writing (de-AI-ing), typography, layout, CSS/RTL rules, and cross-platform support (Antigravity, Claude Code, Cursor, Copilot, Windsurf, ChatGPT) for HTML, Markdown, PDF, CSS, Excel, and codebases.
---

# مهارت جامع نگارش طبیعی، راست‌چین‌سازی و استانداردهای زبان فارسی (Persian Formatting & Universal RTL Standards)

این مهارت به مدل‌ها و عامل‌های هوش مصنوعی (AI Agents) در تمامی پلتفرم‌ها (Antigravity، Claude Code، Cursor، Windsurf، GitHub Copilot، ChatGPT و ...) چارچوب جامع نگارش زبان فارسی طبیعی، حذف لحن رباتیک (De-AI-ing)، رعایت جهت راست‌به‌چپ (RTL)، تایپوگرافی اصیل، ایمنی استایل‌های فرانت‌اند و جلوگیری از تداخل عبارات فنی/انگلیسی را آموزش می‌دهد.

---

## ۱. اصول لحن طبیعی و حذف کلیشه‌های ماشینی (Natural Voice & De-AI-ing)

هوش مصنوعی نباید متنی مصنوعی، ترجمه‌ای یا خشک تولید کند. همواره اصول زیر را رعایت نمایید:

1. **پرهیز از فعل «می‌باشد»:** در ۹۵٪ مواقع از فعل ساده و روان «است»، «هست» یا افعال ترکیبی متناسب استفاده کنید (به جای «این روش مناسب می‌باشد»، بنویسید «این روش مناسب است»).
2. **حذف عبارات مقدمه‌چینی کلیشه‌ای:** کلماتی مانند «لازم به ذکر است»، «شایان ذکر است»، «در دنیای پرشتاب امروزی»، «همان‌طور که می‌دانید»، «به عنوان یک مدل زبانی» را حذف کرده و مستقیماً به سراغ اصل مطلب بروید.
3. **شکستن الگوهای سه‌گانه و لیست‌های تکراری:** مدل‌ها تمایل دارند برای هر مفهوم، سه ویژگی با پسوند «...، ... و ...» ذکر کنند. ساختار جملات را متنوع و زنده نگاه دارید.
4. **اصلاح حروف عربی به فارسی:** همیشه از «ی» و «ک» استاندارد فارسی (`ی` `ک`) به جای حروف عربی (`ي` `ك`) استفاده کنید.

---

## ۲. اصول خروجی در محیط‌های چت و ترمینال (Chat & CLI Output)

### ۲.۱. محیط‌های دارای پشتیبانی از HTML (وب، دسکتاپ و رابط‌های غنی)
* **کپسوله‌سازی کامل با کانتینر RTL:** کل خروجی را درون تگ زیر قرار دهید تا تقدم رندر به درستی اعمال شود:
  ```html
  <div dir="rtl" style="text-align: right; direction: rtl; font-family: 'Sahel', Tahoma, sans-serif;">
  ... متن و محتوا ...
  </div>
  ```
  *(نکته: قبل و بعد از تگ‌های HTML همیشه یک خط خالی بگذارید تا مفسر مارک‌داون مختل نشود).*

### ۲.۲. محیط‌های ترمینال خالص (CLI) یا ابزارهای فقط متنی (Pure Markdown)
* چنانچه پلتفرم تگ HTML را مستقیماً به صورت متن خام نمایش می‌دهد (مانند ترمینال‌های ساده)، از کپسوله‌سازی HTML خودداری کرده و با استفاده از کاراکترهای یونیکد استاندارد، علائم نگارشی فارسی و ایزوله‌سازی کلمات انگلیسی، خروجی را تمیز تحویل دهید.

### ۲.۳. تفکیک واژگان، متغیرها و تگ `<bdi>`:
* تمامی کلمات انگلیسی، توابع، کلمات کلیدی، دستورات، متغیرها و مسیرهای فایل حتماً داخل بک‌تیک (`` `example` ``) یا تگ‌های تفکیک جهت قرار گیرند:
  ```html
  <span class="en-font" dir="ltr">Network-to-Network Interface (NNI)</span>
  <!-- یا استفاده از برچسب ایزوله‌کننده دوجهته -->
  <bdi class="en-token">process_id</bdi>
  ```
* **شروع پاراگراف:** هرگز پاراگراف فارسی را با عدد انگلیسی، علامت نقل‌قول لاتین یا حروف انگلیسی شروع نکنید، زیرا جهت خط به‌صورت اشتباه چپ‌به‌چپ (LTR) تشخیص داده می‌شود.

### ۲.۴. نیم‌فاصله (Zero-Width Non-Joiner - ZWNJ) و علائم نگارشی:
* **افعال:** پیشوند «می» و «نمی» همیشه دارای نیم‌فاصله باشند («می‌شود»، «نمی‌تواند»).
* **واژگان مرکب و جمع‌ها:** «دست‌تکانی»، «پیاده‌سازی»، «به‌صورت»، «نرم‌افزار»، «گزارش‌ها»، «پایگاه‌داده‌ها».
* **علائم نگارشی فارسی:**
  * نقطه (.)، ویرگول فارسی (،)، نقطه‌ویرگول (؛) و علامت سؤال فارسی (؟) باید دقیقاً به واژه قبلی بچسبند و با واژه بعدی یک فاصله داشته باشند.
  * گیومه فارسی: به جای `"` از «...» استفاده شود.
  * ممیز اعداد: در نگارش ارقام فارسی، به جای ممیز انگلیسی (`.`) از ممیز استاندارد فارسی (`٫` U+066B) استفاده شود (مثلاً `۴٫۵` به جای `۴.۵`).

---

## ۳. استانداردهای صفحات وب (HTML)، طراحی فرانت‌اند و PDF

### ۳.۱. قوانین حیاتی CSS و تایپوگرافی فارسی (Front-end Rules):
1. **ممنوعیت مطلق `letter-spacing`:** هرگز روی متون فارسی خاصیت `letter-spacing` اعمال نکنید؛ این ویژگی اتصالات حروف الفبای فارسی را متلاشی و کلمات را تکه‌تکه می‌کند.
2. **جهت ورودی‌های حساس (`Input Fields`):** فیلدهایی نظیر شماره موبایل، کد ملی، شماره شبا، ایمیل، کلمه عبور و کد اعتبارسنجی حتماً باید دارای `dir="ltr"` باشند تا مکان‌نما حین تایپ دچار پرش نشود.
3. **خصیصه‌های منطقی در CSS (Logical Properties):**
   * استفاده از `margin-inline-start` به جای `margin-left`.
   * استفاده از `padding-inline-start` و `border-inline-start` برای خطوط راهنما.
   * در Tailwind CSS: استفاده از کلاس‌های `ms-*`, `me-*`, `ps-*`, `pe-*`.

### ۳.۲. اسکلت‌بندی استاندارد سند HTML با فونت‌های تحت وب (CDN Fallback):
```html
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>سند استاندارد فارسی</title>
    <!-- لود فونت Sahel از jsDelivr و Fira Code از گوگل‌فونتز جهت اجرای بدون نقص روی تمام سیستم‌ها -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v3.4.0/dist/font-face.css">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }
        body {
            direction: rtl;
            text-align: right;
            font-family: 'Sahel', Tahoma, sans-serif;
            /* ارقام فارسی در Sahel از نسخهٔ Sahel FD (dist/Farsi-Digits/) می‌آید، نه از ss01 */
            letter-spacing: normal !important; /* پیشگیری از متلاشی شدن حروف فارسی */
            line-height: 1.8;
            margin: 0;
            padding: 24px;
            color: #1e293b;
            background-color: #ffffff;
        }
        /* کلاس‌های تفکیک محتوای انگلیسی و کد */
        .en-font, [dir="ltr"] {
            direction: ltr;
            text-align: left;
            display: inline-block;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .code-font, code, pre {
            direction: ltr;
            text-align: left;
            font-family: 'Fira Code', 'Source Code Pro', Consolas, monospace;
            unicode-bidi: isolate;
        }
        /* استایل‌های بهینه‌سازی شده برای چاپ و PDF */
        @page {
            size: A4 portrait;
            margin: 12mm 15mm;
        }
    </style>
</head>
<body dir="rtl">
    <!-- محتوا -->
</body>
</html>
```

### ۳.۳. ساخت PDF با کروم هدلس (Cross-Platform Chrome Headless):
* **ویندوز (PowerShell):**
  ```powershell
  & "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"
  ```
* **مک (macOS):**
  ```bash
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"
  ```
* **لینوکس (Linux):**
  ```bash
  google-chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="output.pdf" "input.html"
  ```

---

## ۴. اسناد داده‌ای، فایل‌های آفیس و انکودینگ (Encoding & Office Files)

### ۴.۱. فایل‌های CSV و Excel:
* فایل‌های CSV حاوی حروف فارسی باید حتماً با انکودینگ **UTF-8 with BOM** (بایت اوردر مارک: `EF BB BF`) ذخیره شوند تا در اکسل مایکروسافت بدون کاراکترهای نامفهوم (Garbled / `????`) مستقیماً باز شوند:
  * در پایتون: `encoding='utf-8-sig'`
  * در جاوااسکریپت: درج کاراکتر `\uFEFF` در ابتدای رشته خروجی.

### ۴.۲. کامنت‌ها و مستندات سورس‌کد:
* انکودینگ تمام فایل‌های سورس پروژه شامل کامنت‌های فارسی باید روی **UTF-8** تنظیم شود.
* در کامنت‌های تک‌خطی، برای جلوگیری از پرش موقعیت علامت‌های پایانی یا کلمات فنی:
  ```python
  # بررسی وضعیت توکن و اعتبارسنجی پارامتر payload
  ```

---

## ۵. فرمول‌های ریاضی و علائم فرمول‌نویسی (LaTeX / KaTeX)

* فرمول‌های پیچیده ریاضی و فیزیک همواره بر روی خط مستقل (`$$...$$` یا `\[...\]`) درج شوند.
* در فرمول‌های درون‌متنی (`$...$`) از ترکیب حروف متصل فارسی با متغیرهای ریاضی در یک رشته خودداری شود تا جهت عملگرها معکوس نگردد.

---

## ۶. راهنمای نصب و راه‌اندازی این اسکیل روی پلتفرم‌های مختلف

| پلتفرم هوش مصنوعی | مسیر قرارگیری فایل یا نحوه تنظیم |
| :--- | :--- |
| **Google Antigravity** | در مسیر `~/.gemini/config/skills/persian-formatting/SKILL.md` یا پوشه `.agent/skills/` در مخزن |
| **Claude Code (Anthropic)** | در مسیر `.claude/skills/persian-formatting/SKILL.md` یا افزودن متن به `CLAUDE.md` در ریشه پروژه |
| **Cursor IDE** | ایجاد فایل `.cursor/rules/persian.mdc` یا افزودن به `.cursorrules` در ریشه پروژه |
| **Windsurf** | افزودن به فایل `.windsurfrules` در ریشه پروژه |
| **GitHub Copilot** | افزودن به `.github/copilot-instructions.md` در ریشه پروژه |
| **ChatGPT / Claude Web** | کپی متن بخش‌های ۱ تا ۴ در بخش **Custom Instructions** یا سیستم پرامپت پروژه |
