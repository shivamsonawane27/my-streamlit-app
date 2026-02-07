import streamlit as st
import time
import base64
import os

# https://raw.githubusercontent.com/shivamsonawane27/my-streamlit-app/my-streamlit-app//main/

# Page config
st.set_page_config(page_title="A Special Message 💕", page_icon="🍥")

# Function to autoplay audio with better volume control
def autoplay_audio(file_path, loop=False, volume=0.5):
    if not os.path.exists(file_path):
        return  # Skip if file doesn't exist
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            loop_attr = "loop" if loop else ""
            
            # Detect file type
            if file_path.endswith('.m4a'):
                audio_type = "audio/mp4"
            elif file_path.endswith('.mp3'):
                audio_type = "audio/mp3"
            else:
                audio_type = "audio/mpeg"
            
            md = f"""
                <audio id="bgMusic" autoplay {loop_attr} style="display:none;">
                <source src="data:{audio_type};base64,{b64}" type="{audio_type}">
                </audio>
                <script>
                (function() {{
                    var audio = document.getElementById('bgMusic');
                    if (audio) {{
                        audio.volume = {volume};
                        audio.play().catch(function(e) {{
                            console.log('Audio play failed:', e);
                        }});
                    }}
                }})();
                </script>
                """
            st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading audio: {file_path}")

# Function to play sound effect with proper volume
def play_sound_effect(file_path, volume=0.7):
    if not os.path.exists(file_path):
        return  # Skip if file doesn't exist
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            
            # Detect file type
            if file_path.endswith('.m4a'):
                audio_type = "audio/mp4"
            elif file_path.endswith('.mp3'):
                audio_type = "audio/mp3"
            else:
                audio_type = "audio/mpeg"
            
            import random
            sfx_id = f"sfx_{random.randint(1000, 9999)}"
            md = f"""
                <audio id="{sfx_id}" autoplay style="display:none;">
                <source src="data:{audio_type};base64,{b64}" type="{audio_type}">
                </audio>
                <script>
                (function() {{
                    var audio = document.getElementById('{sfx_id}');
                    if (audio) {{
                        audio.volume = {volume};
                        audio.play().catch(function(e) {{
                            console.log('SFX play failed:', e);
                        }});
                    }}
                }})();
                </script>
                """
            st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading sound effect: {file_path}")

# Debug mode - remove this after fixing
if st.sidebar.checkbox("Show Debug Info"):
    st.sidebar.write("**Files in directory:**")
    files = os.listdir(".")
    for f in sorted(files):
        if f.endswith(('.png', '.mp3', '.m4a', '.jpg')):
            size = os.path.getsize(f) / 1024  # KB
            st.sidebar.write(f"✅ {f} ({size:.1f} KB)")

# Custom CSS for styling  
st.markdown("""
    <style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        text-align: center;
    }
    .naruto-font {
        font-size: 24px !important;
        color: #FF6B35;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
    }
    .center {
        text-align: center;
    }
    .genjutsu {
        font-size: 28px !important;
        color: #8B00FF;
        text-align: center;
        font-weight: bold;
        animation: pulse 1s infinite;
    }
    .smoke-big {
        font-size: 100px !important;
        text-align: center;
        letter-spacing: 20px;
    }
    .smoke-medium {
        font-size: 80px !important;
        text-align: center;
        letter-spacing: 15px;
        opacity: 0.7;
    }
    .smoke-small {
        font-size: 60px !important;
        text-align: center;
        letter-spacing: 10px;
        opacity: 0.4;
    }
    .smoke-tiny {
        font-size: 40px !important;
        text-align: center;
        letter-spacing: 5px;
        opacity: 0.2;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if 'genjutsu_clicks' not in st.session_state:
    st.session_state.genjutsu_clicks = 0
if 'music_started' not in st.session_state:
    st.session_state.music_started = False

# Music starter screen (only shows once)
if not st.session_state.music_started:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<h1 class='center'>Welcome!</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p class='center'>Click below to start your special message</p>", unsafe_allow_html=True)
    st.markdown("<p class='center'>(with sound! 🎵)</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start", use_container_width=True):
            st.session_state.music_started = True
            st.rerun()

else:
    # Play background music at 50% volume
    autoplay_audio("bg_naruto.mp3", loop=True, volume=0.1)

    # Stage 0: Initial message
    if st.session_state.stage == 0:
        # Play sound effect at 70% volume
        play_sound_effect("naruto_hello_sound.mp3", volume=0.7)
        
        st.markdown("<h1 class='center'>A Special Message For You</h1>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<p class='naruto-font'>Hey there Ritika!</p>", unsafe_allow_html=True)
            try:
                st.image("https://raw.githubusercontent.com/shivamsonawane27/my-streamlit-app/refs/heads/main/my-streamlit-app/kakashi1.png", width=300)
            except:
                st.info("📸 Add 'naruto_hello.jpg' here")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p class='big-font'>I have something very important to ask you...</p>", unsafe_allow_html=True)
        
        if st.button("What is it, Kakashi? 👀", use_container_width=True):
            st.session_state.stage = 1
            st.rerun()

    # Stage 1: The question
    elif st.session_state.stage == 1:
        play_sound_effect("question_sound.mp3", volume=0.8)
        
        st.markdown("<h1 class='center'>💕💕💕</h1>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st.image("kakashi2.png", width=300)
            except:
                st.info("📸 Add 'naruto_asking.jpg' here")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p class='big-font'>I'm not sure how to exactly say this but, I like you, so Will you please be my Valentine? 💝</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Yes! 💕", use_container_width=True):
                st.session_state.answer = "yes"
                st.session_state.stage = 3
                st.rerun()
        
        with col2:
            if st.button("Let me think... 🤔", use_container_width=True):
                st.session_state.stage = 2
                st.rerun()

    # Stage 2: Genjutsu trap!
    elif st.session_state.stage == 2:
        play_sound_effect("sharingan.mp3", volume=0.9)
        
        st.markdown("<h1 class='genjutsu'>👁️ GENJUTSU ACTIVATED! 👁️</h1>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<p class='naruto-font'>I must have you Ritika, I'm putting you under my genjutsu! 🌀</p>", unsafe_allow_html=True)
            try:
                st.image("kakashi3.png", width=300)
            except:
                st.info("📸 Add 'naruto_genjutsu.jpg' here")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p class='center'>You're trapped in my jutsu now! The only way out is... 😏</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Yes! I'll be your Valentine! 💕", use_container_width=True):
                st.session_state.answer = "yes"
                st.session_state.stage = 3
                st.rerun()
        
        with col2:
            if st.button("Let me think... 🤔", use_container_width=True, key=f"think_{st.session_state.genjutsu_clicks}"):
                st.session_state.genjutsu_clicks += 1
                st.markdown("<p class='genjutsu'>You can't escape my genjutsu so easily! 😈</p>", unsafe_allow_html=True)
                time.sleep(1)
                st.rerun()
        
        if st.session_state.genjutsu_clicks > 0:
            st.markdown(f"<p class='center'>Escape attempts: {st.session_state.genjutsu_clicks} 😂</p>", unsafe_allow_html=True)

    # Stage 3: Transformation with REAL smoke animation
    elif st.session_state.stage == 3:
        play_sound_effect("transformation_sound.mp3", volume=0.85)
        
        st.markdown("<h1 class='center'>✨ TRANSFORMATION JUTSU! ✨</h1>", unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        animation_placeholder = st.empty()
        
        with animation_placeholder.container():
            st.markdown("<p class='smoke-big'>💥</p>", unsafe_allow_html=True)
            st.markdown("<p class='center' style='font-size: 30px; font-weight: bold;'>POOF!</p>", unsafe_allow_html=True)
        time.sleep(0.5)
        
        with animation_placeholder.container():
            st.markdown("<p class='smoke-big'>💨 💨 💨</p>", unsafe_allow_html=True)
            st.markdown("<p class='smoke-big'>💨 💨 💨</p>", unsafe_allow_html=True)
            st.markdown("<p class='smoke-big'>💨 💨 💨</p>", unsafe_allow_html=True)
        time.sleep(0.7)
        
        with animation_placeholder.container():
            st.markdown("<p class='smoke-medium'>💨 💨</p>", unsafe_allow_html=True)
            st.markdown("<p class='smoke-medium'>💨 💨</p>", unsafe_allow_html=True)
        time.sleep(0.5)
        
        with animation_placeholder.container():
            st.markdown("<p class='smoke-small'>💨</p>", unsafe_allow_html=True)
        time.sleep(0.4)
        
        with animation_placeholder.container():
            st.markdown("<p class='smoke-tiny'>💨</p>", unsafe_allow_html=True)
        time.sleep(0.3)
        
        animation_placeholder.empty()
        time.sleep(0.2)
        
        play_sound_effect("smoke.m4a", volume=0.8)
        
        st.markdown("<h1 class='center'>💕 It was me all along babe!!!! 💕</h1>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st.image("my_photo.png", width=300)
            except:
                st.info("📸 Add 'my_photo.jpg' here")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<p class='big-font'>You said YES! 🎉</p>", unsafe_allow_html=True)
        st.balloons()
        st.markdown("<p class='center'>You have made me very happy and I hope you will be my valentine now and forever!!!! 💕</p>", unsafe_allow_html=True)
        
        if st.session_state.genjutsu_clicks > 0:
            st.markdown(f"<p class='center'>😂 Nice try escaping {st.session_state.genjutsu_clicks} times! But you couldn't resist! 😘</p>", unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        if st.button("Start Over 🔄", use_container_width=True):
            st.session_state.stage = 0
            st.session_state.genjutsu_clicks = 0
            st.rerun()
