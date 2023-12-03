import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
def get_service_stats():
  """
  서비스업 조사 테이블의 요소들을 가져옵니다.
  """
  url = "https://www.atfis.or.kr/fip/front/M000000268/stats/service.do"
  # 페이지 요청
  request = requests.get(url)
  soup = BeautifulSoup(request.text, "html.parser")
  data = soup.find("table", {"class": "left"})
  print (data)
  