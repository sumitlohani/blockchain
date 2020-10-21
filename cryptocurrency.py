#----------------Simple Crptocurrency example------------------------
#   Everytime a miner mine the pending transactions (add them to a new block and passing proof of work)
#   his reward is added to newly created pending transaction array with his toAddress and reward amount
import hashlib
import datetime

class Transaction:
    def __init__(self,fromAddress,toAddress,Amount):
        self.fromAddress=fromAddress
        self.toAddress=toAddress
        self.Amount=Amount        

class Block:
    def __init__(self,date_time,Transactions,previoushash):
        self.date_time=date_time
        self.Transactions=Transactions
        self.previoushash=previoushash
        self.count=0
        self.currenthash=self.calculatehash()
    def calculatehash(self):
        string=str(self.date_time)+str(self.Transactions)+str(self.previoushash)+str(self.count)
        return  hashlib.sha256(string.encode()).hexdigest()
    def mine(self,difficulty):
        x="0"*difficulty
        while(self.currenthash[0:difficulty]!=x):
            self.count+=1
            self.currenthash=self.calculatehash()

class Blockchain:
    def __init__(self,GenesisTransaction,difficulty):
        date_time=datetime.datetime.now()
        self.chain=[Block(date_time,GenesisTransaction,-1)]
        self.difficulty=difficulty
        self.PendingTransactions=[]
        self.miningrewards=100
    def Getlatest(self):
         return self.chain[len(self.chain)-1]
#  mining the list of pending transactions and adding to the chain
#  passing the miners address to add his reward to the new pending transaction list (with his address and reward amount)
    def mineBlock(self,MinerAddress):
        date_time=datetime.datetime.now()
        lasthash=self.Getlatest().currenthash
        newblock=Block(date_time,self.PendingTransactions,lasthash)
        newblock.mine(self.difficulty)
        print("Congo !!! -- A new block mined--")
        print("YIPPEEEEEE!!! -------------Miner rewarded------------")
        print("...Miner's reward will be added once a new block containing his reward is mined")
        print()
        self.chain.append(newblock)
#  adding the miners reward to new pending transaction with his address and reward amount
        self.PendingTransactions=[Transaction(None,MinerAddress,self.miningrewards)]
    def CreateTransaction(self,transaction):
        self.PendingTransactions.append(transaction)
#   Balance of an address is checked by traversing the complete chain and cheching 
#   every transaction object in the transaction array of each block
    def GetBalanceofAddress(self,address):
        balance=0
        for block in self.chain:
            for transaction in block.Transactions:
                if(transaction.fromAddress==address):
                    balance-=transaction.Amount
                elif(transaction.toAddress==address):
                    balance+=transaction.Amount
        return balance
    def isValid(self):
        for i in range(1,len(self.chain)):
            current=self.chain[i]
            previous=self.chain[i-1]
            if(current.previoushash!=previous.currenthash):
                return False
            if(current.currenthash!=current.calculatehash()):
                return False
        return True     
#   Genesis block with new Genesis transaction
GenesisTransactions=[Transaction(None,"Genesis",2000)]                
mychain=Blockchain(GenesisTransactions,4)

mychain.CreateTransaction(Transaction("one","two",1000))
mychain.CreateTransaction(Transaction("two","three",2000))
mychain.CreateTransaction(Transaction("three","four",3000))

mychain.mineBlock("sumit")
#  after mining a new block with above pending transactions miner("Sumit") got a reward 
#  that is saved in a new pending transaction array
print("Balance of --Sumit-- >",mychain.GetBalanceofAddress("sumit"))
print("______________________________________________________________")
print()
#  the balance is 0 as the transactions array with his reward is not yet added to the chain
#  once the pending record with his reward is mined by someone his balance will increase.

mychain.CreateTransaction(Transaction("here","there",2400))
mychain.CreateTransaction(Transaction("here","there",6000))
mychain.mineBlock("sumit")
print("Balance of --Sumit-- >",mychain.GetBalanceofAddress("sumit"))
#  ----------chceck validity-------
print()
print("______________________________")
print()
print("valid : ",mychain.isValid())
    
