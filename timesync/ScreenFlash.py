
# coding: utf-8

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((2200, 1400))

screen.fill((0, 0, 0))
pygame.display.flip()

time.sleep(1)

screen.fill((255, 255, 255))
white_time = time.time()
pygame.display.flip()

time.sleep(1)

screen.fill((0, 0, 0))
black_time = time.time()
pygame.display.flip()

time.sleep(1)

import csv

fname = "init_times_{}.csv".format(time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime()))

with open(fname, "w") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["color", "time"])
    csv_writer.writerow(["white", white_time])
    csv_writer.writerow(["black", black_time])
