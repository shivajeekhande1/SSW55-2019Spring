from datetime import datetime
from prettytable import PrettyTable 
import natsort
from collections import OrderedDict

filepath= "C:/Users/princ/OneDrive/Documents/stevens/test.txt"

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

def CheckMarriageBeforeDivorce():
    FamDict1 = Family_dictionary()
    list = []
    flag = True
    error = {}
    for Famid in FamDict1:
        if FamDict1[Famid]["Divorce_date"] != "NA":
            if FamDict1[Famid]["Divorce_date"] < FamDict1[Famid]["Marriage_date"]:
                list.append(Famid)
                flag = False
                error = {"id":"US04","error":"divorce before marriage","Family id":list}
            else:
                pass
        else:
            pass
    return flag


def CheckDivorceBeforeDeath():
    IndDict1=Individual_dictionary()
    FamDict1=Family_dictionary()
    flag = True
    error = {}
    list = []
    for Famid in FamDict1:
        husbdate = IndDict1[FamDict1[Famid]["Husb_id"]]["Death"]
        Wifedate = IndDict1[FamDict1[Famid]["Wife_id"]]["Death"]
        if FamDict1[Famid]["Divorce_date"] != "NA":
            if husbdate != "NA" and husbdate < FamDict1[Famid]["Divorce_date"]:
                list.append(Famid)
                flag = False
                error = {"id":"US06","error":"divorce before death","Family id":list}
            elif Wifedate != "NA" and Wifedate < FamDict1[Famid]["Divorce_date"]:
                list.append(Famid)
                flag = False
                error = {"id":"US06","error":"divorce before death","Family id":list}
            else:
                pass
    else:
        pass
    print(error)
    return flag


def main():
    printTable()
    print(CheckDivorceBeforeDeath())
    
    
if __name__== "__main__":
  main()


