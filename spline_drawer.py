
import numpy as np
from typing import List
from scipy import interpolate
import matplotlib.pyplot as plt


class spline:
    def __init__(self) -> None:
        pass

    def draw(
        xs: List[int],
        ys: List[int],
        k: int,
        path: str
    ) -> str:

        xs_size = len(xs)
        t = np.linspace(0, 1, xs_size - 2)
        t = [0, 0, 0] + list(t)
        t = list(t) + [1, 1, 1]
        tck_params = [t, [xs, ys], k]

        # create array with length
        u3 = np.linspace(0, 1, (max(xs_size * 2, 70)))

        # Evaluate
        res = interpolate.splev(u3, tck_params)

        # Read image
        img = plt.imread(path)

        # Plot it
        fig, ax = plt.subplots()
        ax.imshow(img)
        # TODO: is need?
        ax.plot(
            xs,
            ys,
            'k--',
            marker='o',
            markerfacecolor='red',
            label='Control polygon'
        )
        ax.plot(res[0], res[1], 'b', linewidth=1.0, label='B-spline curve')
        ax.axis('off')

        # Save file
        filename = './static/out.jpg'
        plt.savefig(filename)
        plt.close()

        return filename
