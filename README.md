# 🐍 Learning Python for Data Science — A Java Developer's Journey

> **Toolkit Document & Project README**
> From Java fundamentals to Python data science — a structured learning journey with working code.

---

## 1. Title & Objective

**Technology chosen:** Python (with NumPy, Pandas, Matplotlib, Scikit-learn)

**Why Python?**
Coming from a Java background, Python was chosen as the entry point into data science because of its dominance in the field, minimal boilerplate syntax, and the richness of its data science ecosystem. Unlike Java, Python allows rapid prototyping — a data pipeline that would take 100 lines in Java often takes 10 in Python.

**End goal:** Build a working data science pipeline — from raw data ingestion and analysis (NumPy + Pandas) through visualisation (Matplotlib) to a trained, saved, and reusable machine learning model (Scikit-learn + Joblib).

---

## 2. Quick Summary of the Technology

**Python** is a high-level, dynamically typed, interpreted programming language first released in 1991. It is the dominant language in data science, machine learning, and AI research.

- **What is it?** A general-purpose language with a vast ecosystem of scientific libraries.
- **Where is it used?** Data analysis, machine learning, automation, web backends (Django/FastAPI), scripting.
- **Real-world example:** Netflix uses Python and Scikit-learn to power its recommendation engine, processing millions of user interactions to predict viewing preferences.

| Java Concept | Python Equivalent |
|---|---|
| `ArrayList` | `list` |
| `HashMap` | `dict` |
| Static typing | Dynamic typing (optional type hints) |
| Maven/Gradle | pip + requirements.txt |
| try-with-resources | `with` statement |
| Stream API | List comprehensions / NumPy vectorisation |
| `public static void main()` | `if __name__ == "__main__":` |

---

## 3. System Requirements

- **OS:** Windows 10+, macOS 11+, or Ubuntu 20.04+
- **Python:** 3.10 or higher ([python.org](https://python.org))
- **Editor:** VS Code (recommended) with the Python extension, or PyCharm Community
- **Terminal:** Any — Command Prompt, PowerShell, bash, or zsh

---

## 4. Installation & Setup

### Step 1 — Install Python
Download from [python.org/downloads](https://python.org/downloads). During installation on Windows, check **"Add Python to PATH"**.

Verify:
```bash
python --version
# Python 3.11.x
```

### Step 2 — Clone or download the project
```bash
git clone https://github.com/your-username/python-ds-journey.git
cd python-ds-journey
```

### Step 3 — Create a virtual environment
```bash
# Create
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

> **Why a virtual environment?** It isolates packages per project — the same role Maven's local repository plays in Java. You will see `(.venv)` in your terminal prompt when it is active.

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

---

## 5. Project Structure

```
python-ds-journey/
│
├── src/
│   ├── phase_1_verification.py     # Python basics — lists, loops, sorting, grading
│   ├── phase_2_numpy_exe.py        # NumPy arrays and vectorised operations
│   ├── phase_3_train.py            # Scatter plot, LinearRegression, model training
│   └── phase_4_predict.py          # Load saved model and predict new values
│
├── models/
│   └── score_model.pkl             # Trained LinearRegression model (generated)
│
├── charts/
│   └── scatter.png                 # Study hours vs exam scores chart (generated)
│
├── requirements.txt
└── README.md
```

---

## 6. Minimal Working Examples

### Phase 1 — Python basics (Hello World equivalent)
```python
# A list of students and their scores
students = [("Alice", 88), ("Bob", 72), ("Carol", 95)]

# Sort by score, highest first
students.sort(key=lambda x: x[1], reverse=True)

# Print with letter grades
for name, score in students:
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"{name}: {score} — Grade {grade}")
```
**Expected output:**
```
Carol: 95 — Grade A
Alice: 88 — Grade B
Bob: 72 — Grade C
```

### Phase 2 — NumPy vectorised operations
```python
import numpy as np

scores = np.array([88, 72, 95, 61, 79, 91, 55, 83])

print(f"Average:      {scores.mean():.1f}")
print(f"Above average: {scores[scores > scores.mean()]}")
print(f"Students passed: {np.sum(scores >= 70)}")
```
**Expected output:**
```
Average:      78.0
Above average: [88 95 79 91 83]
Students passed: 6
```

### Phase 3 — Train and evaluate a model
```bash
python src/phase_3_train.py
# R² Score: 0.9603
# Predicted score for 6 hours: 79.21
# Chart saved → charts/scatter.png
# Model saved → models/score_model.pkl
```

### Phase 4 — Load model and predict
```bash
python src/phase_4_predict.py
# 1 hours -> 51.74
# 4 hours -> 72.45
# 9 hours -> 93.16
```

---

## 7. Running the Code

Run each phase in order from the project root:

```bash
# Phase 1 — Python fundamentals
python src/phase_1_verification.py

# Phase 2 — NumPy operations
python src/phase_2_numpy_exe.py

# Phase 3 — Train the model (run this before Phase 4)
python src/phase_3_train.py

# Phase 4 — Load model and predict
python src/phase_4_predict.py
```

> **Note:** Run Phase 3 before Phase 4. Phase 3 creates the `models/score_model.pkl` file that Phase 4 loads.

---

## 8. AI Prompt Journal

This project was built with the assistance of Claude (Anthropic) as a structured learning tool. Below is a record of key prompts used and what they produced.

---

**Prompt 1**
> *"I'm proficient in Java and want to learn Python for data science. Could you help me create a structured learning journey plan with 3–4 distinct learning phases, prerequisites, learning steps, and verification activities?"*

**AI response summary:** Claude generated a four-phase plan mapping Java concepts to Python equivalents — from syntax fundamentals through NumPy/Pandas, visualisation/ML, to tooling and deployment. Each phase included prerequisites, five learning steps, and a verification challenge.

**Helpfulness:** Very high. Having a structured map prevented aimless Googling and gave each session a clear goal.

---

**Prompt 2**
> *"Tell me more about Phase 1: Python syntax for Java developers"*

**AI response summary:** Claude produced an interactive Java-vs-Python comparison covering types and variables, control flow, functions, collections, and exception handling — with side-by-side code blocks for each concept.

**Helpfulness:** High. The side-by-side format made it easy to see that Python achieves the same outcomes with less ceremony, rather than feeling like re-learning from scratch.

---

**Prompt 3**
> *"What are Python type hints and when should I use them as a Java developer?"*

**AI response summary:** Claude explained that type hints are optional annotations checked by tools like `mypy`, not enforced at runtime. Recommended always annotating public function signatures and class attributes; skipping hints for local variables and exploratory notebook code.

**Helpfulness:** High. As a Java developer, understanding that type hints are opt-in (not mandatory like Java generics) removed a mental block about Python's "looseness".

---

**Prompt 4**
> *"Show me one small working program I can run and modify"* (after feeling overwhelmed)

**AI response summary:** Claude simplified down to a 20-line student scores program using only four concepts: a list, a for loop, an if/else, and print(). This reset the learning pace effectively.

**Helpfulness:** Critical. This was the turning point — going from overwhelmed to productive in one response.

---

**Prompt 5**
> *"Teach me Step 1 of Phase 2: NumPy arrays and vectorised operations vs Java for-loops"*

**AI response summary:** Claude built an interactive five-tab explorer (creating arrays, vectorised ops, indexing/slicing, 2D arrays, and aggregates) with side-by-side Java/NumPy comparisons for each concept.

**Helpfulness:** High. The key insight — that NumPy operations replace loops and run in compiled C — immediately explained why Python can outperform Java loops on numerical data despite being interpreted.

---

**Prompt 6**
> *"Since my project is due in 3 days I just need a mini project"*

**AI response summary:** Claude generated a complete `grades_analyser.py` — a 120-line script loading student data into a Pandas DataFrame, using NumPy for grade assignment and statistics, and producing four Matplotlib charts (histogram, bar chart, subject comparison, scatter plot).

**Helpfulness:** Very high. The script tied together all four phases into one runnable, submittable deliverable.

---

## 9. Common Issues & Fixes

**Error: `ModuleNotFoundError: No module named 'numpy'`**
```
Solution: Your virtual environment is not active, or you installed packages globally.
Fix:
  source .venv/bin/activate        # macOS/Linux
  .venv\Scripts\activate           # Windows
  pip install -r requirements.txt
```

**Error: `FileNotFoundError: [Errno 2] No module named 'score_model.pkl'`**
```
Solution: You ran phase_4_predict.py before phase_3_train.py.
Fix: Run phase_3_train.py first — it creates the model file.
  python src/phase_3_train.py
```

**Error: `ValueError: Expected 2D array, got 1D array instead`**
```
Solution: Scikit-learn requires 2D input arrays.
Fix: Reshape your input before passing to the model.
  X = study_hours.reshape(-1, 1)   # converts 1D to 2D column
```

**IndentationError: unexpected indent**
```
Solution: Python uses indentation as block delimiters — unlike Java's braces.
Fix: Ensure consistent 4-space indentation. Never mix tabs and spaces.
  average = total / len(students)  # must be at the SAME level as 'for', not inside it
```

**Plot window doesn't appear / plt.show() hangs**
```
Solution: On some systems, the matplotlib backend needs configuring.
Fix: Save the chart instead of showing it interactively.
  plt.savefig("charts/scatter.png")
  # Then open the PNG file directly
```

**Chart saved but models/ folder missing**
```
Solution: The output folders don't exist yet.
Fix: Create them before running, or use os.makedirs (already in the code).
  mkdir models charts
```

---

## 10. References

**Official Documentation**
- [Python 3 Docs](https://docs.python.org/3/) — language reference and standard library
- [NumPy User Guide](https://numpy.org/doc/stable/user/) — array operations and indexing
- [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame API reference
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — ML models and pipelines
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/) — chart types and customisation

**Recommended Tutorials**
- [Python for Everybody – Dr. Chuck (YouTube)](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p)
- [Kaggle — Python micro-course (free)](https://www.kaggle.com/learn/python)
- [Kaggle — Pandas micro-course (free)](https://www.kaggle.com/learn/pandas)
- [Scikit-learn — Getting Started](https://scikit-learn.org/stable/getting_started.html)

**Helpful for Java → Python transitions**
- [Python vs Java — Real Python](https://realpython.com/python-vs-java/)
- [mypy — optional static type checking](https://mypy.readthedocs.io/en/stable/)

---

## 11. Contributing

This is a personal learning project. If you are following the same Java → Python journey and want to contribute additional exercises or phase examples, feel free to open a pull request.

1. Fork the repository
2. Create a feature branch: `git checkout -b phase-5-deep-learning`
3. Commit your changes: `git commit -m "Add PyTorch intro exercise"`
4. Push and open a pull request

---

## 12. License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). Free to use, modify, and distribute for personal or educational purposes.

---

*Built with Python 3.11 · NumPy · Pandas · Matplotlib · Scikit-learn · Joblib*
