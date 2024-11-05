import os  # noqa: D100 - Missing docstring in public module (auto-generated noqa)
from datetime import datetime

import matplotlib.gridspec as gridspec
import matplotlib.pylab as pl
import matplotlib.pyplot as plt
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)

## Using graph_plot function as a module in other files:

# import plotter as pl

# pl.graph_plot(y,x,title="Graph", save_fig=True)


def graph_plot(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y: list, x=[], title="", ylabel="", xlabel="", save_fig=False
):
    if x != []:
        plt.plot(x, y)
    else:
        plt.plot(y)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

    if save_fig is True:
        if title == "":
            t = "Plot"
        else:
            t = title.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        plt.savefig(path)
    plt.show()


# Examples

# y=[1,2,3,4,5,6,7,8,9]
# graph_plot(y, title="Sample Graph")


# y=[1,2,3,4,5,6,7,8,9]
# x=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
# graph_plot(y, x, title="Sample Graph1",  ylabel="Voltage", xlabel="Time", save_fig=True)

# _______________________________________________________________________________________________________________________________________________________


def plot_two(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y1: list,
    y2: list,
    x1=[],
    title1="",
    ylabel1="",
    xlabel1="",
    x2=[],
    title2="",
    ylabel2="",
    xlabel2="",
    stitle="",
    save_fig=False,
):
    fig, ax = plt.subplots(nrows=1, ncols=2)
    x1 = x1.tolist()
    x2 = x2.tolist()
    if x1 != [] and x2 != []:
        # create 2 subplots
        ax[0].plot(x1, y1)
        ax[1].plot(x2, y2)
    else:
        ax[0].plot(y1)
        ax[1].plot(y2)

    # plot 2 subplots
    ax[0].set_xlabel(xlabel1)
    ax[0].set_ylabel(ylabel1)
    ax[0].set_title(title1)
    ax[1].set_xlabel(xlabel2)
    ax[1].set_ylabel(ylabel2)
    ax[1].set_title(title2)

    plt.suptitle(stitle)

    # savefig
    if save_fig is True:
        if stitle == "":
            t = "Plot"
        else:
            t = stitle.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        plt.savefig(path)
    plt.show()


# _______________________________________________________________________________________________________________________________________________________


def plot_three(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y1: list,
    y2: list,
    y3: list,
    x1=[],
    title1="",
    ylabel1="",
    xlabel1="",
    x2=[],
    title2="",
    ylabel2="",
    xlabel2="",
    x3=[],
    title3="",
    ylabel3="",
    xlabel3="",
    stitle="",
    save_fig=False,
):
    gs = gridspec.GridSpec(2, 2)

    pl.figure()
    ax = pl.subplot(gs[0, :])
    ax.set_xlabel(xlabel1)
    ax.set_ylabel(ylabel1)
    ax.set_title(title1)
    x1 = x1.tolist()
    x2 = x2.tolist()
    x3 = x3.tolist()
    if x1 != []:
        ax.plot(x1, y1)

    else:
        ax.plot(y1)

    ax = pl.subplot(gs[1, 0])
    ax.set_xlabel(xlabel2)
    ax.set_ylabel(ylabel2)
    ax.set_title(title2)
    if x2 != []:
        ax.plot(x2, y2)
    else:
        ax.plot(y2)

    ax = pl.subplot(gs[1, 1])
    ax.set_xlabel(xlabel3)
    ax.set_ylabel(ylabel3)
    ax.set_title(title3)
    if x3 != []:
        ax.plot(x3, y3)
    else:
        ax.plot(y3)

    pl.suptitle(stitle)

    # savefig
    if save_fig is True:
        if stitle == "":
            t = "Plot"
        else:
            t = stitle.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        pl.savefig(path)
    pl.show()


# _______________________________________________________________________________________________________________________________________________________


def plot_four(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    y1: list,
    y2: list,
    y3: list,
    y4: list,
    x1=[],
    title1="",
    ylabel1="",
    xlabel1="",
    x2=[],
    title2="",
    ylabel2="",
    xlabel2="",
    x3=[],
    title3="",
    ylabel3="",
    xlabel3="",
    x4=[],
    title4="",
    ylabel4="",
    xlabel4="",
    stitle="",
    save_fig=False,
):
    fig, ax = plt.subplots(nrows=2, ncols=2)
    x1 = x1.tolist()
    x2 = x2.tolist()
    x3 = x3.tolist()
    x4 = x4.tolist()

    ax[0, 0].set_xlabel(xlabel1)
    ax[0, 0].set_ylabel(ylabel1)
    ax[0, 0].set_title(title1)
    if x1 != []:
        ax[0, 0].plot(x1, y1)
    else:
        ax[0, 0].plot(y1)

    ax[0, 1].set_xlabel(xlabel2)
    ax[0, 1].set_ylabel(ylabel2)
    ax[0, 1].set_title(title2)
    if x2 != []:
        ax[0, 1].plot(x2, y2)
    else:
        ax[0, 1].plot(y2)

    ax[1, 0].set_xlabel(xlabel3)
    ax[1, 0].set_ylabel(ylabel3)
    ax[1, 0].set_title(title3)
    if x3 != []:
        ax[1, 0].plot(x3, y3)
    else:
        ax[1, 0].plot(y3)

    ax[1, 1].set_xlabel(xlabel4)
    ax[1, 1].set_ylabel(ylabel4)
    ax[1, 1].set_title(title4)
    if x4 != []:
        ax[1, 1].plot(x4, y4)
    else:
        ax[1, 1].plot(y4)

    plt.suptitle(stitle)

    # savefig
    if save_fig is True:
        if stitle == "":
            t = "Plot"
        else:
            t = stitle.replace(" ", "_")
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y_%H-%M-%S")
        path = os.getcwd() + "\\" + t + "_" + current_time + ".png"
        print(path)
        plt.savefig(path)
    plt.show()


# ______________________________________________________________________________________________________________________________________________
