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

import sys
import logging

from google.protobuf import text_format
from modules.localization.proto import localization_pb2


class Reader:
  def __init__(self, f=None, options=None):
    self._file      = None
    self._filename  = None

    self._open_read(f)

  def __iter__(self):
    return self.read_from_pipe()

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, traceback):
    self.close()

  def read_from_pipe(self):
    single_object = ""
    for line in sys.stdin:
      # check if empty line
      if line == '\n':
        yield self.parse_localization(single_object)
        single_object = ""
      else:
        single_object += line

  def parse_localization(self, data):
    logging.debug("parse_localization:")
    logging.debug(data)

    localization = text_format.Parse(
        data,
        localization_pb2.LocalizationEstimate(),
        allow_unknown_field=True)
    logging.debug(localization)
    return localization

  def close(self):
    if self._file:
      self._close_file()

  def _close_file(self):
    self._file.close()
    self._file = None

  def _open_read(self, f):
    if f is not None:
      self._file = open(f, 'rb')
      self._filename = f
