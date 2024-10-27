# Model-specific configurations
MODEL_CONFIGS = {
    "gemini": {
        "capabilities": ["image_analysis", "code_generation", "screen_analysis"],
        "max_tokens": 2048,
        "temperature": 0.7,
        "supports_vision": True,
        "prompt_template": "You are an AI assistant specialized in computer automation..."
    },
    "openai": {
        "capabilities": ["text_analysis", "code_generation", "precise_instructions"],
        "max_tokens": 4096,
        "temperature": 0.5,
        "supports_vision": False,
        "prompt_template": "You are an AI assistant specialized in computer automation..."
    }
}

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
