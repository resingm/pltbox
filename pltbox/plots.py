import matplotlib as mpl
from cycler import cycler
from matplotlib import pyplot as plt

from pltbox import colors

initialized = False
paper_mode = False
bg = None
fg = None

def init(is_paper: bool = False):
    global bg, fg, paper_mode, initialized
    
    initialized = True

    bg_color: str = "#202020"
    fg_color: str = "#ffffff"
    paper_mode = is_paper

    if paper_mode:
        bg_color, fg_color = fg_color, bg_color
        
    ac = colors.n_vibrant(7)
    bg = colors.n_shades_of(bg_color, 3)
    fg = colors.n_shades_of(fg_color, 3)

    # Set the axis color cycle
    mpl.rcParams["axes.prop_cycle"] = cycler("color", ac)

    # Set the default color for text in all figures
    mpl.rcParams["text.color"] = fg[0]
    mpl.rcParams["axes.edgecolor"] = fg[1]
    mpl.rcParams["axes.labelcolor"] = fg[1]
    mpl.rcParams["xtick.color"] = fg[1]
    mpl.rcParams["ytick.color"] = fg[1]
    mpl.rcParams["legend.facecolor"] = bg[1]

    # Box Plot Styling
    mpl.rcParams["boxplot.boxprops.color"] = fg[2]
    mpl.rcParams["boxplot.capprops.color"] = fg[2]
    mpl.rcParams["boxplot.flierprops.color"] = fg[2]
    mpl.rcParams["boxplot.flierprops.markeredgecolor"] = fg[0]
    mpl.rcParams["boxplot.medianprops.color"] = fg[2]
    mpl.rcParams["boxplot.whiskerprops.color"] = fg[2]
    mpl.rcParams["boxplot.vertical"] = False
    mpl.rcParams["boxplot.patchartist"] = True

    # Define default grid styling
    mpl.rcParams["grid.color"] = fg[1]
    mpl.rcParams["axes.grid"] = True
    mpl.rcParams["axes.grid.axis"] = "both"
    mpl.rcParams["grid.linestyle"] = "--"
    mpl.rcParams["grid.linewidth"] = 0.6
    mpl.rcParams["grid.alpha"] = 0.3


def fig(
    rows: int,
    cols: int,
    size_x: float = 12.0,
    size_y: float = 4.0,
    sharex: bool = False,
    sharey: bool = False,
    height_ratios: list = None
) -> tuple:
    global paper_mode, initialized, bg, fg
    
    if not initialized:
        raise Exception("Module `plots` not initialized. Call plots.init(is_paper: bool)")

    height_rations = height_ratios if height_ratios else [1] * rows
    
    if paper_mode:
        fig, ax = plt.subplots(
            rows,
            cols,
            figsize=(size_x, size_y),
            sharex=sharex,
            sharey=sharey,
            gridspec_kw={ "height_ratios": height_ratios },
        )
    else:
        fig, ax = plt.subplots(
            rows,
            cols,
            figsize=(size_x, size_y),
            sharex=sharex,
            sharey=sharey,
            facecolor=bg[0],
            gridspec_kw={ "height_ratios": height_ratios },
        )

    if (rows * cols) > 1:
        ax = ax.T.flatten()
        
        if not paper_mode:
            for e in ax:
                e.set_facecolor(bg[0])
    else:
        if not paper_mode:
            ax.set_facecolor(bg[0])

    return fig, ax

