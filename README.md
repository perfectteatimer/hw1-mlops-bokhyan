# Kaggle nlp hw1 

## Start

1. Собрать образ:
    docker build -t hw1-mlops-bokhyan .

2. Подготовка папок и test.csv:
   mkdir -p output

3. Запуск:
   docker run --rm \
  -v $PWD/input:/app/input \
  -v $PWD/output:/app/output \
  hw1-mlops-bokhyan


4. Результаты будут в ./output:
   - sample_submission.csv
   - importances.json        (топ-5 фич)
   - scores_density.png      (плотность скоров)

## Детали
- Сервис состоит из скриптов:
  app/load_input.py, app/preprocess.py, app/predict.py, app/save_output.py, app/run.py
- Модель и прочее лежат в ./artifacts (я предобучил их во время дз)
- Трейн датасет я уже подгрузил, тк на нем надо инферить
- Результатам не удивляться, сорева такая :)
