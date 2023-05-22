# @file common.py
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

from hashlib import md5

from .options import Options
from .messages import Messages

class Common:
   toolName = 'drawIT'
   toolVersion = '0.10.14'
   toolTitle = toolName + ' ' + toolVersion

   options = None
   messages = None

   def __init__(self):
      self.options = Options(self.toolName)
      self.messages = Messages(self.options)
      return

   # Utilities

   def compress(self, string):
      hash = md5(string.encode())
      return hash.hexdigest()

   def truncateText(self, text, size, linebreak):
      if text.find(linebreak) == -1:
         if len(text) > size:
            return text[0:size-1] + '...'
         else:
            return text
      else:
         textsplit = text.split(linebreak)
         newtext = ''
         count = 0
         for name in textsplit:
            count = count + 1
            if len(name) == 0:
               continue
            elif len(name) > size:
               if count == 1:
                  newtext = name[0:size-1] + '...'
               else:
                  newtext = newtext + linebreak + name[0:size-1] + '...'
            else:
               if count == 1:
                  newtext = name
               else:
                  newtext = newtext + linebreak + name

      if len(newtext) > 0:
         return newtext
      else:
         return text

   # Options

   def getAccountID(self):
      return self.options.getAccountID()

   def setAccountID(self, value):
      self.options.setAccountID(value)

   def getAPIKey(self):
      return self.options.getAPIKey()

   def setAPIKey(self, value):
      self.options.setAPIKey(value)

   def setAllRegion(self):
      self.options.setAllRegion()

   def setGermanyRegion(self):
      self.options.setGermanyRegion()

   def setOsakaRegion(self):
      self.options.setOsakaRegion()

   def setSaoPauloRegion(self):
      self.options.setSaoPauloRegion()

   def setSydneyRegion(self):
      self.options.setSydneyRegion()

   def setTokyoRegion(self):
      self.options.setTokyoRegion()

   def setTorontoRegion(self):
      self.options.setTorontoRegion()

   def setUnitedKingdomRegion(self):
      self.options.setUnitedKingdomRegion()

   def setUSEastRegion(self):
      self.options.setUSEastRegion()

   def setUSSouthRegion(self):
      self.options.setUSSouthRegion()

   def getRegion(self):
      return self.options.getRegion()

   def setRegion(self, value):
      self.options.setRegion(value)

   def getInputFile(self):
      return self.options.getInputFile()

   def setInputFile(self, value):
      self.options.setInputFile(value)

   def getInputFolder(self):
      return self.options.getInputFolder()

   def setInputFolder(self, value):
      self.options.setInputFolder(value)

   def getOutputFile(self):
      return self.options.getOutputFile()

   def setOutputFile(self, value):
      self.options.setOutputFile(value)

   def getOutputFolder(self):
      return self.options.getOutputFolder()

   def setOutputFolder(self, value):
      self.options.setOutputFolder(value)

   def getTablesFolder(self):
      return self.options.getTablesFolder()

   def setTablesFolder(self, value):
      self.options.setTablesFolder(value)

   def getProvider(self):
      return self.options.getProvider()

   def setProvider(self, provider):
      self.options.setProvider(provider)

   def setProviderIBM(self):
      self.options.setProviderIBM()

   def setProviderAny(self):
      self.options.setAnyProviderAny()

   def isProviderIBM(self):
      return self.options.isProviderIBM()

   def isProviderAny(self):
      return self.options.isProviderAny()

   def isBatchMode(self):
      return self.options.isBatchMode()

   def isGUIMode(self):
      return self.options.isGUIMode()

   def isWebMode(self):
      return self.options.isWebMode()

   def isBatchMode(self, value):
      return self.options.isBatchMode(value)

   def isGUIMode(self, value):
      return self.options.isGUIMode(value)

   def isWebMode(self, value):
      return self.options.isWebMode(value)

   def getRunMode(self):
      return self.options.getRunMode()

   def setRunMode(self, value):
      self.options.setRunMode(value)

   def isInputRIAS(self):
      return self.options.isInputRIAS()

   def isInputJSON(self):
      return self.options.isInputJSON()

   def isInputYAML(self):
      return self.options.isInputYAML()

   def isInputTerraform(self):
      return self.options.isInputTerraform()

   def setInputRIAS(self):
      return self.options.setInputRIAS()

   def setInputJSON(self):
      return self.options.setInputJSON()

   def setInputYAML(self):
      return self.options.setInputYAML()

   def setInputTerraform(self):
      return self.options.setInputTerraform()

   #def getInputType(self):
   #   return self.options.getInputType()

   #def setInputType(self, value):
   #   self.options.setInputType(value)

   def setAllIcons(self):
      self.options.setAllIcons()

   def isAllIcons(self):
      return self.options.isAllIcons()

   def isDesignatedVPC(self, name):
      return self.options.isDesignatedVPC(name)

   def setDirectionLR(self):
      self.options.setDirectionLR()

   def setDirectionTB(self):
      self.options.setDirectionTB()

   def isDirectionLR(self):
      return self.options.isDirectionLR()

   def isDirectionTB(self):
      return self.options.isDirectionTB()

   def setAlternateWhite(self):
      self.options.setAlternateWhite()

   def setAlternateLight(self):
      self.options.setAlternateLight()

   def setAlternateNone(self):
      self.options.setAlternateNone()

   def setAlternateUser(self):
      self.options.setAlternateUser()

   def isAlternateWhite(self):
      return self.options.isAlternateWhite()

   def isAlternateLight(self):
      return self.options.isAlternateLight()

   def isAlternateNone(self):
      return self.options.isAlternateNone()

   def isAlternateUser(self):
      return self.options.isAlternateUser()

   def getProvider(self):
      return self.options.getProvider()

   def setProviderAny(self):
      self.options.setProviderAny()

   def setProviderIBM(self):
      self.options.setProviderIBM()

   def isProviderAny(self):
      return self.options.isProviderAny()

   def isProviderIBM(self):
      return self.options.isProviderIBM()

   # Messages

   def printStartDiagram(self, diagramname, cloud):
      self.messages.printStartDiagram(diagramname, cloud)

   def printStartFile(self, filename, cloud):
      self.messages.printStartFile(filename, cloud)

   def printStartRIASwithKey(self, apikey, region):
      self.messages.printStartRIASwithKey(apikey, region)

   def printStartRIASwithAccount(self, apikey, accountid, region):
      self.messages.printStartRIASwithAccount(apikey, accountid, region)

   def printDone(self, filename, cloud):
      self.messages.printDone(filename, cloud)

   def printExit(self):
      self.messages.printExit()

   def printMissingVPCs(self):
      self.messages.printMissingVPCs()

   def printMissingSubnets(self):
      self.messages.printMissingSubnets()

   def printMissingZone(self, subnetname):
      self.messages.printMissingZone(subnetname)

   def printInvalidMode(self, mode):
      self.messages.printInvalidMode(mode)

   def printInvalidProvider(self, provider):
      self.messages.printInvalidProvider(provider)

   def printInvalidInput(self):
      self.messages.printInvalidInput()

   def printInvalidFile(self, inputfile):
      self.messages.printInvalidFile(inputfile)

   def printInvalidInstance(self, instanceid):
      self.messages.printInvalidInstance(instanceid)

   def printInvalidLoadBalancer(self, lbname):
      self.messages.printInvalidLoadBalancer(lbname)

   def printInvalidPrivateLoadBalancer(self, lbname):
      self.messages.printInvalidPrivateLoadBalancer(lbname)

   def printInvalidPublicGateway(self, pubgateid):
      self.messages.printInvalidPublicGateway(pubgateid)

   def printInvalidSubnet(self, subnetid):
      self.messages.printInvalidSubnet(subnetid)

   def printInvalidVPC(self, vpcid):
      self.messages.printInvalidVPC(vpcid)

   def printInvalidVPE(self, vpeid):
      self.messages.printInvalidVPE(vpeid)

   def printMissingPool(self, lbname):
      self.messages.printMissingPool(lbname)

   def printMissingMember(self, lbname, lbpoolname):
      self.messages.printMissingMember(lbname, lbpoolname)

   def printInvalidInstanceMember(self, lbname, lbpoolname, instanceid):
      self.messages.printInvalidInstanceMember(lbname, lbpoolname, instanceid)

   def printRequestMessage(self, code, message, href):
      self.messages.printRequestMessage(code, message, href)

   def printResponseMessage(self, code, message):
      self.messages.printResponseMessage(code, message)

   def printInvalidDirection(self, direction):
      self.messages.printInvalidDirection(direction)

   def printInvalidOutputFormat(self, outputformat):
      self.messages.printInvalidOutputFormat(outputformat)

   def printInvalidFont(self, font):
      self.messages.printInvalidFont(font)

   def printInvalidIcon(self, icon):
      self.messages.printInvalidIcon(icon)

   def printInvalidClusterShape(self, shape):
      self.messages.printInvalidClusterShape(shape)

   def printInvalidNodeShape(self, shape):
      self.messages.printInvalidNodeShape(shape)

   def printInvalidProvider(self, provider):
      self.messages.printInvalidProvider(provider)

   def printInvalidAlternate(self, alternate):
      self.messages.printInvalidAlternate(alternate)

   def printInvalidEdgeStyle(self, style):
      self.messages.printInvalidEdgeStyle(style)

   def printInvalidFillColor(self, color):
      self.messages.printInvalidFillColor(color)

   def printInvalidLineColor(self, color):
      self.messages.printInvalidLineColor(color)

  # Constants

   def getToolName(self):
      return self.toolName

   def getToolVersion(self):
      return self.toolVersion

   def getToolTitle(self):
      return self.toolTitle
