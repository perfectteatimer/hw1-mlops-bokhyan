# HW1-MLOPS-BOKHYAN

```
HW1-MLOPS-BOKHYAN
├── app
│   ├── load_input.py
│   ├── preprocess.py
│   ├── predict.py
│   ├── save_output.py
│   ├── run.py
│   └── utils.py
├── artifacts
│   └── catboost_model.cbm     
├── input                      # монтируется как /app/input
├── output                     # монтируется как /app/output
├── work                       # промежуточные файлы внутри контейнера
├── Dockerfile
├── requirements.txt
└── README.md
```

## Что делает сервис
- load_input → preprocess → predict → save_output
- читает `./input/test.csv` который создается перед запуском (нужно будет положить туда датасет)
- препроцессинг: `transaction_time` → `hour/dayofweek/month`, дальше удаляет исходную дату
- инференс катбуста (`artifacts/catboost_model.cbm`)
- сохраняет:
  - `./output/sample_submission.csv` (колонки: `row_id`, `target`)
  - `./output/feature_importances_top5.json`
  - `./output/score_density.png`

## Как запустить
```bash
mkdir -p input output
cp /путь/к/test.csv ./input/test.csv
docker build -t hw1-mlops-bokhyan .
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  hw1-mlops-bokhyan
```

## Заметки
- Не забудьте положить test.csv








