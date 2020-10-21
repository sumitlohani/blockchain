#------------simple blockchain example------------------
#create a new blockchain (list with a genesis block) --> create new block 
#--> mine the block(pass the proof of work i.e to put some computational power as per the difficulty parameter provided)
#--> add the block -> chehck its validity
import hashlib
import datetime

class Block:
    def __init__(self,index,date_time,data,previoushash):
        self.index=index
        self.date_time=date_time
        self.data=data
        self.previoushash=previoushash
        self.temp=0
        self.currenthash=self.calculatehash()
    def calculatehash(self):
        string=str(self.index)+str(self.date_time)+str(self.data)+str(self.previoushash)+str(self.temp)
        return  hashlib.sha256(string.encode()).hexdigest()
#    increment the temp variable and count calculate the new hash till the pattern of hash matches to a defined pattern
    def mine(self,difficulty):
        # here we are validating proof of work by comparing hash to a set of zeros
        x="0"*difficulty
        while(self.currenthash[0:difficulty]!=x):
            self.temp+=1
            self.currenthash=self.calculatehash()

class Blockchain:
    def __init__(self,data,difficulty):
        date_time=datetime.datetime.now()
        self.chain=[Block(0,date_time,data,-1)]
#        latency is the difficulty parameter to mine the block --> increase the difficulty to increase the mining power
        self.difficulty=difficulty 
    def Getlatest(self):
        return self.chain[len(self.chain)-1]
    def AddBlock(self,data):
        lasthash=self.Getlatest().currenthash
        lastindex=self.Getlatest().index
        date_time=datetime.datetime.now()
        newBlock=Block(lastindex+1,date_time,data,lasthash)
#        mine the block then add to the blockchain
        newBlock.mine(self.difficulty)
        self.chain.append(newBlock)
    def isValid(self):
        for i in range(1,len(self.chain)):
            current=self.chain[i]
            previous=self.chain[i-1]
            if(current.previoushash!=previous.currenthash):
                return False
            if(current.currenthash!=current.calculatehash()):
                return False
        return True                     

#increase the difficulty as per requirement-----------
mychain=Blockchain("Genesis",4)

mychain.AddBlock({"Sender":"skull","Receiver":"candy","Amount":4000}) 
print("new block added")
print("____________________")

mychain.AddBlock({"Sender":"mr","Receiver":"kull","Amount":4000})
print("new block added")
print("____________________")

print("-------------------------------------------------------------")
for i in range(0,len(mychain.chain)):
    print(mychain.chain[i].date_time,end=" | ")
    print(mychain.chain[i].data,end=" | ") 
    print(mychain.chain[i].currenthash,end=" | ")
    print(mychain.chain[i].previoushash,end=" | ")
    print("--------------------------------------------------------")
 #  ----------chceck validity-------
print()
print("______________________________")
print()
print("valid : ",mychain.isValid())
       
