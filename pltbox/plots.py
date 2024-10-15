import matplotlib as mpl
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
    
    if not paper_mode: 
        bg = colors.n_shades_of(bg_color, 2)
        fg = colors.n_shades_of(fg_color, 2)

        # Set the default color for text in all figures
        mpl.rcParams["text.color"] = fg[0]
        mpl.rcParams["axes.edgecolor"] = fg[1]
        mpl.rcParams["axes.labelcolor"] = fg[1]
        mpl.rcParams["xtick.color"] = fg[1]
        mpl.rcParams["ytick.color"] = fg[1]
        mpl.rcParams["legend.facecolor"] = bg[1]
    
    

def fig(
    rows: int,
    cols: int,
    size_x: float = 12.0,
    size_y: float = 4.0,
    sharex: bool = False,
    sharey: bool = False,
) -> tuple:
    global paper_mode, initialized, bg, fg
    
    if not initialized:
        raise Exception("Module `plots` not initialized. Call plots.init(is_paper: bool)")
    
    if paper_mode:
        fig, ax = plt.subplots(rows, cols, figsize=(size_x, size_y), sharex=sharex, sharey=sharey)
    else:
        fig, ax = plt.subplots(
                rows,
                cols,
                figsize=(size_x, size_y),
                sharex=sharex,
                sharey=sharey,
                facecolor=bg[0],
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

