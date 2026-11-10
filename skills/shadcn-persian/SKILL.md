---
name: shadcn-persian
description: >-
  Builds React, Next.js and Vite interfaces with shadcn/ui and PersianLabs/ui
  (shadcn-persian): RTL-first Persian components, Jalali calendars and date
  pickers, Iranian bank card and IBAN (Sheba) inputs, national ID
  validation, price inputs that spell the amount in Toman, Iranian province,
  city and map selectors, plate inputs, and bundled offline source code.
  Installs components with the registry CLI (npx shadcn@latest add
  @persianlabsui/<name>) and falls back to the bundled source when offline.
  Use when building or reviewing a Persian or Iranian web UI with shadcn/ui
  or Tailwind, or when the user mentions PersianLabs, shadcn-persian,
  «تقویم شمسی», «تاریخ شمسی», «کد ملی», «شماره کارت» or «شبا».
license: MIT
compatibility: Node.js with the shadcn CLI; the registry install needs network access, the bundled source does not.
metadata:
  author: Abulfadl Ahmadi
  source: https://github.com/Abulfadl-Ahmadi/shadcn-persian
  upstream-commit: ac1d0c8
  changes: Default Persian font changed from Vazirmatn to Sahel (Farsi digits from the Sahel FD build), and SKILL.md translated from Persian to English with emoji removed and the folder map corrected.
---

# PersianLabs/ui and shadcn/ui for Persian interfaces

Builds accessible, RTL-first web interfaces in React, Next.js, Vite, Tailwind
CSS (v3 and v4) and shadcn/ui, with native support for Iranian and Persian UI
patterns. For the rules behind these components, see `persian-rtl-ui`,
`iran-validation` and `jalali-calendar`.

## Core rules

1. **Do not build custom implementations from scratch.** When a UI component
   is needed (Jalali date picker, bank card input, national ID input, city
   selector, modal, table and so on), use the prebuilt PersianLabs/ui and
   shadcn registry components instead of writing new ones by hand.

2. **Install through the CLI first.** Run the registry command in the
   frontend directory:
   ```bash
   npx shadcn@latest add @persianlabsui/<component-name>
   ```
   For standard base components: `npx shadcn@latest add <component-name>`.

3. **Fall back to the bundled source.** If the CLI install fails (offline or
   network restrictions), copy the exact source from this skill's folder:
   - Components: `source-code/components/<component-name>.tsx` → `src/components/ui/<component-name>.tsx`
   - Hooks: `source-code/hooks/<hook-name>.ts` → `src/hooks/<hook-name>.ts`
   - Lib utilities: `source-code/lib/<util-name>.ts` → `src/lib/<util-name>.ts`

4. **Read the local docs and examples before coding.** The markdown files in
   `components/`, `utilities/`, `getting-started/` and `rules/` give the exact
   props, TypeScript interfaces, Zod schemas and examples.

## Folder layout

```text
shadcn-persian/
├── SKILL.md                  # This guide
├── README.md                 # Upstream README (Persian): install notes and the same catalog
├── getting-started/          # 9 core guides
│   ├── introduction.md       # PersianLabs UI overview
│   ├── installation.md       # Setup for Next.js, Vite and monorepos
│   ├── theming.md            # HSL and OKLCH CSS variables, dark mode
│   ├── rtl.md                # RTL layout rules, logical properties (start/end)
│   ├── fonts.md              # Sahel, Estedad, local and web fonts
│   ├── persian-conventions.md# Persian UI conventions: digits, dates, currency
│   ├── cli.md                # CLI options, presets, registry commands
│   ├── ai.md                 # Prompting and agent workflows
│   └── faq.md                # Common questions and troubleshooting
├── rules/                    # 6 shadcn v4 composition rules
│   ├── styling.md            # Tailwind rules: gap instead of space-x/y, size-*, etc.
│   ├── forms.md              # Form layout with FieldGroup + Field + InputGroup
│   ├── composition.md        # Slot/asChild, Title requirements, grouping
│   ├── icons.md              # data-icon usage and sizing
│   ├── chat.md               # Chat primitives (MessageScroller, Bubble, Attachment)
│   └── base-vs-radix.md      # Base UI vs Radix UI conventions
├── components/               # 89 component docs with props and examples
├── utilities/                # 20 docs for Iranian utilities and algorithms (Zod, checksums, etc.)
├── source-code/              # Offline TypeScript source
│   ├── components/*.tsx      # 86 components
│   ├── hooks/*.ts            # 12 hooks
│   ├── lib/*.ts              # 28 lib utilities and algorithms
│   ├── types/*.d.ts          # Type declarations
│   └── styles/globals.css    # Full theme tokens and CSS variables
├── registry-json/            # 106 shadcn registry item JSONs
└── examples/                 # 482 ready-to-use TypeScript demos
```

## Iranian and Persian components

| Feature | Component / utility | Local doc | CLI command |
| :--- | :--- | :--- | :--- |
| **Bank card and Sheba (IBAN)** | `BankInput`, `CardNumberInput`, `ShabaInput` | `components/bank-input.md` | `npx shadcn@latest add @persianlabsui/bank-input` |
| **National ID (کد ملی) with validation** | `NationalIdInput`, `isValidNationalId` | `components/national-id-input.md` | `npx shadcn@latest add @persianlabsui/national-id-input` |
| **Iranian mobile number** | `MobileNumberInput` | `components/mobile-number-input.md` | `npx shadcn@latest add @persianlabsui/mobile-number-input` |
| **National vehicle plate (پلاک)** | `PlateInput` | `components/plate-input.md` | `npx shadcn@latest add @persianlabsui/plate-input` |
| **Province and city picker** | `CitySelector` | `components/city-selector.md` | `npx shadcn@latest add @persianlabsui/city-selector` |
| **Interactive Iran map** | `IranMapPicker` | `components/iran-map-picker.md` | `npx shadcn@latest add @persianlabsui/iran-map-picker` |
| **Jalali calendar** | `Calendar` | `components/calendar.md` | `npx shadcn@latest add @persianlabsui/calendar` |
| **Jalali date picker** | `DatePicker` | `components/date-picker.md` | `npx shadcn@latest add @persianlabsui/date-picker` |
| **Mobile wheel date picker** | `DateWheelPicker`, `WheelPicker` | `components/date-wheel-picker.md` | `npx shadcn@latest add @persianlabsui/date-wheel-picker` |
| **Persian time picker** | `TimePicker`, `DurationPicker` | `components/time-picker.md` | `npx shadcn@latest add @persianlabsui/time-picker` |
| **Amount input with the amount in words** | `PriceInput` | `components/price-input.md` | `npx shadcn@latest add @persianlabsui/price-input` |
| **Official Toman symbol** | `TomanIcon` | `components/toman-icon.md` | `npx shadcn@latest add @persianlabsui/toman-icon` |
| **Invoice and receipt printing** | `ReceiptPrinter` | `components/receipt-printer.md` | `npx shadcn@latest add @persianlabsui/receipt-printer` |
| **Bank and brand logos** | `@persianlabs/icons` (820+ logos) | Not bundled | `npm install @persianlabs/icons` |
| **Persian password input** | `PasswordInput` | `components/password-input.md` | `npx shadcn@latest add @persianlabsui/password-input` |
| **OTP verification code input** | `InputOtp`, `useCountdown` | `components/input-otp.md` | `npx shadcn@latest add @persianlabsui/input-otp` |
| **Chat and messaging** | `MessageScroller`, `Message`, `Bubble` | `components/message-scroller.md` | `npx shadcn@latest add @persianlabsui/message-scroller` |

## Iranian utilities and algorithms

| Utility | Description | Local doc | CLI command |
| :--- | :--- | :--- | :--- |
| `national-id` | Checksum validation for the 10-digit national ID | `utilities/national-id.md` | `npx shadcn@latest add @persianlabsui/national-id` |
| `iranian-bank` | Detects the bank name and logo from the card prefix and the Sheba number | `utilities/iranian-bank.md` | `npx shadcn@latest add @persianlabsui/iranian-bank` |
| `normalize-persian-digits` | Converts Persian and Arabic digits to Latin and back | `utilities/normalize-persian-digits.md` | `npx shadcn@latest add @persianlabsui/normalize-persian-digits` |
| `normalize-persian-text` | Normalizes ی, ک and ZWNJ (نیم‌فاصله) | `utilities/normalize-persian-text.md` | `npx shadcn@latest add @persianlabsui/normalize-persian-text` |
| `number-to-persian-words` | Spells numbers and amounts in Persian words (Toman/Rial) | `utilities/number-to-persian-words.md` | `npx shadcn@latest add @persianlabsui/number-to-persian-words` |
| `persian-date` | Converts and formats Jalali and Gregorian dates | `utilities/persian-date.md` | `npx shadcn@latest add @persianlabsui/persian-date` |
| `persian-date-zod` | Validates Jalali dates in Zod schemas | `utilities/persian-date-zod.md` | `npx shadcn@latest add @persianlabsui/persian-date-zod` |
| `persian-holidays` | Checks official Iranian calendar holidays | `utilities/persian-holidays.md` | `npx shadcn@latest add @persianlabsui/persian-holidays` |
| `postal-code` | Validates the 10-digit Iranian postal code | `utilities/postal-code.md` | `npx shadcn@latest add @persianlabsui/postal-code` |
| `use-countdown` | Countdown hook for the OTP SMS resend timer | `utilities/use-countdown.md` | `npx shadcn@latest add @persianlabsui/use-countdown` |

## RTL layout and typography

1. **Document direction (`dir="rtl"`).** Set it in the root file
   (`app/layout.tsx` or `index.html`):
   ```tsx
   <html lang="fa" dir="rtl">
   ```
2. **Avoid physical direction properties (`left`/`right`).**
   - Instead of `pl-*` or `pr-*`, use logical classes: `ps-*`
     (padding-inline-start) and `pe-*` (padding-inline-end), or `gap-*` in
     flex and grid.
   - Instead of `space-x-*`, always use `flex gap-*` so spacing does not flip
     in RTL.
   - Instead of `text-left` / `text-right`, use `text-start` / `text-end`.
3. **Persian fonts.**
   - Recommended font: `Sahel` (alternative: `Estedad`).
   - Persian digits in Sahel come from the `Sahel FD` build, not from
     `font-feature-settings: "ss01"`.
4. **Card number and Sheba field alignment.** Bank card and Sheba fields are
   numeric: show them with `dir="ltr"` and `text-start` or `text-center` so
   the digits stay readable. The `@persianlabsui/bank-input` components do
   this automatically.

## Example: complete form with Persian validation

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

## Reading the offline resources

- Exact docs for a component: read `components/<name>.md`.
- Offline source for a component: read `source-code/components/<name>.tsx`.
- Ready demos and examples: search `examples/` for `<name>*`.
- shadcn design principles and rules: read `rules/<rule-name>.md`.
