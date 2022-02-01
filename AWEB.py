def spn(toponym):
    bounded_by = toponym["boundedBy"]["Envelope"]
    upper_corner = bounded_by["upperCorner"].split(" ")
    lower_corner = bounded_by["lowerCorner"].split(" ")
    dlon = float(upper_corner[0]) - float(lower_corner[0])
    dlat = float(upper_corner[1]) - float(lower_corner[1])
    return abs(dlon), abs(dlat)
