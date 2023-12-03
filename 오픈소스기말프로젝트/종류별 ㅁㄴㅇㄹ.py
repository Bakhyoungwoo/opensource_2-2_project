import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

matplotlib.rcParams['font.family']='Malgun Gothic'

# Sample data
sample_data = {
    'Cuisine Type': ['Korean', 'Chinese', 'Japanese', 'Western'] * 6,
    'Reason': ['Hiring Difficulties', 'Decreased Operating Profits', 'Regulatory Requirements', 'Increased Competition', 'Right to Receive Fees', 'Others'] * 4,
    'Percentage': [24.2, 38.9, 10.4, 22.3, 5.1, 9.1, 16.9, 48.9, 14.5, 28.2, 6.7, 10.2, 31.6, 53.7, 2.9, 35.4, 7.8, 11.3, 25.0, 40.0, 12.0, 30.0, 8.0, 12.0]
}

df_sample = pd.DataFrame(sample_data)

# Plotting the data
plt.figure(figsize=(10, 6))
sns.barplot(x='Cuisine Type', y='Percentage', hue='Reason', data=df_sample)
plt.title('Reasons for Business Change by Cuisine Type')
plt.xlabel('Cuisine Type')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=45)
plt.legend(title='Reasons', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()
