def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

six_pack_volume = volume_cylinder(2.5, 6) * 6
