# Jobnova Take Home Challenge

## Part 1 - AI Mock Interview Demo

This demo implements:

* Self Introduction Agent
* Past Experience Agent
* Agent Handoff Logic
* Time-Based Fallback Transition
* Interview Summary

Workflow:

SelfIntroductionAgent
→ Agent Handoff
→ PastExperienceAgent

The fallback timer automatically transitions to the next stage if the normal completion logic is not triggered.

---

## Part 2 - AI Job Source Agent

This demo:

1. Accepts a company name and company website URL
2. Searches for a careers page
3. Finds one open position URL
4. Returns results in the required format

Output:

Company name:
Career page URL:
Open position URL:

---

## Tech Stack

* Python 3.12
* LiveKit Agents
* Requests
* BeautifulSoup
* Playwright

## Run

Part 1:

python part1_mock_interview.py

Part 2:

python part2_job_source.py
