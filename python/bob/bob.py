def hey(phrase):
    question = "?"
    if phrase.strip(" ").endswith("?") and not phrase.isupper():
        return "Sure."
    elif phrase.isupper() and not phrase.endswith("?"):
        return "Whoa, chill out!"
    elif phrase.endswith("?") and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase is None or phrase.strip() == "":
        return "Fine. Be that way!"
    else:
        return 'Whatever.'

if __name__ == "__main__":
    x = hey("Okay if like my  spacebar  quite a bit?   ")
    print(x)
