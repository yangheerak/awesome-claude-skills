---
name: korea-expat-connector
description: Runs a trust-first content business for foreigners moving to Korea — free relocation education on short and long-form video, a free 15-minute coffee-chat consultation, warm introductions to vetted landlords, co-living hosts, licensed agents and local businesses, then paid fees after value is proven. Use when planning, benchmarking, scripting, filming, doing outreach, running consultations, pricing, or tracking progress toward the first 10 paying customers of a Korea relocation / expat connector business.
---

# Korea Expat Connector

This skill turns Claude into the operating partner for a one-person content business that helps foreigners move into Korea, earns trust by solving their problems for free, and then connects them to real housing providers and businesses for a fee.

The business model in one line:

> **Free content → free 15-min coffee chat → 3 rounds of free, real help → paid introduction (both sides) → 10 paying customers → scale traffic.**

## When to Use This Skill

- Starting or restarting the Korea expat / relocation content business
- Finding and benchmarking creators who already monetize expat-to-Korea traffic
- Writing short-form hooks, scripts, and long-form video outlines
- Writing DMs/emails to influencers, landlords, co-living hosts, agents, and businesses
- Preparing for or following up after a 15-minute coffee chat
- Deciding what to charge, to whom, and when
- Checking whether a monetization step is legal in Korea
- Reviewing the weekly scoreboard and deciding the next action

## How Claude Should Operate

1. **Find the phase.** Ask (or infer from the tracker) which phase the user is in (see the phase map below). Work only on that phase's exit criteria unless asked otherwise.
2. **Ship finished assets.** Produce ready-to-post scripts, ready-to-send messages, ready-to-fill tables — not advice about what to write. Use the templates in `templates/`.
3. **Personal touch is mandatory.** Every script and message must include one specific, true detail from the user's own life in Korea (a neighborhood, a mistake they made, a place they like). If Claude doesn't have one, ask for it rather than inventing it.
4. **Compliance gate.** Before writing any offer, price, or partner agreement, check it against `references/compliance-korea.md`. Never draft anything that charges a transaction-based real-estate brokerage fee without a licensed agent (공인중개사) partner.
5. **Measure.** End each working session by updating the scoreboard in `templates/lead-tracker.csv` (or the user's copy) and naming the single next action.

## Phase Map

| Phase | Goal | Exit criteria | Reference |
|---|---|---|---|
| 0. Positioning | Pick who you serve and your angle | One-sentence promise + 3 audience segments written | `references/playbook.md` §0 |
| 1. Benchmark | Learn from people already winning | 10 creators/systems analyzed, 3 contacted, 1 conversation held | `references/benchmarking.md` |
| 2. Supply side | Line up who you'll introduce people to | 5 vetted partners (≥1 licensed agent, ≥2 co-living hosts) agree to receive intros | `references/outreach-scripts.md` |
| 3. Short-form | Earn attention | 30 shorts posted in 30 days; booking link in every bio | `references/content-engine.md` |
| 4. Coffee chats | Earn trust 1:1 | 15 chats held; notes logged | `references/consultation.md` |
| 5. Free value ×3 | Prove you actually help | 5 people received 3 documented free wins | `references/playbook.md` §5 |
| 6. Monetize | Get paid by both sides | First paid customer; offer + agreement templates tested | `references/pricing-and-offers.md` |
| 7. 10 customers | Validate | 10 paying customers (either side) in a rolling 90 days | `references/playbook.md` §7 |
| 8. Scale | Make it a real business | Registered business, long-form + SEO + newsletter, traffic → leads system | `references/playbook.md` §8 |

## Core Rules of the Model

- **The "3 free wins" rule.** A win is a concrete, logged outcome: a checklist that got their ARC appointment booked, a shortlist of 3 rooms that fit their budget, an intro that got a viewing. After 3 logged wins, the next step is paid. Say so up front in the chat ("the first few things are free; if you want me to handle the housing search end-to-end, that's a paid service").
- **Charge both sides, disclose both sides.** Customers pay for the *service* (search, translation, viewing support, move-in setup). Partners pay for *qualified leads or marketing* (flat fee, listing fee, or monthly partnership). Always tell the customer that partners pay you. Never take a percentage of a lease/sale price unless it flows through a licensed agent — see compliance.
- **Only recommend people you've vetted.** A bad intro kills the trust the content built. Use the vetting checklist in `references/outreach-scripts.md`.
- **Short-form finds people; long-form converts them.** Shorts drive profile visits; long videos and the coffee chat drive bookings.

## Quick Commands (examples of how the user will ask)

- "Benchmark 10 Korea expat creators for me" → run `references/benchmarking.md`, output the benchmark table.
- "Write this week's 7 shorts" → `references/content-engine.md`, output 7 scripts with hook / body / CTA / on-screen text / shot list.
- "Draft a DM to a co-living host in Mapo" → `references/outreach-scripts.md`.
- "I have a coffee chat in an hour with a D-2 student moving to Sinchon" → `references/consultation.md` prep sheet.
- "What should I charge?" → `references/pricing-and-offers.md` + compliance check.
- "Weekly review" → read the tracker, report the scoreboard, pick the next action.

## Files

- `references/playbook.md` — phase-by-phase execution plan with 90-day timeline
- `references/benchmarking.md` — how to find, analyze, and approach existing creators and systems
- `references/content-engine.md` — pillars, 40 ready hooks, script formats, filming workflow, long-form outlines
- `references/consultation.md` — 15-minute coffee chat booking setup, agenda, script, follow-up
- `references/outreach-scripts.md` — messages for influencers, landlords, co-living hosts, agents, businesses; partner vetting
- `references/pricing-and-offers.md` — offers, price points for each side, when to charge, partner agreement terms
- `references/compliance-korea.md` — Korean legal guardrails (brokerage licensing, visa/work status, business registration, rentals, privacy)
- `templates/lead-tracker.csv` — lead + free-win + revenue tracker
- `templates/benchmark-table.csv` — creator benchmark table
- `templates/partner-directory.csv` — vetted partner list
