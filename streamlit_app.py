import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # 시각화 라이브러리

# Streamlit for sin and cos fuction visualiztion
st.title('Streamlit for sin and cos fuction visualiztion')

x_start = st.slider('x 시작값' ,  0.0, 10.0, 0.0)
x_end = st.slider('x 시작값' ,  10.0, 20.0, 10.0)
x = np.linspace(x_start, x_end)

y_sin = np.sin(x)
y_cos = np.cos(x)


fig , ax = plt.subplots()

ax.plot(x, y_sin)
ax.plot(x, y_cos)
ax.legend(['sin', 'cos'])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('sin and cos fuction')

st.pyplot(fig)

@st.cache
def expensive_computataion(x):
    return np.sin(x) + np.cos(x)

result = expensive_computataion(x)



#1
import plotly.express as px

data_canada = px.data.gapminder().query("country == 'Canada'")
data_canada
fig1 = px.bar(data_canada, x='year' , y='pop')
st.plotly_chart(fig1)


#2
df = px.data.gapminder().query("continent == 'Oceania'")
df
fig2 = px.bar(df, x = 'year' , y = 'pop' , color = 'country' ,
             labels = {'pop' : 'population of Canada'} , hover_data = ['lifeExp','gdpPercap']
             , barmode = 'group')
st.plotly_chart(fig2)


#3
fig3 = px.bar(df, x = 'year' , y = 'pop' , color = 'country' ,
             labels = {'pop' : 'population of Canada'} , hover_data = ['lifeExp','gdpPercap']
             ,pattern_shape_sequence=["."
             ,'+'])
st.plotly_chart(fig3)

#4
import plotly.graph_objs as go
fig4 = go.Figure(data = go.Bar(
    x = [1,2,3,5.5,10],
    y = [10,8,6,4,2],
    width=[0.8,0.8,0.8, 3.5, 4]
))
st.plotly_chart(fig4)

#5
data_canada = px.data.gapminder().query("country == 'Canada'")
data_canada
fig5 = px.line(data_canada, x = 'year', y = 'lifeExp' ,
              title = 'Life expectacy in Canada')
st.plotly_chart(fig5)

#6
df_1 = px.data.gapminder().query("continent == 'Oceania'")
df_1
fig6 = px.line(df_1, x = 'year', y = 'pop' , color ='country' , symbol='country')
st.plotly_chart(fig6)

#7 piecharts
df_2 = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df_2
fig7 = px.pie(df_2, values = 'pop',  names = 'country' , title = 'population of European contintent')
st.plotly_chart(fig7)

#8 donut chart
labels = ['A','B', 'C' ,'D']
values = [300,200,100,500]
fig8 = go.Figure(data = [go.Pie(labels = labels, values = values, hole=.3)]) # hole 도넛차트 구현
st.plotly_chart(fig8)

#9 donut chart_specific
fig9 = go.Figure(data = [go.Pie(labels = labels, values = values, pull = [0 , 0, 0.2,0])])
st.plotly_chart(fig9)

#10 heatmaps

fig10 = px.imshow([[1,23,49],[123,5,4],[45,6,3]]
                )
st.plotly_chart(fig10)


#11 boxplots
df_3 = px.data.tips()
df_3
fig11 = px.box(df_3, y = 'total_bill' , x = 'time' , points = 'all' , color = 'smoker')
st.plotly_chart(fig11)

#12 boxplots_details
fig12 = px.box(df_3, y = 'total_bill' , x = 'day' , points = 'all' , color = 'smoker')
st.plotly_chart(fig12)

#13 bubble charts
df_4 = px.data.gapminder()
df_4
fig13 = px.scatter(df_4.query("year == 2007"), x = 'gdpPercap' , y = 'lifeExp', size = 'pop', color = 'continent')
st.plotly_chart(fig13)

#14 Treemap
df_5 = px.data.gapminder().query("year == 2007")
df_5
fig14 = px.treemap(df_5, path=[px.Constant('World'), 'continent','country'], values = 'pop' , color = 'lifeExp')
st.plotly_chart(fig14)

# Plotly시각화 상.ipynb
#fig15_barchart
#-width = 가로 크기 조절
#-height = 세로 크기 조절

st.title("Plotly시각화 상.ipynb")
st.text("fig_15_barchart")
st.text("-width = 가로 크기 조절")
st.text("-height = 세로 크기 조절")

fig15 = px.bar(x=["a", "b", "c"], y=[1, 3, 2], width = 600, height = 400)
st.plotly_chart(fig15)

#fig16_margin
st.text("fig16_margin")

fig16 = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig16.update_layout(
    width = 600,
    height = 400,
    margin_l =50, #
    margin_r =50, #
    margin_t =100, #
    margin_b =100 #
)

st.plotly_chart(fig16)

#fig17_title_in_chart
st.markdown("""
    ---
    fig17_title_in_chart
    """)
fig17 = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig17.update_layout( title_text = 'Bar Chart') #title_text =
st.plotly_chart(fig17)

#fig18
st.markdown("""
    ---
    - Express 사용법
    - Graph object 사용법
    """)

import plotly.graph_objects as go
fig18 = go.Figure(go.Bar(x=['A','B','C'], y = [1,3,2]))
st.plotly_chart(fig18)

#fig19
st.markdown("""
---
Font 스타일 지정 (색, 서체, 크기)
""")

fig19 = px.bar(x=["a", "b", "c"], y=[1, 3, 2], title = 'Bar Chart') #title =
fig19.update_layout(
    title_y = 0.9, # 0~1 1은 맨 윗쪽
    title_x = 0.5, # 0~1 1은 맨 오른쪽
    title_xanchor = 'center',
    title_yanchor = 'middle',

    #폰트 스타일 추가
    title_font_size = 50,
    title_font_family = 'Times', #일반적인 기본글꼴 적용
    title_font_color = 'red'
)
st.plotly_chart(fig19)

#fig20
st.markdown("""
---
축타이틀 설정
""")
df_6 = px.data.tips()
df_6
fig20 = px.scatter(df_6, x = 'total_bill', y = 'tip') #축이름 설정  x = 'total_bill', y = 'tip'
st.plotly_chart(fig20)

st.markdown("""
    - 축이름 설정  x = 'total_bill', y = 'tip'
    - 산점도
    - 가로축 : 값정보(수치)
    - 세로축 : 값정보(수치)
    - 가로축과 세로축간에 어떤 관계 , 경향을 보이는지 체크가능
""")

#fig21_scatter_colored
# used df_6

st.markdown("""
---
fig21_scatter_colored
""")
fig21 = px.scatter(df_6, x = 'total_bill', y = 'tip', color = 'sex') #축 설정  x = 'total_bill', y = 'tip'
st.plotly_chart(fig21)
st.markdown("""
---
    - 축 설정  x = 'total_bill', y = 'tip'
""")


#fig22_scatter_colored_with_unit
# used df_6
st.markdown("""
---
fig22_scatter_colored_with_unit
""")

fig22 = px.scatter(df_6, x = 'total_bill', y = 'tip', color = 'sex',
                 labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)' ) )
#축레이블 설정  labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)'
st.plotly_chart(fig22)
st.markdown("""
---
    - 축레이블 설정  labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)'
""")

#fig23_
# used df_6
st.markdown("""
---
fig23_scatter_colored_with_unit
""")


#fig23 = px.scatter(df_6, x = 'total_bill', y = 'tip', color = 'sex',
#                 labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)' ) )
#축레이블 설정  labels = dict(total_bill ='total_bill($)' ,tip = 'tip($)'

#fig23.updata_xaxes(title_text = 'total_bill($)')
#fig23.updata_yaxes(title_text = 'tip($)')
#st.plotly_chart(fig23)


#fig24_
st.markdown("""
fig24 Qiz 막대 그래프 그리기
---
    - 주어진 데이터 x = ['A', 'B', 'C', 'D']와 y = [10, 15, 7, 12]를 사용하여 막대 그래프를 그립니다.   
    - 그래프의 가로 크기를 800픽셀, 세로 크기를 600픽셀로 설정하고, 그래프의 제목을 "카테고리별 수치"로 지정합니다.  
---
""")

fig24 = px.bar(x = ['A', 'B', 'C', 'D'], y = [10, 15, 7, 12], title = '카테고리별 수치')
fig24.update_layout(width = 800, height = 600)
st.plotly_chart(fig24)


#fig25
st.markdown("""
---
fig25 
""")

x = ['A', 'B', 'C', 'D']
y = [10, 200, 7, 12]
fig25 = go.Figure(data=go.Bar(x=x,y=y))
fig25.update_layout(
    title = '카테고리별 수치',
    width = 800,
    height = 600
)
st.plotly_chart(fig25)


#fig26
#used df_7
st.markdown("""
---
fig26 
# 축 범위 지정하기

```
fig.update_xaxes(range = [0,10])
fig.update_yaxes(range = [0,10])
```

""")

df_7 = px.data.iris() #붓꽃
df_7
fig26 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' ,color = 'species' )
st.plotly_chart(fig26)
#전체 종 데이터의 혼합표현

#fig27
st.markdown("""
---
### fig27
### facet_col
- 데이터가 좀 더 해석력을 가질 수 있게 해 주는 코드 중에 하나

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.show()
```
""")

fig27 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
st.plotly_chart(fig27)

#fig28
st.markdown("""
---
### fig28 facet_col

```
fig.update_xaxes(range = [0,10])
fig.update_yaxes(range = [0,10])
```
""")
fig28 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig28.update_xaxes(range = [0,10])
fig28.update_yaxes(range = [0,10])
st.plotly_chart(fig28)

#fig29
st.markdown("""
---
### fig29 그래프 축 역으로 설정

```
fig.update_yaxes(autorange='reversed')
```
""")
fig29 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig29.update_xaxes(range = [0,10])
fig29.update_yaxes(range = [0,10])
fig29.update_yaxes(autorange='reversed')
st.plotly_chart(fig29)

#fig30
st.markdown("""
---
### fig30  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='outside')
fig.show()
```
""")
fig30 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig30.update_yaxes(ticks='outside')
st.plotly_chart(fig30)

#fig31
st.markdown("""
---
### fig31  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='inside')
fig.show()
```
""")
fig31 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig31.update_yaxes(ticks='inside')
st.plotly_chart(fig31)

#fig32
st.markdown("""
---
### fig32  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='inside' , col = 3)# col = 1,2,3 표현한고 싶은 컬럼에 설정
fig.show()
```
""")
fig32 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig32.update_yaxes(ticks='inside' , col = 3)# col = 1,2,3 표현한고 싶은 컬럼에 설정
st.plotly_chart(fig32)

#fig33
st.markdown("""
---
### fig33  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='inside' , col = 1, dtick=0.2) #dtick=0.2 축 간격설정가능
fig.show()
```
""")
fig33 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig33.update_yaxes(ticks='inside' , col = 1, dtick=0.2) #dtick=0.2 축 간격설정가능
st.plotly_chart(fig33)


#fig34
st.markdown("""
---
### fig34  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='inside' , col = 1 )
fig.update_yaxes(tickvals=[5.3,6.4] )  #tickvals=[5.3,6.4]
fig.show()
```
""")
fig34 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig34.update_yaxes(ticks='inside' , col = 1) #dtick=0.2 축 간격설정가능
fig34.update_yaxes(tickvals=[5.3,6.4] )  #tickvals=[5.3,6.4]
st.plotly_chart(fig34)

#fig35
st.markdown("""
---
### fig35  눈금 , tick 레이블 표시 설정

```
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_yaxes(ticks='outside' , tickwidth = 2, tickcolor = 'crimson'  )
fig.show()
```
- minor_tickcolor
```
fig.update_yaxes(minor_ticks='outside' , minor_tickcolor = 'black')
fig.update_xaxes(minor_ticks='outside' , minor_tickcolor = 'black')
```

""")

fig35 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig35.update_yaxes(ticks='outside' , tickwidth = 2, tickcolor = 'crimson'  )
fig35.update_yaxes(minor_ticks='outside' , minor_tickcolor = 'black')
fig35.update_xaxes(minor_ticks='outside' , minor_tickcolor = 'black')
st.plotly_chart(fig35)



#fig36
#used df_8
st.markdown("""
---
### fig36 축스타일 지정

```python
fig.update_xaxes(showline=True , linewidth = 2, linecolor = 'black' , col = 1) # col = 1 컬럼지정 가능
fig.update_yaxes(showline=True , linewidth = 2, linecolor = 'red')
```

""")

df_8 = px.data.tips()
fig36 = px.histogram(df_8, x = 'sex', y ='tip', histfunc  = 'sum', facet_col = 'smoker')
st.plotly_chart(fig36)


#fig37_used df_8
st.markdown("""
---
### fig37 축스타일 지정

```python
fig = px.histogram(df, x = 'sex', y ='tip', histfunc  = 'sum', facet_col = 'smoker')
fig.update_xaxes(showline=True , linewidth = 2, linecolor = 'black' , col = 1)
fig.update_yaxes(showline=True , linewidth = 2, linecolor = 'red')```

""")

df_8 = px.data.tips()
fig37 = px.histogram(df_8, x = 'sex', y ='tip', histfunc  = 'sum', facet_col = 'smoker')
fig37.update_xaxes(showline=True , linewidth = 2, linecolor = 'black' , col = 1)
fig37.update_yaxes(showline=True , linewidth = 2, linecolor = 'red')
st.plotly_chart(fig37)


#fig38_used df_8
st.markdown("""
---
### fig38 축스타일 지정

```python
fig = px.histogram(df, x = 'sex', y ='tip', histfunc  = 'sum', facet_col = 'smoker')
fig.update_xaxes(showline=True , linewidth = 2, linecolor = 'black' ,mirror= True)
fig.update_yaxes(showline=True , linewidth = 2, linecolor = 'red',mirror= True)
```

""")
df_8 = px.data.tips()
fig38 = px.histogram(df_8, x = 'sex', y ='tip', histfunc  = 'sum', facet_col = 'smoker')
fig38.update_xaxes(showline=True , linewidth = 2, linecolor = 'black' ,mirror= True)
fig38.update_yaxes(showline=True , linewidth = 2, linecolor = 'red',mirror= True)
st.plotly_chart(fig38)

#fig39 used df_7
st.markdown("""
---
### fig39 그리드 설정

```python
df = px.data.iris() #붓꽃
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.show()
```

""")

fig39 = px.scatter(df_7, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species',color = 'species' )
st.plotly_chart(fig39)



#fig40 usde df_7 = df_9

st.markdown("""
---
### fig40 그리드 설정

```python
fig = px.scatter(df, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig.update_xaxes(showgrid=True, griddash = 'dash' ,gridcolor = 'burlywood',minor_showgrid = True, minor_gridcolor='gray', minor_griddash = 'dot')
fig.update_yaxes(showgrid=True, griddash = 'dash' ,gridcolor = 'burlywood', minor_showgrid = True, minor_gridcolor='gray' , minor_griddash = 'dot')
fig.show()
```

""")

df_9 = px.data.iris() #붓꽃
fig40 = px.scatter(df_9, x = 'sepal_width' , y = 'sepal_length' , facet_col = 'species' )
fig40.update_xaxes(showgrid=True, griddash = 'dash' ,gridcolor = 'burlywood',minor_showgrid = True, minor_gridcolor='gray', minor_griddash = 'dot')
fig40.update_yaxes(showgrid=True, griddash = 'dash' ,gridcolor = 'burlywood', minor_showgrid = True, minor_gridcolor='gray' , minor_griddash = 'dot')
st.plotly_chart(fig40)


#fig41 
st.markdown("""
---
### fig41 하나의 화면에 여러 그래프를 표현하기

```python
fig = px.scatter(x = [0,1,2,3,4], y = [0,1,4,9,16])
fig.show()
```

""")
fig41 = px.scatter(x = [0,1,2,3,4], y = [0,1,4,9,16])
st.plotly_chart(fig41)



st.markdown("""
---
### fig42 Trace 추가

```python
import plotly.graph_objects as go
fig.add_trace(go.Scatter(x = [0,1,2,3,4], y = [0,1,4,9,16]))
```

""")
import plotly.graph_objects as go
fig42 = px.scatter(x = [0,1,2,3,4], y = [0,1,4,9,16])
fig42.add_trace(go.Scatter(x = [0,1,2,3,4], y = [0,1,4,9,16]))
st.plotly_chart(fig42)


st.markdown("""
---
### fig43 

```python
fig = go.Figure()
```

""")

fig43 = go.Figure()
st.plotly_chart(fig43)

st.markdown("""
---
### fig43_random_x

```python
import numpy as np
N = 100

random_x = np.linspace(0,1,N)
random_x
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5
fig.add_trace(go.Scatter(x = random_x, y = random_y0, mode = 'lines', name = 'lines'))
```

""")

N = 100
random_x = np.linspace(0,1,N)
random_x
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

fig43.add_trace(go.Scatter(x = random_x, y = random_y0, mode = 'lines', name = 'lines'))
st.plotly_chart(fig43)


st.markdown("""
---
```python
fig.add_trace(go.Scatter(x = random_x, y = random_y1, mode = 'lines+markers', name = 'lines+markers'))
```

""")

fig43.add_trace(go.Scatter(x = random_x, y = random_y1, mode = 'lines+markers', name = 'lines+markers'))
st.plotly_chart(fig43)

st.markdown("""
---
```python
fig.add_trace(go.Scatter(x = random_x, y = random_y2, mode = 'markers', name = 'markers'))
```

""")

fig43.add_trace(go.Scatter(x = random_x, y = random_y2, mode = 'markers', name = 'markers'))
st.plotly_chart(fig43)

st.markdown("""
---
### fig44_여러개의 그래프를 레이아웃을 나눠서 그리기

```python
from plotly.subplots import make_subplots
fig = make_subplots(rows=1 , cols=2)
```

""")

from plotly.subplots import make_subplots
fig44 = make_subplots(rows=1 , cols=2)
st.plotly_chart(fig44)

st.markdown("""
---
```python
fig.add_trace(go.Scatter(x=[1,2,3], y = [4,5,6]), row = 1, col =1)
```

""")

fig44.add_trace(go.Scatter(x=[1,2,3], y = [4,5,6]), row = 1, col =1)
st.plotly_chart(fig44)

st.markdown("""
---
```python
fig.add_trace(go.Scatter(x=[10,20,30], y = [40,50,60]), row = 1, col =2)
```

""")

fig44.add_trace(go.Scatter(x=[10,20,30], y = [40,50,60]), row = 1, col =2)
st.plotly_chart(fig44)


st.markdown("""
---
### fig45_subtitle 넣기
```python
fig = make_subplots(rows=1 , cols=2, subplot_titles=('Plot1', 'Plot2'))
# subplot_titles=('Plot1', 'Plot2')
```

""")
fig45 = make_subplots(rows=1 , cols=2, subplot_titles=('Plot1', 'Plot2'))
st.plotly_chart(fig45)

st.markdown("""
---
### fig46_비율 다릐게 하기 
```python
fig = make_subplots(rows=1 , cols=2, subplot_titles=('Plot1', 'Plot2')
,column_widths = [0.8, 0.2])

fig.add_trace(go.Scatter(x=[1,2,3], y = [4,5,6]), row = 1, col =1)
fig.add_trace(go.Scatter(x=[10,20,30], y = [40,50,60]), row = 1, col =2)
```

""")

fig46 = make_subplots(rows=1 , cols=2, subplot_titles=('Plot1', 'Plot2')
,column_widths = [0.8, 0.2])

fig46.add_trace(go.Scatter(x=[1,2,3], y = [4,5,6]), row = 1, col =1)
fig46.add_trace(go.Scatter(x=[10,20,30], y = [40,50,60]), row = 1, col =2)
st.plotly_chart(fig46)

st.markdown("""
---
### fig47 이중 축 사용하기
    사용하는 경우,
    - 가로축을 공통 (지역 , 서울 , 대전, 대구, 부산)
    - 세로축 두개의 선이 그어졌을때, 하나의 선이 온도, 다른 선이 습도

```python
fig = make_subplots(specs = [[{'secondary_y' : True}]])
fig.add_trace(go.Scatter(x = [1,2,3], y = [40,50,60], name = 'yaxis1'), secondary_y = False)
fig.add_trace(go.Scatter(x = [2,4,6], y = [4,5,6], name = 'yaxis2'), secondary_y = True)
```

""")

fig47 = make_subplots(specs = [[{'secondary_y' : True}]])
fig47.add_trace(go.Scatter(x = [1,2,3], y = [40,50,60], name = 'yaxis1'), secondary_y = False)
fig47.add_trace(go.Scatter(x = [2,4,6], y = [4,5,6], name = 'yaxis2'), secondary_y = True)
st.plotly_chart(fig47)



st.markdown("""
---
### fig48 범례의 스타일 지정



```python
fig.update_layout(
                    legend_title_text= 타이틀명 text 입력,        
                    legend_title_font_family = 범례 타이틀 서체,
                    legend_title_font_color= 범례 타이틀 색,
                    legend_title_font_size= 범례 타이틀 글자 크기,
                    legend_font_family= 범례 서체,
                    legend_font_size=범례 글자 크기,
                    legend_font_color=범례 색,
                    legend_bgcolor= 범례 배경색,
                    legend_bordercolor=범례 테두리 색,
                    legend_borderwidth=범례 테두리 두깨
                )


df = px.data.tips()
fig = px.scatter(df, x = 'total_bill', y = 'tip', color = 'sex')
fig.show()
```


""")

# df_3, df_8 = px.data.tips()
df_10 = px.data.tips()
df_10
fig49 = px.scatter(df_10, x = 'total_bill', y = 'tip', color = 'sex')
st.plotly_chart(fig49)



st.markdown("""
---
### fig48 레전드 위치 변경
```python

fig.update_layout(legend_yanchor = 'top',
                  legend_y = 0.99,
                  legend_xanchor='left',
                  legend_x = 0.01)
#왼쪽으로 레전드를 이동
#레전드 위치 조절가능
```
""")

fig49.update_layout(legend_yanchor = 'top',
                  legend_y = 0.99,
                  legend_xanchor='left',
                  legend_x = 0.01)
st.plotly_chart(fig49)

st.markdown("""
---
### fig48 레전드 위치 변경_2
```python

fig.update_layout(legend_yanchor = 'top',
                  legend_y = 0.99,
                  legend_xanchor='left',
                  legend_x = 0.01,
                  legend_orientation='h',
                  legend_entrywidth=70)
#legend_orientation='h',
#legend_entrywidth=70
```
""")

fig49.update_layout(legend_yanchor = 'top',
                  legend_y = 0.99,
                  legend_xanchor='left',
                  legend_x = 0.01,
                  legend_orientation='h',
                  legend_entrywidth=70)
st.plotly_chart(fig49)
