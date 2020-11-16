def tracklist(**kwargs):
    for k, v in kwargs.items():
        print(k)
        for i, j in v.items():
            print("ALBUM:", i, "TRACK:", j)
