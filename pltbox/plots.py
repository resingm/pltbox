import matplotlib as mpl
from matplotlib import pyplot as plt

from pltbox import colors

def fig(
    rows: int,
    cols: int,
    size_x: float = 12.0,
    size_y: float = 4.0,
    sharex: bool = False,
    sharey: bool = False,
    is_paper: bool = False,
    bg_color: str = "#202020",
    fg_color: str = "#ffffff",
) -> tuple:
    
    if not is_paper:
        bg = colors.n_shades_of(bg_color, 2)
        fg = colors.n_shades_of(fg_color, 2)

        # Set the default color for text in all figures
        mpl.rcParams["text.color"] = fg[0]
        mpl.rcParams["axes.edgecolor"] = fg[1]
        mpl.rcParams["axes.labelcolor"] = fg[1]
        mpl.rcParams["xtick.color"] = fg[1]
        mpl.rcParams["ytick.color"] = fg[1]
        mpl.rcParams["legend.facecolor"] = bg[1]
        fig, ax = plt.subplots(
                rows,
                cols,
                figsize=(size_x, size_y),
                sharex=sharex,
                sharey=sharey,
                facecolor=bg[0],
        )
    else:
        fig, ax = plt.subplots(rows, cols, figsize=(size_x, size_y), sharex=sharex, sharey=sharey)

    if (rows * cols) > 1:
        ax = ax.T.flatten()
        for e in ax:
            if not is_paper:
                e.set_facecolor(bg[0])
    else:
        if not is_paper:
            ax.set_facecolor(bg[0])

    return fig, ax


