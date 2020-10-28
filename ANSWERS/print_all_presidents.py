from ANSWERS.president import President

for term_number in range(1, 46):
    p = President(term_number)
    print(f"{p.first_name:30s} {p.last_name:25s} {p.party}")

