def typist(s):
    taps = []
    for j in s:
        if s[0].isupper():
            taps.append(j)
            taps.append(j)
        else:
            taps.append(j)

        for i in range(len(s) - 1):

            if (s[i].isupper() and s[i+1].islower()):
                taps.append(i)
                taps.append(i)
            elif (s[i].islower() and s[i+1].isupper()):
                taps.append(i)
                taps.append(i)

            else:
                taps.append(i)
        return len(taps)
