
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Setting Korean font for matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# Load data from the Excel file
file_path = '음식주점업_시도_산업_객석_수_규모별_현황.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path, header=1)  # Assuming the header is in the first row

# Filtering and preparing the data
seat_categories = df[['시도별', '9석 이하 (개)', '10~19석 (개)', '20~29석 (개)', '30~49석 (개)', '50~99석 (개)', '100석 이상 (개)']]
seat_categories.columns = ['Region', '0-9 좌석', '10-19 좌석', '20-29 좌석', '30-49 좌석', '50-99 좌석', '100이상 좌석']
seat_categories = seat_categories[seat_categories['Region'] != '전국']  # Excluding nationwide data

# Converting numeric columns to numeric data types
for col in seat_categories.columns[1:]:
    seat_categories[col] = pd.to_numeric(seat_categories[col], errors='coerce')

# Plotting the stacked bar graph
plt.figure(figsize=(15, 10))
bottom = None
for col in seat_categories.columns[1:]:
    plt.bar(seat_categories['Region'], seat_categories[col], bottom=bottom, label=col)
    if bottom is None:
        bottom = seat_categories[col]
    else:
        bottom += seat_categories[col]

plt.title('지역별 음식점 갯수 (객석 수 별)')
plt.xlabel('지역')
plt.ylabel('음식점 수')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
