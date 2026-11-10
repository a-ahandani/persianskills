---
name: shadcn-persian
description: Comprehensive guide for building React, Next.js, and Vite UIs using shadcn/ui and PersianLabs/ui (shadcn-persian) with RTL-first Persian components, Jalali calendar/date-pickers, Iranian bank card & IBAN inputs, national ID validation, price inputs with live Toman words, Iranian city/map selectors, plate inputs, and offline source code. Enforces CLI installation (npx shadcn@latest add @persianlabsui/<name>) with offline source fallback.
---

# PersianLabs/ui & shadcn/ui Complete Persian Integration Guide

A unified, production-grade guide for building accessible, RTL-first web interfaces in **React, Next.js, Vite, Tailwind CSS (v3 & v4), and shadcn/ui**, with native support for Iranian and Persian UI patterns.

---

## ⛔ Core Operating Principles

1. **NEVER BUILD CUSTOM IMPLEMENTATIONS FROM SCRATCH**:  
   When any UI component is needed (Jalali date picker, bank card input, national code input, city selector, modal, table, etc.), **NEVER invent new components manually**. Use the pre-built PersianLabs/ui & shadcn registry components.

2. **ALWAYS INSTALL VIA TERMINAL CLI COMMAND FIRST**:  
   Execute the official registry command inside your frontend directory:
   ```bash
   npx shadcn@latest add @persianlabsui/<component-name>
   ```
   *(For standard base components: `npx shadcn@latest add <component-name>`)*

3. **OFFLINE FALLBACK**:  
   If CLI installation fails (e.g. offline/network restrictions), copy the exact pre-downloaded source code from the skill directory:
   - Components: `source-code/components/<component-name>.tsx` → `src/components/ui/<component-name>.tsx`
   - Hooks: `source-code/hooks/<hook-name>.ts` → `src/hooks/<hook-name>.ts`
   - Lib Utilities: `source-code/lib/<util-name>.ts` → `src/lib/<util-name>.ts`

4. **CONSULT LOCAL OFFLINE DOCS & EXAMPLES**:  
   Inspect the local markdown documentation in `components/`, `utilities/`, `getting-started/`, and `rules/` before coding to get exact props, TypeScript interfaces, Zod schemas, and examples.

---

## 📁 Skill Directory Hierarchy

```text
shadcn-persian/
├── SKILL.md                  # Master roadmap & cheat-sheet (< 500 lines)
├── README.md                 # Full Persian catalog and documentation index
├── getting-started/          # 9 Core architectural guides
│   ├── introduction.md       # PersianLabs UI overview
│   ├── installation.md       # Setup for Next.js, Vite, and Monorepos
│   ├── theming.md            # HSL & OKLCH CSS variables, Dark mode
│   ├── rtl.md                # RTL layout rules, logical properties (start/end)
│   ├── fonts.md              # Sahel, Estedad, local & web fonts
│   ├── persian-conventions.md# Persian UI conventions, digits, dates, currency
│   ├── cli.md                # CLI options, presets, registry commands
│   ├── ai.md                 # Prompting & agent workflows
│   └── icons.md              # @persianlabs/icons (820+ Iranian logos)
├── rules/                    # 6 Modern shadcn v4 composition rules
│   ├── styling.md            # Tailwind rules: use gap instead of space-x/y, size-*, etc.
│   ├── forms.md              # Form layout with FieldGroup + Field + InputGroup
│   ├── composition.md        # Slot/asChild, Title requirements, Grouping
│   ├── icons.md              # data-icon usage and sizing
│   ├── chat.md               # Chat primitives (MessageScroller, Bubble, Attachment)
│   └── base-vs-radix.md      # Base UI vs Radix UI conventions
├── components/               # 89 Component documentation files with props & examples
├── utilities/                # 20 Iranian utility & algorithm docs (Zod, checksums, etc.)
├── source-code/              # 131 Complete offline TypeScript source files
│   ├── components/*.tsx      # 87 component source codes
│   ├── hooks/*.ts            # 13 hook source codes
│   ├── lib/*.ts              # 29 lib utility algorithms
│   └── styles/globals.css    # Full theme tokens & CSS variables
├── registry-json/            # 106 official shadcn registry item JSONs
└── examples/                 # 482 ready-to-use TypeScript demo examples
```

---

## 🇮🇷 Iranian & Persian Components Quick Reference

| Feature | Component / Utility | Local Doc Path | Terminal CLI Command |
| :--- | :--- | :--- | :--- |
| **کارت بانکی و شبا** | `BankInput`, `CardNumberInput`, `ShabaInput` | `components/bank-input.md` | `npx shadcn@latest add @persianlabsui/bank-input` |
| **کد ملی با اعتبارسنجی** | `NationalIdInput`, `isValidNationalId` | `components/national-id-input.md` | `npx shadcn@latest add @persianlabsui/national-id-input` |
| **شماره موبایل ایران** | `MobileNumberInput` | `components/mobile-number-input.md` | `npx shadcn@latest add @persianlabsui/mobile-number-input` |
| **پلاک ملی خودرو** | `PlateInput` | `components/plate-input.md` | `npx shadcn@latest add @persianlabsui/plate-input` |
| **انتخاب استان و شهر** | `CitySelector` | `components/city-selector.md` | `npx shadcn@latest add @persianlabsui/city-selector` |
| **نقشه تعاملی ایران** | `IranMapPicker` | `components/iran-map-picker.md` | `npx shadcn@latest add @persianlabsui/iran-map-picker` |
| **تقویم شمسی** | `Calendar` | `components/calendar.md` | `npx shadcn@latest add @persianlabsui/calendar` |
| **دیتپیکر شمسی** | `DatePicker` | `components/date-picker.md` | `npx shadcn@latest add @persianlabsui/date-picker` |
| **دیتپیکر چرخشی موبایل** | `DateWheelPicker`, `WheelPicker` | `components/date-wheel-picker.md` | `npx shadcn@latest add @persianlabsui/date-wheel-picker` |
| **تایمپیکر فارسی** | `TimePicker`, `DurationPicker` | `components/time-picker.md` | `npx shadcn@latest add @persianlabsui/time-picker` |
| **ورودی مبلغ با حروف** | `PriceInput` | `components/price-input.md` | `npx shadcn@latest add @persianlabsui/price-input` |
| **نماد رسمی تومان** | `TomanIcon` | `components/toman-icon.md` | `npx shadcn@latest add @persianlabsui/toman-icon` |
| **چاپ فاکتور و رسید** | `ReceiptPrinter` | `components/receipt-printer.md` | `npx shadcn@latest add @persianlabsui/receipt-printer` |
| **لوگوهای بانکی و برندها** | `@persianlabs/icons` (820+ لوگو) | `getting-started/icons.md` | `npm install @persianlabs/icons` |
| **ورودی رمز عبور فارسی** | `PasswordInput` | `components/password-input.md` | `npx shadcn@latest add @persianlabsui/password-input` |
| **ورودی کد تایید OTP** | `InputOtp`, `useCountdown` | `components/input-otp.md` | `npx shadcn@latest add @persianlabsui/input-otp` |
| **چت و پیامرسان** | `MessageScroller`, `Message`, `Bubble` | `components/message-scroller.md` | `npx shadcn@latest add @persianlabsui/message-scroller` |

---

## 🧮 Iranian Utilities & Algorithmic Helpers

| Utility | Description | Local Doc | CLI Command / Import |
| :--- | :--- | :--- | :--- |
| `national-id` | فرمول اعتبارسنجی چکسام کد ملی ۱۰ رقمی | `utilities/national-id.md` | `npx shadcn@latest add @persianlabsui/national-id` |
| `iranian-bank` | تشخیص نام و لوگوی بانک از پیششماره کارت و شبا | `utilities/iranian-bank.md` | `npx shadcn@latest add @persianlabsui/iranian-bank` |
| `normalize-persian-digits` | تبدیل اعداد فارسی/عربی به انگلیسی و برعکس | `utilities/normalize-persian-digits.md` | `npx shadcn@latest add @persianlabsui/normalize-persian-digits` |
| `normalize-persian-text` | استانداردسازی حروف ی، ک و نیمفاصلهها | `utilities/normalize-persian-text.md` | `npx shadcn@latest add @persianlabsui/normalize-persian-text` |
| `number-to-persian-words` | تبدیل عدد و مبالغ به حروف فارسی (تومان/ریال) | `utilities/number-to-persian-words.md` | `npx shadcn@latest add @persianlabsui/number-to-persian-words` |
| `persian-date` | تبدیل و قالببندی تاریخهای شمسی / میلادی | `utilities/persian-date.md` | `npx shadcn@latest add @persianlabsui/persian-date` |
| `persian-date-zod` | اعتبارسنجی تاریخ شمسی در اسکیماهای Zod | `utilities/persian-date-zod.md` | `npx shadcn@latest add @persianlabsui/persian-date-zod` |
| `persian-holidays` | بررسی تعطیلات رسمی تقویم ایران | `utilities/persian-holidays.md` | `npx shadcn@latest add @persianlabsui/persian-holidays` |
| `postal-code` | اعتبارسنجی کد پستی ۱۰ رقمی ایران | `utilities/postal-code.md` | `npx shadcn@latest add @persianlabsui/postal-code` |
| `use-countdown` | هوک تایمر شمارش معکوس ارسال مجدد پیامک OTP | `utilities/use-countdown.md` | `npx shadcn@latest add @persianlabsui/use-countdown` |

---

## 🎨 RTL Layout & Typography Best Practices

1. **جهتگیری سند (`dir="rtl"`)**:
   در فایل ریشه (`app/layout.tsx` یا `index.html`):
   ```tsx
   <html lang="fa" dir="rtl">
   ```
2. **پرهیز از ویژگیهای جهتدار فیزیکی (`left`/`right`)**:
   - به جای `pl-*` یا `pr-*` از کلاسهای منطقی استفاده کنید: `ps-*` (padding-inline-start) و `pe-*` (padding-inline-end) یا `gap-*` در Flex/Grid.
   - به جای `space-x-*` همیشه از `flex gap-*` استفاده کنید تا در RTL برعکس نشود.
   - به جای `text-left` / `text-right` از `text-start` / `text-end` استفاده کنید.
3. **فونتهای فارسی**:
   - فونت پیشنهادی: `Sahel` (جایگزین: `Estedad`).
   - اعداد فارسی در Sahel از نسخهٔ `Sahel FD` می‌آیند، نه از `font-feature-settings: "ss01"`.
4. **تراز فیلدهای شماره کارت و شبا**:
   - فیلدهای کارت بانکی و شبا ماهیت عددی دارند و باید با `dir="ltr"` و `text-start` یا `text-center` نمایش داده شوند تا خوانایی ارقام حفظ شود. کامپوننتهای `@persianlabsui/bank-input` این را به صورت خودکار مدیریت میکنند.

---

## 📝 Example: Complete Form with Persian Validation

```tsx
"use client"

import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import { isValidNationalId } from "@/lib/national-id"
import { isValidCardNumber } from "@/lib/iranian-bank"
import { FieldGroup, Field, FieldLabel, FieldError } from "@/components/ui/field"
import { NationalIdInput } from "@/components/ui/national-id-input"
import { CardNumberInput } from "@/components/ui/bank-input"
import { DatePicker } from "@/components/ui/date-picker"
import { PriceInput } from "@/components/ui/price-input"
import { Button } from "@/components/ui/button"

const formSchema = z.object({
  nationalCode: z.string().refine(isValidNationalId, {
    message: "کد ملی وارد شده نامعتبر است",
  }),
  cardNumber: z.string().refine(isValidCardNumber, {
    message: "شماره کارت بانکی نامعتبر است",
  }),
  birthDate: z.date({
    required_error: "انتخاب تاریخ تولد الزامی است",
  }),
  amount: z.number().min(10000, "حداقل مبلغ ۱۰,۰۰۰ تومان است"),
})

export function PaymentForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
  })

  return (
    <form onSubmit={form.handleSubmit(console.log)} className="space-y-4">
      <FieldGroup>
        <Field data-invalid={!!form.formState.errors.nationalCode}>
          <FieldLabel>کد ملی</FieldLabel>
          <NationalIdInput {...form.register("nationalCode")} />
          <FieldError>{form.formState.errors.nationalCode?.message}</FieldError>
        </Field>

        <Field data-invalid={!!form.formState.errors.cardNumber}>
          <FieldLabel>شماره کارت بانکی</FieldLabel>
          <CardNumberInput {...form.register("cardNumber")} />
          <FieldError>{form.formState.errors.cardNumber?.message}</FieldError>
        </Field>

        <Field>
          <FieldLabel>تاریخ تولد (شمسی)</FieldLabel>
          <DatePicker onChange={(date) => form.setValue("birthDate", date)} />
        </Field>

        <Field data-invalid={!!form.formState.errors.amount}>
          <FieldLabel>مبلغ پرداختی (تومان)</FieldLabel>
          <PriceInput onChange={(val) => form.setValue("amount", val)} />
          <FieldError>{form.formState.errors.amount?.message}</FieldError>
        </Field>
      </FieldGroup>

      <Button type="submit" className="w-full">تایید و ادامه</Button>
    </form>
  )
}
```

---

## 🔍 How to Read Offline Resources

- برای مطالعه داکیومنت دقیق یک کامپوننت: `read_file(path="components/<name>.md")`
- برای کپی سورس کامپوننت به صورت آفلاین: `read_file(path="source-code/components/<name>.tsx")`
- برای مشاهده دموها و مثالهای آماده: `search_files(path="examples", pattern="<name>*")`
- برای خواندن اصول دیزاین و قوانین شادسن: `read_file(path="rules/<rule-name>.md")`
