import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Setting the font to Malgun Gothic
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# Load the Excel file
file_path = 'opensource_2-2_project-main\오픈소스기말프로젝트\수익성·생산성_분석_22년도_기준.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Filter and process the data
filtered_data = data[(data['특성별(4)'] != '소계') & ~data['2022.3'].isna()]
filtered_data = filtered_data.iloc[1:]  # Skip the first row with column names
filtered_data['좌석 당 매출액'] = pd.to_numeric(filtered_data['2022.3'])

# Group and calculate statistics
grouped_data = filtered_data.groupby('특성별(4)')['좌석 당 매출액']
mean_data = grouped_data.mean()

# Identify categories with the highest, lowest, and average values
max_category = mean_data.idxmax()
min_category = mean_data.idxmin()
average_value = mean_data.mean()
closest_to_average_category = (mean_data - average_value).abs().idxmin()

# Assign colors based on the criteria
colors = ['grey' if category not in [max_category, min_category, closest_to_average_category] else 
          'red' if category == max_category else 
          'green' if category == min_category else 
          'blue' for category in mean_data.index]

# Plotting
plt.figure(figsize=(12, 6))  # Adjust figure size for better layout
mean_data.plot(kind='bar', color=colors)
plt.title('평균 금액')
plt.ylabel('금액 (만원)')

# Adding a line for the average and updating the legends with positioning outside the graph
plt.axhline(y=average_value, color='blue', linestyle='--', label='평균에 가까운 금액')
plt.legend(handles=[
    plt.Line2D([0], [0], color='red', lw=4, label='좌석당 최대 매출액'),
    plt.Line2D([0], [0], color='green', lw=4, label='좌석당 최소 매출액'),
    plt.Line2D([0], [0], color='blue', lw=4, label='좌석당 평균 매출액'),
    plt.Line2D([0], [0], color='blue', linestyle='--', lw=2, label='평균에 가까운 금액')
], loc='upper left', bbox_to_anchor=(1, 1))  # Legend outside the plot

plt.tight_layout()
plt.show()
