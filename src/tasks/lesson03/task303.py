def ask_user_to_input_a_sentence() -> str:
    s = input("введи предложение из двух слов: ")
    return s


def extract_words_from_sentence(s: str) -> list:
    w = s.split(" ")
    assert len(w) == 2, f"error! sentence '{s}' contains <>2 words"
    return w


def render_template(t: str, c: dict) -> str:
    r = t.format(**c)
    return r


def solution(sentence: str) -> str:
    words = extract_words_from_sentence(sentence)

    template = "!{word2} {word1}!"
    context = {
        "word1": words[0],
        "word2": words[1],
    }

    result = render_template(template, context)

    return result


if __name__ == "__main__":
    print(solution(ask_user_to_input_a_sentence()))
