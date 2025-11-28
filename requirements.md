# Scheduling App Requirements
## Hackathon Challenge: Workforce Scheduling Optimization

---

## Background

Our Field Line Chiefs (FLC) manage cleaning and service operations across geographic areas. Each FLC is responsible for 5-20 customer assignments that need to be staffed according to specific time requirements and collective agreement rules.

**Current situation:** All planning is done manually using Excel spreadsheets and whiteboards. This is time-consuming and error-prone. Our existing scheduling system (Quinyx) only handles the final step - assigning employees to shifts and validating against collective agreement rules. There is no system support for the planning steps that come before.

**The opportunity:** Build something that solves any or all parts of this problem - from assignment grouping to employee scheduling. How you approach it is up to you.

---

## The Problem We're Solving

1. Customer assignments have different time requirements, locations and weekly hours
2. These need to be organized into workable schedules
3. Employees with different capacities and skills need to be matched to work
4. The goal: meet all customer requirements while respecting employee constraints and minimizing staffing costs

---

## Inputs

### 1. Customer Assignments
See `Kundplaneringsdata_a.csv` - 70 real customer assignments with:

| Field | Description |
|-------|-------------|
| Kundobjekt | Customer object ID and name |
| Krav på tider | Time requirement |
| Behov per vecka i timmar | Hours needed per week |
| Behov per dag timmar | Hours needed per day |
| Antal dagar i veckan | Days per week (1-7) |
| Antal heltidsekvivalenter | FTE required |
| Gruppering | Geographic group |
| Tjänst | Service type |

**Time requirements:**
- Morgon = Morning (typically 6-10)
- Förmiddag = Late morning (typically 9-12)
- Eftermiddag = Afternoon (typically 12-18)
- Hela dagen = Full day (typically 9-18)
- När som under dagen = Flexible / any time during the day
- Enligt överenskommelse = By agreement

**Geographic groups:** Centrum V, Centrum Ö, Flygstaden, Hallarna, Laholm, Norr, Nyhem Bilgrupp, ICA/Bilgrupp, Cafeterian, Stena Norr, Stena Södra, Övrigt BL

### 2. Employees
See `Medarbetare.csv` - employee roster with:

| Field | Description |
|-------|-------------|
| Anställningsnummer | Employee ID |
| Namn | Name |
| Anställningsgrad | Employment level (0.0-1.0, where 1.0 = full time 38h/week) |
| Kompetenser | Skills/certifications (comma-separated) |
| Kapacitetsfaktor | Capacity factor per skill (see below) |
| Grupp | Primary geographic group |

**Capacity Factor (Kapacitetsfaktor):**
A number between 0.0 and 1.0 representing work capacity relative to a fully trained, fully able employee:
- **0.1 - 0.3**: New employee, still in training
- **0.4 - 0.6**: Partially trained or reduced capacity
- **0.7 - 0.8**: Nearly fully trained
- **0.9 - 1.0**: Fully trained and capable

This factor affects how much time an employee needs to complete tasks. An employee with factor 0.5 needs twice as long to complete the same work as someone with factor 1.0.

### 3. Work Schedules (Pre-negotiated patterns)
These are union-negotiated patterns defining which days an employee can work. A set of available schedules for a 2-week period:

**Week 1:**
| Day | X1 | X2 | X3 | X4 | X5 | X6 | X7 |
|-----|----|----|----|----|----|----|----| 
| Mon | 1  | 1  |    | 1  | 1  | 1  |    |
| Tue |    | 1  | 1  | 1  | 1  | 1  |    |
| Wed | 1  | 1  | 1  |    | 1  | 1  |    |
| Thu | 1  |    | 1  | 1  | 1  | 1  |    |
| Fri | 1  | 1  | 1  | 1  | 1  | 1  |    |
| Sat |    | 1  |    | 1  |    |    |    |
| Sun |    | 1  |    | 1  |    |    |    |

**Week 2:**
| Day | X1 | X2 | X3 | X4 | X5 | X6 | X7 |
|-----|----|----|----|----|----|----|----| 
| Mon | 1  | 1  | 1  |    | 1  | 1  |    |
| Tue | 1  |    | 1  | 1  | 1  | 1  |    |
| Wed | 1  | 1  |    | 1  | 1  | 1  |    |
| Thu |    | 1  | 1  | 1  |    | 1  |    |
| Fri | 1  | 1  | 1  | 1  |    | 1  |    |
| Sat | 1  |    | 1  |    | 1  |    |    |
| Sun | 1  |    | 1  |    | 1  |    |    |

---

## Expected Outputs

The solution should produce a **schedule** that shows:

1. **Which employee works where and when** - assignment of employees to customer assignments with specific days and times
2. **Coverage confirmation** - proof that all customer requirements are met
3. **Rule compliance** - confirmation that collective agreement rules are followed
4. **Utilization metrics** - how efficiently employees are used

Example output format (just an example - feel free to innovate):

```
Employee: Ahmed Hassan (ID: 1012)
Week 1:
  Monday:    07:00-10:00 SuperMarket Gamletull, 10:30-14:30 Tax Authority
  Tuesday:   OFF
  Wednesday: 07:00-10:00 SuperMarket Gamletull, 10:30-14:30 Tax Authority
  ...

Coverage Report:
  SuperMarket Gamletull: 14.7h required, 15.0h scheduled ✓
  Tax Authority: 60.0h required, 60.0h scheduled ✓
  ...
```

---

## Constraints & Business Rules

### Collective Agreement Rules
- Standard full-time week: **38 hours** (including public holidays)
- Schedule cycle: Must repeat on **2 or 4 week** intervals
- Days off: Minimum **4 days off per 2-week period**
- Weekly rest: Minimum **36 consecutive hours** of rest per week

### Assignment Constraints
- Morning ("Morgon") assignments must be staffed at opening
- At least **25% of assignments** are 7-days-per-week with mandatory morning coverage
- Geographic proximity matters for travel between assignments

### Capacity Calculation
When an employee has capacity factor < 1.0, they need more time:
```
Actual time needed = Standard time / Capacity factor
```
Example: A 2-hour task takes 2.5 hours for someone with 0.8 capacity factor.

---

## Success Criteria

A successful solution should:

1. **Produce a valid schedule** - all assignments covered, all rules followed
2. **Handle real complexity** - work with the actual data provided
3. **Consider employee capacity** - account for training levels and abilities
4. **Be understandable** - output that a manager can review and use
5. **Show the trade-offs** - if optimization choices were made, explain them

---

## Stretch Goals

- Optimize for minimum total FTE
- Handle employee preferences or restrictions
- Visualize schedules in a calendar view
- Simulate "what if" scenarios (employee leaves, new assignment added)
- Calculate travel time between assignments
- Suggest training priorities based on coverage gaps

---

## Questions?

Contact Ville Andersson for domain expertise and clarifications.

Good luck! 🚀
