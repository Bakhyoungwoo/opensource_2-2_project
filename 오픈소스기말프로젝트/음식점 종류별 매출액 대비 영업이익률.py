import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

matplotlib.rcParams['font.family']='Malgun Gothic'
# Load the data
file_path = 'opensource_2-2_project-main\오픈소스기말프로젝트\수익성·생산성_분석_22년도_기준.xlsx'
df = pd.read_excel(file_path)

# Filter the data to exclude '소계' in '특성별(4)' and convert data types
df_filtered = df[df['특성별(4)'] != '소계']
df_filtered['특성별(4)'] = df_filtered['특성별(4)'].astype(str)
df_filtered['2022'] = pd.to_numeric(df_filtered['2022'], errors='coerce')

# Create a line plot
plt.figure(figsize=(12, 6))
sns.lineplot(x=df_filtered['특성별(4)'], y=df_filtered['2022'])

# Adding titles and labels
plt.title('음식점 종류별 매출액 대비 영업이익률 (%)')
plt.xlabel('음식점 종류')
plt.ylabel('매출액 대비 영업이익률 (%)')

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
