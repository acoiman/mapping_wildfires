# modified from: https://medium.com/@busybus/rendered-maps-with-python-ffba4b34101c
# script to calculate the zoom start of a Folium Map object
# License: CC0 -- no rights reserved

from math import pi, log, tan, exp, atan, log2, floor

# convert geographical coordinates to pixels
# https://en.wikipedia.org/wiki/Web_Mercator_projection
# note on google API: the world map is obtained with lat=lon=0, w=h=256, zoom=0, therefore:
ZOOM0_SIZE = 512

# Geo-coordinate in degrees => Pixel coordinate
def g2p(lat, lon, zoom):
    return (
        # x
        ZOOM0_SIZE * (2 ** zoom) * (1 + lon / 180) / 2,
        # y
        ZOOM0_SIZE / (2 * pi) * (2 ** zoom) * (pi - log(tan(pi / 4 * (1 + lat / 90))))
    )


# Pixel coordinate => geo-coordinate in degrees
def p2g(x, y, zoom):
    return (
        # lat
        (atan(exp(pi - y / ZOOM0_SIZE * (2 * pi) / (2 ** zoom))) / pi * 4 - 1) * 90,
        # lon
        (x / ZOOM0_SIZE * 2 / (2 ** zoom) - 1) * 180,
    )

def get_zoom_start(bbox):

    ''' 
        Function to calculate the zoom start of a Folium Map object 

        Parameters:
        -----------
        bbox (list): Bonding box of a Folium Map Object

        Returns:
        --------
        integer
            an interger number representing the zoom start level
    '''

    # the region of interest in geo-coordinates in degrees
    # for example, bbox = [120.2206, 22.4827, 120.4308, 22.7578]
    (left, bottom, right, top) = bbox

    # sanity check
    assert (-90 <= bottom < top <= 90)
    assert (-180 <= left < right <= 180)

    # rendered image map size in pixels
    (w, h) = (1024, 1024)

    # The center point of the region of interest
    (lat, lon) = ((top + bottom) / 2, (left + right) / 2)

    # reduce precision of (lat, lon) to increase cache hits
    snap_to_dyadic = (lambda a, b: (lambda x, scale=(2 ** floor(log2(abs(b - a) / 4))): (round(x / scale) * scale)))

    lat = snap_to_dyadic(bottom, top)(lat)
    lon = snap_to_dyadic(left, right)(lon)

    assert ((bottom < lat < top) and (left < lon < right)), "Reference point not inside the region of interest"

    # look for appropriate zoom level to cover the region of interest
    for zoom in range(16, 0, -1):
        # Center point in pixel coordinates at this zoom level
        (x0, y0) = g2p(lat, lon, zoom)

        # the "container" geo-region that the downloaded map would cover
        (TOP, LEFT) = p2g(x0 - w / 2, y0 - h / 2, zoom)
        (BOTTOM, RIGHT) = p2g(x0 + w / 2, y0 + h / 2, zoom)

        # Wwuld the map cover the region of interest?
        if (LEFT <= left < right <= RIGHT):
            if (BOTTOM <= bottom < top <= TOP):
                break
    return zoom