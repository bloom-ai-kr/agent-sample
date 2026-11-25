"""Streamlit 기반 환율 정보 Agent 웹앱.

실행: streamlit run app.py
"""

import streamlit as st

from agent import agent

st.set_page_config(page_title="환율 정보 Agent", page_icon="💱")
st.title("💱 환율 정보 Agent")

# 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("예: 1000달러는 원화로 얼마야?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("생각 중..."):
            result = agent.invoke({"messages": st.session_state.messages})

        # 최종 답변을 먼저 출력
        answer = result["messages"][-1].content
        st.markdown(answer)

        # Agent가 호출한 Tool 확인 (학습용)
        tool_calls = [
            call
            for msg in result["messages"]
            if msg.type == "ai"
            for call in msg.tool_calls
        ]
        if tool_calls:
            with st.expander("🔧 사용한 도구"):
                for call in tool_calls:
                    st.write(f"**{call['name']}**", call["args"])

    st.session_state.messages.append({"role": "assistant", "content": answer})
