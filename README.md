<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Flynotfly/GymStat">
    <img src="images/logo.png" alt="Logo" width="340" height="80">
  </a>

  <h3 align="center">Educa</h3>

  <p align="center">
    Веб-приложение для онлайн курсов.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Содержание</summary>
  <ol>
    <li>
      <a href="#описание-проекта">Описание проекта</a>
      <ul>
        <li><a href="#использованные-технологии">Использованные технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#использование">Использование</a>
      <ul>
        <li><a href="#сборка-и-запуск-проекта">Сборка и запуск проекта</a></li>
        <li><a href="#локальный-запуск-и-разработка">Локальный запуск и разработка</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#контакты">Контакты</a></li>
  </ol>
</details>



## Описание проекта

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Проект представляет собой веб-приложение, которое позволяет записывать результаты тренировок, вести аналитику и ставить личные цели.

Особенности приложения:
* Возможность добавления собственных упражнений
* Автоматизированное заполнение результатов тренировок с помощью шаблонов
* Возможность анализировать результаты отдельно взятых приложений

<p align="right">(<a href="#readme-top">Вверх</a>)</p>



### Использованные технологии
* [![Python][Python-shield]][Python-url]
* [![Django][Django-shield]][Django-url]
* [![Django REST Framework][DRF-shield]][DRF-url]
* [![TypeScript][TypeScript-shield]][TypeScript-url]
* [![React][React-shield]][React-url]
* [![MUI][MUI-shield]][MUI-url]
* [![PostgreSQL][PostgreSQL-shield]][PostgreSQL-url]
* [![Redis][Redis-shield]][Redis-url]
* [![Nginx][Nginx-shield]][Nginx-url]
* [![Docker][Docker-shield]][Docker-url]
* [![GitHub Actions][GitHub-Actions-shield]][GitHub-Actions-url]

<p align="right">(<a href="#readme-top">Вверх</a>)</p>


## Использование

Воспользоваться сайтом можно по URL [system.orange-city.ru](https://system.orange-city.ru/)

### Сборка и запуск проекта

Для сборки проекта и его последующего автоматического запуска на сервере необходимо активировать workflow "Deploy to production" в GitHub Actions. Предварительно необходимо добавить следующие GitHub Actions secrets, если они отсутвуют:
* SERVER_HOST
* SERVER_USER
* SSH_PRIVATE_KEY
* DOCKERHUB_USERNAME
* DOCKERHUB_TOKEN
* DJANGO_SECRET_KEY
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD
* DEFAULT_FROM_EMAIL

На сервере должен быть установлен Docker и получен HTTPS сертификат.

### Локальный запуск и разработка

Алгоритм запуска представлен для машины с ОС Windows 11

1. Установить git, docker, npm 11 и python 3.12.
 
2. Создать и активировать виртуальное окружение python.
```
py -m venv GymStats
cd GymStats
Scripts\activate
```

3. Склонировать репозиторий.
```
git clone https://github.com/Flynotfly/GymStats.git
```

4. Перейти в директорию проекта.
```
cd gymstats
```

5. Перейти в директорию Django проекта.
```
cd gymstat
```

6. Установить зависимости.
```
pip install -r requirements_dev.txt
```

7. Создать файл .env со следующими переменными окружения:
* POSTGRES_DB
* POSTGRES_USER
* POSTGRES_PASSWORD
* EMAIL_HOST_USER
* EMAIL_HOST_PASSWORD
* DEFAULT_FROM_EMAIL
* DJANGO_SECRET_KEY

8. Запустить базу данных.
```
docker-compose -f local_postgres/docker-compose.yml --env-file .env up -d
```

9. Запустить проект.
```
py manage.py runserver_plus localhost:8000 --cert ssl/gymstat.crt --settings gymstat.settings.local 
```

10. Для запуска фронтенда необходимо перейти в директорию "frontend", установить npm и запустить проект в режиме разработчика.
```
cd ..
cd frontend
npm install
npm run dev
```

<p align="right">(<a href="#readme-top">Вверх</a>)</p>

## Roadmap

- [x] Добавить шаблоны тренировок
- [x] Добавить шаблоны упражнений
- [ ] Добавить автоматическое заполнение тренировок
- [ ] Добавить определение результатов тренировок с фото
- [ ] Добавить кэширование запросов
- [ ] Добавить возможность переключения языка

<p align="right">(<a href="#readme-top">Вверх</a>)</p>


## Контакты

alteria001@gmail.com

tg: @flynotfly

Ссылка на проект: https://github.com/Flynotfly/GymStats

<p align="right">(<a href="#readme-top">Вверх</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.jpg

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Django-shield]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[DRF-shield]: https://img.shields.io/badge/Django%20REST%20Framework-A30000?style=for-the-badge&logo=django&logoColor=white
[TypeScript-shield]: https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white
[React-shield]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[MUI-shield]: https://img.shields.io/badge/MUI-007FFF?style=for-the-badge&logo=mui&logoColor=white
[PostgreSQL-shield]: https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white
[Redis-shield]: https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white
[Nginx-shield]: https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white
[Docker-shield]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[GitHub-Actions-shield]: https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white

[Python-url]: https://www.python.org/
[Django-url]: https://www.djangoproject.com/
[DRF-url]: https://www.django-rest-framework.org/
[TypeScript-url]: https://www.typescriptlang.org/
[React-url]: https://reactjs.org/
[MUI-url]: https://mui.com/
[PostgreSQL-url]: https://www.postgresql.org/
[Redis-url]: https://redis.io/
[Nginx-url]: https://nginx.org/
[Docker-url]: https://www.docker.com/
[GitHub-Actions-url]: https://github.com/features/actions
