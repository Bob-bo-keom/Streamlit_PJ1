import streamlit as st

st.set_page_config(
	page_title='Streamlit 프로토타입 만들기',
	page_icon='🎈',
	layout='wide'
)

st.text('🎈김세원 : Streamlit 프로토타입 만들기')

st.title('📌진짜 확인하시는지 궁금합니다.')

st.header('Header(머리글)을 입력하세요.')
st.subheader('Subheader(세부 머리글)을 입력하세요.')

st.header("헤더 헤더")

st.markdown('안녕하세요, 여러분\n\n'
            '저는 김세원 입니다.')

st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')

st.markdown("1. 하나")
st.markdown("2. 둘")
st.markdown("1. 셋")

st.markdown("* 하나")
st.markdown("* 둘")
st.markdown("* 셋")

st.caption('이것은 Caption입니다.')

st.text("텍스트 입력")

st.code("코드 블록 표시")

import pandas as pd

stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)

st.dataframe(df_stocks)

st.dataframe(df_index.style.highlight_max(axis=0))

# symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))
# st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])
#
# symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')
# st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])
#
# st.line_chart(df_index, x='Date')
#
df_chart = pd.DataFrame(columns=['Date'])
df_chart['Date'] = df_stocks['Date'].unique()

for symbol in df_stocks['Symbol'].unique():
	df_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)

st.line_chart(df_chart, x='Date')

st.bar_chart(df_index.tail(30), x='Date')

symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')
symbol_list.insert(0, 'Date')
st.line_chart(df_chart[symbol_list], x='Date')

import datetime

st.write('검색 기간을 설정해 주세요.')
start_day = st.date_input(
	 '시작 일자',
	 datetime.date(2022, 1, 1))

end_day = st.date_input(
	 '종료 일자',
	 datetime.date(2022, 12, 31))

st.write(f'검색 기간 : {start_day} ~ {end_day}')
st.line_chart(df_index[(df_index['Date'] >= str(start_day)) & (df_index['Date'] <= str(end_day))], x='Date')