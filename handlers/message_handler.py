from aiogram import types
from aiogram.filters import CommandStart
from openai_module.gpt_service import generate_response
from knowledge_base.rag_service import get_context_for_query
from config import PRODUCT_BOT_USERNAME, LANDING_PAGE_URL, PROJECT_NAME

# Load the knowledge base content once
KB_CONTENT = get_context_for_query("")

async def start_command_handler(message: types.Message):
    """
    Handles the /start command.
    Implements the required warm greeting, project description,
    benefit explanation, links, and invitation to describe the problem.
    """
    welcome_message = f"""
👋 Привет! Я — твой дружелюбный ИИ-консультант проекта «{PROJECT_NAME}»!

Мы создали научные методики, которые помогают людям самостоятельно проработать более 100 психологических проблем. Думай обо мне как о «Психологе прямо в твоем телефоне» — доступно, анонимно и всего за 250 рублей (цена кружки кофе!).

Моя польза:
✨ Я объясню суть нашего проекта.
✨ Помогу подобрать проработку для твоей проблемы.
✨ Отвечу на любые вопросы о психологии, тревогах и страхах, используя только проверенные научные данные.
✨ Мягко мотивирую тебя начать путь к улучшению своей жизни.

Готов начать?
➡️ Продукт-бот: {PRODUCT_BOT_USERNAME}
➡️ Лэндинг: {LANDING_PAGE_URL}

Чтобы начать, просто опиши свою проблему, вопрос или то, что тебя беспокоит. Я здесь, чтобы помочь!
"""
    await message.answer(welcome_message)

async def text_message_handler(message: types.Message):
    """
    Handles all incoming text messages.
    Implements the RAG-logic and sales-oriented response generation.
    """
    user_query = message.text

    # 1. Анализ вопроса (Implicit in LLM prompt)
    # 2. Поиск нужной информации в базе знаний (RAG-logic)
    # 3. Формирование контекста (KB_CONTENT is the context)
    # 4. Отправка запроса в GPT и 5. Создание красивого живого ответа
    response_text = generate_response(user_query, KB_CONTENT)

    # 6. Предложение перейти в @Digita1_Psychology_Bot (Implicit in GPT response via system prompt)
    await message.answer(response_text)
