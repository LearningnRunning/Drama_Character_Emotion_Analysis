# app.py
#############################################################################


import base64
import os

import streamlit as st
import pandas as pd
import plotly.express as px


def fix_df(df,epi):
    df = df[df['episode'] == epi+'_100_face']
    df = df[df['emotion'] != "None"].reset_index(drop = False)
    return df
def makeChart(df):
        fig1 = px.pie(df, values='count', names='emotion', color='emotion',color_discrete_sequence=px.colors.sequential.RdBu)      #plotly pie차트
        fig1.update_traces(textinfo='label+percent',textfont_size=20, hole=.2)
        st.plotly_chart(fig1)


st.sidebar.header("감정 상관관계 분석")
name = st.sidebar.selectbox("Name", ["드라마별 비교","드라마 내 에피소드별 비교"])
# n_similar = st.sidebar.slider("Max number of similar entries", 1, 100, value=20, step=1)
name1 = '100years'
name2 = 'yawang'
file_list = sorted(os.listdir('./result'))
# df1 = pd.read_csv('./result/'+name1+'_all_df.csv')
# df2 = pd.read_csv('./result/'+name2+'_all_df.csv')
df1_cnt = pd.read_csv('./result/'+name1+'_all_df_cnt.csv')
df2_cnt = pd.read_csv('./result/'+name2+'_all_df_cnt.csv')

if name == "드라마별 비교":
    st.title("드라마별 비교")
    selEpi = st.selectbox('원하시는 회차를 골라주세요?', [1,2,3,4])
    st.write("# " + "에피소드 {0}화".format(selEpi))
    cols = st.columns([0.3,0.8,0.3])
    

    with cols[0]:
        st.write("### " + "백년의 사랑")
        df1_tmp = fix_df(df1_cnt,'epi{0}'.format(selEpi))
        st.write('시청률: {0} %'.format(df1_tmp['rating'][0]))
        fig1 = px.pie(df1_tmp, values='count', names='emotion', color='emotion',color_discrete_sequence=px.colors.sequential.RdBu)      #plotly pie차트
        fig1.update_traces(textinfo='label+percent',textfont_size=20, hole=.2)
        # fig1.update_layout(margin=dict(b=0),)
        st.plotly_chart(fig1)
    with cols[2]:
        st.write("### " + "야왕")
        df2_tmp = fix_df(df2_cnt,'epi{0}'.format(selEpi))
        st.write('시청률: {0} %'.format(df2_tmp['rating'][0]))
        fig2 = px.pie(df2_tmp, values='count', names='emotion', color='emotion',color_discrete_sequence=px.colors.sequential.RdBu)      #plotly pie차트
        fig2.update_traces(textinfo='label+percent',textfont_size=20, hole=.2)
        # fig2.update_layout(margin=dict(b=50),)
        st.plotly_chart(fig2)
        
        
elif name == "드라마 내 에피소드별 비교":
    st.title("드라마 내 에피소드별 비교")
    selEpi = st.selectbox('드라마를 골라주세요.', ['백년의 약속', '야왕'])
    if selEpi == '백년의 약속':
        tmp_df = df1_cnt
        name = '100years'
    else:
        tmp_df = df2_cnt
        name = 'yawang'

    st.line_chart(data=tmp_df, x='episode', y='rating', width=0, height=0, use_container_width=True)
    tab1, tab2, tab3, tab4 = st.tabs(["epi1", "epi2", "epi3","epi4"])
    
    with tab1:
        df1_tmp = fix_df(tmp_df,"epi1")
        makeChart(df1_tmp)
    with tab2:
        df1_tmp = fix_df(tmp_df,"epi2")
        makeChart(df1_tmp)
    with tab3:
        df1_tmp = fix_df(tmp_df,"epi3")
        makeChart(df1_tmp)
    with tab4:
        df1_tmp = fix_df(tmp_df,"epi4")
        makeChart(df1_tmp)
    
    # uploaded_files = st.file_uploader(
    #     "정면으로 찍은 사진을 올려보세요.", type=["png", "jpg"], accept_multiple_files=True
    # )

    # if uploaded_files is not None:
    #     print(uploaded_files, type(uploaded_files))
    #     for uploaded_file in uploaded_files:
    #         content = uploaded_file.getvalue()
    #         bs = "data:image/jpeg;base64," + base64.b64encode(content).decode("utf-8")

    #         obj = DeepFace.analyze(bs, actions=["age", "gender", "race", "emotion"])

    #         race = sortObj("race")
    #         gender = sortObj("gender")
    #         emotions = sortObj("emotion")

    #         st.image(bs, width=250, caption="CLIENT_IMAGE")
    #         st.write("#### 성별")
    #         st.write("{0} : {1}%".format(gender[0][0], round(gender[0][1], 2)))
    #         st.write("#### 감정")
    #         st.write("{0} : {1}%".format(emotions[0][0], round(emotions[0][1], 2)))
    #         st.write("{0} : {1}%".format(emotions[1][0], round(emotions[1][1], 2)))
    #         st.write("#### 인종")
    #         st.write("{0} : {1}%".format(race[0][0], round(race[0][1], 2)))

# elif name == "test":
#     st.title("epi1_100_face")
#     path = "./data./epi1_100_face"
#     uploaded_files = os.listdir(path)
#     print(uploaded_files)
#     if uploaded_files is not None:
#         for uploaded_file in uploaded_files:
#             bs = os.path.join(path, uploaded_file)
#             print(bs)
#             try:
#                 obj = DeepFace.analyze(bs, actions=["age", "gender", "race", "emotion"])
#                 print(object)
#                 race = sortObj("race")
#                 gender = sortObj("gender")
#                 emotions = sortObj("emotion")

#                 st.image(bs, width=250, caption="CLIENT_IMAGE")
#                 st.write("#### 성별")
#                 st.write("{0} : {1}%".format(gender[0][0], round(gender[0][1], 2)))
#                 st.write("#### 감정")
#                 st.write("{0} : {1}%".format(emotions[0][0], round(emotions[0][1], 2)))
#                 st.write("{0} : {1}%".format(emotions[1][0], round(emotions[1][1], 2)))
#             except:

#                 continue
            

