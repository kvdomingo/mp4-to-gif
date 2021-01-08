import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from tqdm import tqdm
from typing import List, Tuple

rc('animation', html='html5')


def read_file(filename: str) -> Tuple[List[np.array], float]:
    cap = cv.VideoCapture(filename)
    fps = cap.get(cv.CAP_PROP_FPS)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frames.append(frame)
    cap.release()
    return frames, fps


def save_file(filename: str, frames: List[np.array], fps: float):
    height, width, _ = frames[0].shape
    dpi = 100
    ims = []
    fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
    ax = plt.Axes(fig, [0, 0, 1, 1])
    ax.set_axis_off()
    fig.add_axes(ax)
    # ax = fig.add_subplot(111)
    for i, frame in enumerate(tqdm(frames)):
        im = ax.imshow(frame, animated=True)
        # ax.grid(0)
        # ax.axis('off')
        # ax.autoscale_view('tight')
        ims.append([im])
    anim = animation.ArtistAnimation(fig, ims)
    savename = f'{"".join(filename.split(".")[:-1])}.gif'
    try:
        # assuming ImageMagick installed
        anim.save(savename, writer='imagemagick', fps=int(fps))
    except Exception as e:
        # fallback to default Pillow
        anim.save(savename, writer='pillow', fps=int(fps))
    plt.close(fig)
