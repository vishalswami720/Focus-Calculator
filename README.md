# 🎯 Focus Calculator

A Python-based application that calculates your daily **Focus Percentage** based on your daily routine. It analyzes your wake-up time, study hours, exercise, screen time, and sleep schedule, then provides suggestions to help improve your productivity.

## 📌 Features

- 🕒 Calculates your daily awake/work time.
- 📚 Tracks study hours.
- 🏃 Includes exercise/sports time.
- 📱 Considers mobile screen time.
- 😴 Uses sleep schedule to determine available productive hours.
- 📊 Calculates a Focus Percentage.
- 💡 Provides personalized suggestions to improve focus.
- ✅ Validates user input to prevent invalid values.

## 🚀 How It Works

The program asks the user to enter:

1. Wake-up Time
2. Study Hours
3. Exercise/Sports Time
4. Mobile Screen Time
5. Sleep Time

It then:

- Calculates the available awake/work time.
- Computes a Focus Percentage.
- Displays personalized suggestions based on the result.

---

## 📈 Focus Percentage Formula

```text
Focus Percentage =
((Study Hours + Exercise Hours) - (Screen Time × 0.5))
------------------------------------------------------ × 100
                 Work Time
```

The result is limited to a range of **0% to 100%**.

---



## 💻 Example

```
Enter your wake-up time: 8
Enter your study hours: 4
Enter your exercise time: 1
Enter your mobile screen time: 3
Enter your sleep time: 10

Your Focus Percentage: 25.00%

Suggestions:
- Increase your study time.
- Reduce your mobile screen time.
```

---

## 🔮 Future Improvements

- Support 12-hour (AM/PM) and 24-hour time formats.
- Accept minutes (e.g., 8:30 AM).
- Store daily history.
- Display graphs and statistics.
- Build a graphical user interface (GUI).
- Export reports to CSV or PDF.

---
