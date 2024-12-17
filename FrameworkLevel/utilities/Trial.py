# import copy
#
# testFlowSuite = {}
#
# def generateTestFlow(tempTestFlow,key,value):
#     testFlow = []
#     iterration_dict = {}
#     for testFlowValues in tempTestFlow.values():
#         if testFlowValues[key]=='':
#             continue
#         testFlow.append(testFlowValues[key])
#         iterration_dict[testFlowValues[key]] = iterration_dict.get(testFlowValues[key],0)+1
#     maxIterartion = max(iterration_dict.values())
#     print(testFlow)
#     print(iterration_dict)
#     print(maxIterartion)
#     iterDictTestFlow = {valuekey:None for valuekey in range(1,maxIterartion+1)}
#     for appendvalue in testFlow:
#         for keyi in iterDictTestFlow:
#             if iterDictTestFlow[keyi] == None:
#                 iterDictTestFlow[keyi]=[appendvalue]
#             elif appendvalue not in iterDictTestFlow[keyi]:
#                 iterDictTestFlow[keyi].append(appendvalue)
#             elif appendvalue in iterDictTestFlow[keyi]:
#                 continue
#             break
#     #print(iterDictTestFlow)
#     testFlowSuite[value]={"testFlow":testFlow,"iterDictTestFlow":iterDictTestFlow}
#
#
#
#
# def extractTestFlow(test_case_ids):
#     testFlow = {'ID': {0: 'VOD_1', 1: 'VOD_2', 2: 'VOD_3', 3: 'VOD_4', 4: 'VOD_5', 5: 'VOD_6', 6: 'VOD_7'},
#                 'TestFlow_1': {0: 'openApp', 1: 'openApp', 2: 'openApp', 3: 'openApp', 4: 'openApp', 5: 'openApp', 6: 'openApp'},
#                 'TestFlow_2': {0: 'ValidateSearchBar', 1: 'ValidateSearchBar', 2: 'ValidateSearchBar', 3: 'ValidateSearchBar', 4: 'ValidateSearchBar', 5: 'ValidateSearchBar', 6: 'ValidateSearchBar'},
#                 'TestFlow_3': {0: 'openApp', 1: 'NavigaToTemplate', 2: 'ValidateUserLogin', 3: 'ValidateLoginPage', 4: 'ValidateSearchBar', 5: 'ValidateLoginPage', 6: 'ValidateLoginPage'},
#                 'TestFlow_4': {0: 'ValidateSearchBar', 1: '', 2: 'NavigaToTemplate', 3: 'ValidateSearchBar', 4: 'NavigaToTemplate', 5: 'ValidateLoginPage', 6: 'ValidateLoginPage'},
#                 'TestFlow_5': {0: '', 1: '', 2: 'ValidateUserLogin', 3: 'Logout', 4: 'Logout', 5: '', 6: ''}}
#
#     tempTestFlow = copy.copy(testFlow)
#     idColumn = testFlow['ID']
#     tempTestFlow.pop('ID')
#     for tc_id in test_case_ids:
#         if tc_id in idColumn.values():
#             for key,value in idColumn.items():
#                 if value==tc_id:
#                     generateTestFlow(tempTestFlow,key, value)
#
#
# def extractData(test_case_ids):
#     extractTestFlow(test_case_ids)
#     pass
#
# test_case_ids = ['VOD_1', 'VOD_2', 'VOD_3', 'VOD_6']
# extractData(test_case_ids)
# print(testFlowSuite)



# import requests
#
# r = requests.post('http://laptop-k9f4b4l9/VenioOndemandAPI/vod/services/login/AuthenticateCredential', headers={"Bearer":"Bearer 5CW6APAE69YrKKxf4bB3aZhgkxU3LqMFi_tPkjAZoXS_WIW022EidgVIt3OHeUwa01Iml5xUsJDPqRoPvs0RiZETq9QsXvzu6q_loPapCe9rUMjTy1aQXwaPVKfb6Tp_U7G2nTm-WOLEfAjSU0EBIM8wYK9mVhgUh2cf4fIUwlHlSxayXc3KcDhP6mqHOr04-3sGGdeZUNlAi5fww9Zqa6tYjGaYkgpHV00Ra0q2r3s8KJ2cm1O5Z66Mj8NCsX1wk7m18JLMQBYA6HgFGWS_oA4h-MgbdCncxvxF8Qaz_WLndKjKp6h4DU1Z6Fu7c4vwJAz1zy94WgtOB5TLGK8LRuptEIoP5oNdbqNzQYvw7GXFS9n2ngjmkntwIcT2c6Cyd67Wb9WDpySYjaXKbXfC2dnFmHWCjUS004V0gF9gjqg"})
#
# print(r.status_code)
# print(r.headers)
# print(r.cookies)
# print(r.content)

# testDataSuite={}
#
# def generateTestData(dictID,tempTestData,test_case_ids):
#     #print(dictID,"\n",tempTestData,"\n",test_case_ids)
#     for tcidkey in test_case_ids:
#         itr_dict_creator = {key:None for key in range(0,len(dictID[tcidkey]))}
#         #print(itr_dict_creator,tcidkey)
#         for datakey,datavalues in tempTestData.items():
#             counter=0
#             for datakeytcidkey in dictID[tcidkey]:
#                 #print(datakeytcidkey,datavalues[datakeytcidkey])
#                 if datavalues[datakeytcidkey]=="":
#                     continue
#                 if itr_dict_creator.get(counter)==None:
#                     itr_dict_creator[counter]={datakey:datavalues[datakeytcidkey]}
#                 else:
#                     itr_dict_creator[counter].update({datakey:datavalues[datakeytcidkey]})
#                 counter+=1
#                 #print(itr_dict_creator)
#         #print(itr_dict_creator)
#         NewDiCT = {}
#         for itrcorrectorkeys,itrcorrectorvalues in itr_dict_creator.items():
#             NewDiCT[itrcorrectorkeys+1]=itrcorrectorvalues
#         testDataSuite[tcidkey]={'iterDictTestData':NewDiCT }
#
#
#
#     print(testDataSuite)    
#
#
#
#
#
# def extractTestData():
#     test_case_ids =['VOD_1','VOD_2','VOD_3','VOD_4']
#     #test_case_ids =['VOD_1']
#
#     tempTestData ={'iteration': {0: 1, 1: 2, 2: 1, 3: 1, 4: 1, 5: 2, 6: 1, 7: 2, 8: 1, 9: 1}, 'URL': {0: 'venioID_1', 1: 'venioID_2', 2: 'venioID_1', 3: 'venioID_1', 4: 'venioID_1', 5: 'venioID_2', 6: 'venioID_1', 7: 'venioID_2', 8: 'venioID_1', 9: 'venioID_1'}, 'SearchData': {0: 'Template_1', 1: 'Template_2', 2: 'Template_1', 3: 'Template_1', 4: 'Template_1', 5: 'Template_2', 6: 'Template_1', 7: 'Template_2', 8: 'Template_1', 9: 'Template_1'}, 'TemplateData': {0: '', 1: '', 2: 'MyDataTemplate', 3: 'MyDataTemplate', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, 'LoginData': {0: '', 1: '', 2: '', 3: 'Super', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}}
#
#     idColumnTestData = {0: 'VOD_1', 1: 'VOD_1', 2: 'VOD_2', 3: 'VOD_3', 4: 'VOD_4', 5: 'VOD_4', 6: 'VOD_5', 7: 'VOD_5', 8: 'VOD_6', 9: 'VOD_7'}
#     tempTestData.pop('iteration')
#     dictID = {}
#     for idtc in test_case_ids:
#         for idkey in idColumnTestData:
#             if idColumnTestData[idkey]==idtc:
#                 if dictID.get(idtc)==None:
#                     dictID[idtc]=[idkey]
#                 else:
#                     dictID.setdefault(idtc, []).append(idkey)
#     generateTestData(dictID, tempTestData,test_case_ids)
#
#
#
# extractTestData()
#
# import ctypes
#
# resolution = ctypes.windll.user32
# screensize = resolution.GetSystemMetrics(0),resolution.GetSystemMetrics(1)

# import logging
#
# #Create and configure logger
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
#
# #Creating an object
# logger=logging.getLogger()
#
# #Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)
#
# #Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")
#
# import datetime
# print(datetime.date())



    
    


















































                



                
                

        