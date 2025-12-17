QUESTIONS = [
    {
        "id": "T1_Q1",
        "question": "Which of the following is qualitative (categorical) data?",
        "options": ["Height", "Weight", "Blood group", "Age"],
        "correct": 2,
        "hint": "Hint:Consider whether the variable represents categories or numerical measurements.",
        "feedback_correct": "Blood group is categorical and therefore qualitative data.",
        "feedback_wrong": {
            0: "Height is measured numerically and is quantitative data.",
            1: "Weight is measured numerically and is quantitative data.",
            3: "Age is numerical and is treated as quantitative data."
        },
        "final_explanation": "Correct answer: C. Blood group consists of categories rather than numerical measurements, so it is qualitative (nominal) data."
    },
    {
        "id": "T1_Q2",
        "question": "The number of students in a class is best classified as:",
        "options": ["Nominal data", "Ordinal data", "Quantitative discrete data", "Quantitative continuous data"],
        "correct": 2,
        "hint": "Hint:Ask yourself whether the variable can take fractional values.",
        "feedback_correct": "This variable is a count and is therefore quantitative discrete data.",
        "feedback_wrong": {
            0: "Nominal data are categories, not numerical counts.",
            1: "Ordinal data involve ranking, not counting.",
            3: "Continuous data can take decimal values; counts cannot."
        },
        "final_explanation": "Correct answer: C. The number of students is a count (0, 1, 2, …), so it is quantitative discrete data."
    },
    {
        "id": "T1_Q3",
        "question": "Which variable is quantitative continuous?",
        "options": ["Number of cars owned", "Letter grade (A, B, C)", "Time taken to complete a task", "Number of absences"],
        "correct": 2,
        "hint": "Hint:Continuous variables are measured and can take decimal values.",
        "feedback_correct": "Time can take any value within a range, so it is quantitative continuous.",
        "feedback_wrong": {
            0: "Number of cars is a count and is discrete.",
            1: "Letter grades are categorical data.",
            3: "Number of absences is a count and is discrete."
        },
        "final_explanation": "Correct answer: C. Time is measured and can take decimal values, so it is quantitative continuous data."
    },
    {
        "id": "T1_Q4",
        "question": "Gender is measured on which level of measurement?",
        "options": ["Nominal", "Ordinal", "Interval", "Ratio"],
        "correct": 0,
        "hint": "Hint:Nominal variables are categories with no natural order.",
        "feedback_correct": "Gender consists of categories with no inherent order, so it is nominal.",
        "feedback_wrong": {
            1: "Ordinal data require ranking; gender categories have no ranking.",
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
        "hint": "Hint:Check whether the categories can be ranked.",
        "feedback_correct": "The categories have a natural order, making the data ordinal.",
        "feedback_wrong": {
            0: "Nominal categories have no order.",
            2: "Equal numerical intervals are not guaranteed for these categories.",
            3: "Ratio data require a true zero, which does not apply here."
        },
        "final_explanation": "Correct answer: B. Satisfaction levels can be ranked, but the differences between categories are not measurable, so the data are ordinal."
    },
    {
        "id": "T1_Q6",
        "question": "Which of the following is an example of nominal data?",
        "options": ["Blood type (A, B, AB, O)", "Class position (1st, 2nd, 3rd)", "Temperature in °C", "Weight (kg)"],
        "correct": 0,
        "hint": "Hint:Nominal data are categories with no order.",
        "feedback_correct": "Blood type is categorical with no natural order, so it is nominal.",
        "feedback_wrong": {
            1: "Class position is ranked, so it is ordinal.",
            2: "Temperature is numerical, not nominal.",
            3: "Weight is numerical, not nominal."
        },
        "final_explanation": "Correct answer: A. Blood type is a set of categories without ordering, so it is nominal."
    },
    {
        "id": "T1_Q7",
        "question": "Which of the following is an example of ordinal data?",
        "options": ["Hair colour", "Movie rating (1–5 stars)", "Height", "Age"],
        "correct": 1,
        "hint": "Hint:Ordinal data are ordered categories (ranked).",
        "feedback_correct": "Movie ratings are ordered categories, so they are ordinal.",
        "feedback_wrong": {
            0: "Hair colour is nominal (no order).",
            2: "Height is quantitative continuous.",
            3: "Age is quantitative."
        },
        "final_explanation": "Correct answer: B. Movie ratings have a natural order, so they are ordinal data."
    },
    {
        "id": "T1_Q8",
        "question": "Which of the following is quantitative discrete data?",
        "options": ["Time taken to travel to campus", "Number of siblings", "Body temperature", "Distance travelled"],
        "correct": 1,
        "hint": "Hint:Discrete data are counted and take whole-number values.",
        "feedback_correct": "Number of siblings is a count, so it is quantitative discrete.",
        "feedback_wrong": {
            0: "Time is measured and typically continuous.",
            2: "Temperature is measured and continuous.",
            3: "Distance is measured and continuous."
        },
        "final_explanation": "Correct answer: B. Number of siblings is a count (0, 1, 2, …), so it is discrete."
    },
    {
        "id": "T1_Q9",
        "question": "Which level of measurement describes numerical data with equal intervals but no true zero?",
        "options": ["Nominal", "Ordinal", "Interval", "Ratio"],
        "correct": 2,
        "hint": "Hint:Interval scales have equal spacing but do not have an absolute zero.",
        "feedback_correct": "Interval data have equal intervals but no true zero.",
        "feedback_wrong": {
            0: "Nominal data are categories without order.",
            1: "Ordinal data are categories with order but unequal intervals.",
            3: "Ratio data have a true zero."
        },
        "final_explanation": "Correct answer: C. Interval data have equal intervals but no true zero."
    },
    {
        "id": "T1_Q10",
        "question": "Temperature measured in degrees Celsius (°C) is classified as:",
        "options": ["Nominal", "Ordinal", "Interval", "Ratio"],
        "correct": 2,
        "hint": "Hint:Consider whether the scale has equal intervals and a true zero.",
        "feedback_correct": "Celsius temperature has equal intervals but no true zero, so it is interval data.",
        "feedback_wrong": {
            0: "Celsius temperature is numerical, not categorical.",
            1: "Celsius temperature is not ranked categories.",
            3: "Ratio scales require a true zero; °C does not have one."
        },
        "final_explanation": "Correct answer: C. Temperature in °C has equal intervals but no true zero, so it is interval data."
    },
    {
        "id": "T1_Q11",
        "question": "Which of the following is an example of ratio data?",
        "options": ["Year of birth", "Temperature in °C", "Weight", "Letter grade (A, B, C)"],
        "correct": 2,
        "hint": "Hint:Ratio data have a true zero and allow meaningful ratio statements.",
        "feedback_correct": "Weight has a true zero and supports ratio comparisons, so it is ratio data.",
        "feedback_wrong": {
            0: "Years are interval data, not ratio data.",
            1: "Celsius temperature is interval data, not ratio data.",
            3: "Letter grades are categorical data."
        },
        "final_explanation": "Correct answer: C. Weight has a true zero and allows meaningful ratios, so it is ratio data."
    },
    {
        "id": "T1_Q12",
        "question": "For which type of data is it generally appropriate to calculate the mean?",
        "options": ["Nominal", "Ordinal", "Interval", "Nominal and ordinal"],
        "correct": 2,
        "hint": "Hint:The mean requires numerical data with meaningful intervals.",
        "feedback_correct": "Interval data are numerical with meaningful differences, so the mean is appropriate.",
        "feedback_wrong": {
            0: "Nominal data are categories, so the mean is not meaningful.",
            1: "Ordinal data do not guarantee equal intervals.",
            3: "Mean is not generally meaningful for nominal or ordinal categories."
        },
        "final_explanation": "Correct answer: C. Interval data support meaningful differences, so the mean is generally appropriate."
    },
    {
        "id": "T1_Q13",
        "question": "Which measure of central tendency is most appropriate for nominal data?",
        "options": ["Mean", "Median", "Mode", "Range"],
        "correct": 2,
        "hint": "Hint:For nominal categories, frequency-based summaries are appropriate.",
        "feedback_correct": "Mode identifies the most frequent category and is appropriate for nominal data.",
        "feedback_wrong": {
            0: "Mean requires numerical data.",
            1: "Median requires ordered data.",
            3: "Range measures spread, not central tendency."
        },
        "final_explanation": "Correct answer: C. The mode is appropriate for nominal data."
    },
    {
        "id": "T1_Q14",
        "question": "Which statement about ordinal data is correct?",
        "options": ["Differences between values are equal", "The data can be ranked", "A true zero exists", "The mean is always appropriate"],
        "correct": 1,
        "hint": "Hint:Ordinal data support ordering (ranking), but intervals are not equal.",
        "feedback_correct": "Ordinal data can be ranked, but equal intervals are not guaranteed.",
        "feedback_wrong": {
            0: "Equal intervals are a property of interval/ratio scales.",
            2: "A true zero is a property of ratio scales.",
            3: "The mean is not generally appropriate for ordinal categories."
        },
        "final_explanation": "Correct answer: B. Ordinal data can be ranked, but the differences between categories are not measured on an equal-interval scale."
    },
    {
        "id": "T1_Q15",
        "question": "Which variable is incorrectly classified?",
        "options": ["Height – continuous", "Age – continuous", "Number of siblings – continuous", "Income – ratio"],
        "correct": 2,
        "hint": "Hint:Check whether the variable can take fractional values.",
        "feedback_correct": "Number of siblings is a count and should be classified as discrete, not continuous.",
        "feedback_wrong": {
            0: "Height is measured on a continuous scale, so this classification is correct.",
            1: "Age is commonly treated as a continuous variable, so this classification is correct.",
            3: "Income has a true zero and is ratio data, so this classification is correct."
        },
        "final_explanation": "Correct answer: C. Number of siblings is a count (0, 1, 2, …) and cannot be fractional; therefore, it is discrete, not continuous."
    },
    {
        "id": "T1_Q16",
        "question": "Which level of measurement allows meaningful statements such as “twice as much”?",
        "options": ["Nominal", "Ordinal", "Interval", "Ratio"],
        "correct": 3,
        "hint": "Hint:Ratio data have a true zero and allow multiplication/division comparisons.",
        "feedback_correct": "Ratio data support meaningful ratio comparisons because they have a true zero.",
        "feedback_wrong": {
            0: "Nominal data are categories without numerical meaning.",
            1: "Ordinal data allow ranking, but not ratio comparisons.",
            2: "Interval data lack a true zero, so ratios are not meaningful."
        },
        "final_explanation": "Correct answer: D. Ratio data have a true zero, so statements like “twice as much” are meaningful."
    },
    {
        "id": "T1_Q17",
        "question": "Likert-scale responses (1–5) are best classified as:",
        "options": ["Nominal", "Ordinal", "Interval", "Ratio"],
        "correct": 1,
        "hint": "Hint:Likert scales have order, but equal spacing is not guaranteed.",
        "feedback_correct": "Likert-scale responses are ordered categories, so they are best treated as ordinal.",
        "feedback_wrong": {
            0: "There is a natural order, so nominal is not best.",
            2: "Equal intervals are not guaranteed for Likert categories.",
            3: "There is no true zero, so ratio is not appropriate."
        },
        "final_explanation": "Correct answer: B. Likert-scale data are ordered categories and are best treated as ordinal."
    },
    {
        "id": "T1_Q18",
        "question": "Which variable may be classified differently depending on how it is recorded?",
        "options": ["Gender", "Blood group", "Age", "Education level"],
        "correct": 3,
        "hint": "Hint:Some variables can be recorded as categories or as numbers.",
        "feedback_correct": "Education level can be recorded in different ways, which can change its classification.",
        "feedback_wrong": {
            0: "Gender is typically recorded as nominal categories.",
            1: "Blood group is nominal categorical data.",
            2: "Age is numerical and typically treated as quantitative."
        },
        "final_explanation": "Correct answer: D. Education level may be recorded as ordinal categories or as a numerical variable (e.g., years of schooling), so its classification can vary by context."
    },
    {
        "id": "T1_Q19",
        "question": "Which operation is not meaningful for ordinal data?",
        "options": ["Ranking", "Finding the mode", "Finding the median", "Calculating differences"],
        "correct": 3,
        "hint": "Hint:Ordinal data do not have equal intervals.",
        "feedback_correct": "Differences between ordinal categories are not meaningful because spacing is not measured.",
        "feedback_wrong": {
            0: "Ranking is meaningful for ordinal data.",
            1: "Mode can be found for ordinal data.",
            2: "Median can be found for ordinal data."
        },
        "final_explanation": "Correct answer: D. Ordinal data support order but not equal intervals, so numerical differences are not meaningful."
    },
    {
        "id": "T1_Q20",
        "question": "Which statement best describes interval data?",
        "options": ["Categories with a natural order", "Numerical data with a true zero", "Numerical data with equal intervals but no true zero", "Categories with no natural order"],
        "correct": 2,
        "hint": "Hint:Interval scales have equal spacing but no absolute zero.",
        "feedback_correct": "Interval data have equal intervals but no true zero.",
        "feedback_wrong": {
            0: "This describes ordinal data.",
            1: "This describes ratio data.",
            3: "This describes nominal data."
        },
        "final_explanation": "Correct answer: C. Interval data are numerical with equal intervals but no true zero."
    }
]
