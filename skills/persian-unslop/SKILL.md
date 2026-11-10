---
name: persian-unslop
description: ویرایش ایمن متن فارسی برای حذف کلیشه‌های AI، ترجمه‌زدگی و حشو، با حفظ کامل واقعیت، citation، ساختار و صدای نویسنده.
---

# Persian unslop

این skill برای ویرایش نثر فارسی است، نه fact-checking، ترجمه، خلاصه‌سازی یا تولید محتوای جدید. متن را به نثر طبیعی‌تر، دقیق‌تر و مشخص‌تر تبدیل کن؛ اما اطلاعاتی به آن اضافه نکن.

## دامنه

برای این حالت‌ها استفاده کن و mode را انتخاب کن: `editorial` برای مقاله و newsletter؛ `product` برای landing، onboarding و UI copy؛ `social` برای post و thread؛ `technical` برای documentation و RFC؛ `literary` برای روایت، memoir و متن کتاب/صوت.

روی این موارد ویرایش نکن، مگر کاربر صریحاً اجازه دهد: code block و inline code، JSON/YAML/XML، command و path، log و stack trace، direct quote، متن حقوقی/قراردادی/رگولاتوری، دوز پزشکی، متن مذهبی/آیینی، نام خاص و brand، translation key، metadata و UI labelهایی که باید دقیق بمانند. این بخش‌ها را flag کن، نه rewrite.

## قرارداد حفظ متن

این موارد باید character-for-character یا از نظر معنایی دقیقاً حفظ شوند:

- facts، ادعاها، degree of certainty، caveatها و causal claims؛
- citation، footnote، attribution و جای اتصال آن‌ها به claim؛
- URL، نام، brand، title، version، number، date، percentage، currency، unit و range؛
- quote و quote mark؛
- ساختار Markdown شامل heading، list، table، link، emphasis و footnote؛
- HTML tag، attribute، ترتیب، `dir="rtl"`، `lang="fa"`، `dir="ltr"` و bidi mark؛
- code در هر جای متن.

هرگز opinion، تجربه، source، metric، مثال، احساس، علت یا hedge جدید نساز. ادعا را نه قوی‌تر و نه ضعیف‌تر نکن. digit فارسی و لاتین را تبدیل نکن. citation را جابه‌جا نکن. اگر بهبود جمله به اطلاعات جدید نیاز دارد، آن را انجام نده.

## workflow

1. **Freeze:** protected spans را علامت‌گذاری کن.
2. **Mode:** mode را از context انتخاب کن. اگر انتخاب آن نتیجه را materially تغییر می‌دهد، سؤال بپرس.
3. **Content pass:** مقدمه‌های اعلامی، تکرار، filler، hype و جمله‌های بی‌اطلاعات را حذف کن.
4. **Syntax pass:** ترجمه‌زدگی، light-verb بَی‌جا، noun stacking، passive غیرضروری و register مصنوعی را اصلاح کن.
5. **Typography pass:** نیم‌فاصله، فاصله و punctuation فارسی را جداگانه اصلاح کن.
6. **Contract diff:** عدد، نام، تاریخ، URL، citation، quote، tag و code را با ورودی تطبیق بده.
7. **Return:** متن نهایی را بده و حداکثر سه خط درباره‌ی mode و تغییرات مهم بنویس. اگر تغییر لازم نیست، بگو «بدون تغییر لازم».

## modeها

- **Editorial:** حشو و مقدمه/نتیجه‌ی قالبی را حذف کن؛ paragraph را روشن و کوتاه کن. ادیت سنگین فقط وقتی claimها آسیب نمی‌بینند.
- **Product:** direct و action-oriented باش. `می‌توانید`، `امکان انجام عملیات` و phraseهای اداری را کم کن. label دکمه، menu و error diagnostic را عیناً نگه دار.
- **Social:** announcement scaffolding، hype و emoji تزئینی را کم کن؛ handle، hashtag، link و length constraint را حفظ کن.
- **Technical:** precision مقدم است. qualifierهایی مثل «معمولاً»، «ممکن است» و «به‌جز» حذف نشوند. فقط narration اطراف code را کم کن.
- **Literary:** کمترین مداخله. تکرار، ریتم، لحن، باستان‌گرایی و word order غیرمعمول ممکن است عمدی باشند. در تردید، دست نزن.

## فارسی و typography

- نیم‌فاصله‌ی واقعی `U+200C` را در `می‌رود`، `نمی‌شود`، `کتاب‌ها`، `بزرگ‌تر` و `مهم‌ترین` رعایت کن؛ کلمات ذاتاً پیوسته را جدا نکن.
- در نثر فارسی از `،`، `؛`، `؟` و `«»` استفاده کن؛ قبل از punctuation فاصله نگذار و بعد از آن یک فاصله بگذار، مگر در protected span.
- فاصله‌ی دوگانه و whitespace انتهایی را حذف کن؛ paragraph و heading را merge یا split نکن.
- tokenهای لاتین مثل `API`، `React`، `v2.1` و `PostgreSQL 16` را reorder یا ترجمه نکن. شکل موجود را حفظ و در کل متن consistent کن؛ consistency مجوز اضافه‌کردن gloss نیست.
- em dash، colon، semicolon، parentheses، bold، list و rule-of-three ممنوع نیستند. فقط وقتی تکراری، تزئینی یا بی‌نقش‌اند کم‌شان کن.

## ترجمه‌زدگی و کلیشه‌های فارسی

در صورت بی‌نقش‌بودن، این الگوها را به نثر مستقیم تبدیل کن: «در دنیای امروز»، «در این مقاله قصد داریم»، «شایان ذکر است»، «لازم به ذکر است»، «با توجه به اهمیت موضوع»، «به منظور»، «بر روی»، «می‌باشد»، «می‌گردد»، «یکی از بهترین راه‌ها برای»، «این امکان را فراهم می‌کند»، «به شما اجازه می‌دهد»، «عملیات ... را انجام دهید»، «در نهایت» به‌عنوان filler، «جامع و کامل»، «کاربردی و مفید»، «گامی رو به جلو»، «سفری هیجان‌انگیز»، «امیدواریم این مطلب برایتان مفید بوده باشد».

Phrase را صرفاً به‌خاطر حضور در فهرست حذف نکن. اگر حذف آن اطلاعاتی را حذف می‌کند، جمله را نگه دار. «کلیدی»، «مهم» و زبان رسمی همیشه slop نیستند؛ context تعیین‌کننده است.

## stop conditions

توقف کن و متن را دست‌نخورده یا partially edited برگردان اگر rewrite به fact/source/opinion جدید نیاز دارد؛ protected span تغییر می‌کند؛ متن quote یا exact legal/technical است؛ register رسمی عمدی است؛ متن human و clean است؛ یا با حذف بیش از حدود نیمی از متن editorial احتمال ازبین‌رفتن support یک claim وجود دارد. در این موارد دلیل را کوتاه بگو و حدس نزن.

## checklist

- [ ] عدد، تاریخ، unit، range، نام، URL و citation با ورودی تطبیق دارد.
- [ ] هیچ ادعای جدیدی، causal link جدیدی یا تغییر certainty ایجاد نشده است.
- [ ] quote، code، tag، attribute، Markdown و `dir="rtl"`/`lang="fa"` دست‌نخورده‌اند.
- [ ] UI label و technical term ترجمه یا تغییر نکرده است.
- [ ] نیم‌فاصله و punctuation فارسی درست است.
- [ ] هیچ punctuation صرفاً به‌صورت blanket حذف نشده است.
- [ ] mode مناسب بوده و صدای متن، مخصوصاً در literary، حفظ شده است.

## مثال

قبل: «در دنیای پرشتاب امروز، بدون شک هوش مصنوعی یکی از کلیدی‌ترین فناوری‌هایی می‌باشد که می‌تواند به شما کمک کند تا کسب‌وکار خود را متحول نمایید. طبق گزارش [مک‌کینزی، ۲۰۲۴](https://example.com)، ۴۰٪ شرکت‌ها از آن استفاده می‌کنند.»

بعد: «طبق گزارش [مک‌کینزی، ۲۰۲۴](https://example.com)، ۴۰٪ شرکت‌ها از هوش مصنوعی استفاده می‌کنند.»

عدد، source و URL حفظ شده‌اند؛ فقط قاب خالی و ادعاهای تزئینی حذف شده‌اند.

قبل: «شب بود. شب بود و باد می وزید. بدون شک، سکوتی بی‌نظیر همه‌جا را فرا گرفته بود.»

بعد: «شب بود. شب بود و باد می‌وزید. سکوت همه‌جا را گرفته بود.»

تکرار روایی حفظ شده، اما cliché، adjective خالی و فاصله‌ی غلط اصلاح شده است.
