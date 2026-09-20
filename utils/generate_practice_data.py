"""교육용 합성 CSV 생성"""
from pathlib import Path

import numpy as np
import pandas as pd


SEED = 923
ROW_COUNT = 400
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "practice_process_data.csv"


def make_practice_data():
    rng = np.random.default_rng(SEED)
    product = rng.choice(["P_A", "P_B", "P_C"], ROW_COUNT, p=[0.45, 0.35, 0.20])
    equipment = rng.choice(["EQ_A", "EQ_B", "EQ_C"], ROW_COUNT)
    recipe = rng.choice(["R1", "R2"], ROW_COUNT, p=[0.60, 0.40])
    temperature = rng.normal(430, 4, ROW_COUNT) + (recipe == "R2") * 6
    process_time = rng.normal(60, 5, ROW_COUNT) + (product == "P_C") * 5
    sensor_a = 50 + 0.65 * (temperature - 430) + rng.normal(0, 2, ROW_COUNT)
    sensor_b = 20 + (equipment == "EQ_C") * 3 + rng.normal(0, 1.5, ROW_COUNT)
    quality = (
        100 + 0.7 * (sensor_a - 50) + 0.12 * (process_time - 60)
        + (product == "P_B") * 4 - (product == "P_C") * 3
        + (equipment == "EQ_B") * 3
        + ((equipment == "EQ_C") & (recipe == "R2")) * 5
        + rng.normal(0, 2, ROW_COUNT)
    )
    data = pd.DataFrame({
        "PRODUCT": product, "EQUIPMENT": equipment, "RECIPE": recipe,
        "PROCESS_TEMP": temperature, "PROCESS_TIME": process_time,
        "SENSOR_A": sensor_a, "SENSOR_B": sensor_b, "QUALITY_VALUE": quality,
    })
    for column, count in {"PROCESS_TEMP": 8, "SENSOR_A": 10, "SENSOR_B": 6,
                          "QUALITY_VALUE": 5}.items():
        data.loc[rng.choice(ROW_COUNT, count, replace=False), column] = np.nan
    temp_rows = rng.choice(data.index[data["PROCESS_TEMP"].notna()], 3, replace=False)
    quality_rows = rng.choice(data.index[data["QUALITY_VALUE"].notna()], 4, replace=False)
    data.loc[temp_rows, "PROCESS_TEMP"] += 40
    data.loc[quality_rows, "QUALITY_VALUE"] += np.array([25, 30, -25, -30])
    return data.round(3)


if __name__ == "__main__":
    if OUTPUT.exists():
        raise SystemExit("기존 CSV를 보존합니다. 재생성이 필요하면 먼저 별도 보관하세요.")
    make_practice_data().to_csv(OUTPUT, index=False)
    print(f"생성 완료: {OUTPUT} ({ROW_COUNT} rows, seed={SEED})")
