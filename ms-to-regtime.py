while (0==0):
    time = int(input("Enter the time value: "))
    time = time / 10000

    hh = int(time / 3600000)
    time = time % 3600000

    mm = int(time / 60000)
    time = time % 60000

    ss = int(time / 1000)
    ms = int(time % 1000)

    print(f"> {hh}:{mm}:{ss}.{ms}")
    input()