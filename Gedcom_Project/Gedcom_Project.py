from datetime import datetime
from prettytable import PrettyTable 
import natsort
from collections import OrderedDict
import unittest

import CombinedTesting

filepath="GedcomFiles/AcceptanceTestFile.txt"
error = {}
def validity_check():
    tags={'0':['NOTE','HEAD','TRLR'],'1':['SEX','BIRT','DEAT','NAME','FAMC','FAMS','HUSB','WIFE','MARR','CHIL','DIV'],'2':['DATE']}
    f = open(filepath,"r")
    for line in f:
        line = line.replace("\n"," ")
        print("<--"+line)
        list = line.split(" ",2)
        if list[0] == "1":
            if list[1] in tags['1']:
                try:
                    print("-->"+list[0]+"|"+list[1]+"|"+"Y"+"|"+list[2]+" ")
                except IndexError:
                    print("-->"+list[0]+"|"+list[1]+"|"+"Y")
            else:
                try:
                    print("-->"+list[0]+"|"+list[1]+"|"+"N"+"|"+list[2]+" ")
                except IndexError:
                    print("-->"+list[0]+"|"+list[1]+"|"+"N"+" ")
        elif list[0] == "2":
            if list[1] in tags['2']:
                print("-->"+list[0]+"|"+list[1]+"|"+"Y"+"|"+list[2]+" ")
            else:
                print("-->"+list[0]+"|"+list[1]+"|"+"N"+"|"+list[2]+" ")
        elif list[0] == "0":
            if list[1] in tags['0']:
                print("-->"+list[0]+"|"+list[1]+"|"+"Y"+"|"+list[2]+" ")
            else:
                if list[2].replace(" ","") == "INDI" or list[2].replace(" ","") == "FAM":
                    print("-->"+list[0]+"|"+list[2]+"|"+"Y"+"|"+list[1]+" ")
                else:
                    
                    print("-->"+list[0]+"|"+list[2]+"|"+"N"+"|"+list[1]+" ")
        else:
            print("-->"+list[0]+"|"+list[1]+"|"+"N"+"|"+list[2]+" ")


def Individual_dictionary():
    def create_indivudual(id):
        Individual[id]={}
        Individual[id]["Alive"] =True
        Individual[id]["Death"] = 'NA'
        Individual[id]["Child"] = 'NA'
        Individual[id]["Spouse"] = 'NA'

    def addName(id, name):
        Individual[id]["Name"] = name

    def addGender(id, gender):
        Individual[id]["Gender"] = gender

    def addBirthday(id,birthdate):
        if Individual[id]["Death"]=='NA':
                Individual[id]["Birthdate"] = birthdate
                birthday = datetime.strptime(birthdate, '%Y-%m-%d')
                end_date = datetime.today()
                age = end_date.year - birthday.year - ((end_date.month, end_date.day) < (birthday.month, birthday.day))
                Individual[id]["Age"] = age

    def addDeath(id,deathday):

        if Individual[id]["Birthdate"]:
            Individual[id]["Alive"]= False
            Individual[id]["Death"] = deathday
            end_date = datetime.strptime(deathday, '%Y-%m-%d')
            birthday = datetime.strptime(Individual[id]["Birthdate"], '%Y-%m-%d')
            age = end_date.year - birthday.year - ((end_date.month, end_date.day) < (birthday.month, birthday.day))
            Individual[id]["Age"] = age

    def addChild(id,cid):
        if Individual[id]['Child']=='NA':
            Individual[id]['Child']=[]
            Individual[id]['Child'].append(cid)
        else:
            Individual[id]['Child'].append(cid)

    def addSpouse(id,sid):
        if Individual[id]['Spouse']=='NA':
            Individual[id]['Spouse']=[]
            Individual[id]['Spouse'].append(sid)
        else:
            Individual[id]['Spouse'].append(sid)
    Individual={}
    f = open(filepath,"r")
    for line in f:
        try:
            line_words = line.split()
  
            if line_words[0]=='1' and line_words[1]=='NAME' and len(line_words)>2:
	            #print_function('Y',1,line_words)
                addName( currentIndi,' '.join(line_words[2:len(line_words)]) )
            elif line_words[0]=='1' and line_words[1]=='BIRT' and len(line_words)==2:
                current_alive=True
  
            elif line_words[0]=='1' and line_words[1]=='DEAT' and len(line_words)==2:
                current_death=False
  
            elif line_words[0]=='2' and line_words[1]=='DATE' and len(line_words)>2:
                date=datetime.strptime(' '.join(line_words[2:len(line_words)]), '%d %b %Y').strftime('%Y-%m-%d')
                if current_alive==True:
                    addBirthday( currentIndi, date )
                    current_alive=False
                if current_death==False:
                    addDeath( currentIndi, date )
                    current_death=True
            elif line_words[0]=='1' and line_words[1]=='SEX' and len(line_words)==3:
                addGender(currentIndi, line_words[2])
 
            elif line_words[0]=='1' and line_words[1]=='FAMC' and len(line_words)==3:
                addChild(currentIndi,line_words[2])

            elif line_words[0]=='1' and line_words[1]=='FAMS' and len(line_words)==3:
                addSpouse(currentIndi,line_words[2])

            elif line_words[0]=="0" and len(line_words)>=3:
                if line_words[2]=='INDI' :
		        #print_function('Y',-1,line_words)
                    currentIndi = line_words[1]
                    current_alive=False
                    current_death=True
                    create_indivudual(line_words[1])
            else:
	        #print_function('N',line_words[0],line_words) 
                pass  
        except:
            pass
    f.close()

    return Individual

def Family_dictionary():
    Indi = Individual_dictionary()
    f = open(filepath,"r")
    dict = {}
    status = False
    date = ""
    for line in f:
        list = line.split()
        if len(list)>=3:
                list[2]=' '.join(list[2:len(list)] )
        if len(list)==2:
                list[1]=list[1].replace(" ","")
        try:
            
            if list[0] == "0" and list[2] == "FAM":
                curr_id = list[1]
                dict[curr_id] = {}
                dict[curr_id]["children"] = []
                dict[curr_id]["Marriage_date"]='NA'
                dict[curr_id]["Divorce_date"]='NA'
                dict[curr_id]["Wife_Name"]='NA'
                dict[curr_id]["Husb_Name"]='NA'
                status = True
            elif list[0] == "0" and list[2] != "FAM":
                status = False
            if status:
              
                if list[1] == "HUSB":
                    dict[curr_id]["Husb_id"] = list[2]
                    dict[curr_id]["Husb_Name"] = Indi[list[2]]["Name"]
                elif list[1] == "WIFE":

                    dict[curr_id]["Wife_id"] = list[2]
                    dict[curr_id]["Wife_Name"] = Indi[list[2]]["Name"]
                elif list[1] == "MARR":
                    date = "Marr"   
                elif list[1] == "DIV":
                    date = "Div"
                elif list[1] == "CHIL":
                    dict[curr_id]["children"].append(list[2])
                if list[1] == "DATE":
                    if date == "Marr":
                        list[2]=datetime.strptime(list[2], '%d %b %Y').strftime('%Y-%m-%d')
                        dict[curr_id]["Marriage_date"] = list[2]
                        date = ""
                    elif date == "Div":
                        list[2]=datetime.strptime(list[2], '%d %b %Y').strftime('%Y-%m-%d')
                        dict[curr_id]["Divorce_date"] = list[2]
                        date = ""
        except:
            pass
    f.close()
    return dict

def SortDict(d):
    keys = natsort.natsorted(d.keys())    
    d_new = OrderedDict((k, d[k]) for k in keys)    
    return d_new

def printTable():
  
    IndDict1=Individual_dictionary()
    FamDict1=Family_dictionary()

    IndDict = SortDict(IndDict1)
    FamDict = SortDict(FamDict1)

    x = PrettyTable()

    x.field_names = ["Id","Name","Gender","Birthday","Age","Alive","Death","Child","Spouce"]

    print("Individuals")
    for key in IndDict:
        x.add_row([key,IndDict[key]["Name"],IndDict[key]["Gender"],IndDict[key]["Birthdate"],IndDict[key]["Age"],IndDict[key]["Alive"],IndDict[key]["Death"],IndDict[key]["Child"],IndDict[key]["Spouse"]])
        #print(key,IndDict[key])

    print(x)

    y = PrettyTable()
    y.field_names = ["Id","Married","Divorce","Husband Id","Husband Name","Wife Id","Wife Name","Children"]
    print("Families")
    for key in FamDict:
        y.add_row([key,FamDict[key]["Marriage_date"],FamDict[key]["Divorce_date"],FamDict[key]['Husb_id'],FamDict[key]["Husb_Name"],FamDict[key]["Wife_id"],FamDict[key]["Wife_Name"],FamDict[key]["children"]])
        #print(key,FamDict[key])
    print(y)

def errorlog(key, error_desc, id_type):
    error[key]={}
    error[key]["error"] = error_desc
    if id_type == "Fam":
        error[key]["Family id"] = []
    else:
        error[key]["IndividualIds"] = []

#user story US04
def CheckMarriageBeforeDivorce():
    FamDict1 = Family_dictionary()
    list = []
    flag = True
    errorlog("US04","Divorse Occurs before Marriage","Fam")
    
    for Famid in FamDict1:
        if FamDict1[Famid]["Divorce_date"] != "NA":
            if FamDict1[Famid]["Divorce_date"] < FamDict1[Famid]["Marriage_date"]:
                list.append(Famid)
                flag = False
            else:
                pass
        else:
            pass
    if flag == False:
        error["US04"]["Family id"]=list
    return flag

#user story US06
def CheckDivorceBeforeDeath():
    IndDict1=Individual_dictionary()
    FamDict1=Family_dictionary()
    flag = True
    list = []
    errorlog("US06","Death Occurs before divorse","Fam")
    
    for Famid in FamDict1:
        husbdate = IndDict1[FamDict1[Famid]["Husb_id"]]["Death"]
        Wifedate = IndDict1[FamDict1[Famid]["Wife_id"]]["Death"]
        if FamDict1[Famid]["Divorce_date"] != "NA":
            if husbdate != "NA" and husbdate < FamDict1[Famid]["Divorce_date"]:
                list.append(Famid)
                flag = False
            elif Wifedate != "NA" and Wifedate < FamDict1[Famid]["Divorce_date"] and flag != False:
                list.append(Famid)
                flag = False
            else:
                pass
    else:
        pass
    if flag == False:
        error["US06"]["Family id"]=list
    return flag

## US03 Birth Before Death
def BirthBeforeDeath():
    Individuals=Individual_dictionary()
    
    errorlog("US03","Birth Occurs before death","Indi")
    
    flag=True
    for individual in Individuals:
        if Individuals[individual]["Death"]< Individuals[individual]["Birthdate"] and Individuals[individual]["Alive"]==False:
            error["US03"]["IndividualIds"].append(individual)
            flag=False
    return flag


def RefactorUS05(Families,Individuals,family,id,getId):
    
    if Families[family]["Marriage_date"] > Individuals[Families[family][id]]["Death"]:
            error["US05"]["IndividualIds"].append([Families[family][id],family,getId[id]])
    
## US05 Marriage before death
def MarriageBeforeDeath():
    Individuals=Individual_dictionary()
    Families=Family_dictionary()
    
    errorlog("US05","Marriage Occurs before death","Indi")
    getId={"Husb_id":"husband's","Wife_id":"wife's"}
    
    flag=True
    for family in Families:
        RefactorUS05(Families,Individuals,family,"Husb_id",getId)
        RefactorUS05(Families,Individuals,family,"Wife_id",getId)  
    return False if len(error["US05"]["IndividualIds"])>0 else True

#US-15 Fewer than 15 siblings
def Checksiblings(): #Checks if the siblings are fewer than 15
    
    errorlog("US15","More than 15 siblings","Fam")
    

    IndDict=Family_dictionary()
    IndDicti=SortDict(IndDict)

    flag=False

    for key in IndDicti:
        
        if(len(IndDicti[key]["children"])<15):
            flag=True
            
        else:
            error["US15"]["Family id"].append(key)
            
    return flag


#US 14 check for less than 5 multiple births in family 
def CheckMultipleBirths():
    
    errorlog("US14","Checking for less than 5 multiple births at a time","Fam")
    
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    flag= True
    
    for key in FamDict:
        if len(FamDict[key]["children"])>=5:
            newlist=list()
            for child in FamDict[key]['children']:
                newlist.append(IndDict[child]["Birthdate"])
            count_dict = dict((i, newlist.count(i)) for i in newlist)
            list_birthdays = count_dict.values()
            if max(list_birthdays) >=5:
                error["US14"]["Family id"].append(key)
                flag = False
            
    return flag

#US07 Individuals age should not exceed 150 
def max_age(): #Checks if the individuals age are not more than 150
    errorlog("US07","Less than 150 years of Age","Indi")
    
    IndDict=Individual_dictionary()
    
    flag=True
    MaxAge=150
    for key in IndDict:
        if(IndDict[key]['Age']>MaxAge):
            error["US07"]["IndividualIds"].append(key)
            flag=False
    return flag

#US18 Check  if the siblings are married
def checkSiblingsmarried():
    errorlog("US18","Siblings are married","Fam")
    
    flag=True    
    
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    for key in FamDict:
        if(len(FamDict[key]['children'])>1):
            childrens=list(FamDict[key]['children'])
            for i in FamDict:
                if FamDict[i]["Husb_id"] in childrens and FamDict[i]["Wife_id"] in childrens:
                    error["US18"]["Family id"].append(key)
                    flag= False 
                
                    
    return flag



     
        
#US 17 No Marriages to children
def NoMarriageChildren():
    error["US17"]= {}
    error["US17"]["error"]="No Marriages to children"
    error["US17"]["Family"]={}
    
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    flag= True
    
    for famID in FamDict:
        childList=FamDict[famID]["children"]
        for childID in childList:
            for key in FamDict:
               if FamDict[key]["Wife_id"]==FamDict[famID]["Wife_id"] and FamDict[key]["Husb_id"]==childID:
                   error["US17"]["Family"][childID]=" in family "+str(key)+" is a husband and is decendant of Spouse "+str(FamDict[famID]["Wife_id"])
                   flag=False
               if FamDict[key]["Husb_id"]==FamDict[famID]["Husb_id"] and FamDict[key]["Wife_id"]==childID:
                   error["US17"]["Family"][childID]=" in family "+str(key)+" is a wife and is decendant of Spouse "+str(FamDict[famID]["Husb_id"])
                   flag=False
    return flag

        




#us08
def BirthBeforeMarriageOfParents():
    errorlog("US08","Checking for births before marriage of parents","Fam")
    flag = True
    fam = Family_dictionary()
    indi = Individual_dictionary()
    for key in fam:
        child = fam[key]["children"]
        for i in child:
            if indi[i]["Birthdate"] < fam[key]["Marriage_date"]:
                flag = False
                error["US08"]["Family id"].append(key)
            else:
                pass 
    return flag

#US16
def AllMaleNames():
    errorlog("US16","Checking if all the males in the family has same last name","Fam")
    flag = True
    fam = Family_dictionary()
    indi = Individual_dictionary()
    for key in fam:
        char = '/'
        name = fam[key]["Husb_Name"]
        last_name = name[name.find(char)+1 :]
        child = fam[key]["children"]
        for i in child:
            if indi[i]["Gender"] == 'M':
                name2 = indi[i]["Name"]
                last_name2 = name2[name2.find(char)+1 :]
                if last_name2 != last_name:
                    error["US16"]["Family id"].append(key)
                    flag = False
                    break
    return flag

#US 19 First cousins should not marry one another
def getchildList(childID,FamDict):
    for famID in FamDict:
        if childID==FamDict[famID]["Husb_id"] or childID==FamDict[famID]["Wife_id"]:
            return FamDict[famID]["children"]
    return []

def SpousesList(grandchildID,FamDict):
    tempList=list([])
    for famID in FamDict:
        if grandchildID==FamDict[famID]["Husb_id"]:
            tempList.append([FamDict[famID]["Wife_id"],famID])
        if grandchildID==FamDict[famID]["Wife_id"]:
            tempList.append([FamDict[famID]["Husb_id"],famID])

    return tempList

def findUS19Error(grandChildrenSpouses,childList,grandchildID,temp_list,childID,FamDict,famID):
    for grandchildspouse in grandChildrenSpouses:
        for otherParent in childList:
            if otherParent!=childID:
                otherParentChildren=getchildList(otherParent,FamDict)
                if grandchildspouse[0] in otherParentChildren and grandchildspouse[0] not in temp_list:
                    error["US19"]["Family"].append("The Family "+str(grandchildspouse[1])+" have marriage between first cousins: " + str(grandchildspouse[0]) + "," + str(grandchildID)+" Since their corresponding parents "+"["+str(otherParent)+","+str(childID)+"]"+" are from same family")
                    temp_list.append(grandchildspouse[0])
                    temp_list.append(grandchildID)
    return temp_list 

def FirstCousinsNoMarriageChildren():
    
    error["US19"]= {}
    error["US19"]["error"]="First cousins should not marry one another"
    error["US19"]["Family"]=[]
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    temp_list=[]
    for famID in FamDict:
        childList=FamDict[famID]["children"]
        for childID in childList:
            grandChildren=getchildList(childID,FamDict)
            if len(grandChildren)!=0:
                for grandchildID in grandChildren:
                    grandChildrenSpouses=SpousesList(grandchildID,FamDict)
                    if len(grandChildrenSpouses)!=0 and grandchildID not in temp_list:
                        temp_list=findUS19Error(grandChildrenSpouses,childList,grandchildID,temp_list,childID,FamDict,famID) 
    return True if len(error["US19"]["Family"])==0 else False

#US25
def UniqueFirstNamesInFamily():
    errorlog("US25","Checking if all the first names are unique in a family","Fam")
    status = True
    famDict = Family_dictionary()
    indDict = Individual_dictionary()
    for i in famDict:
        name = famDict[i]["Husb_Name"].split("/")[0]
        if famDict[i]["Wife_Name"].split("/")[0] == name:
            status = False
            error["US25"]["Family id"].append(i)
        else:
            for j in famDict[i]["children"]:
                if indDict[j]["Name"].split("/")[0] == name:
                    status = False
                    error["US25"]["Family id"].append(i)
    return status

#US23
def UniqueNamesAndDob():
    errorlog("US23","Checking if all individuals have unique names and Dob","Indi")
    dict = {}
    status = True
    indiDict = Individual_dictionary()
    for i in indiDict:
        if indiDict[i]["Name"] in dict:
            for j in dict[indiDict[i]["Name"]]:
                if indiDict[i]["Birthdate"] == indiDict[j]["Birthdate"]:
                    list = [i,j]
                    error["US23"]["IndividualIds"].append(list)
                    status = False
            dict[indiDict[i]["Name"]].append(i)    
                    
        else:
            dict[indiDict[i]["Name"]] = []
            dict[indiDict[i]["Name"]].append(i)
    return status

#US24 Unique families by spouses
def UniqueFamiliesSpouses():
    errorlog("US24","Unique Families By Spouses","Fam")
    flag = True
    family = Family_dictionary()
    dummyId=[]
    for idOne in family:
        for idTwo in family:
            if idOne not in dummyId and idOne!=idTwo and family[idOne]["Husb_Name"]==family[idTwo]["Husb_Name"] and family[idOne]["Wife_Name"]==family[idTwo]["Wife_Name"] and family[idOne]["Marriage_date"]==family[idTwo]["Marriage_date"] :
                flag= False
                dummyId.append(idTwo)
                error["US24"]["Family id"].append([idOne,idTwo])

    return flag

#US38 List upcoming birthdays
def ListUpcomingBirthdays():
    errorlog("US38","List upcoming birthdays","Indi")
    individual=Individual_dictionary()
    PresentDate = datetime.today()  
    for indId in individual:
        birthday = datetime.strptime(individual[indId]["Birthdate"], '%Y-%m-%d')
        if (birthday-PresentDate).days <=30 and birthday>PresentDate:
            error["US38"]["IndividualIds"].append(indId)
    return False if len(error["US38"]["IndividualIds"])==0 else True




#US21 check gender role of spouses in familes
def checkrole():
    error["US21"]={}
    error["US21"]["error"] ="Check gender for role"
    error["US21"]["Family"]=[]
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    
    flag=True
    for key in IndDict:
        if(IndDict[key]['Spouse']!='NA'):
            curr=key
            if(IndDict[key]['Gender']=='F'):
                for i in FamDict:
                    if(curr in FamDict[i]['Husb_id']):
                        error["US21"]["Family"].append([i,key])
                        flag=False
            if(IndDict[key]['Gender']=='M'):
                for i in FamDict:
                    if(curr in FamDict[i]['Wife_id']):
                        error["US21"]["Family"].append([i,key])
                        flag=False
    return flag



#US22 All individual ids and Family ids should be unique

def uniqueIDs():
    error["US22"]={}
    error["US22"]["error"] ="check for unique Ids"
    error["US22"]["Individuals"]=[]
    error["US22"]["Familyids"]=[]
    flag=True
    
    f=open(filepath,"r")
    dummy_Indi=[]
    dumy_Fami=[]
    for line in f:
        try:
            line_words = line.split()
            if line_words[0]=="0" and len(line_words)>=3 and line_words[2]=='INDI':
                if line_words[1] not in dummy_Indi:
                    dummy_Indi.append(line_words[1])
                else:
                    if line_words[1] not in error["US22"]["Individuals"]:
                        error["US22"]["Individuals"].append(line_words[1])
                        flag=False
            if line_words[0]=="0" and len(line_words)>=3 and line_words[2]=='FAM':
                if line_words[1] not in dumy_Fami:
                    dumy_Fami.append(line_words[1])
                else:
                    if line_words[1] not in error["US22"]["Familyids"]:
                        error["US22"]["Familyids"].append(line_words[1]) 
                        flag=False
        except:
            pass
    f.close()
    return flag

#us29
def ListDeceased():
    errorlog("US29","List all Deaceased","Indi")
    list = []
    indi = Individual_dictionary()
    for i in indi:
        if indi[i]["Death"] != "NA":
            list.append(i)
    error["US29"]["IndividualIds"] = list
    
    if len(list)>0:
        return True
    else:
        return False
#US 26 Corresponding entries

def CorrespondingEntries():
    error["US26"]={}
    error["US26"]["error"] ="Corresponding entries"
    error["US26"]["child"]=[]
    error["US26"]["spouse"]=[]
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()

    for key in IndDict:

        if(IndDict[key]['Child']!='NA'):
            if key not in FamDict[IndDict[key]['Child'][0]]['children']:
                error["US26"]["child"].append("Individual: "+key+" child entry is missing in "+IndDict[key]['Child'][0]+" family" )
        if(IndDict[key]['Spouse']!='NA'):
            for sFid in IndDict[key]['Spouse']:
                if IndDict[key]['Gender']=='M' and key==FamDict[sFid]['Wife_id']:
                   error["US26"]["spouse"].append("Individual: "+key+" is misgendered as Female in "+sFid+" family" )

                if key==FamDict[sFid]['Husb_id'] and IndDict[key]['Gender']=='F':
                   error["US26"]["spouse"].append("Individual: "+key+" is misgendered as male in "+sFid+" family" )
    
                if key!=FamDict[sFid]['Husb_id'] and key!=FamDict[sFid]['Wife_id']:
                    error["US26"]["spouse"].append("Individual: "+key+" spouse details are missing in "+sFid+" family" )
    for fId in FamDict:

        if fId not in IndDict[FamDict[fId]['Wife_id']]['Spouse']:
            error["US26"]["spouse"].append("Family: "+fId+" with spouse "+FamDict[fId]['Wife_id']+ " is missing in Individual records" )
        if fId not in IndDict[FamDict[fId]['Husb_id']]['Spouse']:
            error["US26"]["spouse"].append("Family: "+fId+" with spouse "+FamDict[fId]['Husb_id']+ " is missing in Individual records" )
        for childId in FamDict[fId]['children']:
            if fId not in IndDict[childId]["Child"]:
                error["US26"]["child"].append("Family: "+fId+" is missing child entry "+childId+ "'s individual record" )
    return True if len(error["US26"]["child"])==0 and len(error["US26"]["spouse"])==0 else False 


#us30
def ListLivingMarried():
    errorlog("US30","List living and married","Indi")
    list = []
    indi = Individual_dictionary()
    fam = Family_dictionary()
    for key in indi:
        if indi[key]["Death"] == "NA" and indi[key]["Spouse"]!="NA":
            for i in indi[key]["Spouse"]:
                if i in fam:
                    if indi[key]["Gender"]=="M":
                        if fam[i]["Divorce_date"] =="NA" and indi[fam[i]["Wife_id"]]["Death"] =="NA":
                            
                            list.append(key)
                    else:
                        if fam[i]["Divorce_date"] =="NA" and indi[fam[i]["Husb_id"]]["Death"] =="NA":
                            list.append(key)
    error["US30"]["IndividualIds"] = list
    
    if len(list)>0:
        return True
    else:
        return False

def LivingSingle():
    error["US31"]={}
    error["US31"]["error"] ="check for unique Ids"
    error["US31"]["Individuals"]=[]
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()

    tempDict=[]
    flag=False
    for fId in FamDict:

        if FamDict[fId]['Husb_id'] not in tempDict:
            tempDict.append(FamDict[fId]['Husb_id'])
        if FamDict[fId]['Wife_id'] not in tempDict:
            tempDict.append(FamDict[fId]['Wife_id'])
    for indId in IndDict:
        if indId not in tempDict and IndDict[indId]['Age']>30 and IndDict[indId]['Death']=='NA':
            error["US31"]["Individuals"].append(indId)
            flag=True
    return flag
def print_error():
    CheckMarriageBeforeDivorce()
    CheckDivorceBeforeDeath()
    BirthBeforeDeath()
    MarriageBeforeDeath()
    Checksiblings()
    CheckMultipleBirths()
    max_age()
    checkSiblingsmarried()
    
    
    BirthBeforeMarriageOfParents()
    AllMaleNames()
    NoMarriageChildren()
    FirstCousinsNoMarriageChildren()
    UniqueFamiliesSpouses()
    ListUpcomingBirthdays()
    uniqueIDs()
    checkrole()
    UniqueFirstNamesInFamily()
    UniqueNamesAndDob()

    ListDeceased()
    ListLivingMarried()

    CorrespondingEntries()
    LivingSingle()
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    for type in error:
        if type=="US04":

            for famID in error[type]['Family id']:
                print("ERROR: FAMILY: US04: "+str(famID)+":"+" Divorced "+str(FamDict[famID]["Divorce_date"])+" before marriage "+str(FamDict[famID]["Marriage_date"]))
        if type=="US06":
            for famID in error[type]['Family id']:
                if IndDict[FamDict[famID]['Husb_id']]['Death']!='NA' and IndDict[FamDict[famID]['Husb_id']]['Death']<FamDict[famID]["Divorce_date"]:
                    print("ERROR: FAMILY: US06: "+str(famID)+":"+" Divorced "+str(FamDict[famID]["Divorce_date"])+" after husband's "+str('(')+str(FamDict[famID]['Husb_id'])+str(')')+" death on "+str(IndDict[FamDict[famID]['Husb_id']]['Death']))
                if IndDict[FamDict[famID]['Wife_id']]['Death']!='NA' and IndDict[FamDict[famID]['Wife_id']]['Death']<FamDict[famID]["Divorce_date"]:
                    print("ERROR: FAMILY: US06: "+str(famID)+":"+" Divorced "+str(FamDict[famID]["Divorce_date"])+" after wife's "+str('(')+str(FamDict[famID]['Wife_id'])+str(')')+" death on "+str(IndDict[FamDict[famID]['Wife_id']]['Death']))

        if type=="US03":
            
          for indID in error[type]["IndividualIds"]:
                print("ERROR: INDIVIDUAL: US03: "+str(indID)+" : Died "+str(IndDict[indID]["Death"])+" before born "+str(IndDict[indID]["Birthdate"]))
       
        if type=="US05":     
            for indID in error[type]["IndividualIds"]:
                print("ERROR: FAMILY: US05: "+str(indID[1])+": Married "+str(FamDict[indID[1]]["Marriage_date"])+" after "+str(indID[2])+" ("+str(indID[0])+")"+" death on "+str(IndDict[indID[0]]["Death"]))

        if type=="US14":
            for famID in error[type]['Family id']:
                print("ERROR: FAMILY: US14:"+str(famID)+ " :has more than 5 multiple births at a time!")
                
        if type=="US15":
            for indID in error[type]['Family id']:
                print("ERROR: FAMILY: US15: "+str(indID)+" has more than 15 children in their family")
                
        if type=="US07":
            for indID in error[type]['IndividualIds']:
                print("ERROR: Individual: US07: This individual "+str(indID)+" has an age that exceeds 150 years ")
        
        if type=="US18":
            for Famid in error[type]['Family id']:
                print("ERROR: FAMILY: US18: This family "+str(Famid)+" is married to their sibling!")
            
        
        if type == "US16":
            for i in error[type]["Family id"]:
                print("ERROR: Family: US16: "+str(i)+" Does not have all the Male member in the family with same last name")

        if type == "US08":
            list = error[type]["Family id"]
            for i in list:
                list1 = []
                fam = FamDict[i]
                for j in fam["children"]:
                    if IndDict[j]["Birthdate"]<fam["Marriage_date"]:
                        list1.append(j)
                if len(list1)>0:
                    print("ERROR: Family: US08: Childrens with id's "+str(list1)+" In family "+i+" have birth before marriage of parents")

        if type=="US17":
            list=error[type]["Family"]
            for chID in list:
                print("ERROR: Family: US17: Children with id "+str(chID)+list[chID])
            

        if type=="US19":
            for us19 in error[type]["Family"]:
                print("ERROR: Family: US19: "+us19)

        if type=="US21":
            for us21 in error[type]["Family"]:
                print("ERROR: FAMILY: US21: This person "+us21[1]+" is not assigned with the correct role in the Family "+us21[0])
        
        if type=="US22":
            if len(error["US22"]["Individuals"])!=0:
                for us22I in error["US22"]["Individuals"]:
                    print("ERROR: Individual: US22: "+us22I+" have duplicate ids")
            if error["US22"]["Familyids"]!=0:
                for us22F in  error["US22"]["Familyids"]:
                    print("ERROR: FAMILY: US22: "+us22F+" have duplicate ids")
        
        if type == "US23":
            for i in error["US23"]["IndividualIds"]:
                print("ERROR: Individuals: US23: Individuals with Id's "+i[0]+" and "+i[1]+" have same Names and Date of Births")
        
        if type == "US25":
            for i in error["US25"]["Family id"]:
                print("ERROR: Family: US25: In Family with ID "+i+" :Not all the first names are unique")
        if type=="US24":
            for i in error["US24"]["Family id"]:
                print("ERROR: Family: US24: "+" The Family "+i[0]+" have identical spouses & have same marrigae date with Family "+i[1])
        if type=="US38":
            for i in error["US38"]["IndividualIds"]:
                print("UPDATE: Individual: US38: "+"The individual "+i+" has upcoming birthday in the next 30 days.")
        if type == "US29":
            for i in error["US29"]["IndividualIds"]:
                print("UPDATE: Individual: US29: The Individual with Id "+i+" is Deaceased")
        if type == "US30":
            for i in error["US30"]["IndividualIds"]:
                print("UPDATE: Individual: US30: The Individual with ID "+i+" is living and married")
        if type=="US26":
            for i in error["US26"]["child"]:
                print("ERROR: US38: "+i)
            for i in error["US26"]["spouse"]:
                print("ERROR: US38: "+i)
        if type=="US31":
            for i in error["US31"]["Individuals"]:
                print("UPDATE: Individual: US31: "+"The individual "+i+" is a living single with age more than 30")
     

def main():
    printTable()
    
    print_error()
    


if __name__== "__main__":
  main() 

  
