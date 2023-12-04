import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

matplotlib.rcParams['font.family']='Malgun Gothic'
# Data preparation
data = {
    'Region': ['경기도', '서울특별시', '경상남도', '부산광역시', '경상북도', '인천광역시', '대구광역시', '충청남도', '강원도', '전라남도', '충청북도', '전라북도', '대전광역시', '광주광역시', '울산광역시', '제주특별자치도', '세종특별자치시'],
    'BusinessCount': [172168.0, 135182.0, 62518.0, 54935.0, 50244.0, 39116.0, 37299.0, 37172.0, 35139.0, 32669.0, 29194.0, 28629.0, 22658.0, 21744.0, 19533.0, 17962.0, 4486.0]
}

df = pd.DataFrame(data)

# Plotting the graph
plt.figure(figsize=(10,6))
plt.plot(df['Region'], df['BusinessCount'], marker='o')
plt.title('지역별 음식점 갯수')
plt.xlabel('지역')
plt.ylabel('음식점 수')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
