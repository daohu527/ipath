#!/usr/bin/env python

# Copyright 2022 daohu527 <daohu527@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
import logging

from math import nan, isnan, sqrt

from ipath.reader import Reader
from ipath.draw import draw_line, show


def clamp(n, minn, maxn):
  return max(min(maxn, n), minn)

class Point:
  def __init__(self, x=None, y=None, v=None):
    self.x = x
    self.y = y
    self.v = v

  def __str__(self):
    return "{},{},{}".format(self.x, self.y, self.v)


def draw_path(line, has_color):
  draw_line(line, has_color)
  show()

def get_user_data(localization, data_type):
  data = None
  logging.debug(data_type)
  if data_type == 'v':
    velocity = localization.pose.linear_velocity
    data = sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)
  elif data_type == 'a':
    acc = localization.pose.linear_acceleration
    data = sqrt(acc.x**2 + acc.y**2 + acc.z**2)
  logging.debug(data)
  return data

def get_path(data_type):
  line = []
  for localization in Reader():
    logging.debug(localization)
    position = localization.pose.position
    v = get_user_data(localization, data_type)
    point = Point(position.x, position.y, v)
    line.append(point)
  return line

def save_path(filename, line):
  with open(filename, 'w') as f:
    for point in line:
      if not isnan(point.x) and not isnan(point.y):
        f.write("{}\n".format(point))

def read_path(filename):
  line = []
  with open(filename, 'r') as f:
    for l in f:
      l = l.replace("\n", '')
      data = l.split(',')
      point = Point(float(data[0]), float(data[1]), float(data[2]))
      line.append(point)
  return line

def main(args=sys.argv):
  parser = argparse.ArgumentParser(
    description="Apollo path and simple map making tool.",
    prog="main.py")

  parser.add_argument(
    "-s", "--save", action="store", type=str, required=False,
    nargs='?', const='path.txt', help="save waypoint file path")

  parser.add_argument(
    "-c", "--has_color", action="store", type=bool, required=False,
    nargs='?', default=True, const=True, help="draw with color or not")

  parser.add_argument(
    "-d", "--data_type", action="store", type=str, required=False,
    nargs='?', default="v", const="v", help="user define data")

  parser.add_argument(
    "-i", "--input", action="store", type=str, required=False,
    help="waypoint file path")
  parser.add_argument(
    "-o", "--output", action="store", type=str, required=False,
    help="map output path")


  args = parser.parse_args(args[1:])
  # 1. read from pipe
  # 2. show map
  if args.input is not None:
    line = read_path(args.input)
    for p in line:
      logging.debug(p)
    draw_path(line, args.has_color)
  else:
    line = get_path(args.data_type)
    if args.save is not None:
      save_path(args.save, line)
    draw_path(line, args.has_color)

# if __name__ == "__main__":
#   main(sys.argv)
