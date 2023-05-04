import multiprocessing
import os
import time
from concurrent.futures import ProcessPoolExecutor

from PIL import Image, ImageFilter

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]


def create_thumbnail(filename, size=(50, 50), thumb_dir='thumbs'):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'{filename} was processed...')


def main():
    start = time.perf_counter()

    for filename in filenames:
        create_thumbnail(filename)

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


def main2():
    start = time.perf_counter()

    # create processes
    processes = [multiprocessing.Process(target=create_thumbnail, args=[filename])
                 for filename in filenames]

    # start the processes
    for process in processes:
        process.start()

    # wait for completion
    for process in processes:
        process.join()

    with ProcessPoolExecutor() as executor:
        executor.map(create_thumbnail, filenames)

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')


if __name__ == "__main__":
    main()
    main2()
