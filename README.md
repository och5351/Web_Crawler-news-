<h1 align="center">Crawler</h1>
<br><br>

## 웹 크롤러란?

 웹 크롤러(web crawler)는 조직적, 자동화된 방법으로 월드 와이드 웹을 탐색하는 컴퓨터 프로그램이다.

웹 크롤러가 하는 작업을 '웹 크롤링'(web crawling) 혹은 '스파이더링'(spidering)이라 부른다. 검색 엔진과 같은 여러 사이트에서는 데이터의 최신 상태 유지를 위해 웹 크롤링한다. 

<div align="right"><a href ="https://ko.wikipedia.org/wiki/웹_크롤러">참조_위키백과</a></div>

<br><br>

<a id="home1"></a>

## 목차

1. [Crawler 구조](#1)
2. [임시적 Cralwer 구조](#2)

<br><br>
<a href="1"></a>

## 1. Crawler 구조
<br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/45858414/132934475-5a4b3e04-93eb-44d1-8ba9-cc542567ae48.png" width="70%", heigh="70%">
 </p>

Master/Slave 모델을 따르는 Architecture

* Master(Frontier) : 서버역할을 하며 Agent가 수집한 URL을 전송받아 관리하게 되며, 필터링된 URL을 다시 Agent로 분배한다.
    * 각 Agent가 방문해야 할 URL과 다운로드 해야 하는 Resource URL 목록을 보관한다.
    * Agent가 새로 수집한 URL을 전송하면 필터링을 수행한 후 남겨진 URL을 방문해야 할 URL 목록에 추가한다.
    * Agent로 방문해야 할 URL을 분배한다.
    * 방문해야 할 URL 목록이 모두 소진될 때 까지 위 3단계를 반복한다.

  <br><br>

* Slave(Agent) : Frontier로부터 URL을 전송받아, 해당 URL의 웹페이지(HTML)를 처리한다. 웹페이지 처리 결과로 다른 웨페이지에 대한 URL Link와 이미지 등의 리소스 URL Link를 추출한다. 추출된 모든 URL Link는 Frontier로 전송
    * Frontier로 부터 전송받은 URL을 HTTP 프로토콜을 이용해 접근한다.
    * HTTP 응답으로 HTML 문서를 얻어 분석한다.
    * HTML 문서 분석결과로 다음 방문한 URL Link와 수집해야 할 Resource URL Link를 추출한다.
    * 새로 수집된 모든 URL을 Frontier로 전송한다.

  <br><br>

* Monitor : Frontier와 Agent의 동작 상태를 모니터링하고, 제어기능을 포함한다. 
    * Frontier와 Agent의 동작상태를 모니터링하며 데이터를 시각적으로 재구성 출력한다.
    * Frontier와 Agent의 이상(anomaly) 상태를 파악한다.
    * Monitor를 통해 Frontier의 일부 기능을 실시간으로 제어할 수 있다.


<div align="right"><a href="https://lyb1495.tistory.com/104">참조 - 웹 크롤러 아키텍처</a></div>

 <br>

<div align="right"> 

[목차로](#home1) 
</div><br><br>
 
<a href="2"></a>

## 2. 임시적 Cralwer 구조
<br>

<div align="center">
  <img src="https://user-images.githubusercontent.com/45858414/132974618-3175ee14-4c8a-43fa-98b7-78f8a0fe827c.png" weight="70%" />
</div>

<br>

1. Connect Agent 기능
<br>

   1-1. 정해 놓은 검색엔진과 검색어의 검색 결과(URL) 수집.
   1-2. URL Response를 Collect Agent 로 전달.
   1-3. 처음 수집한 페이지 넘버를 확인 후 Queue 구성 후 Collect에 전달 받은 정보 비교 삽입
<br><br>

2. Collect Agent 기능
<br>

   2-1. Connect Agent 에게 넘겨 받은 URL Response의 HTML 수집.
   2-2. Connect Agent 에게 넘겨 받은 HTML 분석 후 페이지 넘버 추출 및 Connect에 전달
<br><br>

3. Save Agent 기능
<br>

   3-1. Collect Agent에서 수집한 HTML을 지정된 PC에 저장.
<br><br>

[추가 될 기능]

1. Parse Agent 를 통한 HTML 유효 데이터 추출
2. Analytics Agent 를 통한 문서 중요도 분석
3. View Agent 를 통한 분석 결과를 Web view로 표현
  -> 상황에 따라 Web view 표현은 현재 Application에서 표현 하지 않을 수 있으므로 데이터를 전송 하거나 Update 할 수 있는 모듈 구현 계획

<br>

<div align="right"> 

[목차로](#home1) 
</div><br><br>

