

# TODO: Add a function to rotate the x_ticks:

def rotate_xticks(ax, rotation=45, alignment="right", mode="anchor"):
    ax.set_xticks(
        ax.get_xticks(),
        ax.get_xticklabels(),
        rotation=rotation,
        ha=alignment,
        rotation_mode=mode,
    )
    


# TODO: Add a function to format major and minor ticks

# ax.xaxis.set_minor_locator(mdates.DayLocator(interval=6))
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=28))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
