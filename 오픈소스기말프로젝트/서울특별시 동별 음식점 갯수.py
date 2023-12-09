import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Setting the font to Malgun Gothic for proper Korean character display
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# Load the Excel file
new_file_path = '식품위생업+현황(동별)(2008년+이후)_20231203151917.xlsx'
new_data = pd.read_excel(new_file_path)

# Filtering out the rows for '소계'
new_data_filtered = new_data[new_data['동별(2)'] != '소계']

# Renaming the columns for clarity
num_columns = len(new_data_filtered.columns)
new_column_names = ['Region_Main', 'Region_Sub', 'Total_2022', 'Food_Service_2022'] + [f'Column_{i}' for i in range(4, num_columns)]
new_data_filtered.columns = new_column_names

# Selecting only the 'Region_Sub' and 'Food_Service_2022' columns for the graph
graph_data_new = new_data_filtered[['Region_Sub', 'Food_Service_2022']]

# Dropping rows with NaN values and '동별(2)' in 'Region_Sub'
graph_data_new = graph_data_new.dropna(subset=['Region_Sub'])
graph_data_left = graph_data_new[graph_data_new['Region_Sub'] != '동별(2)']

# Converting 'Food_Service_2022' to numeric for plotting
graph_data_left['Food_Service_2022'] = pd.to_numeric(graph_data_left['Food_Service_2022'], errors='coerce')

# Extracting data for 일반음식점 (general restaurants)
general_restaurants_left = pd.to_numeric(new_data_filtered['Column_5'], errors='coerce')[new_data_filtered['Region_Sub'] != '동별(2)']

# Grouping by 'Region_Sub' and calculating max, min, and median
grouped_data = graph_data_left.groupby('Region_Sub')['Food_Service_2022'].agg(['max', 'min', 'median'])

# Finding the sub-regions corresponding to the max, min, and median values
max_region = grouped_data[grouped_data['max'] == grouped_data['max'].max()].index[0]
min_region = grouped_data[grouped_data['min'] == grouped_data['min'].min()].index[0]
median_region = grouped_data[grouped_data['median'] == grouped_data['median'].median()].index[0]

# Preparing data for the second graph
graph_values = {
    'Maximum': grouped_data.loc[max_region, 'max'],
    'Minimum': grouped_data.loc[min_region, 'min'],
    'Median': grouped_data.loc[median_region, 'median']
}
regions = [max_region, min_region, median_region]

# Creating a figure with two subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(17, 8))

# First graph: Number of Food Service Businesses by Sub-Region (excluding '동별(2)') and 일반음식점
axes[0].bar(graph_data_left['Region_Sub'], graph_data_left['Food_Service_2022'], color='green', label='식품업점 수')
axes[0].plot(graph_data_left['Region_Sub'], general_restaurants_left, color='red', marker='o', linestyle='-', label='일반음식점')
axes[0].set_xlabel('동별')
axes[0].set_ylabel('업체 수')
axes[0].set_title('2022년 동별 외식업 사업체 분포 및 일반음식점 (동별(2) 제외)')
axes[0].tick_params(axis='x', rotation=90)
axes[0].legend()

# Second graph: Regions with Max, Min, and Median Number of Businesses
axes[1].bar(regions, graph_values.values(), color=['red', 'blue', 'green'])
axes[1].set_xlabel('동별')
axes[1].set_ylabel('식품업점 수')
axes[1].set_title('2022년 외식업 사업체의 최대, 최소, 중간값 지역')
axes[1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
