# ASC (Application Security Control)


## 사용법
  1. appsecuritycontrol.py를 메인 프로그램과 같은 디렉토리로 이동시키기
  2. 프로그램 코드 최상단에 
```py
import appsecuritycontrol
```
작성

## 용도
  1. UAC 코드 대용
  2. 실행 전 사용자 확인용


## 원리
  1. import와 동시에 ASC 실행
  2. 사용자 동의 여부 확인
  3. '허용'일 경우 tkinter root만 종료, '거절'일 경우 프로그램 전체 종료


## 라이선스 / Licnese
**MIT License 사용중**


**Under MIT License.**
