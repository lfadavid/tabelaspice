import streamlit as st
import pandas as pd
import numpy as np

#Informações e listas com as informações da planilha

TabelaSpice = {
          'Código':['ARCRS01','ARCRS02','ARCRS03','ARCRS04','ARCRS05','ARCRS06','ARCRS07','ARCRS08','ARCRS09','ARCRS10','Transf. RS x SZ','ARCSZ01','ARCSZ02','ARCSZ03','ARCSZ04','ARCSZ05','ARCSZ06','ARCSZ07','ARCSZ08','ARCSZ09','ARCSZ10','Transf. SZ x RS','ARCSC01','ARCSC02','ARCSC07','ARCSC10','ARCSC11'],
          'Tipo':['Embalado','Embalado','Embalado','Embalado','Dedicado','Dedicado','Embalado','Embalado','Embalado','Embalado','Transferência','Embalado','Embalado','Embalado','Embalado','Embalado','Embalado','Embalado','Embalado','Embalado','Embalado','Transferência','Embalado','Embalado','Dedicado','Embalado','Transferência'],
          'UF':['RJ','RJ','RJ','RJ','RJ','RJ','RJ','RJ','RJ','RJ','RJ','SP','SP','SP','SP','SP','SP','SP','SP','SP','SP','SP','SC','SC','SC','SC','SC'],
          'Destino_Regiões':['Regiões SP e 01','Regiões 02, 03, 04 e 07','Regiões 06, 08, 09, 10 e 11','Regiões 12, 13, 14, 15 e 17','Região 20','Regiões 23 e 24','Regiões 66 e 68','Regiões 67 e 69','Regiões A5, A6, A7, A8 e F8','Regiões 33, 34, 41, 91 e 98','Suzano','Regiões SP e 01','Regiões 02, 03, 04 e 07','Regiões 06, 08, 09, 10 e 11','Regiões 12, 13, 14, 15 e 17','Região 20','Regiões 23 e 24','Regiões 66 e 68','Regiões 67 e 69','Regiões A5, A6, A7, A8 e F8','Regiões 33, 34, 41, 91 e 98','Resende','Regiões SP e 01','Regiões 02, 03, 04 e 07','Regiões 66 e 68','Regiões 33, 34, 41, 91 e 98','Resende'],
          'Peso_Mínimo':[300,400,450,1.000,00,00,450,3.200,3.200,450,450,300,400,450,1.000,400,400,450,3.200,3.200,450,450,450,400,0,450,450],
          'Frete_Mínimo':[87.00,152.47,234.84,624.58,1092.08,1255.27,314.78,2805.09,3405.08,413.13,58.50,48.00,100.47,176.34,494.58,188.41,205.07,257.81,2399.97,2999.96,356.16,58.50,302.81,329.63,948.98,216.00,316.31],
          'Até_1.000':[290.00,381.17,521.86,624.58,1092.08,1564.05,699.51,876.59,1064.09,918.06,130.00,160.00,251.17,391.86,494.58,471.03,512.68,572.91,749.99,937.49,791.46,130.00,672.91,824.08,948.98,480.00,702.91],
          '1.001_3.000':[276.17,366.95,503.20,601.03,1358.19,2221.81,672.23,840.88,1019.45,918.06,130.00,146.17,236.95,373.20,471.03,448.60,488.27,545.63,714.28,892.85,791.46,130.00,645.63,782.58,1215.08,480.00,675.63],
          '3.001_6.000':[267.90,353.54,485.43,578.60,1938.12,2671.21,672.23,840.88,1019.45,918.06,130.00,137.90,223.54,355.43,448.60,448.60,488.27,545.63,714.28,892.85,791.46,130.00,645.63,769.17,1728.50,480.00,675.63],
          '6.001_13.000':[260.09 ,340.89,468.50,557.23,2319.75,4373.34,672.23,806.86,976.93,918.06,130.00,130.09,210.89,338.50,427.23,427.23,512.68,545.63,680.26,850.33,791.46,130.00,645.63,756.51,2073.70,480.00,675.63],
          'Acima_13.001':[252.73,328.95,452.38,536.89,3396.76,5145.10,646.25,774.47,936.44,880.37,130.00,122.73,198.95,322.38,406.89,406.89,488.27,519.65,647.87,809.84,753.77,130.00,619.65,718.60,3396.76,480.00,649.65],
          'Taxa_NFE':[23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00,23.00],
          'ADV(%)':[0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050,0.050],
          
}