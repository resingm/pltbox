
# The color palettes are crafted by Paul Tom with the intent to provide
# accessibility to visually impaired people.


BLUE = "blue"
CYAN = "cyan"
GREEN = "green"
GREY = "grey"
INDIGO = "indigo"
LIGHT_BLUE = "light blue"
LIGHT_CYAN = "light cyan"
LIGHT_YELLOW ="light yellow"
MAGENTA = "magenta"
MINT = "mint"
OLIVE = "olive"
ORANGE = "orange"
PALE_GREY = "pale grey"
PEAR = "pear"
PINK = "pink"
PURPLE = "purple"
RED = "red"
ROSE = "rose"
SAND = "sand"
TEAL = "teal"
WINE = "wine"
YELLOW = "yellow"


_MAX_OCT = (2 << 7) - 1

# bright
COLORS_BRIGHT = {
    BLUE : "#4477aa",
    CYAN: "#66ccee",
    GREEN: "#228833",
    YELLOW: "#ccbb44",
    RED: "#ee6677",
    PURPLE: "#aa3377",
    GREY: "#bbbbbb",
}

# light
COLORS_LIGHT = {
    LIGHT_BLUE: "#77aadd",
    LIGHT_CYAN: "#00ddff",
    MINT: "#44bb99",
    PEAR: "#bbcc33",
    OLIVE: "#aaaa00",
    LIGHT_YELLOW: "#eedd88",
    ORANGE: "#ee8866",
    PINK: "#ffaabb",
    PALE_GREY: "#dddddd",
}

# muted
COLORS_MUTED = {
    INDIGO: "#332288",
    CYAN: "#88ccee",
    TEAL: "#44aa99",
    GREEN: "#117733",
    OLIVE: "#999933",
    SAND: "#ddcc77",
    ROSE: "#cc6677",
    WINE: "#882255",
    PURPLE: "#aa4499",
    PALE_GREY: "#dddddd",
}

# vibrant
COLORS_VIBRANT = {
    BLUE: "#0077bb",
    CYAN: "#33bbee",
    TEAL: "#009988",
    ORANGE: "#ee7733",
    RED: "#cc3311",
    MAGENTA: "#ee3377",
    GREY: "#bbbbbb",
}


def c_select(color_label: str, palette: dict) -> str:
    """TODO
    """
    if color_label.lower() not in palette.keys():
        raise ValueError(f"'{color_label}' not in color palette")

    return palette[color_label.lower()]
    

def n_select(n: int, palette: dict) -> list:
    """Returns a sample of colors from the given color palette."""

    colors = list(palette.values())
    n_missing = n - len(colors)

    if n_missing > 0:
        missing_colors = n_shades_of(colors[-1], n_missing + 1)
        colors = colors[:-1] + missing_colors

    return colors[:n]

    #if n > len(palette):
    #    raise ValueError(f"Selected color palette just has {len(palette)} colors.")

    #return list(palette.values())[:n]


def bright(color_label: str) -> str:
    """Get a bright color"""
    return c_select(color_label, COLORS_BRIGHT)

def light(color_label: str) -> str:
    """Get a light color"""
    return c_select(color_label, COLORS_LIGHT)

def muted(color_label: str) -> str:
    """Get a muted color"""
    return c_select(color_label, COLORS_MUTED)

def vibrant(color_label: str) -> str:
    """Get a vibrant color"""
    return c_select(color_label, COLORS_VIBRANT)

def n_bright(n: int) -> list:
    """Get n bright colors"""
    return n_select(n, COLORS_BRIGHT)

def n_light(n: int) -> list:
    """Get n light colors"""
    return n_select(n, COLORS_LIGHT)

def n_muted(n: int) -> list:
    """Get n muted colors"""
    return n_select(n, COLORS_MUTED)

def n_vibrant(n: int) -> list:
    """Get n vibrant colors"""
    return n_select(n, COLORS_VIBRANT)



def alpha(color: str, a: float) -> str:
    """Appends the alpha channel to the color string. The alpha value
    should be a number between 0 and 1:

        1 = 100% opaque = intransparent
        0 = 0% opaque = fully transparent
    """
    a = int(a * _MAX_OCT)
    a = hex(a)[2:]
    if len(a) < 2:
        a = "0" + a

    return color + a



def n_shades_of(color: str, n: int) -> list:
    """Get as many shades of the same color as you wish. The colors are
    fully opaque. This means one can still play with the alpha channel
    to modify transparency.
    """
    channels = hex2rgb(color)
    r, g, b = channels

    fracts = [1 - (i / n) for i in range(n)]
    deltas = [_MAX_OCT - e for e in channels]

    shades = []

    for d in fracts:
        rd = _MAX_OCT - int(deltas[0] * d)
        gd = _MAX_OCT - int(deltas[1] * d)
        bd = _MAX_OCT - int(deltas[2] * d)

        shade = rgb2hex((rd, gd, bd))
        shades.append(shade)

    return shades


def hex2rgb(color: str) -> tuple:
    """Converts the color string to a tuple of 3 integers representing
    RGB"""
    color = color.lstrip("#")
    return (int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))


def rgb2hex(rgb: tuple) -> str:
    """Converts a tuple of 3 colors to a color hexstring"""
    rgb = [hex(c)[2:] for c in list(rgb)]
    rgb = map(lambda s: s.rjust(2, "0"), rgb)
    rgb = "".join(rgb)
    return "#" + rgb

