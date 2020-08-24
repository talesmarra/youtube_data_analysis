import itertools
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly_express as px
import calendar

def best_time(us_videos, category=None):
    """
    Given a category, we'll check the most interesting time to publish a video.
    params:
    category: category name. If None, takes all categories into account.
    return:
    best time to publish a video.
    """
    us_videos_cp = us_videos.copy()
    if category:
        us_videos_cp = us_videos_cp[us_videos_cp['category_name']==category]
    us_videos_cp.sort_values(by='views', inplace=True)
    us_videos_cp = us_videos_cp.head(n=100).reset_index(drop=True)

    fig = px.bar(us_videos_cp, x='month', y='views', title='View count by month')
    st.plotly_chart(fig)
    fig2 = px.bar(us_videos_cp, x='hour', y='views', title='View count by hour')
    st.plotly_chart(fig2)
    fig2 = px.bar(us_videos_cp, x='day', y='views', title='View count by day of the month')
    st.plotly_chart(fig2)



def interesting_words(category=None, use_in='title', top=10):
    """
    Given a category, we'll check the most n interesting words to use in title/tags.
    params:
    category: category name. If None, takes all categories into account.
    use_in: title or tags.
    top: the number of best words to be selected.
    return:
    top n words to used in title/tags.
    """
    us_videos_cp = us_videos.copy()
    if category:
        us_videos_cp = us_videos_cp[us_videos_cp['category_name']==category]
    us_videos_cp[use_in] = us_videos_cp[use_in].apply(lambda x: x.lower().split(' '))
    us_videos_cp.sort_values(by='views', ascending=False, inplace=True)
    us_videos_cp = us_videos_cp.head(n=100).reset_index(drop=True)
    res = list(itertools.chain.from_iterable(us_videos_cp[use_in].values))
    res = [''.join(x for x in i if x.isalpha()) for i in res if i not in ['|', '-']] # filtering words
    res = pd.Series([i for i in res if i !=''], name=f'Most interesting words to put in {use_in}').value_counts().head(top)
    res = pd.DataFrame(res)
    return res
    

us_videos = pd.read_csv('data/USvideos.csv')
category_name = {1:'Film and Animation', 2:'Cars and Vehicles', 10: 'Music', 15:'Pets and Animals', 17:'Sport', 
	19:'Travel and Events', 20:'Gaming', 22:'People and Blogs', 23:'Comedy', 24:'Entertainment', 25:'News and Politics',
	26:'How to and Style', 27:'Education', 28:'Science and Technology', 29:'Non-profits and activism'}
us_videos['publish_time'] = pd.to_datetime(us_videos['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
us_videos['category_name'] = us_videos['category_id'].map(category_name)
us_videos['month'] = us_videos['publish_time'].dt.month
us_videos['day'] = us_videos['publish_time'].dt.day
us_videos['year'] = us_videos['publish_time'].dt.year
us_videos['hour'] = us_videos['publish_time'].dt.hour
us_videos['minute'] = us_videos['publish_time'].dt.minute


st.title("The youtuber helper")
st.markdown("Welcome to this youtuber helper. If you want to use data to enhance the views of your video, you are in the right place!")
category = st.selectbox(
    'What is the category of the videos you do?',
     us_videos['category_name'].unique())

use_in = st.selectbox('Where do you need help with the most interesting words?', ['title', 'tags'])
top = st.slider('How many top words?')
st.table(interesting_words(category, use_in, top))
best_time(us_videos, category)
