import streamlit as st
import random as r
import time

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a skill that improves with practice.",
    "Python is a popular programming language.",
    "Artificial Intelligence is the future of technology.",
    "Streamlit makes it easy to build web apps with Python."
]

st.set_page_config(page_title='Typing speed checker')
st.title('Typing speed checker..')

if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'original_text' not in st.session_state:
    st.session_state.original_text = r.choice(sentences)
if 'completed' not in st.session_state:
    st.session_state.completed = False

st.subheader('Type the following sentence:')
st.code(st.session_state.original_text)

typed_text = st.text_area('Start typing here..', height=150)

if typed_text and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

if st.button('submit') and typed_text:
    end_time = time.time()
    total_time = round(end_time - st.session_state.start_time, 2)

    typed_word = typed_text.strip().split()
    original_word = st.session_state.original_text.strip().split()

    wpm = round(len(typed_word) / (total_time / 60), 2)

    correct_words = sum(1 for tw, ow in zip(typed_word, original_word) if tw == ow  )
    accuracy = round((correct_words / len(original_word))* 100, 2)

    st.success("✅ Test Completed!")
    st.write(f"⏱️ Time Taken: **{total_time} seconds**")
    st.write(f"📝 Words Per Minute (WPM): **{wpm}**")
    st.write(f"🎯 Accuracy: **{accuracy}%**")

    st.session_state.completed = True

if st.session_state.completed:
    if st.button('Try Again'):
        st.session_state.start_time = None
        st.session_state.original_text = r.choice(sentences)
        st.session_state.completed = False
        st.rerun()