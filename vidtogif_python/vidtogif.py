##video to gif converter using streamlit and moviepy

##'title' is used to show the text in title formatting

##test theapp by running this in cmd  "streamlit run 'PATH TO APP' "

##the st input widget 'https://docs.streamlit.io/library/api-reference/widgets'  'file uploader' is being used here to upload mp4 video files 
 
##for the converter app - app will convert an mp4 file to GIF File using moviepy


from tracemalloc import start
import streamlit as st
from moviepy.editor import *


st.title('Convert Videos to GIF Online FREE')


def cut_video(clip):
    duration = int(clip.duration)
    start = st.sidebar.number_input('Start time (seconds):',max_value=duration)
    end = st.sidebar.number_input('End time (seconds):',min_value=start+3,max_value=duration)
    clip = clip.subclip(start,end)
    return clip
   
video_upload = st.file_uploader('Upload mp4 video file', type=['mp4', 'mpeg'])
if video_upload is not None:
    st.video(video_upload)
    vid = video_upload.name
    st.write('File Uploaded, processing conversion...')
    with open(vid, mode='wb') as f:
        f.write(video_upload.read())
        
    st_video = open(vid,'rb')
    clip = VideoFileClip(vid)
    clip = cut_video(clip)
    fps = st.sidebar.number_input('Frames per second (fps):',max_value=40)
    gifname = vid.replace('mp4','gif')
    clip.write_gif(gifname)
    clip.write_gif(gifname,fps=fps)
    st.success('Success! Your conversion is completed!')
    st.write('Output GIF: ')
    with open(gifname,'rb') as f:
        st.download_button('Download GIF', f, file_name=gifname)
        



