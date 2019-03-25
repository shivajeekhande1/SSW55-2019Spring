from datetime import datetime
from prettytable import PrettyTable 
import natsort
from collections import OrderedDict
import unittest

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

## US05 Marriage before death
def MarriageBeforeDeath():
    Individuals=Individual_dictionary()
    Families=Family_dictionary()
    
    errorlog("US05","Marriage Occurs before death","Indi")
    
    flag=True
    for family in Families:
        if Families[family]["Marriage_date"] > Individuals[Families[family]["Husb_id"]]["Death"]:
            error["US05"]["IndividualIds"].append([Families[family]["Husb_id"],family,"husband's"])
            flag=False

        if Families[family]["Marriage_date"] > Individuals[Families[family]["Wife_id"]]["Death"]:
            error["US05"]["IndividualIds"].append([Families[family]["Wife_id"],family,"wife's"])
            flag=False  
    return flag

#US-15 Fewer than 15 siblings
def Checksiblings(): #Checks if the siblings are fewer than 15
    
    errorlog("US15","More than 15 siblings","Indi")
    

    IndDict=Family_dictionary()
    IndDicti=SortDict(IndDict)

    flag=False

    for key in IndDicti:
        
        if(len(IndDicti[key]["children"])<15):
            flag=True
            
        else:
            error["US15"]["Individuals"].append(key)
            
    return flag


#US 14 check for less than 5 multiple births in family 
def CheckMultipleBirths():
    
    errorlog("US14","Checking for less than 5 multiple births at a time","Indi")
    
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
                error["US14"]["FamilyID"].append(key)
                flag = False
            
    return flag

#US07 Individuals age should not exceed 150 
def max_age(): #Checks if the individuals age are not more than 150
    errorType="US07"
    error["US07"]={}
    error["US07"]["error"] ="Less than 150 years of Age"
    error["US07"]["Individuals"]=[]
    IndDict=Individual_dictionary()
    
    flag=True
    MaxAge=150
    for key in IndDict:
        if(IndDict[key]['Age']>MaxAge):
            error["US07"]["Individuals"].append(key)
            flag=False
    return flag

#US18 Check  if the siblings are married
def checkSiblingsmarried():
    errorType="US18"
    error["US18"]={}
    error["US18"]["error"] ="Siblings are married"
    error["US18"]["FamilyIds"]=[]
    flag=True    
    
    IndDict=Individual_dictionary()
    FamDict=Family_dictionary()
    for key in FamDict:
        if(len(FamDict[key]['children'])>1):
            childrens=list(FamDict[key]['children'])
            for i in FamDict:
                if FamDict[i]["Husb_id"] in childrens and FamDict[i]["Wife_id"] in childrens:
                    error["US18"]["FamilyIds"].append(key)
                    flag= False 
                
                    
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
            for famID in error[type]['FamilyID']:
                print("ERROR: FAMILY: US14:"+str(famID)+ ":has more than 5 multiple births at a time!")
                
        if type=="US15":
            for indID in error[type]['Individuals']:
                print("ERROR: FAMILY: US15"+str(indID)+"has more than 15 children in their family")
                
        if type=="US07":
            for indID in error[type]['Individuals']:
                print("ERROR: FAMILY: US07- This individual "+str(indID)+" has an age that exceeds 150 years ")
        
        if type=="US18":
            for Famid in error[type]['FamilyIds']:
                print("ERRO: FAMILY: US18- This family "+str(Famid)+"is married to their sibling!")
            
        
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


            
def main():
    printTable()
    
    print_error()
    


if __name__== "__main__":
  main() 

