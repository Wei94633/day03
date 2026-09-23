def count_words(text):
    text = text.lower()

    count = text.count("cat") + text.count("tac")
    count += text.count("garden") + text.count("nedrag")
    count += text.count("mice") + text.count("ecim")

    return count


text1 = "the CataCat attaCk a Cat"
text2 = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"

print(count_words(text1))
print(count_words(text2))