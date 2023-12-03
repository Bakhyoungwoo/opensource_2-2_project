import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

matplotlib.rcParams['font.family']='Malgun Gothic'

file_path = '수익성·생산성_분석_22년도_기준.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Filter out the rows with '소계' in 특성별(4) and convert columns to numeric
filtered_data = data[(data['특성별(4)'] != '소계') & ~data['2022.3'].isna()]
filtered_data = filtered_data.iloc[1:]  # Skip the first row with column names
filtered_data['좌석 당 매출액'] = pd.to_numeric(filtered_data['2022.3'])

# Grouping the data by '특성별(4)' and performing statistical analysis
grouped_data = filtered_data.groupby('특성별(4)')['좌석 당 매출액']
mean_data = grouped_data.mean()
min_data = grouped_data.min()
max_data = grouped_data.max()
std_dev_data = grouped_data.std()

# Plotting the statistical analysis results
plt.figure(figsize=(14, 8))

# Mean values
plt.subplot(1, 3, 1)
mean_data.plot(kind='bar', color='skyblue')
plt.title('평균 금액 per ')
plt.ylabel('금액 (만원)')

# Minimum values
plt.subplot(1, 3, 2)
min_data.plot(kind='bar', color='lightgreen')
plt.title('최소 금액 ')
plt.ylabel('금액 (만원)')

# Maximum values
plt.subplot(1, 3, 3)
max_data.plot(kind='bar', color='salmon')
plt.title('최대 금액')
plt.ylabel('금액 (만원)')


plt.tight_layout()
plt.show()
