def search_lines(file_or_filename, search_words):
    search_words = [word.lower() for word in search_words]

    if isinstance(file_or_filename, str):
        file = open(file_or_filename, "r", encoding="utf-8")
    else:
        file = file_or_filename

    for line in file:
        line_lower = line.lower()
        if any(word in line_lower.split() for word in search_words):
            yield line

    if isinstance(file_or_filename, str):
        file.close()
