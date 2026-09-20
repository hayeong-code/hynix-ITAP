# 공통 유틸리티

여러 주차에서 공유하는 Python 코드와 데이터 생성 스크립트를 관리합니다.

| 파일 | 역할 |
|---|---|
| [generate_practice_data.py](generate_practice_data.py) | seed 923으로 제조 합성 데이터 400행 × 8열 생성 |

프로젝트 루트에서 활성화한 Python 환경으로 실행합니다.

```bash
python utils/generate_practice_data.py
```

출력 위치는 항상 프로젝트 루트의 `data/practice_process_data.csv`입니다. 실행 폴더에 따라 달라지지 않습니다.
기존 CSV가 있으면 덮어쓰지 않고 종료합니다. 기본 실습에서는 제공된 파일을 그대로 사용하세요.
재생성이 필요하면 기존 CSV를 먼저 별도 보관합니다. `make_practice_data()`는 파일을 쓰지 않고 DataFrame을 반환합니다.

주차에 공통 코드를 복사하지 말고 이 폴더에서 관리합니다. 특정 주차에서만 쓰는 실습 코드는 해당 주차에 둡니다.
[공통 데이터 설명](../data/README.md) · [전체 교육자료](../README.md)
