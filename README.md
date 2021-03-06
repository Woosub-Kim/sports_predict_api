# <한국직업전문학교 무재칠시 프로젝트> with <a href='https://github.com/namwon94'>김남원</a>
#### 스포츠 경기결과 예측 API 
참고:      
https://github.com/Woosub-Kim/Project_KBO_Predict               
https://github.com/Woosub-Kim/project_NBA_predict                 
https://github.com/Woosub-Kim/project_MLB_predict                     

# 설명
KBO경기의 경우 홈팀과 원정팀의 선발선수들의 최근 WAR성적을 입력한다.              
MLB경기의 경우 각 팀의 평균 ERA  WHIP  투수WAR SLG OBP 타자WAR을 입력한다.      
NBA경기의 경우 각 팀의 평균 WS VORP BPM을 입력한다.
승리팀이 HOME인지 AWAY인지를 JSON으로 return해준다.    

# 사용예시
|설명|링크|
|----|----|
|KBO경기 예측| root+/KBO?home_pitcher=0.5&home_hitter1=0.9&home_hitter2=0.8&home_hitter3=0.7&home_hitter4=0.6&home_hitter5=0.3&home_hitter6=0&home_hitter7=0.2&homehiatter8=0&home_hitter9=0&away_pitcher=2.1&away_hitter1=0.6&away_hitter2=0.6&away_hitter3=0.8&away_hitter4=1.2&away_hitter5=1.1&away_hitter6=0.6&away_hitter7=0.6&away_hitter8=0.5&away_hitter9=0.3&  |            
|MLB경기 예측|root+/MLB?home_OBP=0.179760&home_SLG=0.216020&home_WAR_b=0.382000&away_OBP=0.213875&away_SLG=0.314812&away_WAR_b=0.231250&home_WHIP=1.712727&home_ERA=5.886818&home_WAR_p=0.445455&away_WHIP=1.739130&away_ERA=7.046957&away_WAR_p=0.469565|                           
|NBA경기 예측| root+/NBA?home_BPM=-0.3&away_BPM=-1.5&home_VORP=0.9&away_VORP=0.6&home_WS=3&away_WS=3 |                    

# 사용방법
API에 해당하는 본 git와 <a href='https://github.com/namwon94/Project_Baseball'> Web application git</a>를 다운로드 후 서버실행하시면 됩니다.

###### 한국직업전문학교 무재칠시 링크
|설명|링크|
|----|----|
|KBO경기 예측| https://github.com/Woosub-Kim/Project_KBO_Predict |            
|MLB경기 예측| https://github.com/Woosub-Kim/project_MLB_predict |                           
|NBA경기 예측| https://github.com/Woosub-Kim/project_NBA_predict |                    
|API| https://github.com/Woosub-Kim/sports_predict_api |                  
|WEB| https://github.com/namwon94/Project_Baseball |                     
