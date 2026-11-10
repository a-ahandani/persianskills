# Persian unslop

این skill با الهام از [Cursor pstack `unslop`](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop) و با بازطراحی فارسی/ایمن برای نثر فارسی ساخته شده است. طراحی آن با Claude Opus بررسی شده و برای محتوای Goosh Bede، editorial/product copy، social، landing pages، newsletters، documentation و متن‌های ادبی تنظیم شده است.

## چرا نسخه‌ی فارسی جدا لازم است؟

نسخه‌ی انگلیسی روی واژه‌های کلیشه‌ای انگلیسی و الگوهای prose انگلیسی تمرکز دارد. در فارسی، مشکلات پرتکرار دیگری وجود دارند: ترجمه‌زدگی، نیم‌فاصله، register اداری، جمله‌های light-verb، مرز فارسی/لاتین و کلیشه‌های محتوای AI.

## تفاوت‌های مهم با upstream

- scope مشخص دارد و به‌صورت خودکار روی همه‌چیز اعمال نمی‌شود.
- punctuation ممنوع نشده؛ فقط استفاده‌ی بی‌نقش کم می‌شود.
- preservation contract برای numbers، citations، URLs، quotes، Markdown، HTML و RTL دارد.
- mode ادبی با مداخله‌ی حداقلی دارد تا صدای روایت و audiobook خراب نشود.
- agent حق ساختن opinion، fact، source، example یا احساس جدید ندارد.
- mode فنی qualifierها و technical terms را حفظ می‌کند.

## استفاده

فقط وقتی فعال شود که کاربر صریحاً بخواهد متن prose ویرایش، naturalize، humanize یا unslop شود. ترتیب امن کار: freeze protected spans، ویرایش محتوا، syntax، typography، سپس contract diff و checklist.

این skill fact-checker یا detector علمی AI نیست. تشخیص کلیشه heuristic است و باید با context و صدای نویسنده سنجیده شود. متن حقوقی، medical، نقل‌قول مستقیم و code باید خارج از rewrite بماند مگر کاربر مجوز دقیق بدهد.
