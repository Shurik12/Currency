# Сервис получения котировок валют. 
## Описание работы сервиса:
	На главной странице сервиса пользователь может выбрать одну или несколько валют. По нажатию на кнопку “Получить котировки” (есть возможность выбрать несколько котировок) формируется простая таблица с котировками, содержащая несколько  столбцов:
		- Код валюты
		- Название валюты
		- Цена
		- Дата котировки
		- Номинал 
	Есть возможность выгрузить ответ в одном из следующих форматов: CSV, XLSX, PDF.
## Пояснения реализации:
	1. Сервис реализован в тестовой среде, локальный запуск
	2. Для запуска:
		- перейти в папку currency
		- активировать виртуальное окружение $ source django_env/bin/activate
		- запустить приложение $ python3 manage.py runserver

## Следующие шаги:
	1. Форма авторизации
	2. Добавление бд (сейчас прикручен лайт вариант sql lite)
	3. Кэширование котировок, так как обновляются раз в сутки
	4. Тестирование (сейчас в приложении есть только шаблон)
	5. Продакшн версия
	6. Маштабирование возможностей
	7. Переход на js framework React.