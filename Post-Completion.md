# Post Completion

**Easiest day (after day 5)**: Day 10 ([part 1](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/solutions/Day%2010%20Part%201.py) and [part 2](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/solutions/Day%2010%20Part%202.py))

**Hardest day**: Day 16 ([part 1](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/solutions/Day%2016%20Part%201.py) and [part 2](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/solutions/Day%2016%20Part%202.py))

## My thoughts after completing Advent of Code 2021

I initially found out about this year's Advent of Code (AoC) through the [Python Discord server](https://discord.gg/python). The admins of the server made an announcement that they would host their own leaderboard, and people in the server who gained all 50 stars would be rewarded with a special role color.

Without thinking much of it, I decided I would participate.

That was a horrible mistake.

I knew what it was because I did a bit of it in 2018, and completely forgot about it in 2019 and 2020. I decided to do a few problems from earlier years to practice, but only got up to Day 8 Part 2 of 2020. I didn't expect to do any better than that.

During the first few days, I developed a sort of routine. Since the challenges unlocked at 9 PM every day (or night), I would attempt both parts between 9 PM-10 PM, and if I didn't finish the problem by then, I'd work on it the following day.

I also tended to not import external modules, as I believed I didn't have the skills necessary to utilize them correctly, nor to learn how to utilize them. This slowly extended to standard library modules as well.

This routine evolved into the additional challenges I would follow throughout the rest of the calendar:

1. Each solution must be completed with **zero imports**, including standard library imports. The one and only exception to this is `os`, which is required to get the correct path of the input files.

2. Each day's puzzles must be completed **within 24 hours** after they are released.

The routine would continue for quite some time. The two additional challenges gave way for some unordinary solutions, as neither speed nor readability were a primary focus for me. My motto became, `"if it works, it works"`.

One such solution was [Day 8 Part 2](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/solutions/Day%208%20Part%202.py), where I had multiple variable redeclarations, and ultimately messy code. Another was [Day 18 Part 2](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/solutions/Day%2018%20Part%202.py), where I interpreted every snailfish number as a literal string, whereas more "standard" solutions would interpret them as nested lists (which is how they're given).

On day 13, I entered myself into another challenge, where contestants were given a problem statement and had to write a function that solved the problem. Whoever wrote the fastest performing function would win either 1 year of Discord Nitro or $100 in Steam credit. As of 12/23/2021, I still don't know if I've won, but I believe I'm close to (or already at) first place. My solution can be found [here](https://github.com/TriG-Tbh/Advent-of-Code-2021/blob/main/bonus/snowman.py).

During the next few days following day 13, all time spent remaining the current day's puzzles were completed would be spent optimizing the solution for the second competition.

So far, the calendar was going by pretty easily.

Then came day 16.

I'm not exaggerating when I say that day 16 was **_hell_**. Constantly needing to figure out where one packet started and another ended was torture. By the time I got to part 2, I was so done with everything that I decided to use `eval()` (which is extremely taboo for Python).

That day was the start of a series of days where I would want to just complete the days whenever I could, while still maintaining the 24 hour rule.

After 23 days of it, I now realize this work ethic made me extremely tired after each day. The self-imposed need to reinvent the wheel in 24 hours every day made this entire calendar more challenging and less fun than it would be if I just took it easy.

I didn't expect myself to get this far. I didn't even expect myself to get past day 10.

Now that I **am** this far, I know I have a lot to work on.

Next year, I'll...

- take a lot of the functions I created this year (depth-first search, Dijkstra's, etc.) and store them for later use tomorrow
- not limit myself to arbitrary constraints that only make the calendar less fun
- be more open to other people's solutions to understand how they interpreted the problem
