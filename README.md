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

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/nsfw_moderator.git
cd nsfw_moderator


