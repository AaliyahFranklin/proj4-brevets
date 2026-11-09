# ACP Brevet Time Calculator

**Author:** Aaliyah Franklin
**Email:** aaliyahf@uoregon.edu

## What it does

A Flask web app that calculates the open and close times for the control
points of an ACP brevet. You choose the brevet distance and start time, then
type a control distance. The open and close times fill in automatically using
Ajax, with no page reload.

## Rules

Each part of the control distance is charged at the speed for its range, and
the times are added up and rounded to the nearest minute. Open time uses the
max speed and close time uses the min speed.

| Range (km)  | Min speed | Max speed |
|-------------|-----------|-----------|
| 0 - 200     | 15        | 34        |
| 200 - 400   | 15        | 32        |
| 400 - 600   | 15        | 30        |
| 600 - 1000  | 11.428    | 28        |
| 1000 - 1300 | 13.333    | 26        |

- A control past the brevet distance is treated as the brevet distance.
- A 200 km finish closes at 13:30, and a 400 km finish at 27:00.
- Controls under 60 km close at distance / 20 + 1 hour.
- The start (0 km) opens at 0:00 and closes at 1:00.

## Known limitations

- Rows only recalculate when their own control distance changes. Changing the
  brevet distance or start time does not update rows already filled in.


