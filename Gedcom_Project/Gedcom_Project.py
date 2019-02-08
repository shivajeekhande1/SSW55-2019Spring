def main():
  tags={'0':['NOTE','HEAD','TRLR'],'1':['SEX','BIRT','DEAT','NAME','FAMC','FAMS','HUSB','WIFE','MARR','CHIL','DIV'],'2':['DATE']}
  f = open("C:/Users/princ/OneDrive/Documents/stevens/proj02test.ged","r")
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
    
if __name__== "__main__":
  main()


