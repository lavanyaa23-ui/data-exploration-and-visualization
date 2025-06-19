# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Step 2: Load the dataset
df = pd.read_csv('spam.csv', encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

# Step 3: Understand the dataset
print(" First 5 Rows:")
print(df.head())

print("\n Data Info:")
print(df.info())

print("\n Data Description:")
print(df.describe())

# Step 4: Check for missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Step 5: Analyze class distribution
print("\n Class Distribution:")
print(df['label'].value_counts())

# Plot class distribution
plt.figure(figsize=(6,4))
sns.countplot(x='label', data=df, palette='Set2')
plt.title("Distribution of Spam vs Ham")
plt.xlabel("Message Type")
plt.ylabel("Count")
plt.show()

# Step 6: Add message length column and visualize
df['length'] = df['message'].apply(len)

plt.figure(figsize=(8,5))
df[df['label'] == 'ham']['length'].plot.hist(bins=50, alpha=0.7, label='Ham', color='skyblue')
df[df['label'] == 'spam']['length'].plot.hist(bins=50, alpha=0.7, label='Spam', color='salmon')
plt.legend()
plt.title("Histogram of Message Lengths")
plt.xlabel("Message Length")
plt.ylabel("Frequency")
plt.show()

# Step 7a: Average message length
print("\n Average Message Length:")
print("Ham:", df[df['label'] == 'ham']['length'].mean())
print("Spam:", df[df['label'] == 'spam']['length'].mean())

# Step 7b: Text-specific word frequency
def get_cleaned_words(messages):
    stop_words = set(stopwords.words('english'))
    words = []
    for msg in messages:
        for word in msg.lower().split():
            word = word.strip(string.punctuation)
            if word not in stop_words and word != "":
                words.append(word)
    return words

spam_words = get_cleaned_words(df[df['label'] == 'spam']['message'])
ham_words = get_cleaned_words(df[df['label'] == 'ham']['message'])

# Step 7c: Word Clouds
# Spam
spam_wc = WordCloud(width=600, height=400, background_color='white').generate(" ".join(spam_words))
plt.figure(figsize=(7,5))
plt.imshow(spam_wc, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud - Spam Messages")
plt.show()

# Ham
ham_wc = WordCloud(width=600, height=400, background_color='white').generate(" ".join(ham_words))
plt.figure(figsize=(7,5))
plt.imshow(ham_wc, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud - Ham Messages")
plt.show()

# Step 8: Correlation check
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})
plt.figure(figsize=(5,4))
sns.heatmap(df[['length', 'label_num']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Step 9: Conclusion
print("\n INSIGHTS:")
print("- Spam messages are generally longer than ham messages.")
print("- Spam messages use words like 'free', 'win', 'cash'.")
print("- Ham messages use more casual words like 'okay', 'home'.")
print("- Message length has moderate correlation with spam classification.")
