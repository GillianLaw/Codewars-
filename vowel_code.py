

def encode(st):
    switcheroo = {97:49, 101:50, 105:51, 111:52, 117:53}

    x = st.lower().translate(switcheroo)
    print(x)


def decode(st):
    switcheroodle = {49:97, 50:101, 51:105, 52:111, 53:117}

    x = st.lower().translate(switcheroodle)
    print(x)

encode("HELLo")
