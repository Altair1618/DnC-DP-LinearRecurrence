def printUtil(milliInterval, peak):
    if milliInterval <= 1e3:
        print(f"Duration: {milliInterval: .3f} milliseconds")
    elif milliInterval <= 6e4:
        print(f"Duration: {milliInterval / 1e3: .3f} seconds")
    else:
        print(f"Duration: {milliInterval / 6e4: .3f} minutes")

    if peak <= 1e4:
        print(f"Memory being used: {peak} Bytes")
    elif peak <= 1e7:
        print(f"Memory being used: {peak // 1e3} KB")
    elif peak <= 1e10:
        print(f"Memory being used: {peak // 1e6} MB")
