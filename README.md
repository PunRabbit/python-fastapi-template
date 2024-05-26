# Python FastAPI Project Template

- Support Korean and English

---

## Koren

### 프로젝트 목적

- 이 프로젝트는 저의 개인적인 코드/프로젝트 스타일을 템플릿화 한 프로젝트 입니다.
- 기본적인 프로젝트 구조를 내포하고 있으며, DockerFile과 docker-compose.yml 파일도 구성되어 있습니다.
- 복잡한 프로젝트일 경우 더 상세한 설정이 들어가지만, 이 프로젝트는 간단한 형태만을 표현합니다.

### 주의 사항

- 구조 및 스타일을 보는 용도로 사용되는 프로젝트 입니다.
- Implement 구현이 제대로 안되어서 sample의 경우, 500으로 반환됩니다. DB Health는 정상 반환 합니다.
- 차후 버전에 따라 기본 메소드를 지원할 예정입니다.

### 실행 방법

- docker-compose.yml 파일에 Dockerfile 참조를 걸어두었습니다.
- docker compose up --build 를 통해, 이미지를 빌드하고 실행해주시면 됩니다.
- 기본적인 노출 포트는 docker-compose.yml 파일에 작성해두었습니다.

### 기본 탑재 시스템 및 중요 디펜던시 정보

- FastAPI
- Dependency-Injector (지원 중단 추정중, 추후 교체 필요)
- Nginx
- MariaDB
- MongoDB
- Redis
- 일부 샘플 도메인 인터페이스 구성 (User, Health)

### 현재 탑재되지 않은 것

- Interface의 Implement 구현
- FastAPI의 response_model 설정
- Celery Method Auto Wiring

### 향후 적용할 것

- NestJS에 존재하는 generate 시스템 동일 구현
- 더 쉬운 Celery Task 할당
- Auth 관련 시스템
- Dependency Injector 개선

### 참고 및 동일 지향점 정보

- https://geminikims.medium.com/지속-성장-가능한-소프트웨어를-만들어가는-방법-97844c5dab63

---

## English

### Project Purpose

- This project is a template of my personal code/project style.
- It contains the basic project structure, and the DockerFile and Docker-compose.yml files are also configured.
- If it is a complex project, more detailed settings are included, but this project only expresses a simple form.

### Notification

- It is a project used to view the architecture and style of develop.
- The Sample's Implementation is not implemented properly, so it is returned to 500. but, health domain will return successfully.
- I will support the basic method depending on the future version.

### How to execute

- Dockerfile reference was hung in docker-compose.yml file.
- You can build and run the image through docker composition up -- build.
- The default exposure port was created in the docker-compose.yml file.

### Basic onboard systems and critical defense information

- FastAPI
- Dependency-Injector (supporting interruption is estimated, replacement required later)
- Nginx
- MariaDB
- MongoDB
- Redis
- Configure some sample domain interfaces (User, Health)

### Not Support Yet

- Implement of Interfaces
- FastAPI's response_model setting
- Celery Method Auto Wiring

### Future

- Same implementation of the generate system present in NestJS
- easier Celery Task assignment
- Auth-related systems
- Improve Dependency Injector

### My favorite and Refer

- https://geminikims.medium.com/지속-성장-가능한-소프트웨어를-만들어가는-방법-97844c5dab63





