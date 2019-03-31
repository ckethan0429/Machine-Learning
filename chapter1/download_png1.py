#라이브러리 읽기
#urllib는 URL다루는 모듈 모아놓은 패키지
#http 또는 ftp 사용해 데이터를 다운로드 
import urllib.request 


#url과 저장 경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename="test.png"

#다운로드
urllib.request.urlretrieve(url,savename) #urlretrieve() 함수는 직접다운로드가능
print("저장되었습니다.")