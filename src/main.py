import os
import sys
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from time import time
from tqdm import tqdm
from typing import List, Tuple
from . import BASE_DIR

rc('animation', html='html5')

TOTAL_STEPS = 5

INITIAL_TIME = time()


def read_file(filename: str, compression: int, output: str) -> Tuple[List[np.array], float]:
    files = os.listdir(BASE_DIR)
    if output in files:
        proceed = input(f'{output} already exists in directory. Proceed and overwrite? [y/N] ')
        if proceed.lower() != 'y':
            sys.exit(0)

    print(f'(1/{TOTAL_STEPS}) Reading video')
    cap = cv.VideoCapture(filename)
    fps = cap.get(cv.CAP_PROP_FPS)
    frames = []

    print(f'(2/{TOTAL_STEPS}) Extracting frames')
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frames.append(frame)

    print(f'(3/{TOTAL_STEPS}) Compressing frames')
    if compression < 100:
        height, width, _ = frames[0].shape
        height = int(height * compression / 100)
        width = int(width * compression / 100)
        frames = list(map(lambda x: cv.resize(x, (width, height)), frames))
    cap.release()
    return frames, fps


def save_file(filename: str, frames: List[np.array], fps: float):
    print(f'(4/{TOTAL_STEPS}) Assembling frames')
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

    print(f'(5/{TOTAL_STEPS}) Rendering GIF')
    try:
        # assuming ImageMagick installed
        anim.save(savename, writer='imagemagick', fps=int(fps))
    except Exception as e:
        # fallback to default backend
        print(e)
        print('Falling back to Pillow...')
        anim.save(savename, writer='pillow', fps=int(fps))
    plt.close(fig)

    end_time = time()
    delta_time = end_time - INITIAL_TIME
    if delta_time >= 60:
        delta_min = int(delta_time / 60)
        delta_sec = round(delta_time % 60, 2)
        delta_str = f'{delta_min} min {delta_sec} s'
    else:
        delta_str = f'{round(delta_time, 2)} s'
    print(f'Done in {delta_str}')
