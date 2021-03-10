def solution(sentence: str) -> bool:
    words = (sentence or "").split(" ")
    result = "code" in words
    return result
