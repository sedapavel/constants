# Dynamické konstanty pro Steam Game Installer V3.9
# Tento soubor se načítá z GitHub pro dynamickou konfiguraci

# === BARVY TLAČÍTEK ===
BUTTON_COLORS = {
    "add_game": "#4CAF50",
    "online_fix": "#2196F3",
    "update": "#9C27B0",
    "dlc": "#FF5722",
    "restart": "#FF9800",
    "open_folder": "#607D8B",
    "shortcut": "#795548",
    "settings": "#455A64",
    "history": "#546E7A",
    "tickets": "#4de8f3",
    "exit": "#f44336",
    "cancel": "#f44336",
    "games": "#000879",
    "dashboard": "#673AB7",
    "editor": "#FF98E9",
    "quick": "#D0FF00",
    "move_to_stauto": "#FF8C00",
    "default": "#607D8B",
}

# === ROZMĚRY OKNA ===
WINDOW_SIZES = {
    "main_small": (455, 1005),
    "main": (1650, 980),
    "setup": (600, 950),
    "settings": (950, 760),
    "console": (600, 400),
    "history": (750, 650),
    "tickets": (900, 620),
    "auth": (420, 475),
    "install": (980, 720),
    "lua_generator": (550, 955),
    "online_fix": (920, 950),
    "update": (550, 720),
    "dlc": (600, 680),
    "preview": (500, 500),
    "games": (650, 800),
    "editor": (600, 700),
    "dashboard": (600, 700),
    "quick_actions": (400, 480),
    "update_check": (500, 685),
    "move_to_stauto": (550, 1000),
    "admin": (1000, 700),
}

# === FONTY ===
FONTS = {
    "title": ("Segoe UI", 18, "bold"),
    "subtitle": ("Segoe UI", 14, "bold"),
    "normal": ("Segoe UI", 11),
    "normal_bold": ("Segoe UI", 11, "bold"),
    "small": ("Segoe UI", 9),
    "tiny": ("Segoe UI", 8),
    "button": ("Segoe UI", 11, "bold"),
    "console": ("Consolas", 10),
    "header": ("Segoe UI", 22, "bold"),
    "card_title": ("Segoe UI", 12, "bold"),
    "stat_number": ("Segoe UI", 24, "bold"),
    "small_bold": ("Segoe UI", 10, "bold"),
}

# === TEXTY A ZPRÁVY ===
MESSAGES = {
    "welcome": "Vítejte v Steam Game Installer!",
    "restart_steam_question": "Chceš restartovat Steam?",
    "steam_restarted": "Steam byl úspěšně restartován.",
    "files_moved": "Soubory byly úspěšně přesunuty.",
    "shortcut_created": "Zástupce byl vytvořen na ploše.",
    "auth_success": "Autorizace proběhla úspěšně!",
    "auth_failed": "Neplatný autorizační klíč!",
    "folder_not_found": "Složka nebyla nalezena.",
    "no_files_found": "Nebyly nalezeny žádné soubory.",
}

# === TICKET TYPY ===
TICKET_TYPES = [
    "bug",
    "documentation",
    "improvements",
    "help wanted",
    "request auth key",
    "request dlc",
    "request game",
    "request online-fix",
    "request update",
]

# === STAUTO SLOŽKY ===
STAUTO_SUBFOLDERS = ["Hra", "Online", "Update", "DLC"]

# === QUICK ACTIONS ===
QUICK_ACTIONS = [
    {"id": "restart_steam", "name": "Restart Steam", "icon": "♻️"},
    {"id": "open_stplugin", "name": "Otevřít stplug-in", "icon": "📁"},
    {"id": "open_stauto", "name": "Otevřít STAuto", "icon": "📁"},
    {"id": "add_game", "name": "Přidat hru", "icon": "🎮"},
]

# === PŘÍPOBY SOUBORŮ ===
FILE_EXTENSIONS = {
    "lua": ".lua",
    "manifest": ".manifest",
}

# === TÉMA ===
DARK_THEME = {
    "bg_primary": "#1a1a2e",
    "bg_secondary": "#16213e",
    "bg_tertiary": "#0f3460",
    "accent": "#e94560",
    "accent_hover": "#ff6b6b",
    "text_primary": "#ffffff",
    "text_secondary": "#a0a0a0",
    "text_muted": "#6c6c6c",
    "success": "#4CAF50",
    "warning": "#FF9800",
    "error": "#f44336",
    "info": "#2196F3",
    "border": "#2a2a4a",
    "online_dot": "#00ff00",
    "card_bg": "#1e2746",
}

LIGHT_THEME = {
    "bg_primary": "#f5f5f5",
    "bg_secondary": "#ffffff",
    "bg_tertiary": "#e0e0e0",
    "accent": "#e94560",
    "accent_hover": "#ff6b6b",
    "text_primary": "#1a1a2e",
    "text_secondary": "#555555",
    "text_muted": "#888888",
    "success": "#4CAF50",
    "warning": "#FF9800",
    "error": "#f44336",
    "info": "#2196F3",
    "border": "#cccccc",
    "online_dot": "#00cc00",
    "card_bg": "#ffffff",
}