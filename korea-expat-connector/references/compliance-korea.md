# Korean Compliance Guardrails

**This isn't legal advice.** It flags the known risk areas so the user can confirm with a professional before charging money. Claude should raise the relevant item every time an offer, price, or partner deal touches it, and recommend confirming with a lawyer (변호사), licensed agent (공인중개사), tax accountant (세무사), or administrative agent (행정사). Laws change, so verify current rules.

## 1. Real-Estate Brokerage (highest risk)

- Under the Licensed Real Estate Agents Act (공인중개사법), brokering real-estate transactions (sale, 전세, 월세 leases) **for a fee** is restricted to registered licensed agents. Unlicensed brokerage for compensation carries criminal penalties (imprisonment or fines).
- **Do:** route every lease/sale transaction through a licensed agent partner. Charge customers for *your* services (consulting, translation, accompaniment, admin help) at a fixed price not tied to the deal. Charge agents only for advertising/marketing under a written agreement, and ask a lawyer to confirm the structure. Receiving a share of an agent's brokerage commission is risky.
- **Don't:** negotiate lease terms on someone's behalf for a fee, take a percentage of rent/deposit, call yourself an agent/부동산, or collect a "commission" from a landlord for a lease without a license.

## 2. Short-Term Rentals / Co-Living

- Short-stay lodging for foreigners in residential housing generally needs a registration such as 외국인관광 도시민박업, and other stay types have their own rules. Some share houses operate as long-term residential leases instead.
- **Do:** only partner with operators who can show the right registration for what they offer, and keep that in `partner-directory.csv`.

## 3. Your Own Visa / Work Status

- If the business owner is a foreign national, running a business and earning income in Korea depends on visa status. Many visas (e.g., D-2 student, E-2 teacher) don't allow outside business income without permission. F-series residents or D-8/D-10 holders have different rules.
- If you're a Korean national, this item doesn't apply.
- Content creators receiving sponsorship/ad income in Korea should confirm their status with 1345 or a 행정사.

## 4. Business Registration and Tax

- Once earning regularly (and before scaling), register a business (사업자등록) with the tax office, keep records, and issue receipts/tax invoices. Creator income categories and VAT treatment vary; ask a 세무사.
- Receiving money into a personal account without registration is fine for early testing only up to what your accountant advises. Plan to register when you pass validation (10 customers).

## 5. Advertising Disclosure

- The Fair Trade Commission's recommendation guidelines (추천·보증 등에 관한 표시·광고 심사지침) require clear disclosure when you're paid or have an economic relationship with a featured business. Use "광고" / "유료 광고 포함" / "#ad" in-video and at the start of captions.
- Tell customers in chats when a recommended partner pays you.

## 6. Personal Information

- Korea's Personal Information Protection Act (개인정보 보호법) requires consent to collect personal data and separate consent to share it with third parties (like partners).
- **Do:** on the booking form, get consent to contact them and, separately, to share their details with named partner types. Collect only what you need. Delete data when no longer needed. Don't share passport/ARC numbers with partners.

## 7. Advice Boundaries

- Visa/immigration: general information only; refer to 1345, Hi Korea, Seoul Global Center, or a 행정사.
- Contracts: general red flags only; formal review by the licensed agent or a lawyer.
- Tax/finance: general information only.

## Quick Check Before Any Offer (Claude runs this)

1. Is any fee tied to a lease/sale price or paid out of brokerage commission? → restructure or route through a licensed agent.
2. Is the partner properly registered for what they sell? → check.
3. Is the relationship disclosed to the customer and in content? → add.
4. Do we have consent to share the customer's info with this partner? → get it.
5. Is the owner's visa status OK for earning this income? → confirm.
6. Is there a written agreement? → draft one.
