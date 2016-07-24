#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import shelve

class Configure:
    __k_accounts = 'accounts'
    __k_servers = 'servers'
    __k_sender = 'sender'
    __k_recipient = 'recipient'
    __k_ttm = 'type_template'
    __k_address = 'address'
    __k_account_number = 'account_number'
    __k_full_name = 'full_name'
    __k_cold_water = 'cold_water'
    __k_hot_water = 'hot_water'
    
    __db = None
    def __init__(self, db_name="config.cfg"):
        self.__db_name = db_name
        try:
            db = shelve.open( self.__db_name, 'r', writeback = True)
        except Exception as exc:
            db = shelve.open( self.__db_name, 'c', writeback = True)
            db[self.__k_accounts] = list()  
            db[self.__k_servers] = list()
            db[self.__k_sender] = ""
            db[self.__k_recipient] = ""
            db[self.__k_ttm] = ""
            db[self.__k_account_number] = ""
            db[self.__k_address] = ""
            db[self.__k_full_name] = ""
            db[self.__k_cold_water] = ""
            db[self.__k_hot_water] = ""
        db.sync()
        db.close()
        
    def __isExists( self, key, type_tm ):
        buff = self.__db[key]
        for element in buff:
            for ckey in element.keys():
                if ckey == type_tm:
                    return True
        return False
    
    def isOpen(self):
        if self.__db == None:
            return False
        return True
    
    def isFill(self):
        if not self.isFillAccounts(): 
            print("Need Fill Accounts")
            return False
        
        if not self.isFillServers(): 
            print("Need Fill Servers")
            return False
        
        if not self.isFillSennder(): 
            print("Need Fill Sennder")
            return False
        
        if not self.isFillRecipient(): 
            print("Need Fill Recipient")
            return False
        return True
            
    def isFillAccounts(self):
        db = self.__db
        if len(db[self.__k_accounts]) > 0:
            return True
        return False
    
    def isFillServers(self):
        db = self.__db
        if len(db[self.__k_servers]) > 0:
            return True
        return False
    
    def isFillSennder(self):
        db = self.__db
        if  db[self.__k_sender] != "":
            return True
        return False
    
    def isFillRecipient(self):
        db = self.__db
        if db[self.__k_recipient] != "":
            return True
        return False
    
    def getTypeTP(self):
        return self.__db[self.__k_ttm];
    
    def setTypeTP(self,type_template):
        self.__db[self.__k_ttm] = type_template
    
    
    def getDB(self):
        return self.__db;
    
    # TODO ADD FLAG OPEN OR CLOSE
    def openDB(self):
        try:
            self.__db = shelve.open( self.__db_name, writeback = True)
        except Exception as exc:
            print("Configure.openDB Error: {}".format( str(exc) ) )

    def syncDB(self):
        try:
            self.__db.sync()
        except Exception as exc:
            print("Configure.syncDB Error: {}".format(str(exc) ) )
        
    def closeDB(self):
        try:
            self.__db.sync()
            self.__db.close()
            self.__db = None
        except Exception as exc:
            print("Configure.closeDB Error: {}".format(str(exc) ) )
        
    def addAccount(self, type_tm, login, password):
        if self.__isExists(self.__k_accounts, type_tm ):
            return False
        buff = self.__db[self.__k_accounts]
        buff.append({ type_tm : [ login, password] } )
        self.__db[self.__k_accounts] = buff
        return True
    
    def addServers( self, type_tm, url, port):
        if self.__isExists(self.__k_servers, type_tm ):
            return False
        buff = self.__db[self.__k_servers]
        buff.append({ type_tm : [ url, port] } )
        self.__db[self.__k_servers] = buff
        return True
        
    def getAccount(self, type_tm):
        for account in self.__db[self.__k_accounts]:
            for key, value in account.iteritems():
                if key == type_tm:
                    return value
        return None
    
    def getServers(self, type_tm):
        for server in self.__db[self.__k_servers]:
            for key, value in server.iteritems():
                if key == type_tm:
                    return value
        return None
        
    def delAccount(self,type_tm):
        buff = self.__db[self.__k_accounts]
        for element in buff:
            for ckey in element.keys():
                if ckey == type_tm:
                    buff.remove(element)

    def delServers( self, type_tm):
        buff = self.__db[self.__k_servers]
        for element in buff:
            for ckey in element.keys():
                if ckey == type_tm:
                    buff.remove(element)
        
    def setSender(self, sender):
        self.__db[self.__k_sender] = sender
    def getSender(self):
        return self.__db[self.__k_sender]
    
    def setRecipient(self, recipient):
        self.__db[self.__k_recipient] = recipient
    def getRecipient(self):
        return self.__db[self.__k_recipient]
        
    def setAccNumber(self, account_number):
        self.__db[self.__k_account_number] = account_number
    def getAccNumber(self):
        return    self.__db[self.__k_account_number]
            
    def setAddress(self, address):
        self.__db[self.__k_address] = address
    def getAddress(self):
        return self.__db[self.__k_address]
    
    def setFullName(self, full_name):
        self.__db[self.__k_full_name] = full_name
    def getFullName(self):
        return self.__db[self.__k_full_name]
        
    def setColdWater(self,cold_water):
        self.__db[self.__k_cold_water] = cold_water
    def getColdWater(self):
        return    self.__db[self.__k_cold_water]
        
    def setHotWater(self, hot_water):
        self.__db[self.__k_hot_water] = hot_water    
    def getHotWater(self):
        return self.__db[self.__k_hot_water]     
        
def main():        
    config = Configure()
    ### Test open/close. need to add check existst the file
    config.openDB()
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setSender("from_mail")
    config.closeDB()
    
    config.openDB()
    print( "Sender:{}".format( config.getSender() ) )
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setRecipient("to_mail")
    config.closeDB()
    
    config.openDB()
    print( "Recipient:{}".format( config.getRecipient() ) )
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setAccNumber("111")
    config.closeDB()
    
    config.openDB()
    print( "AccNumber:{}".format( config.getAccNumber() ) )
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setAddress("street")
    config.closeDB()
    
    config.openDB()
    print( "Address:{}".format( config.getAddress() ) )
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setFullName("Vasiy")
    config.closeDB()
    
    config.openDB()
    print( "FullName:{}".format( config.getFullName() ) )
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setColdWater("01")
    config.closeDB()
    
    config.openDB()
    print( "ColdWater:{}".format( config.getColdWater() ) )
    config.closeDB()
    ###
    
    ### Test set elements
    config.openDB()
    config.setHotWater("02")
    config.closeDB()
    
    config.openDB()
    print( "HotWater:{}".format( config.getHotWater() ) )
    config.closeDB()
    
    ### Test set account
    type_tm = "yandex"
    login = "root"
    password = "12345678"
    
    config.openDB()
    config.addAccount( type_tm, login, password)
    config.addAccount( type_tm, login, password)
    config.syncDB()
    print( config.getAccount(type_tm) )
    config.closeDB()
    ###
    
    ### Test set server
    type_tm = "gmail"
    server = "smtp.gmail.com"
    port = 885
    
    config.openDB()
    config.addServers( type_tm, server, port)
    config.addServers( type_tm, server, port)
    config.syncDB()
    print( config.getServers(type_tm) )
    config.closeDB()
    ###
    
    ### Test del server
    config.openDB()
    config.delServers( type_tm )
    config.delServers( type_tm )
    config.syncDB()
    print( config.getServers(type_tm) )
    config.closeDB()
    ###
    
    
    ### Test del Account
    config.openDB()
    config.delAccount( type_tm )
    config.delAccount( type_tm )
    config.syncDB()
    print( config.getServers(type_tm) )
    config.closeDB()
    ###
    
    ### Test add Accounts
    config.openDB()
    
    type_tm = "yandex"
    login = "root"
    password = "12345678"
    config.addAccount( type_tm, login, password)
    
    type_tm = "gmail"
    login = "admin"
    password = "qwerty"
    
    config.addAccount( type_tm, login, password)
    
    config.syncDB()
    print( config.getAccount(type_tm) )
    config.closeDB()
    ###
    
    ### Test add Servers
    config.openDB()
    
    type_tm = "yandex"
    server = "smtp.yandex.ru"
    port = "879"
    config.addServers( type_tm, server, port)
    
    type_tm = "gmail"
    server = "smtp.gmai.com"
    port = "456"
    
    config.addServers( type_tm, server, port)
    
    config.syncDB()
    print( config.getServers(type_tm) )
    config.closeDB()
    
    ###
    config.openDB()
    print("Point:{}".format(config) )
    print("Fill:{}".format(config.isFill()) )
    config.closeDB()
    ###
    
    ###
    conf_empty = Configure("empty.cfg")
    conf_empty.openDB()
    print("Fill:{}".format(conf_empty.isFill()) )
    conf_empty.closeDB()
    ###
    
    
    try:
        assert( 1 > 2 )
    except Exception as exc:
        print("Assert Error: " )
    
    try:
        assert( 1 > 2 )
    except Exception as exc:
        print("Assert Error: " )

if __name__ == "__main__":
    main()
