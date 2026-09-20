# Week 1 · Basic Background

Python 문법 전체가 아니라 제조 AI 프로젝트에서 반복해서 쓸 데이터 분석 흐름을 익힙니다.

**Data Load → Data Structure → Data Quality → Summary Statistics → Visualization → Observation → Question/Hypothesis**

처음 시작한다면 [00_Pre_Ready 사전 준비](../00_Pre_Ready/00_Pre_Ready.ipynb)에서 Python·Anaconda·Jupyter를 설치하고 [환경 점검 Notebook](../00_Pre_Ready/00_Environment_Check.ipynb)을 실행한 뒤 아래 과정으로 진행하세요.

| 실행 순서 | Notebook | 핵심 활동 |
|---|---|---|
| 1 | [01_Python_Basics](01_Python_Basics.ipynb) | What? 각 문법·라이브러리의 일상 예제 → 제조 적용 → 직접 연습 |
| 2 | [02_Guided_EDA_Practice](02_Guided_EDA_Practice.ipynb) | How? 기초→심화 TODO 20문제, 앞 결과를 활용한 비교와 가설 검토 |
| 해설 | [02_Guided_EDA_Practice_solution](answer/02_Guided_EDA_Practice_solution.ipynb) | 문제별 정답 코드, 관찰 예시 |
| 3 | [03_CapL_Project](03_CapL_Project.ipynb) | Why & What Next? 실제 데이터 적용과 현업 토의 |

설치·실행 방법은 [프로젝트 README](../../README.md)에 있습니다. 라이브러리는 NumPy, Pandas, Matplotlib, JupyterLab, ipykernel이며 전체 실행 검증에는 nbformat, nbclient를 사용합니다.

```text
00_Pre_Ready
    Ready?
    설치·환경 설정·첫 Notebook 실행 확인

        ↓

01_Python_Basics
    What?
    개념과 기본 사용법 이해

        ↓

02_Guided_EDA_Practice
    How?
    교육생이 직접 분석 수행

        ↓

03_CapL_Project
    Why & What Next?
    실제 현업 데이터에 적용하고
    결과를 현업 지식과 함께 해석
```

교재 폴더 전체를 유지하세요. 프로젝트 루트의 `data/practice_process_data.csv`는 기본·실습·해설에서 공통 사용합니다. [데이터 설명](../../data/README.md)을 먼저 확인하고, 각 Notebook에서 위에서부터 셀을 실행합니다.

진행 원칙: 질문을 먼저 읽고 실행한 다음 결과를 기록합니다. 그래프 뒤 `What do you observe?`를 작성하고, 관찰한 사실과 추가 검증할 설명을 구분합니다. 해설은 실습 후 확인합니다.

02는 데이터 이해(Q1–Q3), 품질·조건 선택(Q4–Q7), 분포·관계(Q8–Q11), Context별 비교(Q12–Q15), 심화 분석(Q16–Q20)으로 진행합니다. 심화에서는 Product 고정 → 장비별 Recipe 차이 → IQR 후보 표시 → 제외 전후 민감도 → Product별 센서–품질 가설 검토를 수행합니다. 앞 문제의 결과를 지정한 변수명으로 저장한 뒤 순서대로 실행하세요. 기본은 60–75분, 심화는 30–45분을 권장합니다.

01은 장보기·점수·카페 주문처럼 익숙한 사례에서 시작합니다. 각 Python 문법과 NumPy·Pandas 연산을 **간단한 예제 → 제조 데이터 예제**로 연결하고, TODO와 접힌 확인 기준으로 스스로 점검합니다. Pandas는 작은 DataFrame 만들기부터 CSV 읽기·열 선택·조건 검색·계산 열·결측·GroupBy까지 진행합니다. 네 가지 그래프도 일상/제조 사례를 한 쌍씩 비교합니다.

01의 예제 실행·토의는 100–120분, 직접 연습은 40–60분을 별도로 배정하세요. 두 회차로 나누면 0–6절(Python·NumPy), 7–11절(Pandas·EDA) 순서로 진행합니다. 마지막 종합 연습에서는 카페 표와 공정 CSV에 동일한 분석 workflow를 적용합니다. 일상 데이터는 Notebook 안에서 생성하므로 추가 파일이 필요하지 않습니다.

03은 `DATA_PATH`와 `column_map`을 실제 데이터에 맞게 수정합니다. 데이터가 없어도 끝까지 실행되며 수치 결과는 생성하지 않습니다. **Apply → Analyze → Discuss → Domain Knowledge → Improve → Re-Analyze → Next Hypothesis** 순서로 진행합니다.
