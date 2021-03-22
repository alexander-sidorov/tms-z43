def solution(sentence: str) -> str:
    result = sentence if len(sentence) % 3 else f"{sentence}!"
    return result
