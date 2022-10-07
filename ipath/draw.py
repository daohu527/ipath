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

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cm

from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap

fig, ax = plt.subplots()

def draw_line(line, has_color=True):
  x = [point.x for point in line]
  y = [point.y for point in line]
  v = [point.v for point in line]

  # when v < 1, we set it to 1
  max_value = max(max(v), 1)
  colors = [cm.to_hex(plt.cm.jet(int(vv/max_value*256))) for vv in v]

  points = np.array([x, y]).T.reshape(-1, 1, 2)
  segments = np.concatenate([points[:-1], points[1:]], axis=1)

  lc = None
  if has_color and colors:
    lc = LineCollection(segments, colors=colors, linewidths=1)
  else:
    lc = LineCollection(segments, linewidths=1)

  ax.add_collection(lc)
  ax.autoscale()

def show():
  # show map
  plt.show()
