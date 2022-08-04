# @file options.py
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

from enum import Enum

from common.utils import *

class RunMode(Enum):
   BATCH = 'batch'
   GUI = 'gui'
   WEB = 'web'

class InputType(Enum):
   RIAS = 'rias'
   JSON = 'json'
   YAML = 'yaml'

class OutputSplit(Enum):
   SINGLE = 'single'
   REGION = 'region'
   VPC = 'vpc'

class OutputDetail(Enum):
   LOW = 'low'
   MEDIUM = 'medium'
   HIGH = 'high'

class OutputShapes(Enum):
   LOGICAL = 'logical'
   PRESCRIBED = 'prescribed'

class Regions(Enum):
   ALL = 'all'
   GERMANY = 'eu-de'
   OSAKA = 'jp-osa'
   SAOPAULO = 'br-sao'
   SYDNEY = 'au-syd'
   TOKYO = 'jp-tok'
   TORONTO = 'ca-tor'
   UNITEDKINGDOM = 'eu-gb'
   USEAST = 'us-east'
   USSOUTH = 'us-south'

class Options:
   runMode = None
   inputType = None
   accountID = ''
   apiKey = ''
   inputFile = ''
   region = None
   outputFile = ''
   outputFolder = ''
   outputSplit = None
   outputDetail = None
   outputShapes = None

   def __init__(self):
      self.runMode = RunMode.BATCH
      self.inputType = InputType.JSON
      self.region = Regions.USSOUTH
      self.outputFile = 'output'
      self.outputFolder = os.path.join(os.path.expanduser('~'), 'Documents', TOOLNAME)
      self.outputSplit = OutputSplit.SINGLE
      self.outputDetail = OutputDetail.MEDIUM
      self.outputShapes = OutputShapes.PRESCRIBED
      return

   def getAccountID(self):
      return self.accountID

   def setAccountID(self, value):
      self.accountID = value

   def getAPIKey(self):
      return self.apiKey

   def setAPIKey(self, value):
      self.apiKey = value

   def getRegion(self):
      return self.region

   def setRegion(self, value):
      self.region = value

   def getInputFile(self):
      return self.inputFile

   def setInputFile(self, value):
      self.inputFile = value

   def getOutputFile(self):
      return self.outputFile

   def setOutputFile(self, value):
      self.outputFile = value

   def setOutputFile(self, value):
      self.outputFile = value

   def getOutputFolder(self):
      return self.outputFolder

   def setOutputFolder(self, value):
      self.outputFolder = value

   def isBatchMode(self):
      return self.runMode == RunMode.BATCH

   def isGUIMode(self):
      return self.runMode == RunMode.GUI

   def isWebMode(self):
      return self.runMode == RunMode.WEB

   def getRunMode(self):
      return self.runMode

   def setRunMode(self, value):
      self.runMode = value

   def isInputRIAS(self):
      return self.inputType == InputType.RIAS

   def isInputJSON(self):
      return self.inputType == InputType.JSON

   def isInputYAML(self):
      return self.inputType == InputType.YAML

   def getInputType(self):
      return self.inputType

   def setInputType(self, value):
      self.inputType = value

   def isSingleSplit(self):
      return self.outputSplit == OutputSplit.SINGLE

   def isRegionSplit(self):
      return self.outputSplit == OutputSplit.REGION

   def isVPCSplit(self):
      return self.outputSplit == OutputSplit.VPC

   def getOutputSplit(self):
      return self.outputSplit

   def setOutputSplit(self, value):
      self.outputSplit = value

   def isLowDetail(self):
      return self.outputDetail == OutputDetail.LOW

   def isMediumDetail(self):
      return self.outputDetail == OutputDetail.MEDIUM

   def isHighDetail(self):
      return self.outputDetail == OutputDetail.HIGH

   def getOutputDetail(self):
      return self.outputDetail

   def setOutputDetail(self, value):
      self.outputDetail = value

   def isLogicalShapes(self):
      return self.outputShapes == OutputShapes.LOGICAL

   def isPrescribedShapes(self):
      return self.outputShapes == OutputShapes.PRESCRIBED

   def getOutputShapes(self):
      return self.outputShapes

   def setOutputShapes(self, value):
      self.outputShapes = value
