QUESTIONS = [

# ---------------- LEVEL 1: KNOWLEDGE ----------------

{
"id": "T1_Q1",
"question": "Which of the following is qualitative (categorical) data?",
"options": ["Height", "Weight", "Blood group", "Age"],
"correct": 2,
"hint": "Is this a category or a numerical measurement?",
"feedback_correct": "Blood group is categorical data.",
"feedback_wrong": {
0: "Height is measured numerically.",
1: "Weight is measured numerically.",
3: "Age is numerical."
},
"final_explanation": "Blood group describes categories rather than numerical measurements."
},

{
"id": "T1_Q2",
"question": "The number of students in a class is best classified as:",
"options": ["Nominal data", "Ordinal data", "Quantitative discrete data", "Quantitative continuous data"],
"correct": 2,
"hint": "Can this variable take fractional values?",
"feedback_correct": "This variable is a count.",
"feedback_wrong": {
0: "Nominal data are categories.",
1: "Ordinal data involve ranking.",
3: "Continuous data allow decimals."
},
"final_explanation": "The number of students is a count and therefore quantitative discrete data."
},

{
"id": "T1_Q3",
"question": "Which variable is quantitative continuous?",
"options": ["Number of cars owned", "Letter grade (A, B, C)", "Time taken to complete a task", "Number of absences"],
"correct": 2,
"hint": "Continuous variables are measured and can take decimal values.",
"feedback_correct": "Time is measured on a continuous scale.",
"feedback_wrong": {
0: "Number of cars is a count.",
1: "Letter grades are categorical.",
3: "Number of absences is a count."
},
"final_explanation": "Time can take any value within a range and is therefore continuous."
},

{
"id": "T1_Q4",
"question": "Gender is measured on which level of measurement?",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 0,
"hint": "Is there any natural ordering?",
"feedback_correct": "Gender has no natural order.",
"feedback_wrong": {
1: "Ordinal data require ranking.",
2: "Interval data are numerical.",
3: "Ratio data require a true zero."
},
"final_explanation": "Gender consists of categories without any inherent order."
},

{
"id": "T1_Q5",
"question": "Which measure of central tendency is most appropriate for nominal data?",
"options": ["Mean", "Median", "Mode", "Range"],
"correct": 2,
"hint": "Which measure works with categories?",
"feedback_correct": "Mode summarises the most frequent category.",
"feedback_wrong": {
0: "Mean requires numerical data.",
1: "Median requires ordered data.",
3: "Range measures spread, not centre."
},
"final_explanation": "Nominal data are categorical, so the mode is the appropriate measure."
},

# ---------------- LEVEL 2: UNDERSTANDING ----------------

{
"id": "T1_Q6",
"question": "Why is the mean generally not appropriate for nominal data?",
"options": [
"Nominal data contain extreme values",
"Nominal data have unequal intervals",
"Nominal data are categories without numerical meaning",
"Nominal data cannot be ordered"
],
"correct": 2,
"hint": "Think about what the mean represents mathematically.",
"feedback_correct": "Nominal data do not support arithmetic operations.",
"feedback_wrong": {
0: "Extreme values are not the defining issue.",
1: "Intervals do not apply to nominal data.",
3: "Ordering is not required to compute a mean."
},
"final_explanation": "The mean requires numerical values, but nominal data consist of labels or categories."
},

{
"id": "T1_Q7",
"question": "Which statement best explains why Likert-scale responses are usually treated as ordinal?",
"options": [
"They have a true zero",
"The intervals between values are equal",
"The categories can be ranked but intervals may not be equal",
"They are measured using numbers"
],
"correct": 2,
"hint": "Focus on what is guaranteed and what is not.",
"feedback_correct": "Likert categories have order without guaranteed equal spacing.",
"feedback_wrong": {
0: "A true zero is not present.",
1: "Equal intervals are not guaranteed.",
3: "Using numbers does not imply interval measurement."
},
"final_explanation": "Likert-scale responses are ordered categories, but the spacing between categories is not necessarily equal."
},

{
"id": "T1_Q8",
"question": "Why is temperature measured in degrees Celsius (°C) classified as interval data?",
"options": [
"It has a true zero",
"It allows ratio comparisons",
"It has equal intervals but no true zero",
"It is categorical"
],
"correct": 2,
"hint": "Consider what zero represents on this scale.",
"feedback_correct": "Celsius temperature lacks a true zero but has equal intervals.",
"feedback_wrong": {
0: "Zero degrees Celsius does not indicate absence of temperature.",
1: "Ratio comparisons are not meaningful.",
3: "Temperature is numerical, not categorical."
},
"final_explanation": "Temperature in °C has equal intervals, but zero does not represent the absence of temperature."
},

{
"id": "T1_Q9",
"question": "Which statement about ordinal data is correct?",
"options": [
"Differences between values are equal",
"A true zero exists",
"The data can be ranked",
"The mean is always appropriate"
],
"correct": 2,
"hint": "Ordinal data are defined by ordering.",
"feedback_correct": "Ordinal data support ranking.",
"feedback_wrong": {
0: "Equal intervals are not guaranteed.",
1: "A true zero applies to ratio data.",
3: "The mean is not generally appropriate."
},
"final_explanation": "Ordinal data can be ranked, but the differences between values are not measured on an equal scale."
},

{
"id": "T1_Q10",
"question": "Why is the median often preferred to the mean for skewed data?",
"options": [
"The median uses all data values",
"The median is affected by extreme values",
"The median is resistant to outliers",
"The median requires normality"
],
"correct": 2,
"hint": "Consider the effect of extreme values.",
"feedback_correct": "Median is less influenced by extreme values.",
"feedback_wrong": {
0: "Both mean and median use data values.",
1: "Median is less affected, not more.",
3: "Median does not require normality."
},
"final_explanation": "The median is resistant to outliers, making it more representative for skewed distributions."
},

# ---------------- LEVEL 3: APPLICATION ----------------

{
"id": "T1_Q11",
"question": "A city council records the number of cars owned by each household to plan parking facilities. What type of data is being collected?",
"options": ["Qualitative", "Quantitative continuous", "Quantitative discrete", "Ordinal"],
"correct": 2,
"hint": "Are the values counts or measurements?",
"feedback_correct": "The number of cars is counted in whole numbers.",
"feedback_wrong": {
0: "The data are numerical, not categorical.",
1: "The values cannot take fractional amounts.",
3: "There is no ranking involved."
},
"final_explanation": "The number of cars owned is a count and therefore quantitative discrete data."
},

{
"id": "T1_Q12",
"question": "A hospital asks patients to rate satisfaction as Very Poor, Poor, Fair, Good, or Excellent. How should this data be classified?",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 1,
"hint": "Can the responses be ranked meaningfully?",
"feedback_correct": "The categories have a clear order.",
"feedback_wrong": {
0: "The categories are ordered, not just labels.",
2: "Equal numerical intervals are not guaranteed.",
3: "There is no true zero point."
},
"final_explanation": "Patient satisfaction categories can be ranked, but the differences between categories are not numerically defined."
},

{
"id": "T1_Q13",
"question": "An online retailer analyses delivery times (in days): 2, 3, 3, 4, and 15. Which measure best represents the typical delivery time?",
"options": ["Mean", "Median", "Range", "Maximum"],
"correct": 1,
"hint": "Check for an unusually large value.",
"feedback_correct": "The median is not influenced by extreme values.",
"feedback_wrong": {
0: "The mean is pulled upward by the extreme value.",
2: "Range measures spread, not centre.",
3: "Maximum reflects only the longest delivery time."
},
"final_explanation": "Because the data include an extreme value, the median better represents the typical delivery time."
},

{
"id": "T1_Q14",
"question": "A fitness trainer records clients’ heights in centimetres to design workout programmes. Which level of measurement applies?",
"options": ["Nominal", "Ordinal", "Interval", "Ratio"],
"correct": 3,
"hint": "Does zero represent the absence of height?",
"feedback_correct": "Height has a meaningful zero and supports ratio comparisons.",
"feedback_wrong": {
0: "Height is numerical, not categorical.",
1: "Height is not ranked data.",
2: "Interval data do not have a true zero."
},
"final_explanation": "Height has a true zero point and allows meaningful ratio comparisons, so it is measured on a ratio scale."
},

{
"id": "T1_Q15",
"question": "A university records course results using letter grades (A, B, C, D, F). Which statement correctly describes this data?",
"options": [
"The data are quantitative continuous",
"The data are interval",
"The data are ordinal",
"The data are ratio"
],
"correct": 2,
"hint": "Can the categories be ordered meaningfully?",
"feedback_correct": "The grades form an ordered set of categories.",
"feedback_wrong": {
0: "Grades are not numerical measurements.",
1: "Differences between grades are not equal.",
3: "There is no true zero point."
},
"final_explanation": "Letter grades can be ranked, but numerical differences between grades are not defined."
}

]
