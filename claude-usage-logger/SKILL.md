---
name: claude-usage-logger
description: Logs how you actually use Claude each day - across Claude Code, Claude Desktop, Claude Cowork, and Claude.ai chat - into a local, private, append-only log. Use when building a personal usage journal, setting up a daily tracking routine, or reviewing usage patterns over time.
---

# Claude Usage Logger

This skill keeps a private, local, append-only log of how you use Claude across every surface - Claude Code, Claude Desktop, Claude Cowork, and Claude.ai (web/mobile chat) - so you can see patterns in your own usage over time. Nothing is uploaded anywhere; the log lives only on your machine.

## When to Use This Skill

- You want to build a personal journal of your day-to-day Claude usage
- You're setting up a daily routine that logs your usage automatically
- You want to review your usage patterns over the last week, month, etc.
- You're curious which surfaces (Code, Desktop, Cowork, chat) you actually use and for what

## What This Skill Does

1. **Auto-finds today's Claude Code activity**: Scans local Claude Code session transcripts for the given date and summarizes what projects you worked in.
2. **Asks a few quick questions**: Since Claude Desktop, Cowork, and Claude.ai chat aren't visible from a Claude Code session, it asks one short question per surface.
3. **Writes one entry per surface**: Appends a structured JSON line per surface actually used to a local log file, replacing any existing entry for the same surface/project that day instead of duplicating it.
4. **Confirms with a recap**: Shows a short table of what got logged and where.
5. **Summarizes past days on request**: Reads the log files directly to answer questions like "what did I use Claude for this week?"

## How to Use

### Basic Usage

```
Log my Claude usage for today
```

### Advanced Usage

```
Log my Claude usage for today, using ~/logs/claude-usage as the log directory
```

```
Show me my Claude usage summary for the last 7 days
```

## Instructions

When asked to log usage for a date (default: today):

1. **Resolve the date and log directory**

   Default date is today (local date is fine for the self-report questions; the Claude Code scan works off UTC-prefixed timestamps in transcripts, so use the same `YYYY-MM-DD` for both unless the user says otherwise). Default log directory is `~/.claude-usage-log`; use `--log-dir` if the user names a different one.

2. **Scan Claude Code activity**

   ```bash
   python3 claude-usage-logger/scripts/usage_logger.py scan-code --date YYYY-MM-DD
   ```

   This returns JSON with `found` and a `projects` list (project name, session count, message counts, slugs seen). If `found` is `false`, don't block - just skip straight to the self-report questions.

3. **Ask the self-report questions in a single message**

   ```
   Quick check on your other Claude usage today (skip any you didn't use):

   1. Claude Desktop - did you use it today? If so, one line on what for.
   2. Claude Cowork - did you use it today? If so, one line on what for.
   3. Claude.ai (web/mobile chat) - did you use it today? If so, one line on what for.
   4. (optional) Anything else worth noting about today's Claude usage overall?
   ```

4. **Append one entry per surface with a non-empty answer**

   For each Claude Code project found in step 2, build a `claude-code` entry with `source: "auto"` and a one-sentence `summary` derived from the slugs/messages seen. For each surface the user answered in step 3, build an entry with `source: "self-report"` and their own words as the `summary`. Skip any surface the user left blank or said they didn't use.

   Append each entry:

   ```bash
   python3 claude-usage-logger/scripts/usage_logger.py append --date YYYY-MM-DD --json '<entry as JSON>'
   ```

   Re-running for the same `(surface, project)` pair on the same day replaces the existing line, so it's safe to re-run this skill or a scheduled routine more than once a day.

5. **Print a recap**

   Show a short table of surface -> summary, and the log file path (`<log-dir>/YYYY-MM-DD.jsonl`).

6. **For summary/history requests** (e.g. "last 7 days"), don't script it - Read or Glob the `.jsonl` files in the log directory directly and summarize across days.

## Log Format & Storage

Default directory: `~/.claude-usage-log/` (kept separate from Claude Code's own `~/.claude/` state directory). One file per day: `YYYY-MM-DD.jsonl`, JSON Lines - one entry per surface used, plus one entry per distinct Claude Code project touched that day.

```json
{
  "date": "2026-07-18",
  "logged_at": "2026-07-18T21:04:12Z",
  "surface": "claude-code",
  "source": "auto",
  "summary": "One sentence describing what was done.",
  "topics": ["short", "tags"],
  "project": "awesome-claude-skills",
  "counts": {"sessions": 1, "user_messages": 13, "assistant_messages": 14},
  "notes": null
}
```

- `surface`: one of `claude-code`, `claude-desktop`, `claude-cowork`, `claude-ai-chat`
- `source`: `auto` (Claude Code, derived from local transcripts) or `self-report` (the other three)
- `project` / `counts`: present only on `claude-code` entries
- `topics` / `summary`: short tags and a one-sentence description, written by Claude from transcript content (auto) or the user's own words (self-report)

## Example

**User**: "Log my Claude usage for today"

**Output**:
```
Scanned Claude Code: found 1 project touched today - "awesome-claude-skills" (1 session, 13 user / 14 assistant messages).

Quick check on your other Claude usage today (skip any you didn't use):
1. Claude Desktop - did you use it today? If so, one line on what for.
2. Claude Cowork - did you use it today? If so, one line on what for.
3. Claude.ai (web/mobile chat) - did you use it today? If so, one line on what for.
4. (optional) Anything else worth noting?
```

**User**: "Didn't use Desktop or Cowork. Used Claude.ai chat to draft a birthday message."

**Output**:
```
Logged 2026-07-18 to ~/.claude-usage-log/2026-07-18.jsonl:

| Surface        | Source      | Summary                                  |
|----------------|-------------|-------------------------------------------|
| claude-code    | auto        | Worked in awesome-claude-skills           |
| claude-ai-chat | self-report | Drafted a birthday message                |
```

## Tips

- Run it once a day, ideally near the end of the day, for a clean picture of everything used.
- Nothing leaves your machine - the log is a local file you fully control.
- One-line self-report answers are enough; don't over-think them.
- Pair this with a daily scheduled trigger/routine so the log builds up without you remembering to run it manually.

## Common Use Cases

- Building a personal record of how Claude gets used across surfaces over weeks or months
- Spotting which surface (Code vs. Desktop vs. Cowork vs. chat) handles which kind of work
- Reviewing a week or month of usage before a retro, review, or usage report
- Feeding a lightweight personal analytics habit without any third-party service
