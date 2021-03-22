def solution(sentence: str) -> str:
    n_chars = len(sentence)
    if n_chars > 5:
        return sentence

    result = ["Need more!", "It is five"][n_chars == 5]
    return result
