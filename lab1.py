__author__ = 'michael'

import urllib2
from datetime import datetime
import pandas as pd
import os
import shutil

def Delete():

    shutil.rmtree('/home/michael/PycharmProjects/lab1/VHI')
    os.mkdir('VHI')

time_now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

def Download():
    list = ['24', '25', '05', '06', '27', '23', '26', '07', '11', '13', '14', '15', '16', '17', '18', '19', '21', '22',
            '08', '09', '10', '01', '02', '03', '04', '12', '20']

    k = 1

    for i in list:
        url = "http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + i + ".txt"
        vhi_url = urllib2.urlopen(url)
        out = open('VHI/vhi_id_' + str(k) + '_' + str(time_now) + '.csv', 'wb')
        out.write(vhi_url.read())
        out.close()
        print "VHI " + str(k) + " is downloaded..."
        k += 1
        break

def Treatment(state):
    infile = open('VHI/vhi_id_' + str(state) + '_' + str(time_now) + '.csv', 'r')
    lines = []
    for line in infile:
        lines.append(line)

    infile.close()

    outfile = open('VHI/vhi_id_' + str(state) + '_' + str(time_now) + '.csv', 'w')

    str1 = '-1.00'
    for row in lines:
        if row.find(str1) == -1:
            outfile.write(row)

    outfile.close()



def VHI_for_year(state, year):

    df = pd.read_csv('VHI/vhi_id_' + str(state) + '_' + str(time_now) + '.csv', index_col=False, header=1)
    t = df[(df['year'] == year)]
    k = 0
    while k < len(list(t['VHI'])):
        print list(t['VHI'])[k]
        k += 1

    print t['VHI'].min()
    print t['VHI'].max()


def VHI_for_years_extreme(state, percent):
    df = pd.read_csv('VHI/vhi_id_' + str(state) + '_' + str(time_now) + '.csv', index_col=False, header=1)
    t = df[(df['%Area_VHI_LESS_15'] >= int(percent))]
    print 'Extreme :'

    print str(list(t['year']))+'===>'+str(list(t['VHI']))


def VHI_for_years_pomirno(state, percent):
    df = pd.read_csv('VHI/vhi_id_' + str(state) + '_' + str(time_now) + '.csv', index_col=False, header=1, prefix=' ')
    t = df[(df['%Area_VHI_LESS_35'] >= int(percent))]
    print 'Pomirno : '
    print str(list(t['year']))+'===>'+str(list(t['VHI']))

def VHI_spriyatlivyi(state):
    df = pd.read_csv('VHI/vhi_id_' + str(state) + '_' + str(time_now) + '.csv', index_col=False, header=1, prefix=' ')
    t = df[(df['VHI'] > int(60)) & (((df['week'] > 45) & (df['week'] < 53)) | (df['week'] < 5))]

    print 'Spriyatlivyi :'
    print list(t['year'])


Delete()
Download()
Treatment(1)
VHI_for_year(1, 1981)
VHI_for_years_extreme(1, 60)
VHI_for_years_pomirno(1, 90)
VHI_spriyatlivyi(1)
