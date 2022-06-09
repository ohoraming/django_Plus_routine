# Plus_routine

## 소개
- 일정을 등록하고 일정 수행 정도를 기록하는 애플리케이션입니다.

## 개발 환경
- `Python 3.10.5` 
- `Django 3.2`
- `JavaScript ES6`
- `Bootstrap v5`
- `djangorestframework 3.13.1`
- `postgresql 14`

## 설치 방법
  ```bash
  git clone https://github.com/ohoraming/django_Plus_routine.git
  cd django_Plus_routine-main/
  ```
  데이터베이스 이름을 `routine`으로 생성합니다
  ```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```

## 기능
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/77590526/172838196-4d02be65-2726-4487-97e5-1917c431cf4d.png">
- 일정 등록하기
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/77590526/172838321-a41e486a-f64f-4a28-9b6b-09a2c43f74cf.png">
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/77590526/172838383-82702a8b-4f79-41b7-8ecb-8fcb76535a20.png">
- 일정 수행 여부 등록(안 함/시도/완료) 

## ERD(Entity Relationship Diagram)
  <img width="700" alt="image" src="https://user-images.githubusercontent.com/77590526/172837966-2ba56336-00da-497a-b443-c8a5a7ea97ef.png">

## 개선 사항
- template 이름 간단히 수정 필요
- request/response 체크 추가 
- test code 추가 필요
