# Итог запуска услуг в Испании — 27.10.2026

## Краткий статус

Подготовка к продажам завершена настолько, насколько это возможно без входа владельца аккаунтов и его одобрения публикаций. **Реальных заказов пока не получено.** Fiverr Gig, Workana profile и отклики не опубликованы/не отправлены. Общий расход: **0 €**.

## 1. Что готово и проверено

- Испанская страница услуг: https://furlos-dev-portfolio.onrender.com/es/
- Живая демоверсия калькулятора: https://furlos-dev-portfolio.onrender.com/es/demo/
- Галерея подготовленных изображений: https://furlos-dev-portfolio.onrender.com/es/creatives/
- Учебный [CSV-cleaning example](./examples/csv-cleaning-demo/) содержит Python-код, фиктивные входные данные, очищенный CSV, CSV с исключениями и README на английском. Он обозначен как **portfolio sample, not a client project**.
- К карточке «Automatizaciones» на живой испанской странице добавлена ссылка на sample: [открыть сайт](https://furlos-dev-portfolio.onrender.com/es/).
- Тексты Fiverr и Workana, цены, ответы клиентам и промо-черновики сохранены в этой папке комплекта. Fiverr: [FIVERR.md](./FIVERR.md); Workana: [WORKANA.md](./WORKANA.md); каналы продвижения: [FREE_PROMOTION.md](./FREE_PROMOTION.md).

## 2. Проверки

- Python unit-тесты: **5/5 passed**.
- Запуск на sample-файле: **3 clean rows**, **3 rows to review**. В неоднозначной дате программа не угадывает порядок дня/месяца; повторный ID и некорректные значения попадают в исключения.
- Калькулятор в браузере: изменение числа гостей и услуги пересчитало итог; подготовленная ссылка WhatsApp отразила выбор и сумму. **Сообщение не отправлялось.**
- Живая испанская страница загружена после изменения, ссылка на GitHub sample видна.
- GitHub Actions: Spain WhatsApp quote demo smoke и Spain organic pages verification — успешно; Spain kit check — успешно.
- Полные исходники и данные sample сохранены в GitHub: [CSV-cleaning demo](./examples/csv-cleaning-demo/).

## 3. Подходящие открытые заказы

Публичные карточки проверены 27.10.2026. Upwork отклоняет прямое чтение карточек без авторизованной сессии, поэтому наличие бесплатных Connects и фактическую кнопку подачи нужно сверить в аккаунте перед любой заявкой. Не платить за отклик. Workana показывает открытые проекты публично, но бесплатный недельный лимит предложений зависит от аккаунта и профиля.

### A. Workana — Python automation / APIs

- **Ссылка:** https://www.workana.com/es/job/desarrollo-de-automatizaciones-con-python-buscamos-expertos
- **Дата:** 14.10.2026; карточка отмечена **Abierto** 27.10.
- **Бюджет/срок:** не указаны. Python scripts, API integrations, data processing.
- **Клиент:** страна не показана; 1 опубликованный проект, 0 оплаченных; 53 предложения на момент проверки.
- **Ограничения:** отклик после одобрения профиля; бесплатный лимит зависит от Workana Achievement System. Не покупать план.
- **Сложность/совпадение:** средняя, пока не известен объём. Совпадает с Python/API, но бриф расплывчатый и конкуренция высокая.
- **Статус отклика:** **ТРЕБУЕТ ПРОВЕРКИ** — сначала профиль должен быть одобрен, затем проверить бесплатный лимит и уточнить бюджет.
- **Черновик ES:**
  > Hola. Puedo empezar por una tarea concreta en Python: acordar el formato de entrada, las reglas y el resultado esperado, y dejar una primera versión fácil de probar. Para no estimar a ciegas, ¿qué proceso manual queréis automatizar primero y qué presupuesto tenéis para ese primer alcance?

### B. Upwork — CSV upload → Excel output web app

- **Ссылка:** https://www.upwork.com/freelance-jobs/apply/Python-Developer-for-Web-App_~022100427652989633437/
- **Дата:** карточка показывала «Posted 2 days ago».
- **Бюджет/условия:** 15–35 USD/час; worldwide; intermediate; Python, JavaScript, Django; 20–50 предложений, 0 интервью на момент просмотра.
- **Объём:** веб-приложение принимает CSV, обрабатывает и предлагает скачать Excel. Нужно уточнить правила преобразования, размер файлов и разметку результата.
- **Сложность/совпадение:** средняя; хороший матч с CSV-примером и Python/web API.
- **Статус отклика:** **ТРЕБУЕТ ПРОВЕРКИ** — проверить, что карточка всё ещё открыта и аккаунт показывает бесплатные Connects. Ничего не покупать.
- **Черновик EN:**
  > Hi — I’d first map the CSV columns to the expected workbook and route invalid or ambiguous rows for review instead of silently changing them. I have a small Python sample with fictional data showing validation and exception handling; it is a portfolio example, not previous client work. Could you share a redacted input file and the exact Excel output layout?

### C. Upwork — small Python web app returning JSON

- **Ссылка:** https://www.upwork.com/freelance-jobs/apply/Python-Developer-for-Web-App_~022109811564707576944/
- **Дата:** карточка показывала «Posted 8 hours ago».
- **Бюджет/условия:** 15–35 USD/час; worldwide; under 1 month; intermediate; Python; 20–50 предложений, 0 интервью, последнее посещение заказчиком около 8 часов назад.
- **Объём:** веб-приложение принимает данные, формирует JSON и показывает результат в простой UI.
- **Сложность/совпадение:** низкая-средняя; конкретнее и меньше большого CRM/AI проекта.
- **Статус отклика:** **ТРЕБУЕТ ПРОВЕРКИ** — сверить текущий статус и бесплатные Connects в аккаунте.
- **Черновик EN:**
  > Hi — I’d keep the first version focused: validate the submitted fields, return a predictable JSON structure, and show the result and errors clearly in the UI. I can point to related Python/API work in my portfolio without presenting it as commercial client work. What input fields and JSON response shape do you need?

### Отсеянные проекты

- Workana security review из Murcia: открытый заказ, но требует реального опыта веб-безопасности и отчётной проверки; пользователь не подтверждал опыт профессионального аудита. **Не рекомендую выдавать учебный интерес за production-практику.**
- Большой WhatsApp CRM/AI проект: запрашивает официальный WhatsApp Business API, CRM, автоматизацию, календарь и dashboard. Это существенно превосходит проверенный демо-сценарий; не включён в приоритетные отклики.
- Upwork hotel workbook: $30 за около 1 500 записей/48 листов, большой объём за малую фиксированную цену. Исключён из лучших вариантов.
- Другие найденные заявки имели устаревшую дату, нереалистичный объём, неподходящий уровень или сомнительную экономику. Список не дополнен до пяти ради количества.

## 4. Бесплатные действия и ограничения

- **Workana:** создать профиль и отправить его на бесплатную модерацию; предложения доступны после одобрения, но недельный лимит зависит от уровня. Требуются вход и подтверждения пользователя. [Официальная справка о стоимости](https://help.workana.com/hc/es/articles/360040846094--Cu%C3%A1nto-cuesta-usar-Workana).
- **Fiverr:** подготовлен один Gig с ценами в USD, FAQ, требованиями к заказчику и изображениями. До публикации нужны вход и возможные проверки личности от самого пользователя. Страна/личные данные не менялись; объявление не опубликовано.
- **Upwork:** заявки допустимы только если внутри аккаунта есть бесплатные Connects. Не покупать Connects и не подключать план. [Официальные планы](https://www.upwork.com/pricing/freelancer).
- **LinkedIn:** бесплатная Service Page доступна фрилансерам, но аккаунт не авторизован. Черновик поста есть в [FREE_PROMOTION.md](./FREE_PROMOTION.md); публикацию и видимость нужно проверить и подтвердить владельцу. [Справка LinkedIn](https://www.linkedin.com/help/linkedin/answer/a569534).
- **TECH CLUB SPAIN:** бесплатное сообщество, публично указан хэштег #freelance для поиска проектов и предложения услуг; вход может ждать 3–5 рабочих дней. Черновик готов, публикация не размещалась. [Правила сообщества](https://tech-club-spain.com/es/).
- **Reddit:** не размещать рекламу до проверки правил конкретного сообщества; подходящие актуальные правила подтвердить не удалось.
- **Wallapop:** исключён — платформа запрещает цифровой контент и ПО, а допустимость кастомной разработки не подтверждена.
- **Freelancer.es:** не использовать при бюджете 0 €; официальный тариф требует минимум $20 доступного остатка перед ставкой. [Тарифы](https://www.freelancer.es/feesandcharges).

## 5. Публикации, блокировки и следующие действия

**Опубликовано:** испанский сайт, демо, PNG-галерея и GitHub-материалы, включая CSV sample и этот отчёт.

**Не опубликовано:** Fiverr Gig, пост LinkedIn, пост сообщества. Ничего не находится на модерации.

**Не отправлено:** все отклики в этом отчёте — черновики. С клиентами не связывались.

**Заблокировано входом владельца:** Fiverr/Gig publication, Workana profile approval and proposals, Upwork account Connects, LinkedIn/TECH CLUB membership and post approval. Повторно капчи и проверки безопасности не проходились.

### Минимум действий пользователя

1. Войти в Workana, подтвердить профиль и отправить его на бесплатную модерацию.
2. В аккаунте Workana проверить бесплатный лимит и открыть заказ A; решить, отправлять ли подготовленный отклик.
3. Войти в Upwork и проверить, доступны ли бесплатные Connects и активны ли B/C; не пополнять баланс.
4. Войти в Fiverr, проверить готовый Gig и подтвердить публикацию, если всё устраивает.
5. По желанию войти в LinkedIn/TECH CLUB SPAIN, проверить публичную видимость профиля и подтвердить один подготовленный пост.

## Финансовый итог

- Потрачено: **0 €**.
- Платные планы/реклама/депозиты/покупки Connects: **не подключались**.
- Получено оплаченных заказов: **0**.
