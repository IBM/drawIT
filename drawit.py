# @file drawit.py
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

from argparse import ArgumentParser
from configparser import ConfigParser
from os import path
from platform import system as platform_system
from sys import exit as sys_exit

from drawit import Compose, Common, Load

class Config:
    def __init__(self, appName):
        
        # platform specific...
        if self.isWindows():
            self.filename = appName + ".ini"
        else:
            self.filename =  path.expanduser('~') + '/Library/Application Support/' + appName + ".ini"
        
        self.config = ConfigParser()
        if path.exists(self.filename):
            self.config.read(self.filename)
        if not self.config.has_section("parameters"):
            self.config.add_section("parameters")

        # platform specific...
        if not self.has("inputFolder"):
            if self.isWindows():
                self.setInputFolder("./" + appName)
            else:
                self.setInputFolder(path.join(path.expanduser('~'), 'Documents', appName))

        # platform specific...
        #if not self.has("outputDirectory"):
        #    if self.isWindows():
        #        self.setOutputDirectory("./" + appName)
        #    else:
        #        self.setOutputDirectory(path.join(path.expanduser('~'), 'Documents', appName))
        if not self.has("outputFolder"):
            if self.isWindows():
                self.setOutputFolder("./" + appName)
            else:
                self.setOutputFolder(path.join(path.expanduser('~'), 'Documents', appName))

    def isWindows(self):
        #return hasattr(sys, 'getwindowsversion')
        return platform_system == 'Windows'

    def get(self,propertyName):
        if propertyName in self.config["parameters"]:
            return self.config["parameters"][propertyName]
        else:
            return None
    
    def set(self,propertyName,value):
        self.config.set("parameters",propertyName,value)
        
    def has(self,propertyName):
        return self.config.has_option("parameters",propertyName)

    def write(self):
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)
            
    def getAPIKey(self):
        return self.get("apiKey")
    
    def setAPIKey(self,apiKey):
        self.set("apiKey",apiKey)

    def getAccountID(self):
        return self.get("accountID")
    
    def setAccountID(self,apiKey):
        self.set("accountID",accountID)

    def getInputFile(self):
        return self.get("inputFile")
    
    def setInputFile(self,inputFile):
        self.set("inputFile",inputFile)

    def getInputFolder(self):
        return self.get("inputFolder")
    
    def setInputFolder(self,inputFolder):
        self.set("inputFolder",inputFolder)

    def getOutputFile(self):
        return self.get("outputFile")
    
    def setOutputFile(self,outputFile):
        self.set("outputFile",outputFile)

    #def getOutputDirectory(self):
    #    return self.get("outputDirectory")
    
    #def setOutputDirectory(self,outputDirectory):
    #    self.set("outputDirectory",outputDirectory)

    def getOutputFolder(self):
        return self.get("outputFolder")
    
    def setOutputFolder(self,outputFolder):
        self.set("outputFolder",outputFolder)

    def getRegion(self):
        return self.get("region")
    
    def setRegion(self,region):
        self.set("region",region)

    def getRunMode(self):
        return self.get("runmode")
    
    def setRunMode(self,runmode):
        self.set("runmode",runmode)

    def getProvider(self):
        return self.get("provider")
    
    def setProvider(self,provider):
        self.set("provider",provider)

class drawit:
   title = None
   top = None
   statusText = None
   data = None
   compose = None 
   common = None
   generate = None
   inputFile = ''
   outputFolder = ''

   def __init__(self):
      self.common = Common()
      self.title = self.common.getToolTitle()

   #SAVE top = tkinter.Tk()
   #top.title(TOOLNAME + ' ' + COPYRIGHT.split(' ')[2])
   #SAVE title = COPYRIGHT.split(' - ')
   #SAVE top.title(title[0])
   #SAVE statusText = tkinter.StringVar()

   #printmessage(self.common.getToolCopyright())
   #printmessage(toolheader)

   def main(self): 

        config = Config("drawIT")  
        apikey = config.getAPIKey()
        accountid = config.getAccountID()
        inputfile = config.getInputFile()
        inputfolder = config.getInputFolder()
        outputfile = config.getOutputFile()
        outputfolder = config.getOutputFolder()
        runmode = config.getRunMode()
        provider = config.getProvider()
        region = config.getRegion()

        inputfile = path.join(inputfolder, self.common.getInputFile())
        outputfolder = path.join(outputfolder, self.common.getOutputFolder())

        self.common.setInputFile(inputfile)
        self.common.setInputFolder(inputfolder)
        self.common.setOutputFile(outputfile)
        self.common.setOutputFolder(outputfolder)

        parser = ArgumentParser(description='drawIT')

        parser.add_argument('-key', dest='apikey', default=self.common.getAPIKey(), help='API Key')
        parser.add_argument('-account', dest='accountid', default=self.common.getAccountID(), help='Account ID')
        parser.add_argument('-input', dest='inputfile', default=self.common.getInputFile(), help='JSON/YAML/TFSTATE')
        parser.add_argument('-region', dest='region', default=self.common.getRegion().value, help='all, au-syd, br-sao, ca-tor, eu-de, eu-gb, jp-osa, jp-tok, us-east, us-south')
        parser.add_argument('-output', dest='outputfolder', default=self.common.getOutputFolder(), help='output folder')

        parser.add_argument('-mode', dest='runmode', default=self.common.getRunMode().value, help="batch, gui, or web")
        parser.add_argument('-provider', dest='provider', default=self.common.getProvider().value, help="ibm")
        parser.add_argument('--version', action='version', version='drawIT ' + self.common.getToolTitle().split(' ')[1])
        
        args = parser.parse_args()

        #apikey = args.apikey.replace(' ', '')
        #accountid = args.accountid.replace(' ', '')
        #region = args.region.replace(' ', '')
        #inputfile = args.inputfile.replace(' ', '')
        #outputfolder = args.outputfolder.replace(' ', '')
        #outputtype = "xml"
        #outputdetail = args.outputdetail.replace(' ', '').lower()
        #runmode = args.runmode.replace(' ', '').lower()

        apikey = args.apikey
        accountid = args.accountid
        region = args.region.lower()
        inputfile = args.inputfile
        outputfolder = args.outputfolder
        outputtype = "xml"
        runmode = args.runmode.lower()
        provider = args.provider.lower()

        self.common.setAPIKey(apikey)
        self.common.setAccountID(accountid)
        self.common.setRegion(region)
        self.common.setInputFile(inputfile)
        self.common.setOutputFolder(outputfolder)
        self.common.setProvider(provider)

        if provider == "any":
           self.common.setProviderAny()
        elif provider == "ibm":
           self.common.setProviderIBM()
        else:
           self.common.printInvalidProvider(provider)
           return

        if region == "eu-de":
            self.common.setGermanyRegion()
        elif region == "jp-osa":
            self.common.setOsakaRegion()
        elif region == "br-sao":
            self.common.setSaoPauloRegion()
        elif region == "au-syd":
            self.common.setSydneyRegion()
        elif region == "jp-tok":
            self.common.setTokyoRegion()
        elif region == "ca-tor":
            self.common.setTorontoRegion()
        elif region == "eu-gb":
            self.common.setUnitedKingdomRegion()
        elif region == "us-east":
            self.common.setUSEastRegion()
        elif region == "us-south":
            self.common.setUSSouthRegion()
        else:
            self.common.setAllRegion()

        self.minInfo = False

        done = False

        if self.common.isBatchMode(args.runmode):
            #try: 
                #printmessage(COPYRIGHT)
                #print(toolheader)

                # Check for existing input file and exit if not valid.
                #if not path.isfile(self.inputFile):
                #    print(invalidinputfilemessage % inputfile)
                #    return

                apikey = self.common.getAPIKey()
                accountid = self.common.getAccountID()
                region = self.common.getRegion().value
                inputfile = self.common.getInputFile()
                outputtype = 'xml'

                #backupdirectory(options)

                if len(apikey) > 0:
                    self.common.setInputRIAS()
                    inputbase = apikey
                    outputfile = inputbase + '.' + outputtype
                    self.common.setOutputFile(outputfile)
                    if len(accountid) > 0:
                        self.common.printStartRIASwithAccount(apikey, accountid, region)
                    else:
                        self.common.printStartRIASwithKey(apikey, region)
                elif len(inputfile) > 0:
                    basename = path.basename(inputfile)
                    inputbase = path.splitext(basename)[0]
                    inputtype = path.splitext(basename)[1][1:]
                    if inputtype == 'yaml' or inputtype == 'yml':
                        self.common.setInputYAML()
                    elif inputtype == 'json':
                        self.common.setInputJSON()
                    elif inputtype == 'tfstate':
                        self.common.setInputTerraform()
                    else:
                        self.common.printInvalidFile(args.inputfile)
                        return
                    outputfile = inputbase + '.' + outputtype
                    self.common.setOutputFile(outputfile)
                    self.common.printStartFile(inputfile, self.common.getProvider().value.upper())
                else:
                    self.common.printInvalidInput()
                    return

                self.data = Load(self.common)
                if self.data.loadData():
                    self.compose = Compose(self.common, self.data)
                    self.compose.composeDiagrams()
                    self.common.printDone(path.join(outputfolder, outputfile), self.common.getProvider().value.upper())
                else:
                    self.common.printExit()

                done = True

        elif self.common.isGUIMode(args.runmode):
            from tkinter import Button, Entry, filedialog, Frame, IntVar, Label, messagebox, OptionMenu, StringVar, Tk, LEFT, RIGHT, TOP, E, W, X
        
            self.top = Tk()
            self.title = self.common.getToolTitle()
            self.top.title(self.title)
            self.statusText = StringVar()

            apikey = self.common.getAPIKey()
            accountid = self.common.getAccountID()
            region = self.common.getRegion().value
            inputfile = self.common.getInputFile()
            outputfolder = self.common.getOutputFolder()
            outputtype = 'xml'

            frame = Frame(self.top)
            frame.pack(fill=X, side=TOP)
            frame.grid_columnconfigure(1, weight=1)            
            row = 1
            
            genbutton = Frame(frame)
            eGenerate = Button(genbutton, text="Generate", state='normal', fg="blue", command=lambda: onClickGenerate())
            genbutton.grid(row=row, columnspan=2, sticky=E)
            eGenerate.pack(side=LEFT)
            row = row + 1
            
            Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            Label(frame, text="API Key").grid(row=row)
            lAPIKey = Entry(frame, bd=5)
            lAPIKey.insert(0, apikey)
            lAPIKey.grid(row=row, column=1, sticky=W + E)
            config.set("apiKey",apikey)
            config.write()
            row = row + 1

            Label(frame, text="Account ID").grid(row=row)
            lAccountID = Entry(frame, bd=5)
            lAccountID.insert(0, accountid)
            lAccountID.grid(row=row, column=1, sticky=W + E)
            config.set("accountID", accountid)
            config.write()
            row = row + 1

            Label(frame, text="- or -").grid(row=row, columnspan=2)
            row = row + 1

            #tkinter.Label(frame, text="Yaml").grid(row=row)
            #lInputFile = tkinter.Label(frame, text=inputfile)
            Label(frame, text="JSON/YAML").grid(row=row)
            lInputFile = Entry(frame, bd=5)
            lInputFile.insert(0, inputfile)
            lInputFile.grid(row=row, column=1, sticky=W + E)
            row = row + 1

            if len(apikey) > 0:
                lInputFile.delete(0, 'end')
                self.inputFile = ''
                config.set("inputFile", inputfile)
                config.write()

            def onClickSelectInputFile():
                file_selected = filedialog.askopenfilename(initialdir = inputfile,title = "Select JSON/YAML")
                if file_selected != None and len(file_selected) > 0:
                    self.inputFile = file_selected
                    lAPIKey.delete(0, 'end')
                    lInputFile.delete(0, 'end')
                    lInputFile.insert(0, self.inputFile)
                    lInputFile.configure(text=self.inputFile)
                    lAPIKey.delete(0, 'end')
                    self.apiKey = ''
                    config.set("apiKey", self.apiKey)
                    config.write()
                    config.set("inputFile", self.inputFile)
                    config.write()
                    
            inputbutton = Frame(frame)
            eSelectInputFile = Button(inputbutton, text="Select JSON/YAML", fg="blue", command=lambda: onClickSelectInputFile())
            inputbutton.grid(row=row, columnspan=2, sticky=E)
            eSelectInputFile.pack(side=RIGHT)
            row = row + 1

            Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            Label(frame, text="Directory").grid(row=row)
            lOutputDirectory = Entry(frame, bd=5)
            lOutputDirectory.insert(0, outputfolder)
            lOutputDirectory.grid(row=row, column=1, sticky=W + E)
            row = row + 1

            def onClickSelectOutputDirectory():
                folder_selected = filedialog.askdirectory(initialdir = outputfolder,title = "Select Directory")
                if folder_selected != None and len(folder_selected) > 0:
                    self.outputfolder = folder_selected
                    lOutputDirectory.delete(0, 'end')
                    lOutputDirectory.insert(0, self.outputfolder)
                    lOutputDirectory.configure(text=self.outputfolder)
                    config.set("outputDirectory",self.outputfolder)
                    config.write()
                    self.common.setOutputFolder(self.outputfolder)
                    
            outputbutton = Frame(frame)
            eSelectOutputFolder = Button(outputbutton, text="Select Folder", fg="blue", command=lambda: onClickSelectOutputFolder())
            outputbutton.grid(row=row, columnspan=2, sticky=E)
            eSelectOutputFolder.pack(side=RIGHT)
            row = row + 2

            Label(frame, text="").grid(row=row, columnspan=2)
            row = row + 1

            regionoptions = [
                "All",
                "Germany",
                "Osaka",
                "Sao Paulo",
                "Sydney",
                "Tokyo",
                "Toronto",
                "United Kingdom",
                "US East",
                "US South"]
            eRegion = StringVar(self.top)
            eRegion.set("All")
            Label(frame, text="Region").grid(row=row)
            #regionmenu = tkinter.OptionMenu(self.top, eRegion, *regionoptions).grid(row=row)
            regionmenu = OptionMenu(frame, eRegion, *regionoptions).grid(row=row, column=1, sticky=W + E)
            #regionmenu.pack()
            row = row + 1

            #tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            #row = row + 1

            #tkinter.Label(frame, text="").grid(row=row, columnspan=2)
            #row = row + 1

            def onClickGenerate():
                try:
                    self.statusText.set("Starting")
                    frame.after_idle(onClickGenerate)                   

                    region = str(eRegion.get()).lower()
                    if region == "eu-de":
                       self.common.setGermanyRegion()
                    elif region == "jp-osa":
                       self.common.setOsakaRegion()
                    elif region == "br-sao":
                       self.common.setSaoPauloRegion()
                    elif region == "au-syd":
                       self.common.setSydneyRegion()
                    elif region == "jp-tok":
                       self.common.setTokyoRegion()
                    elif region == "ca-tor":
                       self.common.setTorontoRegion()
                    elif region == "eu-gb":
                       self.common.setUnitedKingdomRegion()
                    elif region == "us-east":
                       self.common.setUSEastRegion()
                    elif region == "us-south":
                       self.common.setUSSouthRegion()
                    else:
                       self.common.setAllRegion()

                    accountid = str(lAccountID.get())
                    self.common.setAccountID(accountid)

                    apikey = str(lAPIKey.get())
                    self.common.setAPIKey(apikey)

                    #inputfile = self.inputFile
                    inputfile = str(lInputFile.get())
                    self.common.setInputFile(inputfile)

                    #outputfolder = self.outputDirectory
                    outputfolder = str(lOutputDirectory.get())
                    self.common.setOutputFolder(outputfolder)

                    outputtype = 'xml'

                    self.statusText.set("Starting")

                    print(self.common.getInputFile())

                    if len(apikey) > 0:
                        self.common.setInputRIAS()
                        inputbase = apikey
                        outputfile = str(inputbase) + '.' + outputtype
                        self.common.setOutputFile(outputfile)
                        if len(accountid) > 0:
                           self.common.printStartRIASwithAccount(apikey, accountid, region)
                        else:
                           self.common.printStartRIASwithKey(apikey, region)
                    elif len(self.common.getInputFile()) > 0:
                        basename = path.basename(self.common.getInputFile())
                        inputbase = path.splitext(basename)[0]
                        inputtype = path.splitext(basename)[1][1:]
                        if inputtype == 'yaml' or inputtype == 'yml':
                            self.common.setInputYAML()
                        elif inputtype == 'json':
                            self.common.setInputJSON()
                        elif inputtype == 'tfstate':
                            self.common.setInputTerraform()
                        else:
                           self.common.printInvalidFile(inputfile)
                           sys_exit()
                        outputfile = inputbase + '.' + outputtype
                        self.common.setOutputFile(outputfile)
                        self.common.printStartFile(inputfile, self.common.getCloudType().upper())
                    else:
                        self.common.printInvalidInput()
                        sys_exit()

                    self.data = Load(self.common)
                    if self.data.loadData():
                        self.compose = Compose(self.common, self.data)
                        self.compose.composeDiagrams()
                        self.common.printDone(path.join(outputfolder, outputfile), self.common.getCloudType().upper())
                    else:
                        self.common.printExit()

                    self.statusText.set("Completed")

                    sys_exit()

                except Exception as error:
                    self.statusText.set("Generate failed")
                    messagebox.showinfo("Generate failed", str(error))
                    #traceback.print_exc()
                    #traceback.print_last()

            eGenerate.pack(side=RIGHT)

            #SAVE self.statusText.set("Ready")    
            self.statusText.set("Ready")    
    
            statusLabel = Label(self.top, textvariable=self.statusText)
            statusLabel.pack(side=RIGHT)
    
            #SAVE self.top.mainloop()
            self.top.mainloop()

        elif self.common.isWebMode(args.runmode):
            basename = path.basename(inputfile)
            inputbase = path.splitext(basename)[0]
            inputtype = path.splitext(basename)[1][1:]
            if inputtype == 'yaml' or inputtype == 'yml':
                self.common.setInputYAML()
            elif inputtype == 'json':
                self.common.setInputJSON()
            elif inputtype == 'tfstate':
                self.common.setInputTerraform()
            else:
                self.common.printInvalidFile(args.inputfile)
                return
            outputtype = 'xml'
            outputfile = inputbase + '.' + outputtype
            self.common.setOutputFile(outputfile)

            self.data = Load(self.common)
            if self.data.loadData():
                self.compose = Compose(self.common, self.data)
                self.compose.composeDiagrams()

        #elif self.common.isTerraformMode(args.runmode):
        #    from terraform.common.common import Common
        #    from terraform.generate.generate import Generate

        #    buildcommon = Common()

        #    outputfolder = self.common.getOutputFolder()
        #    buildcommon.setInputType('xlsx')
        #    buildcommon.setInputDirectory(tablesfolder)
        #    basename = path.basename(outputfolder)
        #    buildcommon.setOutputDirectory(path.join(outputfolder, basename + '.resources'))

        #    self.generate = Generate(buildcommon)
        #    self.generate.all()
   
        else:
            self.common.printInvalidMode(args.runmode)

#main()

if __name__ == "__main__":
   main = drawit()
   main.main()
