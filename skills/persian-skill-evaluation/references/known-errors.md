# Known errors in Persian skills

Wrong claims that showed up in real Persian skills, with the correct fact and
its source. Check every skill under review against this list.

| Wrong claim | Correct | Source |
|---|---|---|
| Tajik or Dari have no CLDR plural rule, or use `other` only | fa, fa-AF and tg all use `one` (0 and 1) and `other` | CLDR `supplemental/plurals.xml` |
| «رییس، ارایه، جزیی، قرایت» are acceptable | Completely wrong; write «رئیس، ارائه، جزئی، قرائت» | Academy, «دستور خطّ فارسی», p. 42, footnote |
| «مسأله، هیأت، جرأت» are standard | «مسئله، هیئت، جرئت» | Academy, pp. 49–50 |
| ZWNJ is needed after every word before a suffix | After a non-joining letter (ا د ذ ر ز ژ و) nothing is needed | Academy, p. 23 |
| «-ها» must always be separate | Joined or separate are both allowed; separate is recommended, and required in six cases | Academy, pp. 40–41 |
| The ezafe after silent ه is «ه‌ی» by rule | The Academy prescribes «هٔ»; «ه‌ی» is a house-style choice | Academy, p. 47 |
| «اینکه» is always «این‌که» | Joined as the conjunction; ZWNJ only for "this person who" | Academy, pp. 34–35 |
| Afghanistan's weekend is Friday | Thursday and Friday | CLDR `supplementalData.xml` |
| Afghan solar months are فروردین… | حمل، ثور، جوزا … حوت | CLDR `fa_AF.xml` |
| Afghan Gregorian months are ژانویه، فوریه… | جنوری، فبروری، مارچ … | CLDR `fa_AF.xml` |
| Tajik uses Persian script | Cyrillic, with ғ ӣ қ ӯ ҳ ҷ | CLDR `tg.xml` |
| Sahel's variable font covers 300–900 and Latin | `Sahel-VF` is weight 400–900 with no Latin; the static TTFs have 300–900 and Latin | Measured in the Sahel v3.4.0 files |
| Sahel is on Google Fonts | It isn't; load it from jsDelivr or self-host | github.com/rastikerdar/sahel-font |
| Vazirmatn's `ss01` gives Persian digits in any font | That feature is Vazirmatn's; Sahel uses its FD build for Persian digits | Font documentation |
| Iran's timezone has daylight saving time | Iran Standard Time is UTC+03:30 with no DST since 2022 | IANA tz database |
| «طرح» is the word for a pricing plan | Reads as "design" or "project"; product copy uses «اشتراک» | Native review, `persian-localization` |
| «اشتباه‌ها را می‌گیرد» for "catches mistakes" | «اشتباه‌ها را پیدا می‌کند» | Native review, `persian-localization` |

When you find a new recurring error, add a row with its source.
