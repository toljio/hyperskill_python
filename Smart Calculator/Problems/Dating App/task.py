def select_dates(potential_dates):
    return ", ".join(x["name"] for x in potential_dates if x["age"] > 30 and "art" in x["hobbies"] and x["city"] == "Berlin")