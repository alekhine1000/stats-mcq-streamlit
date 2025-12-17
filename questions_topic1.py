QUESTIONS = [
{
"id": "T1_Q1",
"question": "Which of the following is qualitative (categorical) data?",
"options": ["Height", "Weight", "Blood group", "Age"],
"correct": 2,
"hint": "Consider whether the variable represents categories or numerical measurements.",
"feedback_correct": "Blood group is categorical and therefore qualitative data.",
"feedback_wrong": {
0: "Height is measured numerically and is quantitative.",
1: "Weight is measured numerically and is quantitative.",
3: "Age is numerical and is treated as quantitative."
},
"final_explanation": "Correct answer: C. Blood group consists of categories rather than numerical measurements, so it is qualitative (nominal) data."
}
]

{
"id": "T1_Q2",
"question": "The number of students in a class is best classified as:",
"options": ["Nominal data", "Ordinal data", "Quantitative discrete data", "Quantitative continuous data"],
"correct": 2,
"hint": "Ask whether the variable can take fractional values.",
"feedback_correct": "This variable is a count and is therefore quantitative discrete data.",
"feedback_wrong": {
0: "Nominal data are categories, not numerical counts.",
1: "Ordinal data involve ranking, not counting.",
3: "Continuous data can take decimal values; counts cannot."
},
"final_explanation": "Correct answer: C. The number of students is a count (0, 1, 2, …) and is therefore quantitative discrete data."
},

{
"id": "T1_Q3",
"question": "Which variable is quantitative continuous?",
"options": ["Number of cars owned", "Letter grade (A, B, C)", "Time taken to complete a task", "Number of absences"],
"correct": 2,
"hint": "Continuous variables are measured and can take decimal values.",
"feedback_correct": "Time can take any value within a range, so it is continuous.",
"feedback_wrong": {
0: "Number of cars is a count and is discrete.",
1: "Letter grades are categorical.",
3: "Number of absences is a count and is discrete."
},
"final_explanation": "Correct answer: C. Time taken is measured and can take decimal values, so it is quantitative continuous data."
},

{
"id": "T1_Q4",
"question": "Gender is measured on which level of measurement?",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 0,
"hint": "Nominal variables are categories with no natural order.",
"feedback_correct": "Gender consists of categories with no inherent order.",
"feedback_wrong": {
1: "Ordinal data require ranking, which does not apply here.",
2: "Interval data are numerical; gender is not numerical.",
3: "Ratio data require a true zero; gender is not numerical."
},
"final_explanation": "Correct answer: A. Gender is a categorical variable with no natural ordering, so it is nominal."
},

{
"id": "T1_Q5",
"question": "Satisfaction level measured as “Very dissatisfied” to “Very satisfied” is best classified as:",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 1,
"hint": "Check whether the categories can be ranked.",
"feedback_correct": "The categories have a natural order, making the data ordinal.",
"feedback_wrong": {
0: "Nominal data have no order.",
2: "Equal numerical intervals are not guaranteed.",
3: "There is no true zero."
},
"final_explanation": "Correct answer: B. Satisfaction levels can be ranked, but the differences between categories are not measurable, so the data are ordinal."
},

{
"id": "T1_Q6",
"question": "Which of the following is an example of ratio data?",
"options": ["Temperature in °C", "Year of birth", "Weight", "IQ score"],
"correct": 2,
"hint": "Ratio data have a true zero and allow meaningful ratio statements.",
"feedback_correct": "Weight has a true zero and allows ratio comparisons.",
"feedback_wrong": {
0: "Celsius temperature has no true zero.",
1: "Years are interval data.",
3: "IQ does not have a true zero."
},
"final_explanation": "Correct answer: C. Weight has a true zero and supports meaningful ratios, so it is ratio data."
},

{
"id": "T1_Q7",
"question": "For which type of data is it generally appropriate to calculate the mean?",
"options": ["Nominal", "Ordinal", "Interval", "Nominal and ordinal"],
"correct": 2,
"hint": "The mean requires numerical data with meaningful intervals.",
"feedback_correct": "Interval data have meaningful differences, making the mean appropriate.",
"feedback_wrong": {
0: "Nominal data are categories.",
1: "Ordinal data lack equal intervals.",
3: "Mean is not meaningful for categorical data."
},
"final_explanation": "Correct answer: C. Interval data have numerical values with meaningful differences, so the mean is appropriate."
},

{
"id": "T1_Q8",
"question": "Hair colour is best classified as:",
"options": ["Quantitative", "Nominal", "Ordinal", "Ratio"],
"correct": 1,
"hint": "Nominal variables are categories
