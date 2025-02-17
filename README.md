# Webcrawling_hsu_home
사용자가 입력한 키워드로  관련 게시물 데이터를 검색하고 결과를 제공

## 소개
1. 키워드 검색:
사용자가 입력한 키워드를 기반으로 관련 게시물을 검색합니다.

3. 결과 표시:
글번호, 작성자, 조회수, 작성일, 글제목 등을 테이블 형태로 출력합니다.

4. 파일 내보내기:
검색 결과를 CSV 파일로 내보낼 수 있습니다.

## 구조
ih_home.html: 키워드를 입력하는 검색 페이지.

h_search.html: 검색 결과를 표시하는 페이지.

h_home.py: 서버 실행 및 데이터 처리.

## 라이브러리
	•	Selenium: 동적으로 데이터를 가져오기 위해 사용.
	•	BeautifulSoup: HTML 파싱 및 데이터 추출.
	•	Flask: 웹 애플리케이션 서버 구현.
	•	Pico.css: 간단하고 아름다운 UI를 위한 CSS 프레임워크.
