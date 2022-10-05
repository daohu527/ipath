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

from math import nan, isnan

from ipath.reader import Reader
from ipath.draw import draw_line, show

class Point:
  def __init__(self, x=None, y=None):
    self.x = x
    self.y = y

  def __str__(self):
    return "{},{}".format(self.x, self.y)


def draw_path(line):
  draw_line(line)
  show()

def get_path():
  line = []
  for localization in Reader():
    logging.debug(localization)
    line.append(localization.pose.position)
  return line

def save_path(filename, line):
  with open(filename, 'w') as f:
    for position in line:
      if not isnan(position.x) and not isnan(position.y):
        f.write(str(position.x) + "," + str(position.y) + "\n")

def read_path(filename):
  line = []
  with open(filename, 'r') as f:
    for l in f:
      l = l.replace("\n", '')
      data = l.split(',')
      point = Point(float(data[0]), float(data[1]))
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
    draw_path(line)
  else:
    line = get_path()
    if args.save is not None:
      save_path(args.save, line)
    draw_path(line)

# if __name__ == "__main__":
#   main(sys.argv)
