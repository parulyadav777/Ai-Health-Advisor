# ##2Chat_py
# from save_appointments import save_appointments
# import streamlit as st
# import re
# from backend import (
#     chat_with_model,
#     load_chat_sessions,
#     load_chat_messages,
#     save_chat_session,
#     update_chat_session
# )

# # =========================
# # AUTH GUARD
# # =========================
# if "user" not in st.session_state:
#     st.warning("Please log in to access the chat.")
#     st.stop()

# # =========================
# # SESSION STATE
# # =========================
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "current_chat_id" not in st.session_state:
#     st.session_state.current_chat_id = None

# # =========================
# # SIDEBAR (CHAT CONTROLS)
# # =========================
# with st.sidebar:
#     st.header("💬 Chat")

#     # --- New Chat ---
#     if st.button("➕ New Chat", use_container_width=True):
#         st.session_state.current_chat_id = None
#         st.session_state.messages = []
#         st.rerun()

#     # --- Clear Chat (UI only) ---
#     if st.button("🗑️ Clear Chat", use_container_width=True):
#         st.session_state.messages = []
#         st.rerun()

#     st.subheader("📜 Past Chats")
#     user_sessions = load_chat_sessions(st.session_state.user["id"])

#     if user_sessions:
#         for chat_id, title in user_sessions:
#             if st.button(title, key=f"chat_{chat_id}", use_container_width=True):
#                 st.session_state.current_chat_id = chat_id
#                 st.session_state.messages = load_chat_messages(chat_id)
#                 st.rerun()
#     else:
#         st.info("No past chats found.")

# # =========================
# # MAIN CHAT UI
# # =========================
# st.title("💬 Chat with AI Health Assistant")

# # Render messages
# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).markdown(msg.get("content", ""))

# # =========================
# # USER INPUT
# # =========================
# user_input = st.chat_input("Ask me anything...")

# if user_input:
#     # Add user msg
#     st.session_state.messages.append({"role": "user", "content": user_input})
#     st.chat_message("user").markdown(user_input)

#     # AI Response
#     with st.spinner("AI is thinking..."):
#         try:
#             ai_response = chat_with_model(
#                 user_input,
#                 chat_history=st.session_state.messages
#             )
#         except Exception:
#             ai_response = "⚠️ Service is temporarily unavailable. Please try again later."

#     if not ai_response or not ai_response.strip():
#         ai_response = "Sorry, I could not generate a response."

#     # DISPLAY RESPONSE
#     st.session_state.messages.append({"role": "assistant", "content": ai_response})
#     st.chat_message("assistant").markdown(ai_response)

#     # =========================
#     # APPOINTMENT DETECTION
#     # =========================
#     date_match = re.search(r"(\d{4}-\d{2}-\d{2})", ai_response)
#     time_match = re.search(r"(\d{2}:\d{2})", ai_response)
#     doctor_match = re.search(r"Dr\.\s+[A-Za-z]+", ai_response)

#     if date_match and time_match and doctor_match:
#         date = date_match.group(1)
#         time = time_match.group(1)
#         doctor = doctor_match.group(0)

#         appointment_datetime = f"{date} {time}:00"
#         patient_name = st.session_state.user["username"]

#         save_appointments(
#             patient_name,
#             doctor,
#             appointment_datetime,
#             "confirmed"
#         )

#         st.success(f"📌 Appointment saved with {doctor} at {appointment_datetime}!")

#     # =========================
#     # SAVE / UPDATE CHAT SESSION
#     # =========================
#     if st.session_state.current_chat_id is None:
#         chat_title = user_input[:30] + "..." if len(user_input) > 30 else user_input
#         st.session_state.current_chat_id = save_chat_session(
#             st.session_state.user["id"],
#             chat_title,
#             st.session_state.messages
#         )
#     else:
#         update_chat_session(
#             st.session_state.current_chat_id,
#             st.session_state.messages
#         )


# pages/2_Chat.py

import streamlit as st
import re
from save_appointments import save_appointments
from backend import (
    chat_with_model,
    load_chat_sessions,
    load_chat_messages,
    save_chat_session,
    update_chat_session
)

# =========================
# AUTH GUARD (MANDATORY)
# =========================
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please log in to access the chat.")
    st.stop()

USER_ID = st.session_state.user["id"]
USERNAME = st.session_state.user["username"]

# =========================
# SESSION STATE INIT
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# =========================
# SIDEBAR – CHAT CONTROLS
# =========================
with st.sidebar:
    st.header("💬 Chat")

    # ➕ New Chat
    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.current_chat_id = None
        st.session_state.messages = []
        st.rerun()

    # 🗑️ Clear Chat (UI only)
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.subheader("📜 Past Chats")

    user_sessions = load_chat_sessions(USER_ID)

    if user_sessions:
        for chat_id, title in user_sessions:
            if st.button(title, key=f"chat_{chat_id}", use_container_width=True):
                st.session_state.current_chat_id = chat_id
                st.session_state.messages = load_chat_messages(chat_id)
                st.rerun()
    else:
        st.info("No past chats found.")

# =========================
# MAIN CHAT UI
# =========================
st.title("💬 Chat with AI Health Assistant")

st.caption(
    "⚠️ This assistant provides guidance only and is not a replacement "
    "for a licensed doctor."
)

# -------------------------
# RENDER CHAT HISTORY
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# USER INPUT
# =========================
prompt = st.chat_input("Ask a medical question or appointment request...")

if prompt:
    # ---------------------
    # USER MESSAGE
    # ---------------------
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------------------
    # AI RESPONSE
    # ---------------------
    with st.chat_message("assistant"):
        with st.spinner("AI is thinking..."):
            try:
                ai_response = chat_with_model(
                    prompt,
                    chat_history=st.session_state.messages
                )
            except Exception:
                ai_response = (
                    "⚠️ Service is temporarily unavailable. "
                    "Please try again later."
                )

        if not ai_response or not ai_response.strip():
            ai_response = "Sorry, I could not generate a response."

        st.markdown(ai_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # =========================
    # APPOINTMENT DETECTION
    # =========================
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", ai_response)
    time_match = re.search(r"(\d{2}:\d{2})", ai_response)
    doctor_match = re.search(r"(Dr\.\s+[A-Za-z\s]+)", ai_response)

    if date_match and time_match and doctor_match:
        appointment_datetime = f"{date_match.group(1)} {time_match.group(1)}:00"
        doctor_name = doctor_match.group(1)

        save_appointments(
            patient_name=USERNAME,
            doctor_name=doctor_name,
            appointment_datetime=appointment_datetime,
            status="confirmed"
        )

        st.success(
            f"📌 Appointment saved with **{doctor_name}** "
            f"at **{appointment_datetime}**"
        )

    # =========================
    # SAVE / UPDATE CHAT SESSION
    # =========================
    if st.session_state.current_chat_id is None:
        title = prompt[:30] + "..." if len(prompt) > 30 else prompt
        st.session_state.current_chat_id = save_chat_session(
            USER_ID,
            title,
            st.session_state.messages
        )
    else:
        update_chat_session(
            st.session_state.current_chat_id,
            st.session_state.messages
        )
