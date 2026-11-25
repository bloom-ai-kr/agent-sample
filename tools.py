"""Agent가 사용할 Tool 정의.

- web_search: LangChain 통합 Tavily 검색 도구
- get_exchange_rate: Frankfurter API(https://frankfurter.dev/) 기반 환율 조회 도구
"""

import requests
from langchain.tools import tool
from langchain_tavily import TavilySearch

# 1) 웹 검색 Tool (TAVILY_API_KEY 환경 변수 필요)
web_search = TavilySearch(
    max_results=5,
    topic="general",
)


# 2) 환율 조회 Tool
@tool
def get_exchange_rate(base: str, target: str, date: str = "latest") -> dict:
    """두 통화 간의 환율을 조회합니다.

    Args:
        base: 기준 통화의 ISO 4217 코드 (예: "USD")
        target: 대상 통화의 ISO 4217 코드 (예: "KRW"). 여러 개는 쉼표로 구분 (예: "KRW,JPY")
        date: 조회할 날짜 (YYYY-MM-DD). 최신 환율은 "latest"
    """
    url = f"https://api.frankfurter.dev/v1/{date}"
    params = {"base": base.upper(), "symbols": target.upper()}

    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        return {"error": f"환율 조회 실패 ({response.status_code}): {response.text}"}

    # 예: {"amount": 1.0, "base": "USD", "date": "2026-11-24", "rates": {"KRW": 1344.51}}
    return response.json()
