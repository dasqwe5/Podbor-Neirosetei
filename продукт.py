import tkinter as tk
from tkinter import ttk, messagebox
import math

# ================= БАЗА ДАННЫХ МОДЕЛЕЙ 2026 =================

MODELS_DB = [

    # === Флагманы США ===
    {
        "name": "GPT-5.4 Pro", "provider": "OpenAI",
        "tasks": ["text", "code", "analysis", "math", "multimodal", "reasoning", "agents"],
        "budget_tier": "premium", "long_context": True, "multimodal": True,
        "speed_tier": "medium", "quality_score": 96, "speed_score": 68,
        "cost_per_m_out": 18.0,
        "description": "Флагман OpenAI. Максимальное качество для любых задач: кодинг, наука, аналитика, мультимодальность."
    },
    {
        "name": "Claude Opus 4.6", "provider": "Anthropic",
        "tasks": ["text", "code", "analysis", "multimodal", "long_context"],
        "budget_tier": "premium", "long_context": True, "multimodal": True,
        "speed_tier": "medium", "quality_score": 95, "speed_score": 65,
        "cost_per_m_out": 25.0,
        "description": "Король длинного контекста и юридических медицинских текстов. Лучший для RAG и работы с документами."
    },
    {
        "name": "Gemini 2.5 Pro", "provider": "Google",
        "tasks": ["text", "analysis", "multimodal", "code", "video"],
        "budget_tier": "balanced", "long_context": True, "multimodal": True,
        "speed_tier": "fast", "quality_score": 89, "speed_score": 84,
        "cost_per_m_out": 10.0,
        "description": "Идеальный баланс цена качество. Лучшая мультимодальность видео аудио. Отлично интегрируется с Google Cloud."
    },
    {
        "name": "Grok 3.5", "provider": "xAI",
        "tasks": ["text", "code", "analysis", "real_time"],
        "budget_tier": "balanced", "long_context": True, "multimodal": False,
        "speed_tier": "fast", "quality_score": 87, "speed_score": 88,
        "cost_per_m_out": 8.0,
        "description": "Модель Илона Маска с доступом к реальным данным X Twitter. Отлична для новостей, финансового анализа и трендов."
    },

    # === Российские модели ===
    {
        "name": "Шедеврум 4.0", "provider": "Яндекс",
        "tasks": ["text", "code", "multimodal", "image_gen"],
        "budget_tier": "balanced", "long_context": True, "multimodal": True,
        "speed_tier": "fast", "quality_score": 86, "speed_score": 85,
        "cost_per_m_out": 3.0,
        "description": "Флагманская нейросеть Яндекса. Отлично понимает русский язык, культуру и менталитет. Генерация и анализ изображений."
    },
    {
        "name": "GigaChat Pro", "provider": "Сбер",
        "tasks": ["text", "code", "analysis", "business"],
        "budget_tier": "balanced", "long_context": True, "multimodal": True,
        "speed_tier": "medium", "quality_score": 84, "speed_score": 72,
        "cost_per_m_out": 4.0,
        "description": "Корпоративная модель Сбера. Соответствует 152-ФЗ, безопасна для бизнеса. Хороша для деловой переписки и документов."
    },
    {
        "name": "YandexGPT 5", "provider": "Яндекс",
        "tasks": ["text", "chat", "fast_response"],
        "budget_tier": "budget", "long_context": False, "multimodal": False,
        "speed_tier": "fast", "quality_score": 78, "speed_score": 90,
        "cost_per_m_out": 0.50,
        "description": "Быстрая и дешёвая модель для массовых задач: чат-боты, колл-центры, классификация. Отличное знание русского."
    },

    # === Китайские модели ===
    {
        "name": "Qwen 2.5 Max", "provider": "Alibaba",
        "tasks": ["text", "code", "analysis", "multimodal", "long_context"],
        "budget_tier": "balanced", "long_context": True, "multimodal": True,
        "speed_tier": "fast", "quality_score": 90, "speed_score": 82,
        "cost_per_m_out": 6.0,
        "description": "Китайский лидер. Огромный контекст 1M токенов. Суперэффективна для анализа кодобаз и длинных документов."
    },
    {
        "name": "DeepSeek R1", "provider": "DeepSeek",
        "tasks": ["text", "code", "math", "reasoning", "science"],
        "budget_tier": "balanced", "long_context": False, "multimodal": False,
        "speed_tier": "slow", "quality_score": 92, "speed_score": 48,
        "cost_per_m_out": 2.19,
        "description": "Модель с усиленным reasoning Chain of Thought. Мировой лидер в математике и сложной логике."
    },
    {
        "name": "Z.ai GLM-5", "provider": "Zhipu AI",
        "tasks": ["text", "code", "analysis", "long_context"],
        "budget_tier": "budget", "long_context": True, "multimodal": True,
        "speed_tier": "fast", "quality_score": 82, "speed_score": 86,
        "cost_per_m_out": 1.20,
        "description": "Отличная китайская модель с поддержкой длинного контекста 200K. Дешёвая и быстрая."
    },
    {
        "name": "Yi 34B Chat", "provider": "01.AI",
        "tasks": ["text", "code", "local_deployment"],
        "budget_tier": "budget", "long_context": True, "multimodal": False,
        "speed_tier": "fast", "quality_score": 80, "speed_score": 88,
        "cost_per_m_out": 0.80,
        "description": "Открытая модель Apache 2.0. Лучшая среди Open Source 34B. Можно запустить локально."
    },
    {
        "name": "StepFun Step-2", "provider": "StepFun",
        "tasks": ["text", "analysis", "multimodal", "math"],
        "budget_tier": "balanced", "long_context": True, "multimodal": True,
        "speed_tier": "medium", "quality_score": 85, "speed_score": 70,
        "cost_per_m_out": 5.0,
        "description": "Новый китайский игрок. Сильная мультимодальность и математика."
    },

    # === Open Source Европа ===
    {
        "name": "Llama 4 Maverick", "provider": "Meta",
        "tasks": ["text", "code", "multimodal", "local_deployment"],
        "budget_tier": "budget", "long_context": True, "multimodal": True,
        "speed_tier": "fast", "quality_score": 85, "speed_score": 80,
        "cost_per_m_out": 0.60,
        "description": "Лучшая открытая модель. Контекст 10M токенов. Идеальна для локального запуска."
    },
    {
        "name": "Mistral Large 3", "provider": "Mistral AI",
        "tasks": ["text", "code", "multimodal", "agents"],
        "budget_tier": "balanced", "long_context": False, "multimodal": True,
        "speed_tier": "fast", "quality_score": 87, "speed_score": 91,
        "cost_per_m_out": 1.50,
        "description": "Европейский чемпион. Очень быстрая и точная. Оптимальна для агентов."
    },
    {
        "name": "Command R+", "provider": "Cohere",
        "tasks": ["text", "analysis", "rag", "search"],
        "budget_tier": "balanced", "long_context": True, "multimodal": False,
        "speed_tier": "medium", "quality_score": 83, "speed_score": 70,
        "cost_per_m_out": 12.0,
        "description": "Специализируется на RAG и поиске. Лучший выбор для корпоративных баз знаний."
    },

    # === Бюджетные и быстрые ===
    {
        "name": "GPT-5 Nano", "provider": "OpenAI",
        "tasks": ["text", "chat", "fast_response"],
        "budget_tier": "budget", "long_context": False, "multimodal": False,
        "speed_tier": "critical", "quality_score": 62, "speed_score": 98,
        "cost_per_m_out": 0.40,
        "description": "Сверхбыстрая и дешёвая. Для чат-ботов, классификации, извлечения сущностей."
    },
    {
        "name": "Claude Haiku 4.5", "provider": "Anthropic",
        "tasks": ["text", "code", "multimodal", "fast_response"],
        "budget_tier": "budget", "long_context": True, "multimodal": True,
        "speed_tier": "critical", "quality_score": 81, "speed_score": 96,
        "cost_per_m_out": 5.0,
        "description": "Самая быстрая модель Anthropic. Мгновенный отклик при высоком качестве."
    },
    {
        "name": "Gemini 2.5 Flash", "provider": "Google",
        "tasks": ["text", "chat", "multimodal", "fast_response"],
        "budget_tier": "budget", "long_context": True, "multimodal": True,
        "speed_tier": "critical", "quality_score": 75, "speed_score": 95,
        "cost_per_m_out": 1.50,
        "description": "Бюджетная молниеносная модель от Google. Длинный контекст и мультимодальность."
    },
    {
        "name": "Phi-4 Mini", "provider": "Microsoft",
        "tasks": ["text", "code", "edge_device"],
        "budget_tier": "budget", "long_context": False, "multimodal": False,
        "speed_tier": "critical", "quality_score": 70, "speed_score": 92,
        "cost_per_m_out": 0.25,
        "description": "Мини-модель от Microsoft. Идеальна для edge-устройств и браузера."
    }
]


class ModernButton(tk.Canvas):
    def __init__(self, parent, text, command, **kwargs):
        self.parent = parent
        self.text = text
        self.command = command
        self.bg_color = kwargs.get('bg', '#2563eb')
        self.hover_color = kwargs.get('hover', '#1d4ed8')
        super().__init__(parent, height=38, width=220, highlightthickness=0, bg=parent['bg'])
        self.create_rounded_rect(0, 0, 220, 38, 19, fill=self.bg_color, tags="rect")
        self.create_text(110, 19, text=text, fill='#ffffff', font=("Segoe UI", 10, "bold"), tags="text")
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = []
        for x, y in [(x1 + radius, y1), (x2 - radius, y1), (x2, y1),
                     (x2, y1 + radius), (x2, y2 - radius), (x2, y2),
                     (x2 - radius, y2), (x1 + radius, y2), (x1, y2),
                     (x1, y2 - radius), (x1, y1 + radius), (x1, y1)]:
            points.extend([x, y])
        return self.create_polygon(points, **kwargs, smooth=True)

    def on_enter(self, e):
        self.delete("rect")
        self.create_rounded_rect(0, 0, 220, 38, 19, fill=self.hover_color, tags="rect")
        self.tag_raise("text")

    def on_leave(self, e):
        self.delete("rect")
        self.create_rounded_rect(0, 0, 220, 38, 19, fill=self.bg_color, tags="rect")
        self.tag_raise("text")

    def on_click(self, e):
        if self.command:
            self.command()


class AIModelSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ ПОДБОР НЕЙРОСЕТЕЙ 2026")
        self.root.geometry("1350x800")
        self.root.minsize(1300, 780)

        self.root.configure(bg="#f3f4f6")
        self._build_ui()

    def _build_ui(self):
        main_frame = tk.Frame(self.root, bg="#f3f4f6")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        header_frame = tk.Frame(main_frame, bg="#f3f4f6")
        header_frame.pack(fill=tk.X, pady=(0, 10))

        self.title_label = tk.Label(header_frame, text="✦ ПОДБОР НЕЙРОСЕТЕЙ 2026 ✦",
                                    font=("Segoe UI", 16, "bold"), bg="#f3f4f6", fg="#1e40af")
        self.title_label.pack()
        tk.Label(header_frame, text="Интеллектуальный подбор нейросетей нового поколения",
                 font=("Segoe UI", 8), bg="#f3f4f6", fg="#6b7280").pack(pady=(2, 0))

        columns_frame = tk.Frame(main_frame, bg="#f3f4f6")
        columns_frame.pack(fill=tk.BOTH, expand=True)

        # Левая панель
        self.left_frame = tk.Frame(columns_frame, bg="#ffffff", relief="flat", bd=0)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 6))
        self._create_shadow_frame(self.left_frame)

        # Правая панель
        self.right_frame = tk.Frame(columns_frame, bg="#ffffff", relief="flat", bd=0)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(6, 0))
        self._create_shadow_frame(self.right_frame)

        self._setup_left_panel()
        self._setup_right_panel()

    def _create_shadow_frame(self, frame):
        border = tk.Frame(frame, bg="#e5e7eb", bd=0)
        border.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        inner = tk.Frame(border, bg="#ffffff")
        inner.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        frame.inner_frame = inner
        frame.border_frame = border

    def _setup_left_panel(self):
        content = self.left_frame.inner_frame

        # Заголовок
        tk.Label(content, text="📌 ПАРАМЕТРЫ ПОИСКА", font=("Segoe UI", 11, "bold"),
                 bg="#ffffff", fg="#1e40af").pack(pady=(10, 10))

        # === ТИП ЗАДАЧИ в 3 колонки ===
        task_frame = tk.LabelFrame(content, text=" ТИП ЗАДАЧИ выбирайте несколько ",
                                   font=("Segoe UI", 9, "bold"),
                                   bg="#ffffff", fg="#374151", padx=10, pady=8)
        task_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 8))

        self.task_vars = {}

        # 3 колонки для чекбоксов
        cols_frame = tk.Frame(task_frame, bg="#ffffff")
        cols_frame.pack(fill=tk.BOTH, expand=True)

        col1 = tk.Frame(cols_frame, bg="#ffffff")
        col2 = tk.Frame(cols_frame, bg="#ffffff")
        col3 = tk.Frame(cols_frame, bg="#ffffff")
        col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        col3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        tasks_list = [
            ("📝 Текст и диалог", "text"),
            ("💻 Программирование", "code"),
            ("🔬 Математика", "math"),
            ("📊 Анализ данных", "analysis"),
            ("🖼️ Мультимодальный", "multimodal"),
            ("🧠 Reasoning", "reasoning"),
            ("🤖 Агенты", "agents"),
            ("📚 Длинный контекст", "long_context"),
            ("🎬 Работа с видео", "video"),
            ("🎨 Генерация изображений", "image_gen"),
            ("⚡ Быстрые ответы", "fast_response"),
            ("💾 Локальный запуск", "local_deployment"),
            ("🔍 Поиск и RAG", "rag"),
            ("🏢 Бизнес", "business"),
            ("🔬 Наука", "science"),
            ("💬 Чат-боты", "chat"),
            ("🌐 Реальные данные", "real_time"),
            ("📄 Документы", "document"),
            ("🔧 Edge устройства", "edge_device"),
        ]

        # Распределяем по 3 колонкам
        for i, (text, value) in enumerate(tasks_list):
            var = tk.BooleanVar()
            self.task_vars[value] = var

            col = col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3
            cb = tk.Checkbutton(col, text=text, variable=var, bg="#ffffff", fg="#374151",
                                selectcolor="#ffffff", activebackground="#ffffff",
                                font=("Segoe UI", 8), anchor="w")
            cb.pack(anchor=tk.W, pady=2)

        # === БЮДЖЕТ в строку ===
        budget_frame = tk.LabelFrame(content, text=" БЮДЖЕТ ", font=("Segoe UI", 9, "bold"),
                                     bg="#ffffff", fg="#374151", padx=10, pady=6)
        budget_frame.pack(fill=tk.X, padx=12, pady=(0, 8))

        self.budget_var = tk.StringVar(value="premium")

        budget_row = tk.Frame(budget_frame, bg="#ffffff")
        budget_row.pack()

        budgets = [
            ("💎 Максимальное качество", "premium"),
            ("⚖️ Баланс цены и качества", "balanced"),
            ("💰 Экономный", "budget"),
        ]

        for text, value in budgets:
            rb = tk.Radiobutton(budget_row, text=text, variable=self.budget_var, value=value,
                                bg="#ffffff", fg="#374151", selectcolor="#ffffff",
                                activebackground="#ffffff", font=("Segoe UI", 8))
            rb.pack(side=tk.LEFT, padx=8)

        # === ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ в строку ===
        extra_frame = tk.LabelFrame(content, text=" ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ ",
                                    font=("Segoe UI", 9, "bold"),
                                    bg="#ffffff", fg="#374151", padx=10, pady=6)
        extra_frame.pack(fill=tk.X, padx=12, pady=(0, 8))

        extra_row = tk.Frame(extra_frame, bg="#ffffff")
        extra_row.pack()

        self.long_context_var = tk.BooleanVar()
        long_cb = tk.Checkbutton(extra_row, text="📖 Длинный контекст",
                                 variable=self.long_context_var, bg="#ffffff", fg="#374151",
                                 selectcolor="#ffffff", activebackground="#ffffff",
                                 font=("Segoe UI", 8))
        long_cb.pack(side=tk.LEFT, padx=15)

        self.multimodal_var = tk.BooleanVar()
        mm_cb = tk.Checkbutton(extra_row, text="🖼️ Мультимодальность",
                               variable=self.multimodal_var, bg="#ffffff", fg="#374151",
                               selectcolor="#ffffff", activebackground="#ffffff",
                               font=("Segoe UI", 8))
        mm_cb.pack(side=tk.LEFT, padx=15)

        # === ПРИОРИТЕТ СКОРОСТИ в строку ===
        speed_frame = tk.LabelFrame(content, text=" ПРИОРИТЕТ СКОРОСТИ ",
                                    font=("Segoe UI", 9, "bold"),
                                    bg="#ffffff", fg="#374151", padx=10, pady=6)
        speed_frame.pack(fill=tk.X, padx=12, pady=(0, 12))

        speed_row = tk.Frame(speed_frame, bg="#ffffff")
        speed_row.pack()

        self.speed_var = tk.StringVar(value="critical")

        speeds = [
            ("🚀 Скорость критична", "critical"),
            ("⚡ Скорость важна", "important"),
            ("🐢 Скорость не важна", "low"),
        ]

        for text, value in speeds:
            rb = tk.Radiobutton(speed_row, text=text, variable=self.speed_var, value=value,
                                bg="#ffffff", fg="#374151", selectcolor="#ffffff",
                                activebackground="#ffffff", font=("Segoe UI", 8))
            rb.pack(side=tk.LEFT, padx=15)

        # Кнопка поиска
        btn_frame = tk.Frame(content, bg="#ffffff")
        btn_frame.pack(pady=(5, 12))
        self.search_btn = ModernButton(btn_frame, "🔍 НАЙТИ НЕЙРОСЕТЬ", self._run_search,
                                       bg="#2563eb", hover="#1d4ed8")
        self.search_btn.pack()

    def _setup_right_panel(self):
        content = self.right_frame.inner_frame

        tk.Label(content, text="📊 РЕЗУЛЬТАТ ПОДБОРА", font=("Segoe UI", 11, "bold"),
                 bg="#ffffff", fg="#1e40af").pack(pady=(10, 8))

        # Панель с описанием системы оценки - компактная но читаемая
        rating_frame = tk.Frame(content, bg="#eff6ff", relief="solid", bd=1)
        rating_frame.pack(fill=tk.X, padx=12, pady=(0, 8))

        tk.Label(rating_frame, text="📈 СИСТЕМА ОЦЕНКИ МОДЕЛЕЙ", font=("Segoe UI", 9, "bold"),
                 bg="#eff6ff", fg="#1e40af").pack(pady=(6, 3))

        # Две колонки для информации об оценке
        rating_cols = tk.Frame(rating_frame, bg="#eff6ff")
        rating_cols.pack(fill=tk.X, padx=10, pady=(0, 6))

        col_left = tk.Frame(rating_cols, bg="#eff6ff")
        col_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        col_right = tk.Frame(rating_cols, bg="#eff6ff")
        col_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Левая колонка - Quality Score
        tk.Label(col_left, text="🏆 QUALITY SCORE 0-100", font=("Segoe UI", 8, "bold"),
                 bg="#eff6ff", fg="#2563eb").pack(anchor=tk.W)

        quality_sources = "• LMArena — предпочтения пользователей\n• GPQA — научные задачи\n• SWE-bench — программирование\n• MMMU — мультимодальность\n• HumanEval — генерация кода"

        tk.Label(col_left, text=quality_sources, font=("Segoe UI", 7),
                 bg="#eff6ff", fg="#374151", justify=tk.LEFT).pack(anchor=tk.W, pady=(2, 0))

        # Правая колонка - Speed Score
        tk.Label(col_right, text="⚡ SPEED SCORE 0-100", font=("Segoe UI", 8, "bold"),
                 bg="#eff6ff", fg="#2563eb").pack(anchor=tk.W)

        speed_sources = "• TTFT — время до первого токена\n• Токенов в секунду — скорость\n• Задержка API"

        tk.Label(col_right, text=speed_sources, font=("Segoe UI", 7),
                 bg="#eff6ff", fg="#374151", justify=tk.LEFT).pack(anchor=tk.W, pady=(2, 0))

        # Итоговый рейтинг
        total_frame = tk.Frame(rating_frame, bg="#eff6ff")
        total_frame.pack(fill=tk.X, padx=10, pady=(0, 6))

        tk.Label(total_frame, text="🎯 ИТОГОВЫЙ РЕЙТИНГ", font=("Segoe UI", 8, "bold"),
                 bg="#eff6ff", fg="#2563eb").pack(anchor=tk.W)

        total_formula = "Учитывает: Бюджет + Приоритет скорости + Стоимость за 1M токенов"

        tk.Label(total_frame, text=total_formula, font=("Segoe UI", 7),
                 bg="#eff6ff", fg="#374151", justify=tk.LEFT).pack(anchor=tk.W, pady=(2, 0))

        # Текстовое поле с прокруткой
        text_frame = tk.Frame(content, bg="#f9fafb")
        text_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        scrollbar = tk.Scrollbar(text_frame, bg="#e5e7eb", troughcolor="#f3f4f6")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.result_text = tk.Text(text_frame, wrap=tk.WORD, font=("Consolas", 9),
                                   bg="#ffffff", fg="#1f2937", relief="flat", bd=0,
                                   yscrollcommand=scrollbar.set, padx=12, pady=10,
                                   insertbackground="#2563eb", selectbackground="#93c5fd")
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.result_text.yview)

        self._show_welcome()

    def _show_welcome(self):
        welcome = """╔════════════════════════════════════════════════════════════════════════════╗
║                          ДОБРО ПОЖАЛОВАТЬ                                              ║
╚════════════════════════════════════════════════════════════════════════════╝

✨ ПОДБОР НЕЙРОСЕТЕЙ 2026 — ваш персональный эксперт по выбору нейросетей.

В базе данных 20 актуальных моделей:
• США: GPT-5.4 Pro, Claude Opus, Gemini 2.5 Pro, Grok 3.5
• Россия: Шедеврум 4.0, GigaChat Pro, YandexGPT 5
• Китай: Qwen 2.5 Max, DeepSeek R1, Z.ai GLM-5, Yi 34B, StepFun Step-2
• Европа: Llama 4, Mistral Large 3, Command R+

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Как это работает:
  1. Выберите параметры в левой панели
  2. Можно выбрать НЕСКОЛЬКО типов задач одновременно
  3. Нажмите НАЙТИ НЕЙРОСЕТЬ
  4. Получите топ-рекомендацию с детальным анализом

Данные на апрель 2026 года

💡 Совет: Выбирайте несколько типов задач для комплексных проектов!"""

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, welcome)
        self.result_text.configure(state=tk.DISABLED)

    def _run_search(self):
        selected_tasks = [task for task, var in self.task_vars.items() if var.get()]

        if not selected_tasks:
            selected_tasks = ["text", "code", "math", "analysis", "multimodal"]

        criteria = {
            "tasks": selected_tasks,
            "budget": self.budget_var.get(),
            "long_context": self.long_context_var.get(),
            "multimodal": self.multimodal_var.get(),
            "speed": self.speed_var.get()
        }
        results = self._match_models(criteria)
        self._display_results(results, criteria)

    def _match_models(self, criteria):
        candidates = []
        for m in MODELS_DB:
            task_match = any(task in m["tasks"] for task in criteria["tasks"])
            if not task_match:
                continue

            if criteria["long_context"] and not m["long_context"]:
                continue
            if criteria["multimodal"] and not m["multimodal"]:
                continue

            score = 0.0

            if criteria["budget"] == "premium":
                score += m["quality_score"] * 1.5
                if m["budget_tier"] == "premium":
                    score += 20
            elif criteria["budget"] == "balanced":
                score += (m["quality_score"] * 0.7) + ((100 - m["cost_per_m_out"]) * 0.3)
            else:
                score += (100 - m["cost_per_m_out"]) * 1.5
                if m["budget_tier"] == "budget":
                    score += 30

            if criteria["speed"] == "critical":
                score += m["speed_score"] * 1.8
            elif criteria["speed"] == "important":
                score += m["speed_score"] * 1.0
            else:
                score += m["speed_score"] * 0.3

            if criteria["budget"] == "premium" and m["budget_tier"] == "budget":
                score -= 15
            if criteria["budget"] == "budget" and m["budget_tier"] == "premium":
                score -= 25

            candidates.append((score, m))

        candidates.sort(key=lambda x: x[0], reverse=True)
        return candidates[:5]

    def _display_results(self, candidates, criteria):
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)

        if not candidates:
            self.result_text.insert(tk.END, "╔══════════════════════════════════════════════════════════════╗\n")
            self.result_text.insert(tk.END, "║ ⚠️ НИЧЕГО НЕ НАЙДЕНО                                              ║\n")
            self.result_text.insert(tk.END, "╚══════════════════════════════════════════════════════════════╝\n\n")
            self.result_text.insert(tk.END, " Попробуйте изменить параметры:\n")
            self.result_text.insert(tk.END, " • Выберите больше типов задач\n")
            self.result_text.insert(tk.END, " • Снять галочку Длинный контекст или Мультимодальность\n")
            self.result_text.insert(tk.END, " • Выбрать другой бюджет\n\n")
            self.result_text.insert(tk.END, " Рекомендация по умолчанию: Gemini 2.5 Pro")
            self.result_text.configure(state=tk.DISABLED)
            return

        # Показываем выбранные типы задач
        selected_names = []
        task_name_map = {
            "text": "Текст", "code": "Код", "math": "Математика", "analysis": "Анализ",
            "multimodal": "Мультимодальный", "reasoning": "Рассуждение", "agents": "Агенты",
            "long_context": "Длинный контекст", "video": "Видео", "image_gen": "Генерация изображений",
            "fast_response": "Быстрые ответы", "local_deployment": "Локальный запуск", "rag": "Поиск и RAG",
            "business": "Бизнес", "science": "Наука", "chat": "Чат-боты", "real_time": "Реальные данные",
            "document": "Документы", "edge_device": "Edge устройства"
        }
        for t in criteria["tasks"]:
            if t in task_name_map:
                selected_names.append(task_name_map[t])

        self.result_text.insert(tk.END, "╔══════════════════════════════════════════════════════════════╗\n")
        self.result_text.insert(tk.END,
                                f"║ ✅ НАЙДЕНО {len(candidates)} МОДЕЛЕЙ                                              ║\n")
        self.result_text.insert(tk.END, "╚══════════════════════════════════════════════════════════════╝\n")

        # Компактное отображение выбранных типов
        tasks_str = ", ".join(selected_names[:8])
        if len(selected_names) > 8:
            tasks_str += f" и ещё {len(selected_names) - 8}"
        self.result_text.insert(tk.END, f"\n 📌 Выбрано: {tasks_str}\n\n")

        for i, (score, m) in enumerate(candidates, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "⭐"
            self.result_text.insert(tk.END, f"┌{'─' * 62}┐\n")
            self.result_text.insert(tk.END,
                                    f"│ {medal} {i}. {m['name']:<25} {m['provider']}{' ' * (30 - len(m['name']) - len(m['provider']))}│\n")
            self.result_text.insert(tk.END, f"├{'─' * 62}┤\n")

            speed_ru = {"critical": " МГНОВЕННО", "fast": "⚡ БЫСТРО", "medium": " СРЕДНЕ", "slow": " МЕДЛЕННО"}
            self.result_text.insert(tk.END, f"│ Цена: ${m['cost_per_m_out']:<5.2f} за 1M токенов ")
            self.result_text.insert(tk.END, f"⚡ {speed_ru.get(m['speed_tier'], 'СРЕДНЕ'):<15}│\n")

            self.result_text.insert(tk.END, f"│ Качество: {m['quality_score']}/100 ")
            self.result_text.insert(tk.END, f"️ {m['budget_tier'].upper():<10}{' ' * (28 - len(m['budget_tier']))}│\n")

            ctx_str = " 1M+ токенов" if m["long_context"] else " 128K токенов"
            mm_str = "️ Мультимодальна" if m["multimodal"] else " Только текст"
            self.result_text.insert(tk.END, f"│ {ctx_str:<20} {mm_str:<38}│\n")

            self.result_text.insert(tk.END, f"├{'─' * 62}┤\n")

            desc_lines = [m["description"][j:j + 58] for j in range(0, len(m["description"]), 58)]
            for line in desc_lines:
                self.result_text.insert(tk.END, f"│ {line:<60}│\n")

            self.result_text.insert(tk.END, f"└{'─' * 62}┘\n\n")

        self.result_text.insert(tk.END, "╔══════════════════════════════════════════════════════════════╗\n")
        best = candidates[0][1]
        self.result_text.insert(tk.END, f"║ ИТОГОВАЯ РЕКОМЕНДАЦИЯ: {best['name']:<32}║\n")
        self.result_text.insert(tk.END, "╚══════════════════════════════════════════════════════════════╝\n\n")

        if len(candidates) > 1:
            second = candidates[1][1]
            self.result_text.insert(tk.END, f" Альтернатива: {second['name']}\n\n")

        self.result_text.insert(tk.END, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        self.result_text.insert(tk.END, " Интеграция: API провайдера | HuggingFace | Ollama | Локальный запуск\n")

        self.result_text.configure(state=tk.DISABLED)
        self.result_text.see("1.0")


if __name__ == "__main__":
    root = tk.Tk()
    app = AIModelSelectorApp(root)
    root.mainloop()