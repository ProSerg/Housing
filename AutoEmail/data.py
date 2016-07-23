#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

#TODO need rename Data => Message
class DataTemplate:
    keys = {
        "YK" : ['Address' , 'AccountNumber', 'FullName' , 'ColdWater' , 'HotWater' ],
        "GG" : ["aa", "bb", "cc", "dd"]
    }
    templates = {
        "YK" : """\
        <html>
          <head>
          </head>
            <body>
            <h2>{Address}</h1>
                <table>
                  <tr>
                    <th width="100"></th>
                    <th width="10"></th>
                    <th></th>
                  </tr>
                  <tr>
                    <td>Номер счёта</td>
                    <td width="10">:</td>
                    <td>{AccountNumber}</td>
                  </tr>
                  <tr>
                    <td>ФИО</td>
                    <td width="10">:</td>
                    <td>{FullName}</td>
                  </tr>
                </table>
                
            <p><b>Показания счётчиков на воду</b></p>
                <table >
                  <tr>
                    <th></th>
                    <th width="10"></th>
                    <th ></th>
                  </tr>
                  <tr>
                    <td>ХВС</td>
                    <td width="10">:</td>
                    <td>{ColdWater}</td>
                  </tr>
                  <tr>
                    <td>ГВС</td>
                    <td width="10">:</td>
                    <td>{HotWater}</td>
                  </tr>
                </table>
          </body>
        </html>
        """,
        "GG" : """ BEY GG"""
    }    
    def getKey(self, type_name):
        try:
            return self.keys.get(type_name)
        except Exception as exc:
            print( "DataTemplate.getKey({}) failed; {}".format(type_name,str(exc)) ) # give a error message
            
    def getTemplate(self, type_name):
        try:
            return self.templates.get(type_name)
        except Exception as exc:
            print( "DataTemplate.getTemplate({}) failed; {}".format(type_name,str(exc)) ) # give a error message
            return None
        

#dt = DataTemplate()
#print( dt.getData("YK") )
#print( dt.getTemplate("YK") )

#print( dt.getData("GG") )
#print( dt.getTemplate("GG") )
