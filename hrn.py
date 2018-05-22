#!/usr/bin/python27

import os,sys

if __name__ == "__main__":
    elaspedTime = 0

    procList = list()
    
    maxRatio = 0

    if os.path.exists(os.path.abspath(".\\input.txt")) :
        print "[+] file opening.\n"
        
        with open(".\\input.txt","r") as fp:
            data = fp.read()
        print "process list"
        print data+"\n"
    else :
        print "[-] file doesn't exists."
        sys.exit(1)
    

    for each in data.split("\n"):
            if not len(each.split(",")) == 3:
                break

            procList.append(
                {"procNum":each.split(",")[0],
                 "procArvtime":each.split(",")[1],
                 "procBursttime":each.split(",")[2],
                 "procRatio":""}
                )



    print "Number of Process : "+str(len(procList))+"\n"
    print "proc_id \tarv_time\tburst_time\tfin_time\tret_time\tregret_time"
    print"-"*90        
    
    elapsedTime = int(procList[0]["procBursttime"])

    cur = procList[0]["procNum"]
    regret = str(elapsedTime/float(procList[0]["procBursttime"]))[:4]+"s"
    print cur+"\t\t"+procList[0]["procArvtime"]+"\t\t"+procList[0]["procBursttime"]+"\t\t"+str(elapsedTime)+"\t\t"+str(elapsedTime)+"\t\t"+regret
    procList.remove(procList[0])


    for i in range(0,len(procList)):

        queue = list()
        
        for items in procList :

            if int(items["procArvtime"]) <= elapsedTime:
                queue.append(items)
            else :
                break

        if len(queue)==1:
            
            cur = queue[0]["procNum"]
            elapsedTime = elapsedTime + int(queue[0]["procBursttime"])
            rettime = elapsedTime - int(queue[0]["procArvtime"])
            regret = str(elapsedTime/float(rettime))[:4]+"s"
            print cur+"\t\t"+queue[0]["procArvtime"]+"\t\t"+queue[0]["procBursttime"]+"\t\t"+str(elapsedTime)+"\t\t"+str(rettime) +"\t\t"+regret
            procList.remove(queue[0])

            
        else :
            for items in queue :
                items["procRatio"] = ((elapsedTime - int(items["procArvtime"]))+int(items["procBursttime"]))/float(items["procBursttime"])


            for items in queue :
                if maxRatio<= items["procRatio"] :
                    maxRatio = items["procRatio"]

            for items in queue :
                if maxRatio == items["procRatio"]:
                    
                    cur = items["procNum"]
                    elapsedTime = elapsedTime + int(items["procBursttime"])
                    rettime = elapsedTime - int(items["procArvtime"])
                    regret = str(elapsedTime/float(rettime))[:4]+"s"
                    print cur+"\t\t"+items["procArvtime"]+"\t\t"+items["procBursttime"]+"\t\t"+str(elapsedTime) +"\t\t"+str(rettime)+"\t\t"+regret
                    procList.remove(items)
                    break
