import streamlit as st
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import test
import random

client_id = '2d5fab86e45744328c7245fbbca349a9'
client_secret = 'b366932953fc4730aa29f70fc65d675c'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)

header  = st.container()
inp = st.container()
pred = st.container()

with header:
    
    st.title('Recomood')
    st.markdown('**Hedef : Kullanıcının duygusunu tespit edip ona uygun şarkı önermek**')

with inp:
    st.title("Görüntü Yakalama")
    st.markdown("**Kullanıcının yüzünün görüntüsünü yakalama. Görüntünüzün yakalanması için açılan pencerede Shift+c'ye basın**")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    test.take_input()
    cv2.destroyAllWindows()

with pred:
    st.title("Dinlemen gereken şarkılar!!")

    img = cv2.imread('photo.jpg')

    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    
        

    predictions = DeepFace.analyze(img)

    st.text("Your emotion is {}".format(predictions['dominant_emotion']))  

    if(predictions['dominant_emotion'] != 'happy' and predictions['dominant_emotion'] != 'neutral'):

        st.markdown("Mutlu görünmüyorsun. Seni mutlu edecek şarkılar:")
        playlist_id = '6TWKL25TbMP6mtxSH5XIAN?si=21c4f33857a549eb'

        def get_track_ids(playlist_id):
            music_id_list = []
            playlist = sp.playlist(playlist_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlist_id)

        for i in range(27):

            random.shuffle(track_ids)

            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html=True)
    if(predictions['dominant_emotion'] == 'happy'):

        st.markdown("Mutlu görünüyorsun. Seni daha da mutlu edecek şarkılar: ")
        playlist_id = '37i9dQZF1DXaXB8fQg7xif?si=10dd0f1a917241cb'

        def get_track_ids(playlist_id):
            music_id_list = []
            playlist = sp.playlist(playlist_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlist_id)

        for i in range(27):

            random.shuffle(track_ids)

            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html=True)  
    if(predictions['dominant_emotion'] == 'neutral'):

        st.markdown("Durgun görünüyorsun. Moduna göre sakin şarkılar:")
        playlist_id = '37i9dQZF1DX19AnUWIQ7nB?si=6cabc84c47be455b'

        def get_track_ids(playlist_id):
            music_id_list = []
            playlist = sp.playlist(playlist_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlist_id)

        for i in range(27):

            random.shuffle(track_ids)

            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html=True)   


