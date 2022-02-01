def spn(toponym):
    bounded_by = toponym["boundedBy"]["Envelope"]
    upper_corner = bounded_by["upperCorner"].split(" ")
    lower_corner = bounded_by["lowerCorner"].split(" ")
    dlen = float(upper_corner[0]) - float(lower_corner[0])
    dwid = float(upper_corner[1]) - float(lower_corner[1])
    return abs(dlen), abs(dwid)
