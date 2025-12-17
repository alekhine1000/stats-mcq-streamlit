QUESTIONS = [

# ---------------- BASIC ----------------

{
"id": "T1_Q1",
"question": "Which of the following is qualitative data?",
"options": ["Height", "Weight", "Blood group", "Age"],
"correct": 2,
"hint": "Hint: Is this a category or a numerical measurement?",
"feedback_correct": "✔ Well done! Blood group is categorical and non-numerical.",
"feedback_wrong": {
0: "❌ Height is measured numerically.",
1: "❌ Weight is measured numerically.",
3: "❌ Age is numerical."
},
"final_explanation": "Correct answer: C — Blood group. It describes categories rather than numerical measurements, so it is qualitative (nominal) data."
},

{
"id": "T1_Q2",
"question": "The number of students in a class is:",
"options": ["Nominal", "Ordinal", "Quantitative discrete", "Quantitative continuous"],
"correct": 2,
"hint": "Hint: Can the value be a fraction?",
"feedback_correct": "✔ Correct! This is a count, so it is quantitative discrete.",
"feedback_wrong": {
0: "❌ Nominal data are categories.",
1: "❌ Ordinal data involve ranking.",
3: "❌ Continuous data allow decimals."
},
"final_explanation": "Correct answer: C — Quantitative discrete. The number of students is a count and cannot take fractional values."
},

{
"id": "T1_Q3",
"question": "Which variable is quantitative continuous?",
"options": ["Number of cars", "Test grade (A, B, C)", "Time taken to finish a race", "Number of absentees"],
"correct": 2,
"hint": "Hint: Can the variable take any value within a range?",
"feedback_correct": "✔ Well done! Time can take any value within a range.",
"feedback_wrong": {
0: "❌ Number of cars is a count.",
1: "❌ Grades are categorical.",
3: "❌ Absentees are counted."
},
"final_explanation": "Correct answer: C — Time taken to finish a race. Time is measured on a continuous scale."
},

{
"id": "T1_Q4",
"question": "Gender is measured on which level of measurement?",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 0,
"hint": "Hint: Is there any natural order?",
"feedback_correct": "✔ Correct! Gender is categorical with no natural order.",
"feedback_wrong": {
1: "❌ There is no ranking.",
2: "❌ Interval data are numerical.",
3: "❌ Ratio data require a true zero."
},
"final_explanation": "Correct answer: A — Nominal. Gender consists of categories without order or numerical meaning."
},

{
"id": "T1_Q5",
"question": "Satisfaction level (Very dissatisfied to Very satisfied) is:",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 1,
"hint": "Hint: Can the categories be ranked?",
"feedback_correct": "✔ Well done! The categories have a natural order.",
"feedback_wrong": {
0: "❌ Nominal data have no order.",
2: "❌ Differences are not numerically equal.",
3: "❌ There is no true zero."
},
"final_explanation": "Correct answer: B — Ordinal. Satisfaction levels can be ranked but the gaps between them are not equal."
},

# ---------------- INTERMEDIATE ----------------

{
"id": "T1_Q6",
"question": "Which of the following is an example of ratio data?",
"options": ["Temperature in °C", "Year of birth", "Weight", "IQ score"],
"correct": 2,
"hint": "Hint: Does zero mean 'none'?",
"feedback_correct": "✔ Correct! Weight has a true zero.",
"feedback_wrong": {
0: "❌ Celsius has no true zero.",
1: "❌ Years are interval data.",
3: "❌ IQ has no true zero."
},
"final_explanation": "Correct answer: C — Weight. It has a true zero and allows meaningful ratios."
},

{
"id": "T1_Q7",
"question": "Which type of data can be meaningfully averaged?",
"options": ["Nominal", "Ordinal", "Interval", "Nominal and ordinal"],
"correct": 2,
"hint": "Hint: Do the differences between values matter?",
"feedback_correct": "✔ Well done! Interval data have equal intervals.",
"feedback_wrong": {
0: "❌ Nominal data are labels.",
1: "❌ Ordinal gaps are unequal.",
3: "❌ Mean is not meaningful here."
},
"final_explanation": "Correct answer: C — Interval. Equal intervals make the mean meaningful."
},

{
"id": "T1_Q8",
"question": "Hair colour is classified as:",
"options": ["Quantitative", "Nominal", "Ordinal", "Ratio"],
"correct": 1,
"hint": "Hint: Is there any ranking?",
"feedback_correct": "✔ Correct! Hair colour is categorical.",
"feedback_wrong": {
0: "❌ It is not numerical.",
2: "❌ There is no order.",
3: "❌ No true zero exists."
},
"final_explanation": "Correct answer: B — Nominal. Hair colour consists of categories without order."
},

{
"id": "T1_Q9",
"question": "Which of the following is ordinal data?",
"options": ["Temperature", "Salary", "Movie rating (1–5 stars)", "Height"],
"correct": 2,
"hint": "Hint: Is there a ranking but unequal gaps?",
"feedback_correct": "✔ Well done! Star ratings are ordered categories.",
"feedback_wrong": {
0: "❌ Temperature is interval.",
1: "❌ Salary is ratio.",
3: "❌ Height is continuous."
},
"final_explanation": "Correct answer: C — Movie rating. It is ordinal data with a natural order."
},

{
"id": "T1_Q10",
"question": "Which measure is most appropriate for nominal data?",
"options": ["Mean", "Median", "Mode", "Range"],
"correct": 2,
"hint": "Hint: Which measure works with categories?",
"feedback_correct": "✔ Correct! Mode identifies the most frequent category.",
"feedback_wrong": {
0: "❌ Mean requires numerical data.",
1: "❌ Median requires ordered data.",
3: "❌ Range measures spread."
},
"final_explanation": "Correct answer: C — Mode. It is the only appropriate measure for nominal data."
},

# ---------------- ADVANCED / TRICKY ----------------

{
"id": "T1_Q11",
"question": "Temperature measured in Kelvin is:",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 3,
"hint": "Hint: Does the scale have a true zero?",
"feedback_correct": "✔ Well done! Kelvin has an absolute zero.",
"feedback_wrong": {
0: "❌ Not categorical.",
1: "❌ Not ranked categories.",
2: "❌ Interval scales lack a true zero."
},
"final_explanation": "Correct answer: D — Ratio. Kelvin temperature has a true zero."
},

{
"id": "T1_Q12",
"question": "Which variable is discrete?",
"options": ["Distance travelled", "Weight", "Number of books", "Time taken"],
"correct": 2,
"hint": "Hint: Can the values be counted?",
"feedback_correct": "✔ Correct! Books are counted in whole numbers.",
"feedback_wrong": {
0: "❌ Distance is continuous.",
1: "❌ Weight is continuous.",
3: "❌ Time is continuous."
},
"final_explanation": "Correct answer: C — Number of books. It is a discrete count."
},

{
"id": "T1_Q13",
"question": "Exam scores out of 100 are usually treated as:",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 2,
"hint": "Hint: Are differences between scores meaningful?",
"feedback_correct": "✔ Well done! Score differences are meaningful.",
"feedback_wrong": {
0: "❌ Not categorical.",
1: "❌ More than just ranking.",
3: "❌ Zero does not mean no ability."
},
"final_explanation": "Correct answer: C — Interval. Differences between scores are meaningful."
},

{
"id": "T1_Q14",
"question": "Which statement about ordinal data is TRUE?",
"options": ["Differences are meaningful", "Mean is appropriate", "Data can be ranked", "There is a true zero"],
"correct": 2,
"hint": "Hint: What defines ordinal data?",
"feedback_correct": "✔ Correct! Ordinal data are ranked.",
"feedback_wrong": {
0: "❌ Gaps are not equal.",
1: "❌ Mean is not appropriate.",
3: "❌ No true zero exists."
},
"final_explanation": "Correct answer: C — Data can be ranked, but differences are not equal."
},

{
"id": "T1_Q15",
"question": "Which variable is incorrectly classified?",
"options": [
"Height – continuous",
"Age – continuous",
"Number of siblings – continuous",
"Income – ratio"
],
"correct": 2,
"hint": "Hint: Can siblings be fractional?",
"feedback_correct": "✔ Well spotted! Number of siblings is discrete.",
"feedback_wrong": {
0: "❌ Height is continuous.",
1: "❌ Age is treated as continuous.",
3: "❌ Income is ratio data."
},
"final_explanation": "Correct answer: C — Number of siblings is discrete, not continuous."
},

{
"id": "T1_Q16",
"question": "Which data type allows statements like 'twice as much'?",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 3,
"hint": "Hint: Think about meaningful ratios.",
"feedback_correct": "✔ Correct! Ratio data allow meaningful comparisons.",
"feedback_wrong": {
0: "❌ Labels only.",
1: "❌ Ranking only.",
2: "❌ No true zero."
},
"final_explanation": "Correct answer: D — Ratio. It has a true zero and supports ratios."
},

{
"id": "T1_Q17",
"question": "Likert-scale data (1–5) are BEST classified as:",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 1,
"hint": "Hint: Are the gaps guaranteed to be equal?",
"feedback_correct": "✔ Well done! Likert scales are ordered categories.",
"feedback_wrong": {
0: "❌ There is an order.",
2: "❌ Equal intervals are not guaranteed.",
3: "❌ No true zero."
},
"final_explanation": "Correct answer: B — Ordinal. Likert scales have order but unequal intervals."
},

{
"id": "T1_Q18",
"question": "Which variable may change classification depending on context?",
"options": ["Gender", "Blood group", "Age", "Education level"],
"correct": 3,
"hint": "Hint: Can it be categorical or numerical?",
"feedback_correct": "✔ Correct! Education level depends on how it’s recorded.",
"feedback_wrong": {
0: "❌ Always nominal.",
1: "❌ Always nominal.",
2: "❌ Always numerical."
},
"final_explanation": "Correct answer: D — Education level. It can be ordinal or numerical depending on context."
},

{
"id": "T1_Q19",
"question": "Which operation is NOT meaningful for ordinal data?",
"options": ["Ranking", "Finding the mode", "Finding the median", "Calculating differences"],
"correct": 3,
"hint": "Hint: Are numerical gaps meaningful?",
"feedback_correct": "✔ Correct! Differences are not meaningful for ordinal data.",
"feedback_wrong": {
0: "❌ Ranking is meaningful.",
1: "❌ Mode can be found.",
2: "❌ Median can be found."
},
"final_explanation": "Correct answer: D — Calculating differences. Ordinal data do not have equal intervals."
},

{
"id": "T1_Q20",
"question": "Which best describes interval data?",
"options": [
"Categories with order",
"Numerical data with a true zero",
"Numerical data with equal intervals but no true zero",
"Categories without order"
],
"correct": 2,
"hint": "Hint: Think about equal spacing but no absolute zero.",
"feedback_correct": "✔ Well done! This is the defining feature of interval data.",
"feedback_wrong": {
0: "❌ That describes ordinal data.",
1: "❌ That describes ratio data.",
3: "❌ That describes nominal data."
},
"final_explanation": "Correct answer: C — Interval data have equal intervals but no true zero."
}

]
