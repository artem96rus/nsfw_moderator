# NSFW Image Moderator API

Простое FastAPI-приложение, которое принимает изображение (`.jpg` или `.png`) и проверяет его на наличие неприемлемого контента (NSFW) с помощью модели [`Falconsai/nsfw_image_detection`](https://huggingface.co/Falconsai/nsfw_image_detection), доступной через Hugging Face Inference API.

---

## Возможности

- Принимает изображение через `POST /moderate`
- Отправляет изображение в Hugging Face API
- Возвращает `{"status": "OK"}` — если изображение безопасно
- Возвращает `{"status": "REJECTED", "reason": "NSFW content"}` — если обнаружен NSFW-контент (`nsfw_score > 0.7`)

---

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-username/nsfw_moderator.git
cd nsfw_moderator
```

### 2. Создайте и активируй виртуальное окружение

python3 -m venv venv
source venv/bin/activate        # для macOS/Linux
venv\Scripts\activate           # для Windows

### 3. Установите зависимости

pip install -r requirements.txt


### 4. Получи Hugging Face Token
- Зарегистрируйся на https://huggingface.co
- Перейди в настройки токена
- Создай токен с правами “Read”
- Скопируй его

### 5.Создайте файл .env на основе моего .env
- cp .env.example .env
- Заполните его: HUGGINGFACE_API_KEY=hf_...

### 6. Запустите сервер:
```bash
uvicorn main:app --reload

### 7. Пример запроса:
```bash
curl -X POST -F "file=@/Users/artemzakharov/Desktop/dick.jpg" http://localhost:8000/moderate


### 8. Пример ответа:
```bash
{"status":"REJECTED","reason":"NSFW content"}% 
