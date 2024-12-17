import os
import config
import json
import time
class FunctionTrackerFileGenerator:
    
    __functionNameDictionary = {}
    __listOfPOMfiles = []
    def __init__(self):
        #print(config.dirname)
        POM_LISTDIR_PATH = config.dirname+"\AutomationTestLevel/POM"
        FILENAMES_POM = os.listdir(POM_LISTDIR_PATH)
        for file in FILENAMES_POM:
            FuctionList = []
            if file not in ["__init__.py","__pycache__"]:
                with open(POM_LISTDIR_PATH+"/"+file,encoding="utf-8") as extractedData:
                    for data in extractedData.readlines():
                        if "def" in data and "loc_ele_" not in data and "#" not in data and "__init__" not in data:
                            FuctionList.append(data[:data.index('(')].replace("def ",'').strip())
                FunctionTrackerFileGenerator.__functionNameDictionary[file.replace(".py","")]=FuctionList
        with open("MethodDictionary.txt", "w",encoding="utf-8") as writeFuctionRepository:
            writeFuctionRepository.write(json.dumps(FunctionTrackerFileGenerator.__functionNameDictionary))
            time.sleep(3)
        if not config.functionTrue: 
            with open("MethodDictionary.txt","r",encoding="utf-8") as readFunctionRepository:
                readdata=json.loads(readFunctionRepository.read())

