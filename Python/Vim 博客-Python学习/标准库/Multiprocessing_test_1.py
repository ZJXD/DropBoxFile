import os
import os.path
import subprocess
import wget

def retrieving_obpg(filelist,outpath):
    '''Download data'''
    f = open(filelist,'r')
    log= open(outpath + 'test_log.txt','w')
    os.chdir(outpath)
    print(os.curdir)
    for i in f:
        try:
            each_item = str(i.strip())
            
            print(cmd)            
            if not os.path.exists(outpath + each_item):
                status = subprocess.call(cmd,shell = True)
                if status !=0:
                    log.write('\nFailed:'+each_item)
                    continue
                log.write('\nSuccess:'+each_item)
            log.flush()
        except:
            log.write('\nFailed:'+each_item)
            continue        
    f.close()
    log.close()


if __name__  =='__main__':        
        import glob
        outpath = './test/'
        filelist = 'test_1.txt'
        retrieving_obpg(filelist,outpath)
        print('END')
