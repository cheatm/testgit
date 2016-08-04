import pandas
import os,os.path,time
import indicator

dirpath='D:/ForexData'

def fileList(dir=dirpath,include=None):
    listdir=os.listdir(dir)

    if include is not None:
        for l in listdir:
            if include not in l:
                listdir.remove(l)

    return (listdir)


def addColumns(file,dir=dirpath,columns=None):
    fname=dir+'/'+file
    f=open(fname,'r')
    dataString=f.read()
    f.close()
    # data=dataString.split('\n')
    # data.insert(0,columns)
    # dataString='\n'.join(data)
    dataString=columns+'\n'+dataString
    f=open(fname,'w+')
    f.write(dataString)
    f.close()
    print(file + ' add successed')
    # print(dataString)




def readForexData(fileName,dir=dirpath):

    file=dir+'/'+fileName
    print('Reading %s' % file)
    data=pandas.read_csv(file)
    # print(data[0:100])
    for i in data.index:
        t=data.get_value(i,'date')
        try:
            mktime=time.mktime(time.strptime(t,'%Y.%m.%d'))
        except:
            pass
        data.set_value(i,'time',mktime)


    return (data)



if __name__ == '__main__':
    forex=fileList(include='csv')[1]
    print(forex)

    data=readForexData(forex)
    analisys=indicator.MACD_Analisys(data)
    analisys=analisys.set_index('date',drop=True)
    print(analisys)
    savePath='D:/%s/%s.xlsx' % ('MACD_Analysis',forex[:-4])
    print('Saving to %s' % savePath)
    analisys.to_excel(savePath)
    print('Accomplished')