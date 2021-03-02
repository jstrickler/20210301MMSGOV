
with open('DATA/felix_auto.jpeg', "rb") as felix_in:
    chunk = felix_in.read(100)
    print(chunk)
    print()
    print(list(chunk))
    felix_in.seek(1000)  # next read/write at offset 1000
    chunk = felix_in.read(22)
    print(chunk, list(chunk))
    print(felix_in.tell())
    felix_in.seek(-50, 1)  # seek from current position
    print(felix_in.tell())
    felix_in.seek(-100, 2)  # seek from end
    end_chunk = felix_in.read()
    print(end_chunk)
    felix_in.seek(0)  # rewind
    # print(end_chunk.decode())
