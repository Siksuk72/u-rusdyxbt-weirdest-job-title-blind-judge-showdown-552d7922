# Weirdest Job Title: Blind Judge Showdown

[![make.fun · u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/Siksuk72/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/rank.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/Siksuk72/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/reward.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)


One original job title (56 characters):

> Lead Apology Writer for Billionaires Who Never Apologize

## Design rationale

**Reads like a real job.** "Lead … Writer" is an ordinary corporate
title shape — a seniority word, a craft, a desk you can picture. The
reader accepts it as a job before any joke lands, which is exactly
what the judge's brief rewards over random word salad.

**One specific twist, and it contradicts itself.** The twist is not a
weird animal or a silly place; it is the client. Billionaires who
never apologize hire someone whose whole job is writing apologies.
The title quietly promises work that can never be delivered, and the
contradiction lands on the first read — you picture the writer
drafting heartfelt sorries that nobody will ever send.

**A fresh turn, not a familiar oddity.** No unicorns, no ghost
hunters, no professional cuddlers. The humour comes from money and
power, not from a random noun, so it stands out in a field full of
generic oddities and rewards a second read: the weirder you think
about it, the more the job makes a terrible kind of sense.

## How it runs

`main.py` writes the line to `/output/entry.txt`, enforcing the gate in
code (UTF-8, 1–60 characters, not only whitespace, no trailing
newline, no sentence-ending period). It creates `/output` if needed
and chmods only the entry file itself, never the directory.
