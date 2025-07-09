# 🧠 Ethical Reflection: AI Bias & Fairness in ML Applications

### 1. Bias in the MNIST Model
Even though MNIST is considered a "clean" dataset, it can still reflect biases:
- **Limited handwriting diversity**: Most digits come from American high school students.
- **Overfitting to style**: If tested on different cultural handwriting styles, accuracy may drop.
- **Accessibility bias**: Assumes all users can provide digital handwritten digits.

### Mitigation Techniques
- **TensorFlow Fairness Indicators**: These can assess model fairness across different slices (e.g., gender, age, writing tools).
- **Data Augmentation**: Add distortions, angles, or styles to better simulate real-world diversity.
- **Cross-dataset validation**: Test on datasets like EMNIST or Digits Datasets from other countries.

---

### 2. Bias in Amazon Reviews Sentiment Model
The spaCy + TextBlob sentiment pipeline may misinterpret:
- **Sarcasm**: “Great phone, broke in 2 days 🙄” may score as positive.
- **Dialectal language**: Slang or non-standard grammar may reduce performance.

### Mitigation Techniques
- **Custom rule-based NLP**: Adjust patterns to catch sarcasm, emojis, slang (e.g., "trash", "lit").
- **Balanced data**: Include more diverse reviews in terms of geography, product category, and expression style.
- **Lexicon expansion**: Extend the positive/negative word lists used in TextBlob.

---

### 3. Responsible AI Practice
- **Transparency**: Document model training data and limitations.
- **User-centered design**: Build interfaces that let users contest or clarify predictions.
- **Inclusive design**: Ensure datasets and models represent all user groups.
