# @file types.py
#
# Copyright contributors to the drawIT project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import time

from .common import Common

from .constants import ShapeKind, ShapeStyle
from .elements import Elements

class Types:
   common = None
   data = None
   elements = None
   icons = None

   def __init__(self, common):
      self.common = common
      self.data = {'header': {'type': 'device',
                              'compressed': 'false'}}
      self.elements = Elements(self.data)
      random.seed(time.time())

   def buildLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow != "":
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow != "":
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': ''},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLink(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow == "":
         style += 'startArrow=none;startFill=0;'
      else:
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow == "":
         style += 'endArrow=none;endFill=0;'
      else:
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLinkSingleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow != "":
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow != "":
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
               'geo':   {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildSolidLinkDoubleArrow(self, id, label, source, target, startarrow, endarrow, startfill, endfill, meta):
      style = 'dashed=0;'

      if startarrow != "":
         style += 'startArrow=' + startarrow + ';startFill=' + ('1' if startfill else '0')+ ';'
         if startarrow == "oval":
           style += "sourcePerimeterSpacing=4;"

      if endarrow != "":
         style += 'endArrow=' + endarrow + ';endFill=' + ('1' if endfill else '0') + ';'
         if endarrow == "oval":
           style += "targetPerimeterSpacing=4;"

      data = {'header': {'id': id,
                         'label': label},
              'cell':   {'style': style,
                         'edge': '1',
                         'parent': '1',
                         'source': source,
                         'target': target},
              'geo':    {'relative': '1',
                         'as': 'geometry'}}
      return data

   def buildNode(self, id, node, x, y, width, height, meta):
      shape = node["shape"].lower()
      if shape == "actor":
         style = ShapeStyle.ACTOR.value
      elif shape == "component":
         if self.common.isProviderAny():
            style = ShapeStyle.LOGICAL_COMPONENT.value
         else:
            style = ShapeStyle.PRESCRIBED_COMPONENT.value
      elif shape == "node":
         if self.common.isProviderAny():
            style = ShapeStyle.LOGICAL_NODE.value
         else:
            style = ShapeStyle.PRESCRIBED_NODE.value
      elif shape == "location":
         if self.common.isProviderAny():
            style = ShapeStyle.LOGICAL_LOCATION.value
         else:
            style = ShapeStyle.PRESCRIBED_LOCATION.value
      elif shape == "zone":
         style = ShapeStyle.ZONE.value
      else:
         style = ShapeStyle.PRESCRIBED_NODE.value

      if node["hideicon"] == True:
         style += ShapeStyle.HIDE_ICON.value

      pencolor = node["pencolor"]
      style += "strokeColor=" + pencolor + ';' 

      bgcolor = node["bgcolor"]
      if bgcolor:
         style += "fillColor=" + bgcolor + ';' 
      else:
         style += "fillColor=none;" 

      multiplicity = node["many"]
      if multiplicity:
         style += "ibmMultiplicity=1;"

      name = node["label"]
      subname = node["sublabel"]

      badgetext = node["badgetext"]
      badgeshape = node["badgeshape"]
      badgepencolor = node["badgepencolor"]
      badgebgcolor = node["badgebgcolor"]

      parentid = node["parentid"]
      parentid = '1' if parentid == None else parentid

      icon = node["icon"]
      #tempname = node["icon"]
      #iconname, tempcolor = self.icons.getIcon(tempname)

      shapelabel = "<b style='font-weight:600'>%Primary-Label%</b><br>%Secondary-Text%"
      #labelsize = 30
      labelsize = 24

      if len(name) > 0:
         name = self.common.truncateText(name, labelsize, '<br>')

      if len(subname) > 0:
         subname = self.common.truncateText(subname, labelsize, '<br>')

      header = {'id': id,
                'label': shapelabel,
                'placeholders': '1'}

      cell = {'parent': parentid,
              'style': style,
              'vertex': '1'}

      geo = {'x': str(x),
             'y': str(y),
             'width': str(width),
             'height': str(height),
             'as': 'geometry'}

      props = {'Badge-Text': badgetext,
               #'Icon-Name': iconname,
               'Icon-Name': icon,
               'Primary-Label': name,
               'Secondary-Text': subname}

      if meta != None:
         props.update(meta)

      data = {'header': header, 'cell': cell, 'geo': geo, 'props':  props}

      return data

   def buildValue(self, id, parentid, name, parent, subname, text, x, y, width, height):
      shape = ibmshapes['text']
      style = shape['style']  
      data = {'cell': {'id': id,
                       'value': text,
                       'style': style,
                       'parent': parentid,
                       'vertex': '1'},
              'geo':  {'x': str(x),
                       'y': str(y),
                       'width': str(width),
                       'height': str(height),
                       'as': 'geometry'}}
      return data

   def buildPage(self, name):
      data = {'header': {'id': self.common.compress(name),
                         'name': name},
              'graph':  {'dx': '1326',
                         'dy': '846',
                         'grid': '1',
                         'gridSize': '10',
                         'guides': '1',
                         'tooltips': '1',
                         'connect': '1',
                         'arrows': '1',
                         'fold': '1',
                         'page': '1',
                         'pageScale': '1',
                         'pageWidth': '850',
                         'pageHeight': '1100',
                         'math': '0',
                         'shadow': '0'},
              'cell0':  {'id': '0'},
              'cell1':  {'id': '1',
                         'parent': '0'}}
      return data

   def buildXML(self, vpcdata, pagedata):
      self.elements.buildXML(vpcdata, pagedata)

   def dumpXML(self, file, folder):
      self.elements.dumpXML(file, folder)

   def resetXML(self):
      self.data = {'header': {'type': 'device',
                         'compressed': 'false'}}
      self.elements.resetXML(self.data)
