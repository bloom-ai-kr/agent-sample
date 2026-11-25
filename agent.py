"""LangChain v1 `create_agent`로 환율 정보 Agent를 생성합니다."""

from dotenv import load_dotenv

# .env 파일에서 OPENAI_API_KEY, TAVILY_API_KEY 로드
# tools.py가 import될 때 TavilySearch가 API 키를 읽으므로, 반드시 tools import 전에 호출해야 합니다.
load_dotenv()

from langchain.agents import create_agent  # noqa: E402

from tools import get_exchange_rate, web_search  # noqa: E402

SYSTEM_PROMPT = """당신은 환율 정보를 알려주는 친절한 어시스턴트입니다.

- 환율 수치는 반드시 `get_exchange_rate` 도구로 조회해서 답변하세요.
- 환율 전망, 변동 원인, 관련 뉴스 등은 `web_search` 도구로 검색해서 답변하세요.
- 답변에는 기준 날짜와 출처를 함께 알려주세요.
- 항상 한국어로 답변하세요.
"""

agent = create_agent(
    model="openai:gpt-5.4-mini",
    tools=[get_exchange_rate, web_search],
    system_prompt=SYSTEM_PROMPT,
)


if __name__ == "__main__":
    # 터미널에서 간단히 테스트: python agent.py
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "오늘 달러 환율 알려줘"}]}
    )
    print(result["messages"][-1].content)
