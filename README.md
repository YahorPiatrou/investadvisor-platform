# InvestAdvisor Platform  
**Интеллектуальная система рекомендаций инвестиционных портфелей**

### Краткое описание проекта
SaaS-платформа с элементами robo-advisory, предназначенная для начинающих и среднеопытных инвесторов. Система формирует персонализированные инвестиционные портфели на основе:
- адаптивного опроса (риск-профиль, сектора интереса, горизонт инвестирования),
- автоматического считывания криптокошельков через публичные блокчейн-обозреватели (Etherscan, Tonviewer и др.),
- ручного импорта брокерских счетов,
- коллаборативной фильтрации (сравнение с портфелями более опытных пользователей),
- LSTM-моделей прогнозирования доходности и анализа волатильности.

Монетизация — реферальные комиссии 0,5–2 % от транзакций через интеграции с Binance, Bybit, Tinkoff Investments, Interactive Brokers и др.  
Целевая аудитория: Россия/СНГ + глобальный рынок (прогноз — 200 000 активных пользователей к Q2 2027).

**Текущий статус:** Проект находится в разработке.

### Техническое задание
Полное ТЗ (Лабораторная работа №2) доступно по ссылке:  
[Техническое_задание](docs/ЛР2_ТЗ.pdf)

### Технологический стек
| Слой              | Технологии                                      |
|-------------------|--------------------------------------------------|
| Backend           | Python 3.11, FastAPI, Uvicorn                    |
| ML / Аналитика    | PyTorch / TensorFlow, scikit-learn               |
| Frontend (Web)    | React 18 + TypeScript + Vite + TailwindCSS       |
| Mobile            | React Native (Expo) — заготовка                  |
| База данных       | PostgreSQL 16                                    |
| Кэш / очереди     | Redis                                            |
| Инфраструктура    | Docker + Docker Compose, GitHub Actions (CI/CD)  |
| Документация API  | OpenAPI (Swagger UI)                             |

### Сборка и запуск проекта

#### Вариант 1 — через Docker Compose
```bash
git clone https://github.com/<ваш-username>/investadvisor-platform.git
cd investadvisor-platform

# Запуск БД, Redis и бэкенда
docker-compose up --build -d

# Frontend (в отдельном терминале)
cd frontend/web
npm install
npm run dev
```

#### Вариант 2 — локально без Docker
```bash
git clone https://github.com/<ваш-username>/investadvisor-platform.git
cd investadvisor-platform

# Backend
cd backend
python -m venv venv && source venv/bin/activate  # Linux/Mac
# или venv\Scripts\activate                     # Windows
pip install -r requirements.txt
uvicorn main:app --reload --port=8000

# Frontend (в отдельном терминале)
cd frontend/web
npm install
npm run dev
```
