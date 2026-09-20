# 공통 데이터 · 실습 데이터 설명

`practice_process_data.csv`는 제조 공정을 모사한 **교육용 합성 데이터**입니다. 실제 회사 데이터, 실제 CapL 값, 실제 공정의 물리식이나 품질 규격은 포함하지 않습니다.

- 크기: 400행 × 8열
- 한 행: 가상의 공정 관측 1건. 실제 wafer/lot 또는 시계열을 뜻하지 않습니다.
- 형식: UTF-8 CSV, 쉼표 구분, 첫 행은 열 이름, index 없음
- 생성: NumPy `default_rng(923)`; 수치는 소수 셋째 자리까지 저장
- 결측: CSV의 빈 칸이며 Pandas가 결측값으로 읽습니다.

| 열 | 의미 | 자료형 / 예시 | 단위 |
|---|---|---|---|
| PRODUCT | 가상 제품 | 범주: P_A, P_B, P_C | 없음 |
| EQUIPMENT | 가상 장비 | 범주: EQ_A, EQ_B, EQ_C | 없음 |
| RECIPE | 가상 공정 조건 | 범주: R1, R2 | 없음 |
| PROCESS_TEMP | 가상 공정 온도 | 수치 | 실습용 °C |
| PROCESS_TIME | 가상 공정 시간 | 수치 | 실습용 초 |
| SENSOR_A | 가상 센서 A | 수치 | 임의 단위(a.u.) |
| SENSOR_B | 가상 센서 B | 수치 | 임의 단위(a.u.) |
| QUALITY_VALUE | 가상 품질 측정값 | 수치 | 임의 단위(a.u.) |

## 의도적으로 포함한 데이터 품질 문제

PROCESS_TEMP 8개, SENSOR_A 10개, SENSOR_B 6개, QUALITY_VALUE 5개에 결측을 넣었습니다. 열별 위치는 독립적으로 선택하므로 결측이 있는 **행 수**와 결측 **셀 수**의 합은 다를 수 있습니다. 범주형 열과 PROCESS_TIME에는 결측을 넣지 않았습니다.

결측 위치를 피해서 PROCESS_TEMP 3행에 +40, QUALITY_VALUE 4행에 각각 +25, +30, −25, −30을 적용했습니다. 이는 의도적으로 주입한 극단값의 수입니다. Boxplot 수염 밖 점의 수와 같다는 뜻은 아닙니다. 이상치 후보를 발견해도 곧바로 삭제하지 않고 원인을 확인하는 연습을 합니다.

그룹별 비교와 질문 생성이 가능하도록 Product 효과, Equipment 효과, Equipment × Recipe 조합 효과 및 SENSOR_A와 QUALITY_VALUE의 관계를 임의로 설계했습니다. 제품·장비·Recipe 구성, 표본 수, 산포를 함께 확인하세요. 설계된 관계를 실제 공정의 원인 또는 예측 성능으로 해석해서는 안 됩니다.

## 재현

기본 실습에서는 제공된 CSV를 그대로 사용합니다. 생성 코드는 [`generate_practice_data.py`](../utils/generate_practice_data.py)이며 같은 seed와 라이브러리 환경에서 같은 값을 재현합니다.

```bash
# 프로젝트 루트에서 실행합니다. 기존 CSV가 있으면 덮어쓰지 않고 종료합니다.
.venv/bin/python utils/generate_practice_data.py
```

재생성이 필요하면 기존 CSV를 별도 보관한 뒤 실행하세요. 원본 DataFrame은 보존하고 결측은 해당 그림이나 집계에서 어떻게 제외되는지 확인합니다.

## 실제 프로젝트 데이터

실제 데이터는 이 CSV와 별개입니다. Week 1의 03에서 프로젝트 루트를 기준으로 읽는 위치는 `data/private/capl_process_data.csv`이며 해당 폴더는 `.gitignore`에 등록되어 있습니다. 파일이 없으면 분석을 생략합니다. 실제 CSV를 읽은 Notebook 출력에도 원본 값이 포함될 수 있으므로 공유 시 출력 내용을 확인하세요.
