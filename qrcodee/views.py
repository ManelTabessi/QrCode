from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
import json
import collections 
import qrcode
import cv2
from pyzbar.pyzbar import decode
import qrtools
import io 
import os
import glob
import IPython.display as display
from PIL import Image
from flask import Flask, render_template, url_for
from django.http import FileResponse
from django.http import JsonResponse
import datetime

from django.core.files import File
# Create your views here.
def index(request):
	return HttpResponse ('<h1>Hello</h1>')

def defaultconverter(o):
  if isinstance(o, datetime.date):
      return o.__str__()

def getJson(request,rib,DD,DF):
     class create_dict(dict): 
  
     
            def __init__(self): 
               self = dict() 
          
     
            def add(self, key, value): 
              self[key] = value
     conn = mysql.connector.connect(host="localhost",
                               user="root", password="", 
                               database="qrcode")
      
     cursor = conn.cursor()
     mydict = create_dict()
     cursor.execute("SELECT mouvement.idmouvement,mouvement.date,mouvement.montant,mouvement.mouvementtype FROM  compte ,compte_mouvement RIGHT OUTER JOIN mouvement ON mouvement.idmouvement = compte_mouvement.mouvement_idmouvement WHERE compte.rib = %s AND (compte_mouvement.compte_rib=compte.rib) AND (mouvement.date >= %s AND mouvement.date <= %s)   ORDER BY mouvement.date;",(rib,DD,DF)) 
     # sql_select_query = """select * from client where id_client = %d"""
     # cursor.execute(sql_select_query, (id,))
     #cursor.execute("SELECT  id_client,first_name,last_name FROM client WHERE id_client= %d"  )
     rows = cursor.fetchall()
     
     
     #objects_list = []
     for row in rows:
        #d = collections.OrderedDict()
        #d["rib"]=row[0]
        # d["date"]=row[0]
        # d["montant"]=row[1]
        # d["type"]=row[2]
       # d["last_name"]=row[3]

   
        mydict.add(row[0],({"date":row[1],"montant":row[2],"type":row[3]}))
        #objects_list.append(d)
        j = json.dumps(mydict, indent=2, sort_keys=True,default=defaultconverter)
        filename = "Client"+str(rib)
        with open(filename+".js", "w") as f:
            f.write(j)
             # os.chdir("/")
     # filename = glob.glob(file+".js")
     file=str(filename+'.js')
     with open(file)as f:  
         data =f.read()  

     img = qrcode.make(data) 
     #file2=str(filename.replace('.js',''))
     file2=str(filename)
   
     img.save(file2+".png")
    
     imagg = open("Client"+str(rib)+".png", "rb").read()
     
     return HttpResponse (imagg, content_type="image/png")
    

def getJsonClient(request,file):     
     # os.chdir("/")
     # filename = glob.glob(file+".js")
   
     with open(file)as f:  
         data =f.read()  

     img = qrcode.make(data) 
     file2=str(file.replace('.js',''))
     img.save(file2+".png")   
     
     return HttpResponse (img, content_type="image/png")


def getClientDecode(request,filename):
  
   #fil=str(filee)+".png"
   img = cv2.imread(filename)
   qr_detector = cv2.QRCodeDetector()
   Data,BBOX,Straight_QRcode = qr_detector.detectAndDecode(img)
   if BBOX is not None:
      if Data:
         
         return HttpResponse(Data,content_type="json")
  

def getDecode(request):
  
   
    return render(request,'decode.html')





def ListeRib (request) :
     con = mysql.connector.connect(host="localhost",
                               user="root", password="", 
                               database="qrcode")
      
     cursor = con.cursor()
     cursor.execute("SELECT RIB FROM compte")
     rows = cursor.fetchall()
     
     # objects_list = []
     # for row in rows:
     #    d = collections.OrderedDict()
     #    d["Rib"]=row[0]
     # objects_list.append(d)   
     #return HttpResponse(rows)
     return render (request,'liste.html',{'rows':rows})
          
def Rib (request) :
    
    
     return render (request,'rib.html')          



def GetCompte  (request,rib) :
    conn = mysql.connector.connect(host="localhost",
                               user="root", password="", 
                               database="qrcode")
      
    cursor = conn.cursor()
    req1=cursor.execute("SELECT first_name FROM  client  JOIN compte WHERE compte.rib = %s AND (client.id_client=compte.client_id_client);", [rib] ) 
    rows = cursor.fetchall()
        
     
   
   
     
        
    return render (request,'compte.html',{'rib':rib})       

def getClientDecode2(request,filename):
  
   fil=str(filename)+".png"
   img = cv2.imread(fil)
   qr_detector = cv2.QRCodeDetector()
   Data,BBOX,Straight_QRcode = qr_detector.detectAndDecode(img)
   if BBOX is not None:
      if Data:
         
         return HttpResponse(Data,content_type="json")
  



def GetInfo  (request,rib) :

    class create_dict(dict): 
  
     
            def __init__(self): 
               self = dict() 
          
     
            def add(self, key, value): 
              self[key] = value
    conn = mysql.connector.connect(host="localhost",
                               user="root", password="", 
                               database="qrcode")
      
    cursor = conn.cursor()
    mydict = create_dict()
    req1=cursor.execute("SELECT compte.rib,client.first_name, client.last_name  FROM  client  JOIN compte WHERE compte.rib = %s AND (client.id_client=compte.client_id_client);", [rib] ) 
    rows = cursor.fetchall()
    for row in rows:
       

   
        mydict.add(row[0],({"Firstname":row[1],"Lastname":row[2]}))
        
        j = json.dumps(mydict, indent=2, sort_keys=True,default=defaultconverter)
        filename = "Rib"+str(rib)
        with open(filename+".js", "w") as f:
            f.write(j)
           
    file=str(filename+'.js')
    with open(file)as f:  
         data =f.read()  


    return HttpResponse(data)     
       