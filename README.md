# 💱 환율 정보 Agent (LangChain v1 + Streamlit)

LangChain v1의 `create_agent`로 만든 환율 정보 Agent를 Streamlit 채팅 UI로 사용하는 교육용 샘플입니다.

- **LLM**: OpenAI `gpt-5.4-mini`
- **Tools**
  - `get_exchange_rate`: [Frankfurter API](https://frankfurter.dev/)로 실시간·과거 환율 조회
  - `tavily_search`: LangChain 통합 [Tavily](https://tavily.com/) 웹 검색 (환율 뉴스, 전망 등)

## 파일 구성

| 파일 | 설명 |
| --- | --- |
| `tools.py` | 웹 검색 Tool, 환율 조회 Tool 정의 |
| `agent.py` | `create_agent`로 Agent 생성 (단독 실행으로 터미널 테스트 가능) |
| `app.py` | Streamlit 채팅 웹앱 |

## 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # OPENAI_API_KEY, TAVILY_API_KEY 입력
streamlit run app.py
```

## 질문 예시

- 오늘 달러 환율 알려줘
- 100만 원은 엔화로 얼마야?
- 2025년 1월 2일 유로/원 환율은?
- 최근 원·달러 환율이 오른 이유가 뭐야?
