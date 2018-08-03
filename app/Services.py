from os import statvfs

'''
Return the free space and the total space of the HDD
@:return tuple(free_space,total_space)
'''


def space() -> "tuple(float, float)":
    st = statvfs("/")
    free_space = st.f_bavail * st.f_frsize / 1024 / 1024 / 1024
    total = (st.f_blocks * st.f_frsize) / 1024 / 1024 / 1024
    return round(free_space, 2), round(total, 2)
