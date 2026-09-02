import os


# about habitat scene
INVALID_SCENE_ID = []

# about chatgpt api
END_POINT = os.getenv("THREE_DMEM_OPENAI_BASE_URL", "")
OPENAI_KEY = os.getenv("THREE_DMEM_OPENAI_KEY", "")
OPENAI_MODEL = os.getenv("THREE_DMEM_OPENAI_MODEL", "gpt-4o")
OPENAI_TEMPERATURE = float(os.getenv("THREE_DMEM_OPENAI_TEMPERATURE", "0.7"))
