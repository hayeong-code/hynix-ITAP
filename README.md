# hynix-iTAP 실습자료

고려대학교–SK하이닉스 산학 교육 프로그램 “In-Line ICBV 학습을 통한 CapL 예측 Model 개발”의 주차별 교육자료입니다.

이번 1주차 목표는 Python 문법 전체를 배우는 것이 아니라 다음 데이터 분석 workflow를 스스로 수행하는 것입니다.

**Data Load → Data Structure 확인 → Data Quality 확인 → Summary Statistics → Visualization → Observation → Question/Hypothesis**

## 디렉터리 구조

```text
hynix-iTAP/
├── README.md
├── requirements.txt
├── data/                          # 모든 주차의 공통 데이터
│   ├── README.md
│   ├── practice_process_data.csv
│   └── private/                   # 실제 데이터, Git 제외
├── utils/                         # 모든 주차의 공통 코드
│   ├── README.md
│   └── generate_practice_data.py
├── week1/
│   ├── README.md
│   ├── 00_Pre_Ready/
│   │   ├── 00_Pre_Ready.ipynb
│   │   └── 00_Environment_Check.ipynb
│   └── 01_Basic_Background/
│       ├── README.md
│       ├── 01_Python_Basics.ipynb
│       ├── 02_Guided_EDA_Practice.ipynb
│       ├── 03_CapL_Project.ipynb
│       └── answer/02_Guided_EDA_Practice_solution.ipynb
├── week2/
├── week3/
├── week4/
├── week5/
├── week6/
└── week7/
```

공통 데이터는 `data`, 공통 코드는 `utils`에서 관리합니다. 주차 폴더에 공통 CSV를 복사하지 않고 같은 파일을 참조합니다.

## 실행 준비

처음 설치하는 교육생은 [00_Pre_Ready 설치 안내](week1/00_Pre_Ready/00_Pre_Ready.ipynb)부터 진행하세요. Python·Anaconda·Jupyter의 역할, Windows/macOS/Linux 설치, 실습 환경 생성, Kernel 선택, 오류 해결을 순서대로 안내합니다. 설치 후 [00_Environment_Check.ipynb](week1/00_Pre_Ready/00_Environment_Check.ipynb)에서 표·CSV·그래프 실행을 확인합니다.

Anaconda 경로에서는 `hynix-eda` 환경을 사용합니다. 아래는 **이미 Python을 사용하는 사람을 위한 venv 경로**입니다. 한 가지 환경 구성 방식을 선택하면 됩니다.

### 기존 Python 사용자의 venv 경로

Python 3.12를 권장합니다. macOS/Linux에서는 프로젝트 디렉터리에서 다음을 실행합니다.

```bash
cd /home/hayeong/dev/hynix-iTAP
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

다른 컴퓨터에서는 `cd` 경로를 프로젝트 위치로 바꾸세요. Windows 명령 프롬프트에서 기존 Python 3.12로 구성한다면 프로젝트 루트에서 `py -3.12 -m venv .venv`, `.venv\Scripts\activate.bat`를 차례대로 실행한 뒤 위의 pip 설치와 `jupyter lab` 명령을 사용합니다. Linux에서 `venv` 생성 시 `ensurepip` 오류가 나면 Python의 venv 지원 패키지가 필요합니다. 현재 작업 환경에는 `.venv`와 라이브러리가 준비되어 있으므로 다음 명령으로 바로 시작할 수 있습니다.

```bash
cd /home/hayeong/dev/hynix-iTAP
.venv/bin/jupyter lab
```

프로젝트 루트에서 JupyterLab을 실행하면 `week1` 안의 `00_Pre_Ready`와 `01_Basic_Background`, 공통 `data`·`utils`를 모두 볼 수 있습니다. VS Code에서는 `.ipynb`를 열고 사용 중인 환경을 Kernel로 선택합니다. Anaconda 경로라면 `Python (hynix-eda)`, 현재 Linux venv라면 `hynix-iTAP/.venv/bin/python`입니다. 각 Notebook은 독립적으로 실행할 수 있으며, **Restart Kernel and Run All Cells**로 위에서부터 실행하세요. Guided Practice의 TODO는 학습자가 직접 채웁니다.

필요한 라이브러리:

- `numpy`, `pandas`: 수치 계산 및 표 데이터 분석
- `matplotlib`: 시각화
- `jupyterlab`, `ipykernel`: Notebook 편집과 실행
- `nbformat`, `nbclient`: Notebook 형식 검사와 전체 실행 검증

설치 범위는 [requirements.txt](requirements.txt)를 참고하세요.

## Week 1 실행 순서와 파일 역할

| 순서 | 파일 | 역할 |
|---|---|---|
| 0 | [00_Pre_Ready](week1/00_Pre_Ready/00_Pre_Ready.ipynb) / [환경 점검 Notebook](week1/00_Pre_Ready/00_Environment_Check.ipynb) | Python·Anaconda·Jupyter 설치부터 첫 Notebook 실행까지 사전 준비 |
| 1 | [01_Python_Basics.ipynb](week1/01_Basic_Background/01_Python_Basics.ipynb) | 문법·NumPy·Pandas·시각화마다 간단한 일상 예제 → 제조 적용 → 직접 연습 |
| 2 | [02_Guided_EDA_Practice.ipynb](week1/01_Basic_Background/02_Guided_EDA_Practice.ipynb) | 기초에서 심화로 이어지는 20문제; 앞 결과를 재사용하며 가설 검토까지 수행; 정답 코드 없음 |
| 해설 | [02_Guided_EDA_Practice_solution.ipynb](week1/01_Basic_Background/answer/02_Guided_EDA_Practice_solution.ipynb) | 모든 문제의 실행 가능한 코드와 관찰·토의 예시 |
| 3 | [03_CapL_Project.ipynb](week1/01_Basic_Background/03_CapL_Project.ipynb) | 실제 데이터에 적용하고 현업 의견을 다음 가설로 연결하는 공동 분석 기록장 |

01·02·해설은 기업에 종속되지 않는 범용 제조 AI 자료입니다. 03만 산학 프로젝트에 특화되어 있습니다.

## 데이터 위치

- 실습 CSV: [data/practice_process_data.csv](data/practice_process_data.csv)
- 변수 정의·결측·단위·생성 원칙: [data/README.md](data/README.md)
- 재현용 생성 코드: [generate_practice_data.py](utils/generate_practice_data.py), seed `923`, 400행 × 8열
- 실제 프로젝트 CSV: 기본 `data/private/capl_process_data.csv`(프로젝트 루트 기준); 

## 교육 진행 방법

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


01에서는 각 주제를 **간단한 예제 → 제조 데이터 예제 → 결과 확인 / 직접 해보기**로 반복합니다. 

02의 질문은 **데이터 이해(Q1–Q3) → 품질·조건 선택(Q4–Q7) → 분포·관계(Q8–Q11) → Context별 비교(Q12–Q15) → 심화·가설 검토(Q16–Q20)** 순서입니다. 

03의 진행 순서는 **Apply → Analyze → Discuss → Domain Knowledge → Improve → Re-Analyze → Next Hypothesis**입니다. 마지막 Next Hypothesis를 다음 회차의 Today's Question으로 이어갑니다. 
