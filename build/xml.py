# @file xml.py
#
# Copyright IBM Corporation 2022
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

import os
import xml.etree.ElementTree as ET

class XML:
   def __init__(self, data):
      self.xml = ET.Element("mxfile", data['header'])
      self.root = None

   def addDiagram(self, data):
      diagram = ET.SubElement(self.xml, "diagram", data['header'])
      mxGraphModel = ET.SubElement(diagram, "mxGraphModel", data['graph'])
      self.root = ET.SubElement(mxGraphModel, "root")
      ET.SubElement(self.root, "mxCell", data['cell0'])
      ET.SubElement(self.root, "mxCell", data['cell1'])

   def addNode(self, data):
      userObject = ET.SubElement(self.root, "UserObject", data['header'] | data['props'])
      mxCell = ET.SubElement(userObject, "mxCell", data['cell'])
      mxGeometry = ET.SubElement(mxCell, "mxGeometry", data['geo'])

   def addValue(self, data):
      mxCell = ET.SubElement(self.root, "mxCell", data['cell'])
      mxGeometry = ET.SubElement(mxCell, "mxGeometry", data['geo'])

   def addLink(self, data):
      userObject = ET.SubElement(self.root, "UserObject", data['header'])
      mxCell = ET.SubElement(userObject, "mxCell", data['cell'])
      mxGeometry = ET.SubElement(mxCell, "mxGeometry", data['geo'])

   def buildXML(self, vpcdata, diagramdata):
      self.addDiagram(diagramdata)

      for key, data in vpcdata.items():
         if key == 'nodes':
            for node in data:
               self.addNode(node)
         elif key == 'values':
            for value in data:
               self.addValue(value)
         else:
            for link in data:
               self.addLink(link)

   def dumpXML(self, file, folder):
      pathname = os.path.join(folder, file)
      filepath, filename = os.path.split(pathname)

      if not os.path.exists(filepath):
         os.makedirs(filepath)

      tree = ET.ElementTree(self.xml)
      tree.write(pathname)

   def resetXML(self, data):
      self.xml = ET.Element("mxfile", data['header'])
      self.root = None
