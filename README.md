## Задача 3:
Используя проект с открытым исходным кодом https://github.com/mozilla/DeepSpeech
1) выполнить тренировку собственной модели использую предоставленный датасет
2) получить результаты распознавания обученной модели по dev, test и train частям dataset

Результатом выполнения задачи будет:
1) файл весов обученной модели
2) текстовые файлы с результатами распознавания

Если Вы выберете эту задачу, обратитесь к нам за датасетом.

## Замечания.
1) настроил python окружение
2) с помощью программы создал csv файлы
2.1) создал alphabet.txt для кирилицы
3) "перегнал" wav-данные в 16000 sample rate
4) запустил deepspeech:

$ python DeepSpeech.py --n_hidden 2048 --epochs 3 --dev_files ../Dataset/dev/dev.csv --test_files ../Dataset/test/test.csv --train_files ../Dataset/train/train.csv --learning_rate 0.0001 --export_dir output_models/ --checkpoint_dir chckpt

результаты см. training.log