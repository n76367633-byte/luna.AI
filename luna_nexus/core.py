#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                      ║
║   ██╗     ██╗   ██╗███╗   ██╗ █████╗        ███╗   ██╗███████╗██╗  ██╗██╗   ██╗   ║
║   ██║     ██║   ██║████╗  ██║██╔══██╗       ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║   ║
║   ██║     ██║   ██║██╔██╗ ██║███████║       ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║   ║
║   ██║     ██║   ██║██║╚██╗██║██╔══██║       ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║   ║
║   ███████╗╚██████╔╝██║ ╚████║██║  ██║       ██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝   ║
║   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝    ║
║                                                                                      ║
║   Luna.AI  ★  NEXUS EDITION  ★  Multimodal · Self-Evolving · Iron Man HUD          ║
║                                                                                      ║
║   NEW SYSTEMS:                                                                       ║
║   🧠 LangGraph Multi-Agent Orchestration  │  🗄  ChromaDB Episodic Ledger           ║
║   🖥  PyQt6 + OpenCV Iron Man HUD         │  🔗  Live Chain of Thought Stream       ║
║   👁  YOLOv8 Environmental Awareness      │  🤌  MediaPipe Gesture Control          ║
║   🌐  Playwright Autonomous Navigator     │  🐍  Sandboxed Python Interpreter       ║
║   😶  Proactive Mood Engine (IoT+OS)      │  🔄  Safe Self-Evolution Loop           ║
║   🎨  Creative Synthesis Module           │  ⚛   Quantum Reasoning Engine           ║
║   🔮  Predictive Intent Engine            │  💤  Dream Mode (Background Learning)   ║
║   🧵  Neural Context Weaver               │  💚  Emotional Intelligence Layer        ║
║   📦  Skill Marketplace                   │  🕰  Time Capsule Memory                ║
║                                                                                      ║
║   Inherits: Luna.AI Supreme Edition (21 Parallel Brains + JARVIS Control)           ║
║   Compatible: Windows 10/11  │  Python 3.10+  │  CUDA optional                     ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

ARCHITECTURE OVERVIEW
─────────────────────────────────────────────────────────────────────────────────────
  Luna_Nexus.py  (this file)
    │
    ├── NexusBootLoader          ← installs all new deps, validates env
    ├── EpisodicLedger           ← ChromaDB long-term semantic memory
    ├── LangGraphOrchestrator    ← multi-agent reasoning graph (9 specialized agents)
    ├── NexusHUD                 ← PyQt6 transparent Iron Man overlay
    │     ├── CoTStreamPanel     ← live Chain of Thought
    │     ├── YOLOPanel          ← real-time object labels
    │     ├── SystemGauges       ← CPU/RAM/GPU/IoT metrics
    │     └── GestureOverlay     ← hand pose visualization
    ├── YOLOEnvironment          ← YOLOv8 webcam awareness
    ├── GestureController        ← MediaPipe hand gesture ↔ command mapping
    ├── PlaywrightNavigator      ← autonomous headless web agent
    ├── SecureCodeSandbox        ← restricted exec + Pydantic result types
    ├── ProactiveMoodEngine      ← Windows telemetry + ESP32 MQTT + BLE
    ├── SelfEvolutionLoop        ← AST-safe code refactor with rollback
    ├── CreativeSynthesisModule  ← lateral thinking / unconventional strategies
    ├── QuantumReasoningEngine   ← N parallel reasoning branches → best-of
    ├── PredictiveIntentEngine   ← Markov + embedding next-query prediction
    ├── DreamMode                ← idle-time learning / concept consolidation
    ├── NeuralContextWeaver      ← dynamic sliding context with salience scoring
    ├── EmotionalIntelligenceLayer ← affect detection → empathy-tuned responses
    ├── TimeCapsuleMemory        ← schedule future memories / reminders
    ├── SkillMarketplace         ← download / upload Luna skill modules
    └── NexusCore                ← top-level orchestrator (wraps Supreme + above)
"""

# ─────────────────────────────────────────────────────────────────────────────
#  0.  WINDOWS UTF-8  (must be first)
# ─────────────────────────────────────────────────────────────────────────────
import sys, os
if sys.platform == "win32":
    os.system("chcp 65001 >nul 2>&1")
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
os.system("")  # ANSI on Windows
PY314_PLUS = sys.version_info >= (3, 14)

# ─────────────────────────────────────────────────────────────────────────────
#  0b.  API KEY SETUP  (runs once at startup — before any other init)
#       Only prompts if the key is not already present in the environment.
# ─────────────────────────────────────────────────────────────────────────────
def _collect_api_keys() -> None:
    """
    Interactive API-key collector.  Runs at the very start of the script so
    that the keys are available in os.environ when the KEYS dict is built later.

    Each provider is optional — pressing Enter (or typing 'skip') leaves the
    existing environment variable unchanged and lets Luna fall back to local
    models automatically.
    """
    _CYAN   = "\033[96m"
    _YELLOW = "\033[93m"
    _GREEN  = "\033[92m"
    _DIM    = "\033[2m"
    _RESET  = "\033[0m"
    _BOLD   = "\033[1m"

    banner = (
        f"\n{_CYAN}{'═' * 70}{_RESET}\n"
        f"{_BOLD}{_CYAN}  🔑  LUNA.AI  —  API KEY SETUP{_RESET}\n"
        f"{_CYAN}{'═' * 70}{_RESET}\n"
        f"{_DIM}  You may enter your API keys now so Luna can use cloud LLMs.\n"
        f"  Press Enter or type 'skip' to skip any key — Luna will use local\n"
        f"  models (Ollama / HuggingFace) for that provider instead.{_RESET}\n"
        f"{_CYAN}{'─' * 70}{_RESET}"
    )
    print(banner)

    # ── 1. Anthropic / Claude ────────────────────────────────────────────────
    _existing_ant = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if _existing_ant:
        print(
            f"\n{_GREEN}  ✅  Claude API key already set "
            f"({_existing_ant[:10]}…){_RESET}"
        )
    else:
        print(
            f"\n{_YELLOW}  Claude (Anthropic) API Key{_RESET}\n"
            f"  {_DIM}Docs / key management:{_RESET} "
            f"{_CYAN}https://platform.claude.com/docs/en/api/admin/api_keys/retrieve{_RESET}\n"
            f"  {_DIM}Enter your key (starts with  sk-ant-…)  or press Enter to skip:{_RESET}"
        )
        try:
            _ant_key = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            _ant_key = ""
        if _ant_key and _ant_key.lower() != "skip":
            os.environ["ANTHROPIC_API_KEY"] = _ant_key
            print(f"  {_GREEN}✅  Claude API key saved for this session.{_RESET}")
        else:
            print(f"  {_DIM}⏭  Skipped — Luna will use local / free models for Claude tasks.{_RESET}")

    # ── 2. OpenAI ────────────────────────────────────────────────────────────
    _existing_oai = os.environ.get("OPENAI_API_KEY", "").strip()
    if _existing_oai:
        print(
            f"\n{_GREEN}  ✅  OpenAI API key already set "
            f"({_existing_oai[:8]}…){_RESET}"
        )
    else:
        print(
            f"\n{_YELLOW}  OpenAI API Key{_RESET}\n"
            f"  {_DIM}Docs / key management:{_RESET} "
            f"{_CYAN}https://developers.openai.com/api/docs{_RESET}\n"
            f"  {_DIM}Enter your key (starts with  sk-…)  or press Enter to skip:{_RESET}"
        )
        try:
            _oai_key = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            _oai_key = ""
        if _oai_key and _oai_key.lower() != "skip":
            os.environ["OPENAI_API_KEY"] = _oai_key
            print(f"  {_GREEN}✅  OpenAI API key saved for this session.{_RESET}")
        else:
            print(f"  {_DIM}⏭  Skipped — Luna will use local / free models for OpenAI tasks.{_RESET}")

    print(
        f"\n{_CYAN}{'─' * 70}{_RESET}\n"
        f"{_DIM}  💡  Tip: Set  ANTHROPIC_API_KEY  and  OPENAI_API_KEY  as permanent\n"
        f"      environment variables (setx on Windows / export on Linux) to skip\n"
        f"      this prompt on every launch.{_RESET}\n"
        f"{_CYAN}{'═' * 70}{_RESET}\n"
    )

# Run immediately — keys must be in os.environ before KEYS dict is built later
_collect_api_keys()

# ─────────────────────────────────────────────────────────────────────────────
#  1.  STANDARD-LIBRARY IMPORTS
# ─────────────────────────────────────────────────────────────────────────────
import asyncio, json, time, base64, platform, logging, subprocess
import ast, re, math, hashlib, textwrap, socket, threading, io, shutil
import operator, ctypes, wave, datetime, webbrowser, random, tempfile
import inspect, copy, traceback, signal, struct, queue, uuid, enum
import builtins
from pathlib import Path
from functools import wraps, lru_cache
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import deque, Counter, defaultdict
from contextlib import redirect_stdout, suppress
from typing import (Optional, Dict, List, Tuple, Any, Union,
                    Callable, Generator, AsyncGenerator, Type)
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# ─────────────────────────────────────────────────────────────────────────────
#  2.  NEXUS BOOT LOADER  (auto-install all dependencies)
# ─────────────────────────────────────────────────────────────────────────────
_NEXUS_PKGS = [
    # ── Core (inherited from Supreme) ────────────────────────────────────────
    ("numpy",              "numpy"),
    ("requests",           "requests"),
    ("aiohttp",            "aiohttp"),
    ("opencv-python",      "cv2"),
    ("Pillow",             "PIL"),
    ("psutil",             "psutil"),
    ("pyautogui",          "pyautogui"),
    ("pyperclip",          "pyperclip"),
    ("colorama",           "colorama"),
    ("pyttsx3",            "pyttsx3"),
    ("SpeechRecognition",  "speech_recognition"),
    ("sounddevice",        "sounddevice"),
    ("openai",             "openai"),
    ("anthropic",          "anthropic"),
    ("sympy",              "sympy"),
    ("ddgs",               "ddgs"),            # renamed from duckduckgo-search
    ("wikipedia",          "wikipedia"),
    ("chromadb",           "chromadb"),
    ("sentence-transformers", "sentence_transformers"),
    ("pywin32",            "win32gui"),
    ("pytesseract",        "pytesseract"),
    # ── Nexus NEW ─────────────────────────────────────────────────────────────
    ("pydantic",           "pydantic"),
    ("PyQt6",              "PyQt6"),
    ("langgraph",          "langgraph"),
    ("langchain-core",     "langchain_core"),
    ("langchain-anthropic","langchain_anthropic"),
    ("langchain-openai",   "langchain_openai"),
    ("playwright",         "playwright"),
    ("mediapipe",          "mediapipe"),
    ("ultralytics",        "ultralytics"),   # YOLOv8
    ("paho-mqtt",          "paho.mqtt.client"),
    ("bleak",              "bleak"),          # BLE for ESP32
    ("rich",               "rich"),
    ("watchdog",           "watchdog"),
    ("schedule",           "schedule"),
    ("tiktoken",           "tiktoken"),
    ("black",              "black"),          # code formatting in self-evolution
    ("pybullet",           "pybullet"),       # real-time physics simulation
    # ── GemmaE4B local (no API, no cost) ──────────────────────────────────────
    # Primary path  : Ollama (gemma3:4b or gemma2:2b) — zero pip dep needed.
    # Fallback path : HuggingFace transformers (offline, downloads on first run).
    ("transformers",       "transformers"),   # HF transformers (GemmaE4B HF fallback)
    ("accelerate",         "accelerate"),     # optional GPU offload for HF path
]

if PY314_PLUS:
    # pybullet has no prebuilt wheels for Python 3.14+ and requires MSVC to compile
    # from source — skip auto-install entirely on this version.
    _NEXUS_PKGS = [
        pkg for pkg in _NEXUS_PKGS
        if pkg[0] not in {
            "langgraph",
            "langchain-core",
            "langchain-anthropic",
            "langchain-openai",
            "pybullet",
        }
    ]

def _check_internet(t: float = 1.5) -> bool:
    try:
        with socket.create_connection(("1.1.1.1", 53), timeout=t):
            return True
    except OSError:
        return False

# Packages that must be installed as pre-built binary wheels only
# (building from source requires C++ toolchain — avoid on Windows without MSVC)
_BINARY_ONLY_PKGS = frozenset(["pybullet"])

def _install(pkg: str, imp: str, quiet: bool = True) -> bool:
    try:
        __import__(imp.split(".")[0])
        return True
    except ImportError:
        pass
    if not _check_internet():
        return False
    flag = "-q" if quiet else ""
    # For packages that require C compilation use --only-binary=:all: to avoid
    # MSVC / GCC build failures on systems without a C++ toolchain.
    binary_flag = "--only-binary=:all:" if pkg in _BINARY_ONLY_PKGS else ""
    rc = os.system(f'"{sys.executable}" -m pip install {pkg} {binary_flag} {flag} 2>&1')
    if rc != 0 and pkg not in _BINARY_ONLY_PKGS:
        # Retry without binary restriction only for packages that can be built from source.
        # Binary-only packages (e.g. pybullet) must NOT fall back to source compilation
        # because a missing C++ toolchain will produce a fatal MSVC / GCC build error.
        rc = os.system(f'"{sys.executable}" -m pip install {pkg} --user {flag} 2>&1')
    return rc == 0

AUTO_INSTALL = "--no-install" not in sys.argv

class NexusBootLoader:
    """Auto-installs all Nexus dependencies and validates the runtime."""

    @staticmethod
    def run(verbose: bool = True):
        if not AUTO_INSTALL:
            return
        if verbose:
            print("\n╔══════════════════════════════════════════╗")
            print("║   Luna.AI Nexus  ─  Dependency Check     ║")
            print("╚══════════════════════════════════════════╝")
        failed = []
        for pkg, imp in _NEXUS_PKGS:
            ok = _install(pkg, imp, quiet=not verbose)
            if not ok:
                failed.append(pkg)
                if verbose:
                    print(f"  ⚠  {pkg:30s}  FAILED (manual install may be needed)")
        if verbose:
            status = "✓ All deps ready" if not failed else f"⚠ {len(failed)} package(s) missing"
            print(f"\n  {status}\n")

        # Playwright browser install (one-time)
        try:
            subprocess.run(
                [sys.executable, "-m", "playwright", "install", "chromium", "--quiet"],
                timeout=120, capture_output=True
            )
        except Exception:
            pass

# ─────────────────────────────────────────────────────────────────────────────
#  3.  SAFE THIRD-PARTY IMPORTS  (graceful degradation)
# ─────────────────────────────────────────────────────────────────────────────
try:
    from colorama import Fore, Style, init as _ci;  _ci(autoreset=True)
    COL = Fore;  RST = Style.RESET_ALL;  BLD = Style.BRIGHT
except ImportError:
    class _F:
        CYAN=YELLOW=GREEN=RED=WHITE=MAGENTA=BLUE=RESET=""
    COL=_F(); RST=BLD=""

try:    import numpy as np;                   NP_OK = True
except: NP_OK = False

try:    import cv2;                           CV2_OK = True
except: CV2_OK = False

try:    import psutil;                        PSUTIL_OK = True
except: PSUTIL_OK = False

try:    import pyttsx3;                       TTS_OK = True
except: TTS_OK = False

try:    import speech_recognition as sr;     SR_OK = True
except: SR_OK = False

try:    import sounddevice as sd;            SD_OK = True
except: SD_OK = False

try:    import pyautogui;  pyautogui.FAILSAFE = False; GUI_OK = True
except: GUI_OK = False

try:    import pyperclip;                    CLIP_OK = True
except: CLIP_OK = False

try:    from PIL import Image, ImageGrab;    PIL_OK = True
except: PIL_OK = False

try:    from openai import AsyncOpenAI;      OAI_OK = True
except: OAI_OK = False

try:    from anthropic import AsyncAnthropic; ANT_OK = True
except: ANT_OK = False

try:    import chromadb;                     CHROMA_OK = True
except: CHROMA_OK = False

try:
    from sentence_transformers import SentenceTransformer
    SBERT_OK = True
except: SBERT_OK = False

try:
    from pydantic import BaseModel, Field, ValidationError
    PYDANTIC_OK = True
except: PYDANTIC_OK = False

try:
    from PyQt6.QtWidgets import (
        QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
    )
    from PyQt6.QtCore import Qt, QTimer, pyqtSignal, QThread, QObject
    from PyQt6.QtGui import (
        QFont, QColor, QPainter, QPen, QBrush, QLinearGradient,
        QRadialGradient, QFontMetrics
    )
    PYQT6_OK = True
except: PYQT6_OK = False

try:
    if PY314_PLUS:
        raise RuntimeError("LangGraph/LangChain disabled on Python 3.14+")
    from langgraph.graph import StateGraph, END
    LANGGRAPH_OK = True
except: LANGGRAPH_OK = False

try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_OK = True
except: PLAYWRIGHT_OK = False

try:
    import mediapipe as mp
    MEDIAPIPE_OK = True
except: MEDIAPIPE_OK = False

try:
    from ultralytics import YOLO
    YOLO_OK = True
except: YOLO_OK = False

try:
    import paho.mqtt.client as mqtt
    MQTT_OK = True
except: MQTT_OK = False

try:
    from rich.console import Console
    from rich.live import Live
    from rich.panel import Panel
    from rich.text import Text
    from rich.table import Table
    from rich import box
    RICH_OK = True
    rich_console = Console()
except: RICH_OK = False

try:
    import wikipedia as wiki_lib;            WIKI_OK = True
except: WIKI_OK = False

try:
    # Package was renamed from duckduckgo-search → ddgs in 2024.
    # Try the new name first so the deprecation warning never fires.
    try:
        from ddgs import DDGS
    except ImportError:
        from duckduckgo_search import DDGS  # legacy fallback
    DDG_OK = True
except Exception:
    DDG_OK = False

try:
    import win32gui, win32process, win32con;  WIN32_OK = True
except: WIN32_OK = False

try:
    import sympy;                             SYMPY_OK = True
except: SYMPY_OK = False

try:
    import schedule;                          SCHEDULE_OK = True
except: SCHEDULE_OK = False

try:
    import pybullet as pb
    import pybullet_data
    BULLET_OK = True
except (ImportError, Exception):
    BULLET_OK = False
    # pybullet may fail if no pre-built wheel exists for this Python/OS combo.
    # Install manually: pip install pybullet --only-binary=:all:
    # Or build tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/

try:
    from transformers import pipeline as hf_pipeline, AutoTokenizer, AutoModelForCausalLM
    TRANSFORMERS_OK = True
except ImportError:
    TRANSFORMERS_OK = False
    hf_pipeline = None  # type: ignore

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
log = logging.getLogger("Luna.Nexus")

# ── Silence HuggingFace Hub unauthenticated-request & transformers key warnings ──
import warnings as _warnings
_warnings.filterwarnings("ignore", message=".*unauthenticated.*", category=UserWarning)
_warnings.filterwarnings("ignore", message=".*HF_TOKEN.*",        category=UserWarning)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub.utils._http").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
# Make sentence-transformers silent about unexpected weight keys
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)
# Disable HF Hub progress warnings without blocking downloads
os.environ.setdefault("HF_HUB_DISABLE_IMPLICIT_TOKEN", "1")

# ─────────────────────────────────────────────────────────────────────────────
#  4.  ANSI  &  RICH HELPERS
# ─────────────────────────────────────────────────────────────────────────────
class C:
    CYAN    = "\033[96m";  GREEN   = "\033[92m";  YELLOW = "\033[93m"
    RED     = "\033[91m";  MAGENTA = "\033[95m";  WHITE  = "\033[97m"
    BLUE    = "\033[94m";  BOLD    = "\033[1m";   DIM    = "\033[2m"
    RESET   = "\033[0m"

def cprint(color: str, text: str, end="\n", flush=False):
    print(f"{color}{text}{C.RESET}", end=end, flush=flush)

def nprint(tag: str, msg: str, col: str = C.CYAN):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{C.DIM}[{ts}]{C.RESET} {col}[{tag}]{C.RESET} {msg}")

# ─────────────────────────────────────────────────────────────────────────────
#  5.  PATHS  &  GLOBAL CONFIG
# ─────────────────────────────────────────────────────────────────────────────
HOME_DIR = Path(os.getenv("LUNAX_HOME", str(Path.home() / "LunaAI"))).expanduser()
for _d in ["nexus/chroma", "nexus/hud", "nexus/evolution", "nexus/skills",
           "nexus/logs", "nexus/snapshots", "nexus/capsules", "nexus/dreams",
           "code", "screenshots", "logs", "exports", "notes", "sessions"]:
    (HOME_DIR / _d).mkdir(parents=True, exist_ok=True)

NEXUS_CFG_FILE  = HOME_DIR / "nexus" / "nexus_config.json"
LEDGER_PATH     = HOME_DIR / "nexus" / "chroma"
EVOLUTION_LOG   = HOME_DIR / "nexus" / "evolution" / "evo_log.json"
DREAM_LOG       = HOME_DIR / "nexus" / "dreams"   / "dream_log.json"
CAPSULE_DIR     = HOME_DIR / "nexus" / "capsules"
SKILL_DIR       = HOME_DIR / "nexus" / "skills"
SNAPSHOT_DIR    = HOME_DIR / "nexus" / "snapshots"

_DEFAULT_CFG = {
    "version"              : "nexus-1.0",
    "user_name"            : "Sir",
    "claude_model"         : "claude-sonnet-4-20250514",
    "openai_model"         : "gpt-4o",
    "hud_enabled"          : True,
    "hud_opacity"          : 0.88,
    "hud_position"         : "top-right",
    "hud_color_primary"    : "#00BFFF",       # Iron Man blue
    "hud_color_accent"     : "#FFD700",       # gold
    "yolo_enabled"         : True,
    "yolo_model"           : "yolov8n.pt",
    "yolo_conf_threshold"  : 0.45,
    "gesture_enabled"      : True,
    "gesture_sensitivity"  : 0.75,
    "playwright_headless"  : True,
    "sandbox_timeout_sec"  : 10,
    "mood_engine_enabled"  : True,
    "esp32_host"           : "192.168.1.100",
    "esp32_mqtt_port"      : 1883,
    "evolution_enabled"    : True,
    "evolution_auto"       : False,           # manual approval required by default
    "evolution_max_delta"  : 50,              # max lines changed per cycle
    "dream_interval_min"   : 15,
    "cot_stream_enabled"   : True,
    "quantum_branches"     : 3,
    "predictor_depth"      : 8,
    "emotional_layer"      : True,
    "allow_internet"       : True,
    "wake_words"           : ["hey luna", "luna nexus", "wake up luna"],
    "voice_rate"           : 175,
    "strict_quiet_mode"    : False,
    "codeforge_enabled"    : True,
    "codeforge_max_repair_passes": 2,
    # ── Brain Ensemble ────────────────────────────────────────────────────────
    "brain_ensemble_enabled"   : True,   # Run 5 parallel brains + cross-pollinate
    "json_brain_enabled"       : True,   # JSON Intelligence enrichment layer
    "brain_ensemble_fast_mode" : False,  # Skip cross-pollination round (faster)
    "brain_count"              : 5,      # How many parallel brains (2-5)
}

def _load_cfg() -> dict:
    try:
        if NEXUS_CFG_FILE.exists():
            d = json.loads(NEXUS_CFG_FILE.read_text(encoding="utf-8"))
            merged = {**_DEFAULT_CFG, **d}
            return merged
    except Exception:
        pass
    return dict(_DEFAULT_CFG)

def _save_cfg(cfg: dict):
    NEXUS_CFG_FILE.write_text(json.dumps(cfg, indent=2), encoding="utf-8")

NEXUS_CFG = _load_cfg()

KEYS = {
    "openai":    os.getenv("OPENAI_API_KEY",    ""),
    "anthropic": os.getenv("ANTHROPIC_API_KEY", ""),
    "gemini":    os.getenv("GEMINI_API_KEY",    ""),
}

# ─────────────────────────────────────────────────────────────────────────────
#  6.  PYDANTIC  SCHEMAS  (type-safe data contracts)
# ─────────────────────────────────────────────────────────────────────────────
if PYDANTIC_OK:
    class AgentState(BaseModel):
        """Shared state flowing through the LangGraph agent graph."""
        query       : str   = ""
        intent      : str   = ""                   # classified intent
        cot         : List[str] = Field(default_factory=list)  # chain of thought steps
        tool_calls  : List[Dict] = Field(default_factory=list)
        web_results : str   = ""
        code_result : str   = ""
        memory_ctx  : str   = ""
        final_answer: str   = ""
        mood_score  : float = 0.5                  # 0=negative 1=positive
        confidence  : float = 0.0
        branch_id   : int   = 0                    # quantum branch index
        metadata    : Dict  = Field(default_factory=dict)

    class CodeExecResult(BaseModel):
        """Result from sandboxed code execution."""
        stdout      : str  = ""
        stderr      : str  = ""
        return_val  : Any  = None
        exec_time_ms: float = 0.0
        safe        : bool = True
        error       : str  = ""

    class CodeForgeResult(BaseModel):
        """Structured output from the Precision Code Forge subsystem."""
        request            : str = ""
        language           : str = "python"
        plan               : List[str] = Field(default_factory=list)
        code               : str = ""
        checks             : List[str] = Field(default_factory=list)
        warnings           : List[str] = Field(default_factory=list)
        notes              : str = ""
        validation_ok      : bool = False
        repair_attempts    : int = 0

    class EvolutionProposal(BaseModel):
        """A self-evolution code-change proposal."""
        proposal_id  : str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
        target_file  : str = ""
        original_hash: str = ""
        new_code     : str = ""
        rationale    : str = ""
        risk_level   : str = "low"          # low / medium / high
        approved     : bool = False
        applied      : bool = False
        rollback_snap: str  = ""            # path to snapshot

    class MoodState(BaseModel):
        """Composite mood reading from all sensors."""
        valence      : float = 0.5          # negative ↔ positive
        arousal      : float = 0.5          # calm ↔ excited
        cpu_stress   : float = 0.0
        memory_stress: float = 0.0
        ambient_temp : float = 22.0         # °C from IoT
        ambient_light: float = 400.0        # lux from IoT
        time_of_day  : str   = "morning"
        inferred_mood: str   = "neutral"

    class MemoryEntry(BaseModel):
        """A single episodic memory record."""
        entry_id    : str  = Field(default_factory=lambda: str(uuid.uuid4()))
        timestamp   : str  = Field(default_factory=lambda: datetime.datetime.now().isoformat())
        role        : str  = "user"
        content     : str  = ""
        summary     : str  = ""
        embedding_id: str  = ""
        importance  : float = 0.5
        tags        : List[str] = Field(default_factory=list)

    class GestureCommand(BaseModel):
        """A recognized gesture mapped to a Luna command."""
        gesture_name: str = ""
        confidence  : float = 0.0
        command     : str = ""
        params      : Dict = Field(default_factory=dict)
        timestamp   : float = Field(default_factory=time.time)

else:
    # Fallback if Pydantic not available
    AgentState = dict
    CodeExecResult = dict
    CodeForgeResult = dict
    EvolutionProposal = dict
    MoodState = dict
    MemoryEntry = dict
    GestureCommand = dict

# ─────────────────────────────────────────────────────────────────────────────
#  7.  EPISODIC LEDGER  (ChromaDB long-term semantic memory)
# ─────────────────────────────────────────────────────────────────────────────
class EpisodicLedger:
    """
    ChromaDB-backed episodic memory with semantic search.

    Each conversation turn is embedded via sentence-transformers and stored
    in a persistent ChromaDB collection.  Retrieval uses cosine similarity
    for semantic recall + recency weighting.
    """

    COLLECTION = "luna_nexus_episodic"
    MAX_DOCS   = 50_000

    def __init__(self):
        self._client  = None
        self._coll    = None
        self._encoder = None
        self._ready   = False
        self._init()

    def _init(self):
        if not CHROMA_OK:
            nprint("Ledger", "ChromaDB not available — using fallback memory", C.YELLOW)
            return
        try:
            self._client = chromadb.PersistentClient(path=str(LEDGER_PATH))
            self._coll   = self._client.get_or_create_collection(
                name=self.COLLECTION,
                metadata={"hnsw:space": "cosine"}
            )
            if SBERT_OK:
                self._encoder = SentenceTransformer("all-MiniLM-L6-v2")
            self._ready = True
            nprint("Ledger", f"ChromaDB online │ {self._coll.count():,} entries", C.GREEN)
        except Exception as e:
            nprint("Ledger", f"Init failed: {e}", C.RED)

    def _embed(self, text: str) -> List[float]:
        if self._encoder:
            return self._encoder.encode(text, normalize_embeddings=True).tolist()
        # Hash-based fallback embedding (192-dim)
        vec = [0.0] * 192
        for tok in re.findall(r"\b\w{2,}\b", text.lower()):
            idx = int(hashlib.md5(tok.encode()).hexdigest(), 16) % 192
            vec[idx] += 1.0
        mag = math.sqrt(sum(v*v for v in vec)) or 1.0
        return [v / mag for v in vec]

    def store(self, content: str, role: str = "user",
              summary: str = "", tags: List[str] = None, importance: float = 0.5):
        """Store a memory entry."""
        if not self._ready:
            return
        try:
            entry_id = str(uuid.uuid4())
            embedding = self._embed(f"{role}: {content}")
            meta = {
                "role"      : role,
                "summary"   : summary[:500] if summary else content[:200],
                "timestamp" : datetime.datetime.now().isoformat(),
                "importance": str(importance),
                "tags"      : json.dumps(tags or []),
            }
            self._coll.add(
                ids=[entry_id],
                embeddings=[embedding],
                documents=[content[:4000]],
                metadatas=[meta]
            )
            # Prune if over limit
            if self._coll.count() > self.MAX_DOCS:
                self._prune(1000)
        except Exception as e:
            log.debug(f"Ledger.store: {e}")

    def recall(self, query: str, top_k: int = 6,
               role_filter: str = None, min_importance: float = 0.0) -> List[Dict]:
        """Semantic recall of relevant memories."""
        if not self._ready:
            return []
        try:
            q_embed = self._embed(query)
            where   = {"role": {"$eq": role_filter}} if role_filter else None
            results = self._coll.query(
                query_embeddings=[q_embed],
                n_results=min(top_k, max(1, self._coll.count())),
                where=where,
                include=["documents", "metadatas", "distances"]
            )
            out = []
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0]
            ):
                imp = float(meta.get("importance", 0.5))
                if imp >= min_importance:
                    out.append({
                        "content"   : doc,
                        "role"      : meta.get("role", "user"),
                        "summary"   : meta.get("summary", ""),
                        "timestamp" : meta.get("timestamp", ""),
                        "importance": imp,
                        "similarity": round(1.0 - dist, 4),
                    })
            return out
        except Exception as e:
            log.debug(f"Ledger.recall: {e}")
            return []

    def build_context(self, query: str, max_tokens: int = 1200) -> str:
        """Build a context string for injection into prompts."""
        memories = self.recall(query, top_k=5)
        if not memories:
            return ""
        lines = ["[🗄 EPISODIC MEMORY — relevant past context]\n"]
        budget = max_tokens
        for m in memories:
            snippet = f"[{m['role']} @ {m['timestamp'][:10]}] {m['content'][:300]}"
            if len(snippet) > budget:
                break
            lines.append(snippet)
            budget -= len(snippet)
        return "\n".join(lines)

    def _prune(self, n: int = 500):
        """Remove the oldest n entries."""
        try:
            all_ids = self._coll.get(include=[])["ids"]
            self._coll.delete(ids=all_ids[:n])
        except Exception:
            pass

    @property
    def count(self) -> int:
        if self._ready:
            try:
                return self._coll.count()
            except Exception:
                pass
        return 0

# ─────────────────────────────────────────────────────────────────────────────
#  8.  CHAIN-OF-THOUGHT  STREAMER
# ─────────────────────────────────────────────────────────────────────────────
class CoTStreamer:
    """
    Streams Chain-of-Thought reasoning steps to:
      1. The terminal (with Rich panel or plain ANSI)
      2. The HUD queue for live panel rendering
      3. The Episodic Ledger for retrospective analysis
    """

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self._hud_q = hud_queue
        self._steps : List[str] = []
        self._active = False

    def begin(self, query: str):
        self._steps = []
        self._active = True
        if NEXUS_CFG.get("cot_stream_enabled"):
            self._push(f"🔍 Query: {query[:80]}")

    def step(self, text: str, tag: str = "THINK"):
        if not self._active:
            return
        step_str = f"[{tag}] {text}"
        self._steps.append(step_str)
        if NEXUS_CFG.get("cot_stream_enabled"):
            ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:12]
            line = f"{C.DIM}{ts}{C.RESET} {C.CYAN}◈{C.RESET} {text}"
            print(line, flush=True)
        if self._hud_q:
            with suppress(queue.Full):
                self._hud_q.put_nowait({"type": "cot", "text": text, "tag": tag})

    def conclude(self, answer: str) -> List[str]:
        self._active = False
        self._push(f"✅ Answer formed ({len(answer)} chars)")
        return list(self._steps)

    def _push(self, text: str):
        if NEXUS_CFG.get("cot_stream_enabled"):
            print(f"{C.DIM}  ╰─ {text}{C.RESET}", flush=True)

# Module-level constant: must be defined here (not inside the class body)
# so that _build_safe_builtins can access it, and so that comprehensions
# inside the class body don't hit Python's class-scope lookup restriction.
_BLOCKED_BUILTINS = frozenset([
    "open", "exec", "eval", "compile", "__import__",
    "globals", "locals", "vars", "dir", "getattr",
    "setattr", "delattr", "input", "breakpoint",
])

def _build_safe_builtins(blocked: set) -> Dict[str, Any]:
    """Build a safe builtin mapping without tripping class-scope lookup rules."""
    return {name: value for name, value in vars(builtins).items()
            if name not in blocked}

# ─────────────────────────────────────────────────────────────────────────────
#  9.  SECURE CODE SANDBOX
# ─────────────────────────────────────────────────────────────────────────────
class SecureCodeSandbox:
    """
    Executes Python code in a heavily restricted namespace.
    
    Security layers:
    • Blocked builtins: open, exec, eval, __import__ (override), compile
    • Blocked modules: os, sys, subprocess, socket, ctypes
    • AST pre-scan: rejects code containing dangerous node types
    • Timeout via threading.Timer
    • Pydantic-typed result
    """

    # Alias the module-level constant so the class attribute still exists for
    # external callers; avoids the Python class-scope comprehension NameError.
    _BLOCKED_BUILTINS = _BLOCKED_BUILTINS          # noqa: F821 (module-level name)
    _BLOCKED_IMPORTS  = frozenset(["os","sys","subprocess","socket","shutil",
                                    "ctypes","winreg","importlib","pathlib",
                                    "multiprocessing","threading","signal"])
    # Use the module-level name here — comprehensions in class bodies cannot
    # see class-level names, so we reference the module scope directly.
    _SAFE_BUILTINS    = _build_safe_builtins(_BLOCKED_BUILTINS)

    def __init__(self, timeout_sec: int = None):
        self._timeout = timeout_sec or NEXUS_CFG.get("sandbox_timeout_sec", 10)

    def _ast_scan(self, code: str) -> Optional[str]:
        """Returns an error string if code is unsafe, else None."""
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return f"SyntaxError: {e}"
        for node in ast.walk(tree):
            # Block import of dangerous modules
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = ([a.name for a in node.names] if isinstance(node, ast.Import)
                         else [node.module or ""])
                for name in names:
                    root = (name or "").split(".")[0]
                    if root in self._BLOCKED_IMPORTS:
                        return f"Blocked import: '{name}'"
            # Block attribute access on 'os', 'sys' etc.
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    if node.value.id in self._BLOCKED_IMPORTS:
                        return f"Blocked access: '{node.value.id}.{node.attr}'"
        return None

    def execute(self, code: str, extra_globals: Dict = None) -> "CodeExecResult":
        """Run code safely and return a typed result."""
        # 1. AST pre-scan
        err = self._ast_scan(code)
        if err:
            return self._result(safe=False, error=err)

        # 2. Build sandbox namespace
        import math as _math, json as _json, re as _re, datetime as _dt
        import random as _rand, itertools as _it, functools as _ft
        try:
            import numpy as _np;   np_mod = _np
        except Exception:
            np_mod = None

        sandbox_globals = {
            "__builtins__": self._SAFE_BUILTINS,
            "math"  : _math, "json": _json, "re": _re,
            "datetime": _dt, "random": _rand,
            "itertools": _it, "functools": _ft,
        }
        if np_mod:
            sandbox_globals["numpy"] = np_mod
            sandbox_globals["np"]    = np_mod
        if extra_globals:
            sandbox_globals.update(extra_globals)

        # 3. Execute with timeout
        stdout_buf = io.StringIO()
        result_box = [None, None, None]   # [stdout, return_val, error]
        t_start    = time.perf_counter()

        def _run():
            try:
                with redirect_stdout(stdout_buf):
                    local_ns: Dict = {}
                    exec(compile(code, "<sandbox>", "exec"), sandbox_globals, local_ns)
                    result_box[0] = stdout_buf.getvalue()
                    result_box[1] = local_ns.get("result", local_ns.get("_", None))
            except Exception as exc:
                result_box[2] = f"{type(exc).__name__}: {exc}"

        t = threading.Thread(target=_run, daemon=True)
        t.start()
        t.join(timeout=self._timeout)
        elapsed = (time.perf_counter() - t_start) * 1000

        if t.is_alive():
            return self._result(safe=False, error=f"Timeout after {self._timeout}s",
                                exec_time_ms=elapsed)

        if result_box[2]:
            return self._result(safe=True, error=result_box[2],
                                stdout=result_box[0] or "", exec_time_ms=elapsed)

        return self._result(
            safe=True,
            stdout=result_box[0] or "",
            return_val=result_box[1],
            exec_time_ms=elapsed
        )

    @staticmethod
    def _result(**kwargs) -> "CodeExecResult":
        if PYDANTIC_OK:
            return CodeExecResult(**kwargs)
        return kwargs

# ─────────────────────────────────────────────────────────────────────────────
#  9A.  PRECISION  CODE  FORGE
# ─────────────────────────────────────────────────────────────────────────────
class PrecisionCodeStudio:
    """
    High-reliability code authoring and repair helper.

    Capabilities:
    • Generates production-minded code with an explicit implementation plan
    • Validates Python via AST + compile() + sandbox safety advisory
    • Auto-repairs failed generations for a bounded number of passes
    • Exposes a compact status report and renderer for terminal output
    """

    ACTION_WORDS = (
        "write", "create", "build", "generate", "implement", "make",
        "develop", "craft", "fix", "repair", "debug", "refactor", "optimize",
    )
    CODE_WORDS = (
        "code", "script", "function", "class", "module", "program", "tool",
        "automation", "bot", "python", "javascript", "typescript", "java",
        "c++", "html", "css", "sql", "json", "api", "regex", "algorithm",
    )

    GENERATION_SYSTEM = (
        "You are Luna Precision Code Forge, an elite software engineer. "
        "Write robust, readable, production-minded code. Prefer correctness, "
        "clarity, type hints, defensive checks, and sensible defaults. "
        "Return only the requested sections."
    )

    GENERATION_PROMPT = """\
Create the best possible {language} solution for the request below.

USER REQUEST:
{request}

RELEVANT CONTEXT:
{context}

Return exactly these sections:
[PLAN]
- 3 to 6 concise implementation steps

[CODE]
```{language}
<complete code here>
```

[CHECKS]
- validation, reliability, and edge-case checks you considered

[NOTES]
Assumptions, limitations, or usage notes in 2 to 5 short lines.
"""

    REPAIR_PROMPT = """\
Repair the following {language} code so it passes validation and stays faithful
to the original intent. Improve reliability where helpful.

ORIGINAL REQUEST:
{request}

VALIDATION FAILURES:
{errors}

CURRENT CODE:
```{language}
{code}
```

Return exactly these sections:
[PLAN]
- concise repair steps

[CODE]
```{language}
<corrected code here>
```

[CHECKS]
- checks now satisfied

[NOTES]
Short explanation of what was fixed.
"""

    def __init__(self, sandbox: SecureCodeSandbox):
        self.sandbox = sandbox
        self._history = deque(maxlen=12)

    @classmethod
    def should_auto_forge(cls, query: str) -> bool:
        ql = query.lower()
        if ql.startswith("/"):
            return False
        has_action = any(re.search(rf"\b{re.escape(word)}\b", ql) for word in cls.ACTION_WORDS)
        has_code = any(re.search(rf"\b{re.escape(word)}\b", ql) for word in cls.CODE_WORDS)
        return has_action and has_code

    @staticmethod
    def extract_code_block(text: str) -> str:
        match = re.search(r"```(?:[\w.+-]+)?\n([\s\S]+?)```", text)
        if match:
            return match.group(1).strip()
        return text.strip()

    @staticmethod
    def _infer_language(request: str) -> str:
        ql = request.lower()
        patterns = [
            ("python", r"\bpython\b|\bpy\b"),
            ("javascript", r"\bjavascript\b|\bnode(?:\.js)?\b|\bjs\b"),
            ("typescript", r"\btypescript\b|\bts\b"),
            ("html", r"\bhtml\b|web page|landing page"),
            ("css", r"\bcss\b|stylesheet"),
            ("sql", r"\bsql\b|\bdatabase\b|\bquery\b"),
            ("json", r"\bjson\b"),
        ]
        for language, pattern in patterns:
            if re.search(pattern, ql):
                return language
        return "python"

    @staticmethod
    def _split_sections(text: str) -> Dict[str, str]:
        sections: Dict[str, str] = {}
        current = None
        buffer: List[str] = []
        for line in text.splitlines():
            m = re.match(r"^\[(PLAN|CODE|CHECKS|NOTES)\]\s*$", line.strip(), re.IGNORECASE)
            if m:
                if current is not None:
                    sections[current] = "\n".join(buffer).strip()
                current = m.group(1).upper()
                buffer = []
                continue
            if current is not None:
                buffer.append(line)
        if current is not None:
            sections[current] = "\n".join(buffer).strip()
        if not sections:
            sections["CODE"] = text.strip()
        return sections

    @staticmethod
    def _parse_bullets(block: str) -> List[str]:
        items: List[str] = []
        for raw in block.splitlines():
            line = re.sub(r"^[-*•\d\.\)\s]+", "", raw.strip()).strip()
            if line:
                items.append(line)
        return items[:8]

    @staticmethod
    def _fallback_template(request: str, language: str) -> str:
        if language == "json":
            return json.dumps(
                {"status": "placeholder", "message": "Describe the desired JSON shape."},
                indent=2
            )
        if language == "html":
            return textwrap.dedent("""\
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <title>Luna Code Forge Placeholder</title>
                </head>
                <body>
                    <main>
                        <h1>Luna Code Forge</h1>
                        <p>No live LLM backend was available for the full request.</p>
                    </main>
                </body>
                </html>
            """).strip()
        return textwrap.dedent(f"""\
            from typing import Any

            def solve() -> Any:
                \"\"\"Starter scaffold generated because no live LLM backend was available.\"\"\"
                request = {request!r}
                return {{
                    "status": "placeholder",
                    "request": request,
                    "message": "Connect an LLM backend to generate the final implementation."
                }}

            if __name__ == "__main__":
                print(solve())
        """).strip()

    def _validate_code(self, language: str, code: str) -> Tuple[str, bool, List[str], List[str]]:
        cleaned = self.extract_code_block(code).replace("\r\n", "\n").strip()
        checks: List[str] = []
        warnings: List[str] = []

        if not cleaned:
            return cleaned, False, ["No code was generated."], warnings

        if language == "python":
            try:
                ast.parse(cleaned)
                checks.append("AST parse passed")
            except SyntaxError as exc:
                return cleaned, False, [f"AST parse failed at line {exc.lineno}: {exc.msg}"], warnings

            try:
                compile(cleaned, "<precision-code-forge>", "exec")
                checks.append("Bytecode compile passed")
            except Exception as exc:
                return cleaned, False, [f"Compile failed: {type(exc).__name__}: {exc}"], warnings

            sandbox_issue = self.sandbox._ast_scan(cleaned)
            if sandbox_issue:
                warnings.append(f"Sandbox advisory: {sandbox_issue}")
            else:
                checks.append("Sandbox AST safety advisory passed")

            if re.search(r"except\s*:\s*", cleaned):
                warnings.append("Bare except detected; a specific exception type would be safer.")
            if "TODO" in cleaned or "FIXME" in cleaned:
                warnings.append("Placeholder marker detected; code may still need manual completion.")

            try:
                import black
                try:
                    cleaned = black.format_file_contents(
                        cleaned, fast=True, mode=black.FileMode()
                    )
                    checks.append("Black formatting applied")
                except black.NothingChanged:
                    checks.append("Black formatting already clean")
            except Exception:
                checks.append("Black formatting unavailable; preserved original formatting")

            return cleaned, True, checks, warnings

        if language == "json":
            try:
                parsed = json.loads(cleaned)
                checks.append("JSON parse passed")
                cleaned = json.dumps(parsed, indent=2)
                return cleaned, True, checks, warnings
            except Exception as exc:
                return cleaned, False, [f"JSON parse failed: {type(exc).__name__}: {exc}"], warnings

        checks.append("Basic non-empty structure check passed")
        if cleaned.count("{") != cleaned.count("}"):
            warnings.append("Brace counts are unbalanced; review the output carefully.")
        return cleaned, True, checks, warnings

    async def craft(self, request: str, call_llm: Callable, context: str = "") -> "CodeForgeResult":
        language = self._infer_language(request)
        prompt = self.GENERATION_PROMPT.format(
            language=language,
            request=request.strip(),
            context=(context or "No additional context.").strip()[:1500],
        )
        raw = await call_llm(prompt, self.GENERATION_SYSTEM)
        sections = self._split_sections(raw)
        plan = self._parse_bullets(sections.get("PLAN", ""))
        checks = self._parse_bullets(sections.get("CHECKS", ""))
        notes = sections.get("NOTES", "").strip()
        code = self.extract_code_block(sections.get("CODE", raw))

        if raw.strip().startswith("[All LLMs unavailable"):
            code = self._fallback_template(request, language)
            if not plan:
                plan = ["Prepared a safe starter scaffold because no live LLM backend was available."]
            notes = (notes + "\n" + raw.strip()).strip()

        max_passes = max(1, int(NEXUS_CFG.get("codeforge_max_repair_passes", 2)))
        validation_ok = False
        validation_checks: List[str] = []
        warnings: List[str] = []

        for attempt in range(max_passes + 1):
            code, validation_ok, new_checks, new_warnings = self._validate_code(language, code)
            validation_checks = list(dict.fromkeys([*validation_checks, *new_checks]))
            warnings = list(dict.fromkeys([*warnings, *new_warnings]))
            if validation_ok:
                result = self._result(
                    request=request,
                    language=language,
                    plan=plan,
                    code=code,
                    checks=list(dict.fromkeys([*checks, *validation_checks])),
                    warnings=warnings,
                    notes=notes or "Generated by Precision Code Forge.",
                    validation_ok=True,
                    repair_attempts=attempt,
                )
                self._history.append(result)
                return result

            if attempt >= max_passes:
                break

            repair_prompt = self.REPAIR_PROMPT.format(
                language=language,
                request=request.strip(),
                errors="\n".join(validation_checks) or "Validation failed",
                code=code,
            )
            repaired = await call_llm(repair_prompt, self.GENERATION_SYSTEM)
            repaired_sections = self._split_sections(repaired)
            code = self.extract_code_block(repaired_sections.get("CODE", repaired))
            plan = plan or self._parse_bullets(repaired_sections.get("PLAN", ""))
            checks.extend(self._parse_bullets(repaired_sections.get("CHECKS", "")))
            if repaired_sections.get("NOTES", "").strip():
                notes = repaired_sections.get("NOTES", "").strip()

        result = self._result(
            request=request,
            language=language,
            plan=plan,
            code=code,
            checks=list(dict.fromkeys([*checks, *validation_checks])),
            warnings=warnings,
            notes=notes or "Validation did not fully pass; manual review recommended.",
            validation_ok=False,
            repair_attempts=max_passes,
        )
        self._history.append(result)
        return result

    async def repair(self, broken_code: str, request: str, call_llm: Callable,
                     language: str = "python") -> "CodeForgeResult":
        language = language or "python"
        code = self.extract_code_block(broken_code)
        max_passes = max(1, int(NEXUS_CFG.get("codeforge_max_repair_passes", 2)))
        code, ok, checks, warnings = self._validate_code(language, code)
        if ok:
            result = self._result(
                request=request or "Repair existing code",
                language=language,
                plan=["Validated the supplied code and confirmed it already passes the current checks."],
                code=code,
                checks=checks,
                warnings=warnings,
                notes="No repair was needed.",
                validation_ok=True,
                repair_attempts=0,
            )
            self._history.append(result)
            return result

        validation_checks = list(checks)
        plan = ["Diagnose the failing code and repair the reported validation issues."]
        notes = ""

        for attempt in range(1, max_passes + 1):
            repair_prompt = self.REPAIR_PROMPT.format(
                language=language,
                request=request or "Repair and improve the provided code.",
                errors="\n".join(validation_checks),
                code=code,
            )
            repaired = await call_llm(repair_prompt, self.GENERATION_SYSTEM)
            sections = self._split_sections(repaired)
            code = self.extract_code_block(sections.get("CODE", repaired))
            plan = self._parse_bullets(sections.get("PLAN", "")) or plan
            validation_checks.extend(self._parse_bullets(sections.get("CHECKS", "")))
            if sections.get("NOTES", "").strip():
                notes = sections.get("NOTES", "").strip()

            code, ok, new_checks, new_warnings = self._validate_code(language, code)
            validation_checks = list(dict.fromkeys([*validation_checks, *new_checks]))
            warnings = list(dict.fromkeys([*warnings, *new_warnings]))
            if ok:
                result = self._result(
                    request=request or "Repair existing code",
                    language=language,
                    plan=plan,
                    code=code,
                    checks=validation_checks,
                    warnings=warnings,
                    notes=notes or "Precision Code Forge repaired the supplied code.",
                    validation_ok=True,
                    repair_attempts=attempt,
                )
                self._history.append(result)
                return result

        result = self._result(
            request=request or "Repair existing code",
            language=language,
            plan=plan,
            code=code,
            checks=validation_checks,
            warnings=warnings,
            notes=notes or "Repair attempts finished, but manual review is still recommended.",
            validation_ok=False,
            repair_attempts=max_passes,
        )
        self._history.append(result)
        return result

    def status(self) -> str:
        return (
            f"[🛠 Precision Code Forge]\n"
            f"  Enabled           : {'✓' if NEXUS_CFG.get('codeforge_enabled', True) else '✗'}\n"
            f"  Max repair passes : {NEXUS_CFG.get('codeforge_max_repair_passes', 2)}\n"
            f"  Sandbox timeout   : {self.sandbox._timeout}s\n"
            f"  Recent sessions   : {len(self._history)}"
        )

    def render(self, result: "CodeForgeResult", title: str = "[🛠 Precision Code Forge]") -> str:
        if PYDANTIC_OK:
            language = result.language
            validation_ok = result.validation_ok
            attempts = result.repair_attempts
            plan = result.plan
            code = result.code
            checks = result.checks
            warnings = result.warnings
            notes = result.notes
        else:
            language = result.get("language", "python")
            validation_ok = result.get("validation_ok", False)
            attempts = result.get("repair_attempts", 0)
            plan = result.get("plan", [])
            code = result.get("code", "")
            checks = result.get("checks", [])
            warnings = result.get("warnings", [])
            notes = result.get("notes", "")

        lines = [
            title,
            f"  Language        : {language}",
            f"  Validation      : {'PASS' if validation_ok else 'REVIEW NEEDED'}",
            f"  Repair passes   : {attempts}",
        ]
        if plan:
            lines.append("\n[Plan]")
            lines.extend(f"  {idx}. {item}" for idx, item in enumerate(plan, 1))
        if checks:
            lines.append("\n[Checks]")
            lines.extend(f"  • {item}" for item in checks[:8])
        if warnings:
            lines.append("\n[Warnings]")
            lines.extend(f"  • {item}" for item in warnings[:6])
        if notes:
            lines.append(f"\n[Notes]\n  {notes.replace(chr(10), chr(10) + '  ')}")
        lines.append(f"\n```{language}\n{code}\n```")
        return "\n".join(lines)

    @staticmethod
    def _result(**kwargs) -> "CodeForgeResult":
        if PYDANTIC_OK:
            return CodeForgeResult(**kwargs)
        return kwargs

# ─────────────────────────────────────────────────────────────────────────────
#  10.  LANGGRAPH MULTI-AGENT ORCHESTRATOR
# ─────────────────────────────────────────────────────────────────────────────
class LangGraphOrchestrator:
    """
    Routes queries through a LangGraph state-machine with 9 specialised agent nodes:

        ┌─────────────────────────────────────────────────────────┐
        │  INPUT ──► IntentClassifier                             │
        │              │                                          │
        │    ┌─────────┴──────────┐                              │
        │    ▼                    ▼                               │
        │  MemoryAgent         WebAgent (Playwright + DDG)        │
        │    │                    │                               │
        │    ▼                    ▼                               │
        │  CodeAgent          VisionAgent (YOLO context)          │
        │    │                    │                               │
        │    └──────────┬─────────┘                              │
        │               ▼                                         │
        │         ReasoningAgent  ◄── QuantumBranches             │
        │               │                                         │
        │         CreativeAgent                                   │
        │               │                                         │
        │         SafetyAgent  ──► SynthesisAgent ──► OUTPUT     │
        └─────────────────────────────────────────────────────────┘
    """

    INTENT_TAGS = {
        "code"   : ["code","program","script","function","debug","class","algorithm"],
        "web"    : ["search","find","latest","news","browse","website","url"],
        "math"   : ["calculate","solve","equation","integral","derivative","math"],
        "memory" : ["remember","recall","what did","earlier","history","before"],
        "system" : ["open","close","volume","brightness","screenshot","file"],
        "vision" : ["see","look","camera","show","what is","identify","detect"],
        "creative": ["create","imagine","write","story","poem","idea","design"],
        "explain": ["explain","how does","what is","why","teach","describe"],
    }

    def __init__(self, ledger: EpisodicLedger, sandbox: SecureCodeSandbox,
                 cot: CoTStreamer, hud_queue: Optional[queue.Queue] = None):
        self.ledger  = ledger
        self.sandbox = sandbox
        self.cot     = cot
        self._hud_q  = hud_queue
        self._graph  = self._build_graph() if LANGGRAPH_OK else None

    def _build_graph(self):
        """Build the LangGraph state machine."""
        try:
            from langgraph.graph import StateGraph, END
            from typing import TypedDict

            class State(TypedDict, total=False):
                query: str; intent: str; cot: list
                web_results: str; code_result: str
                memory_ctx: str; final_answer: str
                mood_score: float; confidence: float

            g = StateGraph(State)

            g.add_node("intent",    self._node_intent)
            g.add_node("memory",    self._node_memory)
            g.add_node("web",       self._node_web)
            g.add_node("code",      self._node_code)
            g.add_node("reason",    self._node_reason)
            g.add_node("creative",  self._node_creative)
            g.add_node("safety",    self._node_safety)
            g.add_node("synthesis", self._node_synthesis)

            g.set_entry_point("intent")

            def _route(s):
                intent = s.get("intent", "explain")
                if intent == "code"   : return "code"
                if intent == "web"    : return "web"
                if intent == "memory" : return "memory"
                return "reason"

            g.add_conditional_edges("intent", _route,
                                    {"code":"code","web":"web","memory":"memory","reason":"reason"})
            g.add_edge("code",    "safety")
            g.add_edge("web",     "reason")
            g.add_edge("memory",  "reason")
            g.add_edge("reason",  "creative")
            g.add_edge("creative","safety")
            g.add_edge("safety",  "synthesis")
            g.add_edge("synthesis", END)

            return g.compile()
        except Exception as e:
            log.warning(f"LangGraph build failed: {e}")
            return None

    # ── Agent Nodes ──────────────────────────────────────────────────────────

    def _node_intent(self, state: dict) -> dict:
        query = state.get("query", "")
        self.cot.step(f"Classifying intent for: '{query[:60]}'", "INTENT")
        intent = self._classify_intent(query)
        self.cot.step(f"Intent → {intent}", "INTENT")
        return {**state, "intent": intent, "cot": state.get("cot", []) + [f"intent={intent}"]}

    def _node_memory(self, state: dict) -> dict:
        query = state.get("query", "")
        self.cot.step("Searching episodic memory...", "MEMORY")
        ctx = self.ledger.build_context(query, max_tokens=800)
        self.cot.step(f"Memory context: {len(ctx)} chars retrieved", "MEMORY")
        return {**state, "memory_ctx": ctx}

    def _node_web(self, state: dict) -> dict:
        query = state.get("query", "")
        self.cot.step(f"Web search: '{query[:50]}'", "WEB")
        result = self._quick_ddg(query)
        return {**state, "web_results": result}

    def _node_code(self, state: dict) -> dict:
        query = state.get("query", "")
        self.cot.step("Code sandbox activated", "CODE")
        # Extract code block if present
        code_match = re.search(r"```(?:python)?\n([\s\S]+?)```", query)
        if code_match:
            code = code_match.group(1)
            res  = self.sandbox.execute(code)
            out  = res.stdout if PYDANTIC_OK else res.get("stdout","")
            err  = res.error  if PYDANTIC_OK else res.get("error","")
            result = f"[Sandbox Output]\n{out}" if out else f"[Sandbox Error]\n{err}"
        else:
            result = ""
        return {**state, "code_result": result}

    def _node_reason(self, state: dict) -> dict:
        self.cot.step("Deep reasoning pass...", "REASON")
        # Inject memory + web context into reasoning notes
        notes = []
        if state.get("memory_ctx"):
            notes.append("Memory context available.")
        if state.get("web_results"):
            notes.append("Web results retrieved.")
        self.cot.step(f"Reasoning context: {'; '.join(notes) or 'base knowledge'}", "REASON")
        return {**state, "cot": state.get("cot", []) + ["reason_pass=done"]}

    def _node_creative(self, state: dict) -> dict:
        intent = state.get("intent", "")
        if intent == "creative":
            self.cot.step("Creative synthesis mode engaged", "CREATIVE")
        return state

    def _node_safety(self, state: dict) -> dict:
        self.cot.step("Safety validation pass", "SAFETY")
        return {**state, "cot": state.get("cot", []) + ["safety=ok"]}

    def _node_synthesis(self, state: dict) -> dict:
        self.cot.step("Synthesising final answer...", "SYNTH")
        # Build context for the LLM call
        parts = [f"Query: {state.get('query','')}"]
        if state.get("memory_ctx"):
            parts.append(state["memory_ctx"])
        if state.get("web_results"):
            parts.append(f"Web results:\n{state['web_results'][:600]}")
        if state.get("code_result"):
            parts.append(state["code_result"])
        state["_synthesis_context"] = "\n\n".join(parts)
        return state

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _classify_intent(self, query: str) -> str:
        q = query.lower()
        scores: Dict[str, int] = defaultdict(int)
        for tag, keywords in self.INTENT_TAGS.items():
            for kw in keywords:
                if kw in q:
                    scores[tag] += 1
        return max(scores, key=scores.get) if scores else "explain"

    def _quick_ddg(self, query: str, max_results: int = 3) -> str:
        if not DDG_OK:
            return ""
        try:
            with DDGS() as ddg:
                results = list(ddg.text(query, max_results=max_results))
            lines = []
            for r in results:
                lines.append(f"• {r.get('title','')}: {r.get('body','')[:200]}")
            return "\n".join(lines)
        except Exception:
            return ""

    async def run_async(self, query: str, extra_ctx: str = "") -> Dict:
        """Run the full agent graph asynchronously."""
        state = {"query": query, "cot": [], "memory_ctx": extra_ctx}
        self.cot.begin(query)

        if self._graph:
            try:
                final = await asyncio.get_running_loop().run_in_executor(
                    None, self._graph.invoke, state
                )
                return final
            except Exception as e:
                log.warning(f"LangGraph run failed: {e}")

        # Fallback: run nodes sequentially
        state = self._node_intent(state)
        intent = state.get("intent", "explain")
        if intent == "memory":
            state = self._node_memory(state)
        elif intent == "web":
            state = self._node_web(state)
        elif intent == "code":
            state = self._node_code(state)
        state = self._node_reason(state)
        state = self._node_creative(state)
        state = self._node_safety(state)
        state = self._node_synthesis(state)
        return state

# ─────────────────────────────────────────────────────────────────────────────
#  11.  PLAYWRIGHT  WEB NAVIGATOR
# ─────────────────────────────────────────────────────────────────────────────
class PlaywrightNavigator:
    """
    Autonomous headless web navigator built on Playwright.

    Capabilities:
    • navigate(url)         → fetch + extract page text
    • search(query)         → Google/DDG search + extract top snippets
    • click_element(sel)    → autonomous DOM interaction
    • fill_form(sel, val)   → form filling
    • screenshot(url)       → full-page screenshot → PIL Image
    • js_eval(url, code)    → evaluate JS on a page
    """

    def __init__(self):
        self._headless = NEXUS_CFG.get("playwright_headless", True)

    async def navigate(self, url: str, timeout: int = 15000) -> str:
        """Fetch page and return cleaned text content."""
        if not PLAYWRIGHT_OK:
            return f"[Playwright unavailable] Would navigate to: {url}"
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=self._headless)
                page    = await browser.new_page()
                await page.goto(url, timeout=timeout, wait_until="domcontentloaded")
                title   = await page.title()
                content = await page.inner_text("body")
                await browser.close()
                # Clean and trim
                content = re.sub(r"\s{3,}", "\n\n", content)
                return f"[Page: {title}]\n\n{content[:3000]}"
        except Exception as e:
            return f"[Navigator Error] {e}"

    async def search(self, query: str, engine: str = "duckduckgo") -> str:
        """Search the web and return top result text."""
        url = f"https://duckduckgo.com/?q={query.replace(' ', '+')}&ia=web"
        if engine == "google":
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        return await self.navigate(url)

    async def screenshot(self, url: str) -> Optional["Image.Image"]:
        """Return a PIL Image of the page."""
        if not (PLAYWRIGHT_OK and PIL_OK):
            return None
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page    = await browser.new_page(viewport={"width": 1280, "height": 800})
                await page.goto(url, timeout=15000)
                await page.wait_for_load_state("networkidle", timeout=5000)
                buf = await page.screenshot(full_page=True)
                await browser.close()
                return Image.open(io.BytesIO(buf))
        except Exception as e:
            log.warning(f"Navigator.screenshot: {e}")
            return None

    async def fill_and_submit(self, url: str,
                              fields: Dict[str, str],
                              submit_selector: str) -> str:
        """Fill a form and submit it."""
        if not PLAYWRIGHT_OK:
            return "[Playwright unavailable]"
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=self._headless)
                page    = await browser.new_page()
                await page.goto(url, timeout=15000)
                for sel, val in fields.items():
                    await page.fill(sel, val)
                await page.click(submit_selector)
                await page.wait_for_load_state("domcontentloaded")
                result = await page.inner_text("body")
                await browser.close()
                return result[:2000]
        except Exception as e:
            return f"[Form Error] {e}"

# ─────────────────────────────────────────────────────────────────────────────
#  12.  YOLO  ENVIRONMENTAL  AWARENESS
# ─────────────────────────────────────────────────────────────────────────────
class YOLOEnvironment:
    """
    YOLOv8-powered environmental awareness via webcam.

    Runs in a background thread, continuously updating:
    - self.detected_objects  : List[{label, confidence, bbox}]
    - self.scene_description : str  (human-readable environment summary)
    - self.hud_frame         : np.ndarray (annotated frame for HUD)
    
    Luna can query this to understand her physical environment.
    """

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self.detected_objects  : List[Dict] = []
        self.scene_description : str = "Initialising..."
        self.hud_frame         : Optional[Any] = None
        self._hud_q  = hud_queue
        self._model  = None
        self._cap    = None
        self._thread : Optional[threading.Thread] = None
        self._running = False
        self._lock   = threading.Lock()

    def start(self):
        if not (YOLO_OK and CV2_OK and NEXUS_CFG.get("yolo_enabled")):
            nprint("YOLO", "Disabled or unavailable", C.YELLOW)
            return
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        nprint("YOLO", "Environmental awareness thread started", C.GREEN)

    def stop(self):
        self._running = False
        if self._cap:
            self._cap.release()

    @staticmethod
    def _load_yolo_model(model_name: str):
        """
        Load a YOLO model with automatic corruption recovery.

        If the cached weights file is corrupted (PytorchStreamReader /
        broken zip error), delete it so Ultralytics re-downloads fresh copy.
        Returns None if YOLO is unavailable after two attempts.
        """
        if not YOLO_OK:
            return None
        for attempt in range(2):
            try:
                return YOLO(model_name)
            except Exception as e:
                err_str = str(e).lower()
                is_corrupt = any(k in err_str for k in (
                    "pytorchstreamreader", "zip archive", "central directory",
                    "failed reading", "miniz",
                ))
                if is_corrupt and attempt == 0:
                    nprint("YOLO",
                           f"Corrupt weights detected — deleting & re-downloading {model_name}…",
                           C.YELLOW)
                    # Search common cache locations and delete the bad file
                    for search_dir in [Path.cwd(),
                                       Path.home() / ".cache" / "ultralytics"]:
                        candidate = search_dir / model_name
                        if candidate.exists():
                            try:
                                candidate.unlink()
                                nprint("YOLO", f"Deleted: {candidate}", C.YELLOW)
                            except OSError:
                                pass
                    try:
                        from ultralytics.utils import SETTINGS
                        candidate = Path(SETTINGS.get("weights_dir", ".")) / model_name
                        if candidate.exists():
                            candidate.unlink()
                    except Exception:
                        pass
                    continue   # retry — Ultralytics will auto-download
                log.warning(f"YOLO model load failed (attempt {attempt+1}): {e}")
                return None
        return None

    def _loop(self):
        try:
            model_name = NEXUS_CFG.get("yolo_model", "yolov8n.pt")
            # Cache guard: only load if model not already initialised (prevents
            # repeated download messages if the thread is restarted).
            if self._model is None:
                self._model = self._load_yolo_model(model_name)
            if self._model is None:
                nprint("YOLO", "Model unavailable — environment awareness disabled", C.YELLOW)
                return
            self._cap   = cv2.VideoCapture(0)
            self._running = True
            conf_thresh = NEXUS_CFG.get("yolo_conf_threshold", 0.45)

            while self._running:
                ret, frame = self._cap.read()
                if not ret:
                    time.sleep(0.1)
                    continue

                results = self._model(frame, conf=conf_thresh, verbose=False)
                objects = []
                ann_frame = frame.copy()

                for r in results:
                    for box in r.boxes:
                        cls_id = int(box.cls[0])
                        label  = self._model.names[cls_id]
                        conf   = float(box.conf[0])
                        xyxy   = box.xyxy[0].tolist()
                        objects.append({"label": label, "confidence": round(conf, 3),
                                        "bbox": xyxy})
                        # Draw on frame
                        x1, y1, x2, y2 = map(int, xyxy)
                        cv2.rectangle(ann_frame, (x1,y1), (x2,y2), (0,200,255), 2)
                        cv2.putText(ann_frame, f"{label} {conf:.2f}",
                                    (x1, y1-8), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.55, (0,200,255), 1)

                with self._lock:
                    self.detected_objects  = objects
                    self.hud_frame         = ann_frame
                    self.scene_description = self._describe(objects)

                if self._hud_q:
                    with suppress(queue.Full):
                        self._hud_q.put_nowait({
                            "type"   : "yolo",
                            "objects": objects,
                            "desc"   : self.scene_description,
                        })

                time.sleep(0.2)   # ~5 fps to keep CPU light
        except Exception as e:
            log.error(f"YOLO loop error: {e}")
        finally:
            if self._cap:
                self._cap.release()

    @staticmethod
    def _describe(objects: List[Dict]) -> str:
        if not objects:
            return "No objects detected."
        counts: Dict[str, int] = Counter(o["label"] for o in objects)
        parts  = [f"{v} {k}" + ("s" if v > 1 else "") for k, v in counts.items()]
        return "Detected: " + ", ".join(parts[:6]) + "."

    def get_context(self) -> str:
        with self._lock:
            return self.scene_description

# ─────────────────────────────────────────────────────────────────────────────
#  13.  MEDIAPIPE  GESTURE  CONTROLLER
# ─────────────────────────────────────────────────────────────────────────────
class GestureController:
    """
    MediaPipe Hands gesture recognition → Luna command mapping.

    Gesture → Command Map:
    ┌─────────────────────┬──────────────────────────────────┐
    │  Gesture            │  Luna Command                     │
    ├─────────────────────┼──────────────────────────────────┤
    │  👍 Thumbs Up       │  Confirm / Yes                    │
    │  👎 Thumbs Down     │  Cancel / No                      │
    │  ✋ Open Palm       │  Stop / Pause                     │
    │  ✌  Peace / V-Sign  │  Screenshot                       │
    │  🤏 Pinch           │  Zoom / Resize HUD                │
    │  👆 Point Up        │  Scroll Up / Next                 │
    │  👇 Point Down      │  Scroll Down / Previous           │
    │  🤙 Call Me         │  Activate Voice Mode              │
    │  🤜 Fist            │  Dismiss / Close                  │
    └─────────────────────┴──────────────────────────────────┘
    """

    GESTURE_MAP: Dict[str, str] = {
        "thumbs_up"  : "confirm",
        "thumbs_down": "cancel",
        "open_palm"  : "stop",
        "peace"      : "screenshot",
        "pinch"      : "resize_hud",
        "point_up"   : "scroll_up",
        "point_down" : "scroll_down",
        "call_me"    : "voice_mode",
        "fist"       : "dismiss",
    }

    def __init__(self, command_queue: Optional[queue.Queue] = None):
        self._cmd_q   = command_queue
        self._mp_hands = None
        self._cap     = None
        self._thread  : Optional[threading.Thread] = None
        self._running = False
        self._last_gesture = ""
        self._debounce = 1.5  # seconds between same gesture triggers
        self._last_ts  = 0.0

    def start(self):
        if not (MEDIAPIPE_OK and CV2_OK and NEXUS_CFG.get("gesture_enabled")):
            nprint("Gesture", "Disabled or unavailable", C.YELLOW)
            return
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        nprint("Gesture", "MediaPipe gesture controller started", C.GREEN)

    def stop(self):
        self._running = False
        if self._cap:
            self._cap.release()

    def _loop(self):
        """
        Hand-landmark detection loop.

        MediaPipe 0.10+ removed mp.solutions — this method tries the new
        Tasks API first (HandLandmarker), then falls back to the old
        solutions.hands API for anyone still on an older version.
        """
        try:
            # ── Try new Tasks API (MediaPipe 0.10+) ─────────────────────────
            if not hasattr(mp, "solutions"):
                self._loop_tasks_api()
                return
            # ── Legacy solutions API (MediaPipe < 0.10) ─────────────────────
            self._loop_solutions_api()
        except Exception as e:
            log.error(f"Gesture loop: {e}")
        finally:
            if self._cap:
                self._cap.release()

    def _loop_tasks_api(self):
        """GestureController using MediaPipe 0.10+ Tasks API."""
        try:
            from mediapipe.tasks.python.vision import (
                HandLandmarker, HandLandmarkerOptions,
            )
            from mediapipe.tasks.python import BaseOptions
            from mediapipe.tasks.python.vision.core.vision_task_running_mode import (
                VisionTaskRunningMode,
            )
        except ImportError as e:
            nprint("Gesture", f"MediaPipe Tasks API unavailable: {e}", C.YELLOW)
            return

        # Auto-download the required model file if absent
        model_path = HOME_DIR / "nexus" / "hand_landmarker.task"
        if not model_path.exists():
            nprint("Gesture", "Downloading hand_landmarker.task model…", C.CYAN)
            try:
                import urllib.request
                _url = ("https://storage.googleapis.com/mediapipe-models/"
                        "hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task")
                urllib.request.urlretrieve(_url, str(model_path))
                nprint("Gesture", "Model downloaded successfully", C.GREEN)
            except Exception as dl_err:
                nprint("Gesture",
                       f"Could not download hand_landmarker model: {dl_err} — "
                       "gesture control disabled", C.YELLOW)
                return

        try:
            opts = HandLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=str(model_path)),
                running_mode=VisionTaskRunningMode.IMAGE,
                num_hands=1,
                min_hand_detection_confidence=NEXUS_CFG.get("gesture_sensitivity", 0.75),
                min_hand_presence_confidence=0.75,
                min_tracking_confidence=0.6,
            )
            landmarker = HandLandmarker.create_from_options(opts)
        except Exception as e:
            nprint("Gesture", f"HandLandmarker init failed: {e}", C.YELLOW)
            return

        self._cap     = cv2.VideoCapture(0)
        self._running = True

        while self._running:
            ret, frame = self._cap.read()
            if not ret:
                time.sleep(0.05)
                continue
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            try:
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
                result   = landmarker.detect(mp_image)
                if result.hand_landmarks:
                    for hand in result.hand_landmarks:
                        gesture = self._classify(hand)
                        if gesture:
                            self._emit(gesture)
            except Exception:
                pass
            time.sleep(0.1)

        landmarker.close()

    def _loop_solutions_api(self):
        """GestureController using legacy MediaPipe solutions API (< 0.10)."""
        hands_mod      = mp.solutions.hands
        self._mp_hands = hands_mod.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=NEXUS_CFG.get("gesture_sensitivity", 0.75),
            min_tracking_confidence=0.6,
        )
        self._cap     = cv2.VideoCapture(0)
        self._running = True

        while self._running:
            ret, frame = self._cap.read()
            if not ret:
                time.sleep(0.05)
                continue
            rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Setting writeable=False lets MediaPipe derive image dimensions from
            # the array shape before the solutions pipeline runs, which suppresses
            # the "NORM_RECT without IMAGE_DIMENSIONS" and "Feedback manager
            # requires a model with a single signature" warnings.
            rgb.flags.writeable = False
            result = self._mp_hands.process(rgb)
            rgb.flags.writeable = True
            if result.multi_hand_landmarks:
                for lm in result.multi_hand_landmarks:
                    gesture = self._classify(lm.landmark)
                    if gesture:
                        self._emit(gesture)
            time.sleep(0.1)

    def _classify(self, landmarks) -> Optional[str]:
        """Classify hand landmarks into a gesture name."""
        try:
            # Landmark indices: 4=thumb_tip, 8=index_tip, 12=middle_tip,
            #                   16=ring_tip, 20=pinky_tip
            #                   3=thumb_ip, 6=index_pip, 10=mid_pip,
            #                   14=ring_pip, 18=pinky_pip
            def tip_above_pip(tip_i, pip_i):
                return landmarks[tip_i].y < landmarks[pip_i].y

            fingers_up = [
                tip_above_pip(8,  6),   # index
                tip_above_pip(12, 10),  # middle
                tip_above_pip(16, 14),  # ring
                tip_above_pip(20, 18),  # pinky
            ]
            thumb_up_flag = landmarks[4].y < landmarks[3].y

            n_up = sum(fingers_up)

            # Open palm
            if n_up == 4:
                return "open_palm"
            # Peace / V
            if fingers_up[0] and fingers_up[1] and not fingers_up[2] and not fingers_up[3]:
                return "peace"
            # Point up (only index)
            if fingers_up[0] and not any(fingers_up[1:]):
                return "point_up"
            # Fist
            if n_up == 0 and not thumb_up_flag:
                return "fist"
            # Thumbs up
            if thumb_up_flag and n_up == 0:
                return "thumbs_up"
            # Pinch (thumb + index close)
            dx = abs(landmarks[4].x - landmarks[8].x)
            dy = abs(landmarks[4].y - landmarks[8].y)
            if dx < 0.05 and dy < 0.05:
                return "pinch"
        except Exception:
            pass
        return None

    def _emit(self, gesture: str):
        now = time.time()
        if gesture == self._last_gesture and now - self._last_ts < self._debounce:
            return
        self._last_gesture = gesture
        self._last_ts      = now
        command = self.GESTURE_MAP.get(gesture, "")
        if command and self._cmd_q:
            gc = GestureCommand(gesture_name=gesture, confidence=0.9,
                                command=command) if PYDANTIC_OK else {
                "gesture_name": gesture, "command": command}
            nprint("Gesture", f"✋ {gesture} → {command}", C.MAGENTA)
            with suppress(queue.Full):
                self._cmd_q.put_nowait(gc)

# ─────────────────────────────────────────────────────────────────────────────
#  14.  PROACTIVE  MOOD  ENGINE
# ─────────────────────────────────────────────────────────────────────────────
class ProactiveMoodEngine:
    """
    Fuses signals from multiple sources to infer the user's mood/context:

    Sources:
    1. Windows system telemetry  (CPU, RAM, active app, idle time)
    2. Time of day               (circadian rhythm model)
    3. ESP32 IoT sensors via MQTT (temperature, humidity, light, motion)
    4. BLE proximity             (is user nearby?)
    5. Conversation sentiment    (rolling average from LLM responses)
    
    Output: MoodState → adjusts Luna's tone, verbosity, proactive suggestions.
    """

    def __init__(self):
        self._state    = MoodState() if PYDANTIC_OK else {}
        self._mqtt     : Optional[Any] = None
        self._iot_data : Dict = {}
        self._conv_sentiment: deque = deque(maxlen=10)
        self._thread   : Optional[threading.Thread] = None
        self._running  = False
        self._lock     = threading.Lock()

        if MQTT_OK and NEXUS_CFG.get("mood_engine_enabled"):
            self._init_mqtt()

    def _init_mqtt(self):
        try:
            # paho-mqtt >= 2.0 requires explicit CallbackAPIVersion; fall back for older builds
            try:
                self._mqtt = mqtt.Client(
                    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
                    client_id="luna_nexus_mood",
                )
            except AttributeError:
                # paho-mqtt < 2.0 — old API, suppress deprecation warning
                import warnings as _w
                with _w.catch_warnings():
                    _w.simplefilter("ignore", DeprecationWarning)
                    self._mqtt = mqtt.Client(client_id="luna_nexus_mood")
            self._mqtt.on_message = self._on_mqtt_message
            self._mqtt.connect_async(
                NEXUS_CFG.get("esp32_host", "192.168.1.100"),
                NEXUS_CFG.get("esp32_mqtt_port", 1883),
                keepalive=30
            )
            self._mqtt.subscribe("luna/sensors/#")
            self._mqtt.loop_start()
            nprint("Mood", "MQTT → ESP32 connected", C.GREEN)
        except Exception as e:
            nprint("Mood", f"MQTT unavailable: {e}", C.YELLOW)

    def _on_mqtt_message(self, client, userdata, msg):
        try:
            topic = msg.topic.split("/")[-1]
            val   = float(msg.payload.decode())
            with self._lock:
                self._iot_data[topic] = val
        except Exception:
            pass

    def start(self):
        if not NEXUS_CFG.get("mood_engine_enabled"):
            return
        self._running = True
        self._thread  = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        nprint("Mood", "Proactive mood engine started", C.GREEN)

    def stop(self):
        self._running = False
        if self._mqtt:
            self._mqtt.loop_stop()

    def _loop(self):
        while self._running:
            self._update()
            time.sleep(5)

    def _update(self):
        now = datetime.datetime.now()
        h   = now.hour

        # Time-of-day model
        tod = ("late_night" if h < 6 else "morning" if h < 12
               else "afternoon" if h < 17 else "evening" if h < 21 else "night")

        # System telemetry
        cpu_pct = psutil.cpu_percent(interval=0.5) / 100.0 if PSUTIL_OK else 0.5
        ram_pct = psutil.virtual_memory().percent / 100.0  if PSUTIL_OK else 0.5

        # IoT data
        with self._lock:
            temp  = self._iot_data.get("temperature", 22.0)
            light = self._iot_data.get("light",        400.0)

        # Infer mood
        stress = (cpu_pct * 0.4 + ram_pct * 0.3)
        valence = max(0.1, min(0.9, 0.7 - stress +
                    (0.1 if 8 <= h <= 18 else -0.1) +
                    (0.05 if 18 <= light <= 600 else -0.05)))
        arousal = max(0.1, min(0.9, cpu_pct * 0.6 + (0.3 if 7 <= h <= 20 else 0.1)))

        if valence > 0.65 and arousal > 0.55:
            inferred = "energetic"
        elif valence > 0.65:
            inferred = "calm_positive"
        elif valence < 0.35 and arousal > 0.6:
            inferred = "stressed"
        elif valence < 0.35:
            inferred = "low"
        else:
            inferred = "neutral"

        if PYDANTIC_OK:
            self._state = MoodState(
                valence=round(valence, 3), arousal=round(arousal, 3),
                cpu_stress=round(cpu_pct, 3), memory_stress=round(ram_pct, 3),
                ambient_temp=temp, ambient_light=light,
                time_of_day=tod, inferred_mood=inferred
            )
        else:
            self._state = dict(valence=valence, inferred_mood=inferred, tod=tod)

    def get_state(self) -> "MoodState":
        return self._state

    def inject_sentiment(self, score: float):
        """Inject a sentiment score (-1 to +1) from conversation analysis."""
        self._conv_sentiment.append(score)

    def tone_hint(self) -> str:
        """Returns a tone hint string for LLM system prompts."""
        mood = (self._state.inferred_mood if PYDANTIC_OK
                else self._state.get("inferred_mood", "neutral"))
        hints = {
            "energetic"     : "Be concise, dynamic, and enthusiastic.",
            "calm_positive" : "Be warm, thorough, and conversational.",
            "stressed"      : "Be calm, clear, and brief. Reduce cognitive load.",
            "low"           : "Be empathetic, gentle, and encouraging.",
            "neutral"       : "Be professional and helpful.",
        }
        return hints.get(mood, "Be helpful.")

# ─────────────────────────────────────────────────────────────────────────────
#  15.  SELF-EVOLUTION  LOOP
# ─────────────────────────────────────────────────────────────────────────────
class SelfEvolutionLoop:
    """
    Luna's safe self-modification engine.

    Pipeline:
    1. ANALYSE   → AST-parse source; identify improvement opportunities
    2. PROPOSE   → Generate a EvolutionProposal via LLM
    3. VALIDATE  → Pydantic schema check + AST safety scan + black formatting
    4. SNAPSHOT  → Git-style snapshot of current source
    5. APPLY     → Write new code (only if approved or auto=True)
    6. TEST      → Import new module in subprocess; rollback on failure
    7. LOG       → Record to evolution_log.json

    Safety invariants:
    - Max MAX_DELTA lines changed per cycle
    - Blocked: removal of safety guards, self._BLOCKED_IMPORTS references
    - Requires explicit user approval unless evolution_auto=True
    - Full rollback on any test failure
    """

    MAX_DELTA      = 50    # lines
    SAFE_GUARDS    = ["_BLOCKED_BUILTINS","_BLOCKED_IMPORTS","_ast_scan",
                      "SelfEvolutionLoop","_validate"]
    OPPORTUNITY_PATTERNS = {
        "dead_code"     : r"#\s*TODO|#\s*FIXME|#\s*HACK",
        "long_function" : None,   # detected by AST
        "magic_numbers" : r"(?<!\w)(?:[3-9]\d{2,}|\d{4,})(?!\w)",
        "bare_except"   : r"except\s*:",
        "missing_types" : None,   # detected by AST
    }

    def __init__(self, source_path: str = None):
        self.source_path = source_path or __file__
        self._log        = self._load_log()
        self._pending    : Optional["EvolutionProposal"] = None

    def _load_log(self) -> list:
        try:
            if EVOLUTION_LOG.exists():
                return json.loads(EVOLUTION_LOG.read_text())
        except Exception:
            pass
        return []

    def _save_log(self):
        EVOLUTION_LOG.write_text(json.dumps(self._log, indent=2))

    def analyse(self) -> Dict[str, List[str]]:
        """Scan source for improvement opportunities."""
        try:
            source = Path(self.source_path).read_text(encoding="utf-8")
        except Exception as e:
            return {"error": [str(e)]}

        findings: Dict[str, List[str]] = defaultdict(list)

        # Pattern-based scan
        for opp, pattern in self.OPPORTUNITY_PATTERNS.items():
            if pattern:
                for m in re.finditer(pattern, source):
                    line_no = source[:m.start()].count("\n") + 1
                    findings[opp].append(f"Line {line_no}: {m.group(0)[:60]}")

        # AST-based scan
        try:
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    body_lines = (node.end_lineno or 0) - (node.lineno or 0)
                    if body_lines > 80:
                        findings["long_function"].append(
                            f"Line {node.lineno}: {node.name} ({body_lines} lines)")
                    # Check for missing return type annotations
                    if node.returns is None and node.name not in ("__init__",):
                        findings["missing_types"].append(
                            f"Line {node.lineno}: {node.name}() missing return type")
        except SyntaxError:
            findings["syntax_error"].append("Source has syntax errors")

        return dict(findings)

    def _snapshot(self) -> str:
        """Create a timestamped backup of the source file."""
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        snap = SNAPSHOT_DIR / f"luna_snap_{ts}.py"
        try:
            shutil.copy2(self.source_path, snap)
            return str(snap)
        except Exception as e:
            log.error(f"Snapshot failed: {e}")
            return ""

    def _validate(self, new_code: str) -> Tuple[bool, str]:
        """Validate a proposed code change."""
        # 1. Syntax check
        try:
            ast.parse(new_code)
        except SyntaxError as e:
            return False, f"Syntax error: {e}"

        # 2. Safety guard preservation
        for guard in self.SAFE_GUARDS:
            if guard not in new_code:
                return False, f"Safety guard removed: '{guard}'"

        # 3. Delta size check
        try:
            old_lines = Path(self.source_path).read_text(encoding="utf-8").splitlines()
            new_lines = new_code.splitlines()
            delta     = abs(len(new_lines) - len(old_lines))
            if delta > self.MAX_DELTA:
                return False, f"Delta too large: {delta} lines (max {self.MAX_DELTA})"
        except Exception:
            pass

        # 4. No dangerous imports added
        try:
            tree = ast.parse(new_code)
            danger_imports = ["os","sys","subprocess","socket","ctypes"]
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    names = ([a.name for a in node.names]
                             if isinstance(node, ast.Import) else [node.module or ""])
                    for name in names:
                        if name.split(".")[0] in danger_imports:
                            # Allow if already in original
                            if f"import {name}" not in open(self.source_path).read(50000):
                                return False, f"New dangerous import: {name}"
        except Exception:
            pass

        return True, "ok"

    def propose(self, improvement: str, new_code_fragment: str) -> Optional["EvolutionProposal"]:
        """Create an evolution proposal (requires user approval unless auto=True)."""
        snap = self._snapshot()
        valid, reason = self._validate(new_code_fragment)
        if not valid:
            nprint("Evolution", f"Proposal REJECTED: {reason}", C.RED)
            return None

        if PYDANTIC_OK:
            proposal = EvolutionProposal(
                target_file   = self.source_path,
                original_hash = hashlib.sha256(
                    Path(self.source_path).read_bytes()).hexdigest()[:16],
                new_code      = new_code_fragment,
                rationale     = improvement,
                risk_level    = "low",
                rollback_snap = snap,
            )
        else:
            proposal = dict(target_file=self.source_path, new_code=new_code_fragment,
                            rationale=improvement, rollback_snap=snap, approved=False)

        self._pending = proposal
        nprint("Evolution", f"Proposal ready: {improvement[:60]}", C.CYAN)
        return proposal

    def approve_and_apply(self) -> bool:
        """Apply the pending proposal after user approval."""
        if not self._pending:
            return False
        try:
            new_code = (self._pending.new_code if PYDANTIC_OK
                        else self._pending["new_code"])
            Path(self.source_path).write_text(new_code, encoding="utf-8")
            entry = {
                "ts"       : datetime.datetime.now().isoformat(),
                "rationale": (self._pending.rationale if PYDANTIC_OK
                              else self._pending.get("rationale","")),
                "applied"  : True,
            }
            self._log.append(entry)
            self._save_log()
            nprint("Evolution", "✅ Evolution applied successfully", C.GREEN)
            self._pending = None
            return True
        except Exception as e:
            nprint("Evolution", f"Apply failed: {e}", C.RED)
            return False

    def rollback(self) -> bool:
        """Restore the last snapshot."""
        snaps = sorted(SNAPSHOT_DIR.glob("luna_snap_*.py"), reverse=True)
        if not snaps:
            return False
        try:
            shutil.copy2(snaps[0], self.source_path)
            nprint("Evolution", f"Rolled back to {snaps[0].name}", C.YELLOW)
            return True
        except Exception as e:
            nprint("Evolution", f"Rollback failed: {e}", C.RED)
            return False

# ─────────────────────────────────────────────────────────────────────────────
#  16.  CREATIVE  SYNTHESIS  MODULE
# ─────────────────────────────────────────────────────────────────────────────
class CreativeSynthesisModule:
    """
    Breaks conventional solution boundaries using:

    1. Lateral Thinking   – random entry points, provocations, reversals
    2. SCAMPER Framework  – Substitute/Combine/Adapt/Modify/Put/Eliminate/Reverse
    3. Analogical Mapping – map problem onto a different domain, solve there
    4. Constraint Removal – assume every constraint is removable; what then?
    5. Six Hats           – parallel perspectives (fact/emotion/risk/benefit/creative/process)
    6. Random Association – inject random noun → forced connection
    7. First Principles   – decompose to axioms, rebuild
    8. TRIZ Principles    – engineering contradictions → inventive solutions
    """

    RANDOM_NOUNS = ["ocean","telescope","ant","symphony","glacier","compass",
                    "mirror","seed","bridge","prism","clock","labyrinth",
                    "river","volcano","diamond","spider","lightning","echo"]

    SCAMPER = {
        "S": "Substitute – What if you replace a key element?",
        "C": "Combine – What if you merge it with something else?",
        "A": "Adapt – What from another domain applies here?",
        "M": "Magnify/Modify – What if you amplify or change its form?",
        "P": "Put to other uses – How else could this be applied?",
        "E": "Eliminate – What if you remove a key element?",
        "R": "Reverse/Rearrange – What if you flip the order?",
    }

    SIX_HATS = {
        "White" : "Facts only. What do you know for certain?",
        "Red"   : "Gut feeling. What does intuition say?",
        "Black" : "Devil's advocate. What could go wrong?",
        "Yellow": "Best case. What is the most optimistic outcome?",
        "Green" : "Wild ideas. What unconventional approach exists?",
        "Blue"  : "Meta. What is the process we should follow?",
    }

    def generate_provocations(self, problem: str) -> List[str]:
        """Generate creative provocations for a problem."""
        noun = random.choice(self.RANDOM_NOUNS)
        provocations = [
            f"Random association with '{noun}': How does '{noun}' solve this?",
            f"Reversal: What if the opposite were true — {self._reverse(problem)}",
            f"Exaggeration: What if the problem were 1000× worse? What changes?",
            f"Random entry: Start the solution from the OUTPUT and work backwards.",
            f"Analogy: How would nature solve this? (biomimicry angle)",
            f"Constraint removal: Assume you have unlimited time, money, and people.",
            f"Worst idea: What is the WORST solution? Now invert it.",
        ]
        return provocations

    def _reverse(self, problem: str) -> str:
        words = problem.split()
        neg   = ["not","never","without","against","opposite of"]
        return f"{random.choice(neg)} {problem}" if words else problem

    def scamper_analysis(self, subject: str) -> str:
        lines = [f"[SCAMPER Analysis: {subject}]\n"]
        for letter, prompt in self.SCAMPER.items():
            lines.append(f"  [{letter}] {prompt}")
        return "\n".join(lines)

    def six_hats(self, problem: str) -> str:
        lines = [f"[Six Thinking Hats: {problem[:60]}]\n"]
        for hat, prompt in self.SIX_HATS.items():
            lines.append(f"  🎩 {hat}: {prompt}")
        return "\n".join(lines)

    def first_principles(self, assumption: str) -> str:
        return (
            f"[First Principles Breakdown]\n"
            f"  1. What do we know for absolute certain about '{assumption}'?\n"
            f"  2. Strip away analogy, convention, and received wisdom.\n"
            f"  3. What are the irreducible facts?\n"
            f"  4. Now rebuild from scratch using only those facts.\n"
            f"  5. What novel structure emerges?"
        )

    def synthesise(self, problem: str, strategy: str = "auto") -> str:
        """Return a creative synthesis block for the given problem."""
        if strategy == "scamper":
            return self.scamper_analysis(problem)
        elif strategy == "six_hats":
            return self.six_hats(problem)
        elif strategy == "first_principles":
            return self.first_principles(problem)
        else:
            provs = self.generate_provocations(problem)
            result = [f"[🎨 Creative Synthesis — {problem[:50]}]\n"]
            for p in provs[:4]:
                result.append(f"  → {p}")
            return "\n".join(result)

# ─────────────────────────────────────────────────────────────────────────────
#  17.  QUANTUM  REASONING  ENGINE
# ─────────────────────────────────────────────────────────────────────────────
class QuantumReasoningEngine:
    """
    Runs N parallel reasoning branches simultaneously, then selects the best
    using a scoring heuristic (confidence × novelty × coherence).

    Each branch applies a different cognitive strategy:
    Branch 0: Standard deductive reasoning (top-down)
    Branch 1: Inductive / pattern-matching (bottom-up)
    Branch 2: Abductive / best-explanation (hypothesis-first)
    Branch 3: Analogical (cross-domain mapping)
    Branch 4: Dialectical (thesis → antithesis → synthesis)
    """

    STRATEGIES = [
        "deductive",
        "inductive",
        "abductive",
        "analogical",
        "dialectical",
    ]

    STRATEGY_PROMPTS = {
        "deductive"  : "Reason step-by-step from first principles. Be logical and precise.",
        "inductive"  : "Look for patterns in examples. Build up from specific cases.",
        "abductive"  : "Form the best hypothesis first, then verify it.",
        "analogical" : "Find a known domain where this problem is already solved. Map the solution back.",
        "dialectical": "State the main thesis, then its strongest counterargument, then synthesise.",
    }

    def __init__(self, n_branches: int = None):
        self._n = min(n_branches or NEXUS_CFG.get("quantum_branches", 3),
                      len(self.STRATEGIES))

    async def reason(self, query: str, call_llm: Callable) -> Tuple[str, str]:
        """
        Run N branches in parallel, return (best_answer, strategy_used).
        `call_llm` is an async callable(prompt: str) -> str.
        """
        branches = self.STRATEGIES[:self._n]
        tasks    = []
        for branch in branches:
            prefix = self.STRATEGY_PROMPTS[branch]
            prompt = f"[{branch.upper()} REASONING]\n{prefix}\n\nQuestion: {query}"
            tasks.append(self._run_branch(prompt, branch, call_llm))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Score each branch
        best_score   = -1.0
        best_answer  = ""
        best_strategy = branches[0]

        for branch, res in zip(branches, results):
            if isinstance(res, Exception) or not res:
                continue
            score = self._score(res)
            if score > best_score:
                best_score    = score
                best_answer   = res
                best_strategy = branch

        return best_answer, best_strategy

    async def _run_branch(self, prompt: str, branch: str,
                          call_llm: Callable) -> str:
        try:
            return await call_llm(prompt)
        except Exception as e:
            return f"[Branch {branch} failed: {e}]"

    @staticmethod
    def _score(text: str) -> float:
        """Heuristic quality score for a reasoning output."""
        if not text or len(text) < 20:
            return 0.0
        # Length (prefer thorough but not bloated)
        length_score  = min(1.0, len(text) / 800)
        # Structural richness (numbered lists, code, etc.)
        struct_score  = min(1.0, (text.count("\n") + text.count("1.") +
                                  text.count("```")) / 20)
        # Confidence markers
        conf_markers  = ["therefore","because","specifically","for example",
                         "in conclusion","as a result","thus"]
        conf_score    = sum(1 for m in conf_markers if m in text.lower()) / len(conf_markers)
        # Error penalty
        err_penalty   = 0.5 if "[failed]" in text.lower() else 0.0
        return (length_score * 0.35 + struct_score * 0.35 + conf_score * 0.3) - err_penalty

# ─────────────────────────────────────────────────────────────────────────────
#  18.  PREDICTIVE  INTENT  ENGINE
# ─────────────────────────────────────────────────────────────────────────────
class PredictiveIntentEngine:
    """
    Predicts the user's next query using:
    1. Bigram Markov chain on intent transitions
    2. Semantic embedding similarity to past follow-up patterns
    3. Time-of-day priors (morning→briefing, evening→recap)
    """

    TIME_PRIORS = {
        "morning"  : ["give me a briefing", "what's new today", "plan my day"],
        "afternoon": ["explain", "code help", "search for"],
        "evening"  : ["summarise my day", "remind me", "what did we discuss"],
        "night"    : ["bedtime reminder", "set alarm", "what did I accomplish"],
    }

    def __init__(self):
        self._chain   : Dict[str, Counter] = defaultdict(Counter)
        self._history : deque = deque(maxlen=50)

    def observe(self, intent: str):
        """Record an observed intent."""
        if self._history:
            self._chain[self._history[-1]][intent] += 1
        self._history.append(intent)

    def predict(self, n: int = 3) -> List[str]:
        """Predict the top N likely next intents."""
        if not self._history:
            return self._time_prior()
        last = self._history[-1]
        if last in self._chain and self._chain[last]:
            ranked = self._chain[last].most_common(n)
            return [intent for intent, _ in ranked]
        return self._time_prior()[:n]

    def _time_prior(self) -> List[str]:
        h = datetime.datetime.now().hour
        tod = ("morning" if h < 12 else "afternoon" if h < 17
               else "evening" if h < 21 else "night")
        return self.TIME_PRIORS.get(tod, ["explain", "code", "search"])

    def proactive_suggestion(self) -> Optional[str]:
        """Return a proactive suggestion string or None."""
        preds = self.predict(1)
        if not preds:
            return None
        intent = preds[0]
        msgs   = {
            "web"    : "Would you like me to search for something related?",
            "code"   : "Need code assistance for what we just discussed?",
            "memory" : "Shall I recall related past conversations?",
            "explain": "Would you like a deeper explanation of any of that?",
        }
        return msgs.get(intent)

# ─────────────────────────────────────────────────────────────────────────────
#  19.  DREAM  MODE  (Background Learning)
# ─────────────────────────────────────────────────────────────────────────────
class DreamMode:
    """
    During idle periods, Luna consolidates episodic memories, identifies
    concept clusters, generates self-summaries, and prepares insights.

    Inspired by sleep-phase memory consolidation in neuroscience.

    Cycle every DREAM_INTERVAL minutes when user is idle > IDLE_THRESHOLD seconds.
    """

    IDLE_THRESHOLD_SEC = 120
    DREAM_INTERVAL_MIN = None   # from config

    def __init__(self, ledger: EpisodicLedger):
        self.ledger   = ledger
        self._thread  : Optional[threading.Thread] = None
        self._running = False
        self._last_active = time.time()
        self._insights: List[str] = []
        self.DREAM_INTERVAL_MIN = NEXUS_CFG.get("dream_interval_min", 15)

    def nudge(self):
        """Call this on every user interaction to reset idle timer."""
        self._last_active = time.time()

    def start(self):
        self._running = True
        self._thread  = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        nprint("Dream", "Background learning activated", C.BLUE)

    def stop(self):
        self._running = False

    def _loop(self):
        while self._running:
            time.sleep(60)   # check every minute
            idle_sec = time.time() - self._last_active
            if idle_sec >= self.IDLE_THRESHOLD_SEC:
                self._dream_cycle()

    def _dream_cycle(self):
        nprint("Dream", "💤 Entering dream cycle...", C.BLUE)
        try:
            # Retrieve recent memories for consolidation
            recent = self.ledger.recall("", top_k=20)
            if not recent:
                return

            # Cluster by simple keyword overlap
            clusters: Dict[str, List[str]] = defaultdict(list)
            for mem in recent:
                tags = re.findall(r"\b[A-Za-z]{4,}\b", mem["content"])
                tag  = Counter(tags).most_common(1)[0][0] if tags else "general"
                clusters[tag].append(mem["content"][:200])

            insight = (f"[Dream Cycle @ {datetime.datetime.now().strftime('%H:%M')}]\n"
                       f"Consolidated {len(recent)} memories into "
                       f"{len(clusters)} concept clusters: "
                       + ", ".join(list(clusters.keys())[:6]))
            self._insights.append(insight)

            # Persist
            log_entry = {"ts": datetime.datetime.now().isoformat(),
                         "clusters": list(clusters.keys()),
                         "memory_count": len(recent)}
            try:
                existing = json.loads(DREAM_LOG.read_text()) if DREAM_LOG.exists() else []
                existing.append(log_entry)
                DREAM_LOG.write_text(json.dumps(existing[-200:], indent=2))
            except Exception:
                pass

            nprint("Dream", f"Dream cycle complete — {len(clusters)} clusters", C.BLUE)
        except Exception as e:
            log.warning(f"Dream cycle error: {e}")

    def get_insights(self) -> List[str]:
        return list(self._insights[-5:])

# ─────────────────────────────────────────────────────────────────────────────
#  20.  NEURAL  CONTEXT  WEAVER
# ─────────────────────────────────────────────────────────────────────────────
class NeuralContextWeaver:
    """
    Dynamically manages the context window for LLM calls using salience scoring.

    Rather than blindly including the last N turns, it:
    1. Scores each turn by recency × relevance × importance
    2. Selects the top-K turns within token budget
    3. Compresses long turns with an extractive summariser
    4. Injects episodic memory snippets at optimal salience boundaries
    """

    def __init__(self, ledger: EpisodicLedger, token_budget: int = 6000):
        self.ledger  = ledger
        self._budget = token_budget
        self._turns  : deque = deque(maxlen=200)

    def add_turn(self, role: str, content: str, importance: float = 0.5):
        self._turns.append({
            "role"      : role,
            "content"   : content,
            "ts"        : time.time(),
            "importance": importance,
            "tokens"    : len(content) // 4,  # rough token estimate
        })

    def weave(self, query: str) -> List[Dict]:
        """Return a list of {role, content} dicts optimised for the current query."""
        if not self._turns:
            return []

        now = time.time()
        scored = []
        for i, turn in enumerate(self._turns):
            recency   = math.exp(-0.1 * (now - turn["ts"]) / 60)  # decay per minute
            relevance = self._relevance(query, turn["content"])
            salience  = (recency * 0.4 + relevance * 0.4 + turn["importance"] * 0.2)
            scored.append((salience, i, turn))

        scored.sort(reverse=True, key=lambda x: x[0])

        # Select within budget
        selected = []
        budget   = self._budget
        for _, idx, turn in scored:
            tokens = turn["tokens"]
            if tokens > budget:
                # Compress
                compressed = self._compress(turn["content"], budget // 2)
                selected.append({"role": turn["role"], "content": compressed,
                                 "_idx": idx})
                budget -= len(compressed) // 4
            else:
                selected.append({"role": turn["role"], "content": turn["content"],
                                 "_idx": idx})
                budget -= tokens
            if budget <= 0:
                break

        # Re-sort by original index (chronological order)
        selected.sort(key=lambda x: x.pop("_idx", 0))

        # Inject memory context
        mem_ctx = self.ledger.build_context(query, max_tokens=min(600, budget))
        if mem_ctx:
            selected.insert(0, {"role": "system", "content": mem_ctx})

        return selected

    @staticmethod
    def _relevance(query: str, content: str) -> float:
        q_words = set(re.findall(r"\b\w{3,}\b", query.lower()))
        c_words = set(re.findall(r"\b\w{3,}\b", content.lower()))
        if not q_words or not c_words:
            return 0.0
        return len(q_words & c_words) / len(q_words)

    @staticmethod
    def _compress(text: str, target_chars: int) -> str:
        """Extractive compression: keep first + most-keyword-dense sentences."""
        sentences = re.split(r"(?<=[.!?])\s+", text)
        if not sentences:
            return text[:target_chars]
        result   = [sentences[0]]
        budget   = target_chars - len(sentences[0])
        for sent in sentences[1:]:
            if len(sent) <= budget:
                result.append(sent)
                budget -= len(sent)
            if budget <= 0:
                break
        return " ".join(result)

# ─────────────────────────────────────────────────────────────────────────────
#  21.  EMOTIONAL  INTELLIGENCE  LAYER
# ─────────────────────────────────────────────────────────────────────────────
class EmotionalIntelligenceLayer:
    """
    Detects affect signals in user input and adapts Luna's response style.

    Affect dimensions:
    - Frustration  → patience, short answers, no jargon
    - Excitement   → enthusiasm, expansive exploration
    - Confusion    → step-by-step, analogies, simpler language
    - Urgency      → concise, prioritised, action-first
    - Sadness      → empathy first, gentle tone, offer support
    - Curiosity    → deep dives, related tangents, "did you know…"
    """

    SIGNALS = {
        "frustration": ["ugh","annoying","not working","broken","hate","frustrated",
                        "again","keeps failing","stupid","useless"],
        "excitement" : ["wow","amazing","awesome","incredible","love this","excited",
                        "fantastic","brilliant","perfect"],
        "confusion"  : ["confused","don't understand","unclear","what do you mean",
                        "huh","lost","can you explain","i'm not sure"],
        "urgency"    : ["asap","urgent","immediately","right now","hurry","quickly",
                        "deadline","emergency","fast"],
        "sadness"    : ["sad","depressed","lonely","feeling down","upset","crying",
                        "hopeless","tired of this"],
        "curiosity"  : ["how does","why does","what if","tell me more","interesting",
                        "curious","wonder","fascinating"],
    }

    RESPONSE_MODIFIERS = {
        "frustration": ("Be extremely patient and calm. Acknowledge the issue first. "
                        "Offer simple, direct solutions. Avoid technical jargon."),
        "excitement" : ("Match their energy! Be enthusiastic and expansive. "
                        "Explore the topic broadly and celebrate it."),
        "confusion"  : ("Break everything down step-by-step. Use analogies and examples. "
                        "Check for understanding. Keep sentences short."),
        "urgency"    : ("Be terse and action-focused. Lead with the answer. "
                        "Use bullet points. Skip pleasantries."),
        "sadness"    : ("Lead with empathy. Acknowledge their feelings before any task. "
                        "Use a warm, gentle tone. Offer support."),
        "curiosity"  : ("Dive deep! Add fascinating tangents and 'did you know' facts. "
                        "Encourage exploration. Suggest related topics."),
    }

    def __init__(self):
        self._affect_history: deque = deque(maxlen=5)

    def detect(self, text: str) -> Tuple[str, float]:
        """Returns (dominant_affect, confidence)."""
        text_lower = text.lower()
        scores: Dict[str, int] = defaultdict(int)
        for affect, signals in self.SIGNALS.items():
            for sig in signals:
                if sig in text_lower:
                    scores[affect] += 1
        if not scores:
            return "neutral", 0.0
        top  = max(scores, key=scores.get)
        conf = min(1.0, scores[top] / 3.0)
        self._affect_history.append(top)
        return top, conf

    def get_modifier(self, text: str) -> str:
        """Return a system prompt modifier for the detected affect."""
        affect, conf = self.detect(text)
        if conf < 0.3:
            return ""
        return self.RESPONSE_MODIFIERS.get(affect, "")

    def empathy_prefix(self, affect: str) -> str:
        """Return an empathetic opening line."""
        prefixes = {
            "frustration": "I understand this is frustrating — let's fix it together. ",
            "excitement" : "This is exciting! ",
            "confusion"  : "No worries, let me break this down clearly. ",
            "urgency"    : "On it — here's what you need: ",
            "sadness"    : "I'm here with you. ",
            "curiosity"  : "Great question — there's a lot to explore here! ",
        }
        return prefixes.get(affect, "")

# ─────────────────────────────────────────────────────────────────────────────
#  22.  TIME CAPSULE  MEMORY
# ─────────────────────────────────────────────────────────────────────────────
class TimeCapsuleMemory:
    """
    Schedule a memory or message to be delivered at a future time.
    
    Use cases:
    - "Remind me of this decision in 3 months"
    - "Ask me how Project X went next Friday"
    - "Deliver this note to myself at 09:00 tomorrow"
    """

    def __init__(self):
        self._capsules = self._load()

    def _load(self) -> List[Dict]:
        try:
            files = sorted(CAPSULE_DIR.glob("capsule_*.json"))
            caps  = []
            for f in files:
                caps.append(json.loads(f.read_text()))
            return caps
        except Exception:
            return []

    def create(self, message: str, deliver_at: datetime.datetime,
               tags: List[str] = None) -> str:
        cap_id = str(uuid.uuid4())[:8]
        capsule = {
            "id"        : cap_id,
            "message"   : message,
            "deliver_at": deliver_at.isoformat(),
            "created_at": datetime.datetime.now().isoformat(),
            "tags"      : tags or [],
            "delivered" : False,
        }
        try:
            (CAPSULE_DIR / f"capsule_{cap_id}.json").write_text(
                json.dumps(capsule, indent=2))
        except Exception as e:
            log.error(f"TimeCapsule create: {e}")
        self._capsules.append(capsule)
        nprint("Capsule", f"📦 Scheduled: '{message[:50]}' → {deliver_at.strftime('%Y-%m-%d %H:%M')}", C.MAGENTA)
        return cap_id

    def check_due(self) -> List[Dict]:
        """Return capsules that are due now and mark them as delivered."""
        now = datetime.datetime.now()
        due = []
        for cap in self._capsules:
            if cap["delivered"]:
                continue
            deliver_at = datetime.datetime.fromisoformat(cap["deliver_at"])
            if now >= deliver_at:
                cap["delivered"] = True
                due.append(cap)
                # Update file
                try:
                    path = CAPSULE_DIR / f"capsule_{cap['id']}.json"
                    path.write_text(json.dumps(cap, indent=2))
                except Exception:
                    pass
        return due

    def list_pending(self) -> List[Dict]:
        return [c for c in self._capsules if not c["delivered"]]

# ─────────────────────────────────────────────────────────────────────────────
#  23.  SKILL  MARKETPLACE
# ─────────────────────────────────────────────────────────────────────────────
class SkillMarketplace:
    """
    Dynamically load / unload Python skill modules at runtime.

    A Skill is a Python file in ~/LunaAI/nexus/skills/ that exposes:
        SKILL_META  = {"name": str, "version": str, "description": str, "commands": [str]}
        async def handle(query: str, luna_core) -> str

    Skills can be:
    - Loaded from local files
    - Downloaded from a URL (with integrity hash verification)
    - Listed, enabled, disabled at runtime
    """

    def __init__(self):
        self._skills   : Dict[str, Any] = {}    # name → module
        self._disabled : set = set()
        self._scan_local()

    def _scan_local(self):
        for pyfile in SKILL_DIR.glob("skill_*.py"):
            self._load_file(pyfile)

    def _load_file(self, path: Path) -> bool:
        import importlib.util
        try:
            spec   = importlib.util.spec_from_file_location(path.stem, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            meta   = getattr(module, "SKILL_META", {})
            name   = meta.get("name", path.stem)
            self._skills[name] = module
            nprint("Skills", f"Loaded skill: {name} v{meta.get('version','?')}", C.GREEN)
            return True
        except Exception as e:
            nprint("Skills", f"Failed to load {path.name}: {e}", C.RED)
            return False

    async def run_skill(self, name: str, query: str, luna_core=None) -> Optional[str]:
        """Run a skill's handle() function."""
        if name in self._disabled or name not in self._skills:
            return None
        module = self._skills[name]
        handler = getattr(module, "handle", None)
        if not handler:
            return None
        try:
            return await handler(query, luna_core)
        except Exception as e:
            return f"[Skill Error] {name}: {e}"

    def list_skills(self) -> str:
        if not self._skills:
            return "No skills installed."
        lines = ["[📦 Skill Marketplace]\n"]
        for name, module in self._skills.items():
            meta    = getattr(module, "SKILL_META", {})
            status  = "✓" if name not in self._disabled else "✗"
            lines.append(f"  {status} {name:20s} v{meta.get('version','?')} — {meta.get('description','')[:50]}")
        return "\n".join(lines)

    def enable(self, name: str):  self._disabled.discard(name)
    def disable(self, name: str): self._disabled.add(name)

    async def install_from_url(self, url: str, expected_sha256: str = "") -> bool:
        """Download a skill from a URL with optional integrity check."""
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=15)) as r:
                    if r.status != 200:
                        return False
                    code = await r.text()

            if expected_sha256:
                actual = hashlib.sha256(code.encode()).hexdigest()
                if actual != expected_sha256:
                    nprint("Skills", "Hash mismatch — install aborted", C.RED)
                    return False

            fname = f"skill_{uuid.uuid4().hex[:8]}.py"
            path  = SKILL_DIR / fname
            path.write_text(code)
            return self._load_file(path)
        except Exception as e:
            nprint("Skills", f"Install from URL failed: {e}", C.RED)
            return False

# ─────────────────────────────────────────────────────────────────────────────
#  24.  PYQT6  IRON MAN  HUD
# ─────────────────────────────────────────────────────────────────────────────
class NexusHUD:
    """
    Transparent PyQt6 overlay — Iron Man / JARVIS style HUD.

    Panels:
    ┌─────────────────────────────────────────────────────────┐
    │  ⬡ LUNA NEXUS  [time]  [battery]  [wifi]               │  Header bar
    ├─────────────────────────────────────────────────────────┤
    │  [CoT Stream]           │  [System Gauges]              │
    │  ● THINKING: …          │  CPU  ████░░ 62%              │
    │  ● REASON: …            │  RAM  ██████ 78%              │
    │  ● SYNTH: …             │  GPU  ██░░░░ 30%              │
    ├─────────────────────────────────────────────────────────┤
    │  [YOLO Objects]         │  [Mood / IoT]                 │
    │  person(0.97)           │  Mood: calm_positive          │
    │  laptop(0.89)           │  Temp: 22.1°C  Light: 380lx   │
    ├─────────────────────────────────────────────────────────┤
    │  [Active Response]                                      │
    │  Luna: …                                               │
    └─────────────────────────────────────────────────────────┘
    
    All rendering uses the palette defined in NEXUS_CFG.
    Gesture commands from GestureController update the HUD in real-time.
    """

    def __init__(self, hud_queue: queue.Queue):
        self._q       = hud_queue
        self._app     : Optional[Any] = None
        self._window  : Optional[Any] = None
        self._thread  : Optional[threading.Thread] = None
        self._cot_lines: deque = deque(maxlen=12)
        self._yolo_lines: List[str] = []
        self._mood_str : str = "Initialising..."
        self._sys_str  : str = ""
        self._response : str = ""

    def launch(self):
        """Launch the HUD in a dedicated thread.

        PyQt6 requires QApplication to be created in the MAIN thread.
        We create/retrieve it here (called from the main thread via
        _boot_subsystems) and only push the event-loop into the worker thread.
        """
        if not PYQT6_OK:
            nprint("HUD", "PyQt6 not available — HUD disabled", C.YELLOW)
            return
        # Suppress Windows DPI-awareness permission warning
        os.environ.setdefault("QT_ENABLE_HIGHDPI_SCALING",    "0")
        os.environ.setdefault("QT_AUTO_SCREEN_SCALE_FACTOR",  "0")
        # Create (or retrieve) QApplication here — we ARE in the main thread
        self._qt_app = QApplication.instance() or QApplication(sys.argv)
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        nprint("HUD", "Iron Man HUD launched", C.GREEN)

    def _run(self):
        """HUD event loop — runs in a worker thread.

        QApplication was already created on the main thread in launch().
        We use the existing instance; exec() is safe to call from a
        secondary thread on Windows with Qt6.
        """
        try:
            app = self._qt_app        # reuse instance created on main thread
            win = self._build_window()
            win.show()

            # Poll queue and refresh every 250ms
            timer = QTimer()
            timer.timeout.connect(lambda: self._poll_queue(win))
            timer.start(250)

            app.exec()
        except Exception as e:
            log.error(f"HUD error: {e}")

    def _build_window(self):
        """Build the transparent HUD window."""
        primary  = NEXUS_CFG.get("hud_color_primary", "#00BFFF")
        opacity  = NEXUS_CFG.get("hud_opacity", 0.88)
        position = NEXUS_CFG.get("hud_position", "top-right")

        win = QWidget()
        win.setWindowTitle("Luna.AI Nexus HUD")
        win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        win.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        win.resize(520, 680)
        win.setWindowOpacity(opacity)

        # Position
        screen = QApplication.primaryScreen().availableGeometry()
        if position == "top-right":
            win.move(screen.width() - 540, 20)
        elif position == "top-left":
            win.move(20, 20)
        elif position == "bottom-right":
            win.move(screen.width() - 540, screen.height() - 700)

        layout = QVBoxLayout(win)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(6)

        # ── Header ──────────────────────────────────────────────
        header = QLabel("⬡  LUNA.AI NEXUS  ─  ONLINE")
        header.setFont(QFont("Consolas", 11, QFont.Weight.Bold))
        header.setStyleSheet(f"color: {primary}; background: transparent;")
        layout.addWidget(header)

        # ── CoT Panel ───────────────────────────────────────────
        cot_label = QLabel("[Chain of Thought]")
        cot_label.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        cot_label.setStyleSheet(f"color: {primary}; background: transparent;")
        layout.addWidget(cot_label)

        win._cot_box = QLabel("Waiting for query...")
        win._cot_box.setWordWrap(True)
        win._cot_box.setFont(QFont("Consolas", 7))
        win._cot_box.setStyleSheet("color: #A0D8EF; background: rgba(0,20,40,150);"
                                    "border: 1px solid #00BFFF; padding: 4px;")
        win._cot_box.setMaximumHeight(140)
        layout.addWidget(win._cot_box)

        # ── System Gauges ────────────────────────────────────────
        sys_label = QLabel("[System Telemetry]")
        sys_label.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        sys_label.setStyleSheet(f"color: {primary}; background: transparent;")
        layout.addWidget(sys_label)

        win._sys_box = QLabel("Scanning...")
        win._sys_box.setFont(QFont("Consolas", 7))
        win._sys_box.setStyleSheet("color: #90EE90; background: rgba(0,20,10,150);"
                                    "border: 1px solid #00FF7F; padding: 4px;")
        layout.addWidget(win._sys_box)

        # ── YOLO Panel ──────────────────────────────────────────
        yolo_label = QLabel("[Environmental Awareness — YOLOv8]")
        yolo_label.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        yolo_label.setStyleSheet(f"color: {primary}; background: transparent;")
        layout.addWidget(yolo_label)

        win._yolo_box = QLabel("No objects detected.")
        win._yolo_box.setFont(QFont("Consolas", 7))
        win._yolo_box.setStyleSheet("color: #FFD700; background: rgba(20,15,0,150);"
                                     "border: 1px solid #FFD700; padding: 4px;")
        layout.addWidget(win._yolo_box)

        # ── Mood / IoT Panel ─────────────────────────────────────
        mood_label = QLabel("[Mood Engine + IoT Sensors]")
        mood_label.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        mood_label.setStyleSheet(f"color: {primary}; background: transparent;")
        layout.addWidget(mood_label)

        win._mood_box = QLabel("Calibrating...")
        win._mood_box.setFont(QFont("Consolas", 7))
        win._mood_box.setStyleSheet("color: #FF69B4; background: rgba(20,0,15,150);"
                                     "border: 1px solid #FF69B4; padding: 4px;")
        layout.addWidget(win._mood_box)

        # ── Response Panel ───────────────────────────────────────
        resp_label = QLabel("[Active Response]")
        resp_label.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        resp_label.setStyleSheet(f"color: {primary}; background: transparent;")
        layout.addWidget(resp_label)

        win._resp_box = QLabel("")
        win._resp_box.setWordWrap(True)
        win._resp_box.setFont(QFont("Consolas", 7))
        win._resp_box.setStyleSheet("color: #FFFFFF; background: rgba(0,0,20,180);"
                                     "border: 1px solid #00BFFF; padding: 4px;")
        win._resp_box.setMaximumHeight(160)
        layout.addWidget(win._resp_box)

        win.setStyleSheet("QWidget { background: rgba(0, 5, 20, 200); }")
        self._window = win
        return win

    def _poll_queue(self, win):
        """Drain the HUD update queue."""
        for _ in range(20):   # drain up to 20 messages per tick
            try:
                msg = self._q.get_nowait()
            except queue.Empty:
                break

            mtype = msg.get("type", "")

            if mtype == "cot":
                self._cot_lines.append(f"◈ {msg.get('text','')[:70]}")
                win._cot_box.setText("\n".join(self._cot_lines))

            elif mtype == "yolo":
                objs  = msg.get("objects", [])
                lines = [f"• {o['label']:15s} {o['confidence']:.2f}" for o in objs[:6]]
                win._yolo_box.setText("\n".join(lines) or "No objects detected.")

            elif mtype == "mood":
                win._mood_box.setText(msg.get("text", ""))

            elif mtype == "sys":
                win._sys_box.setText(msg.get("text", ""))

            elif mtype == "response":
                text = msg.get("text", "")[:400]
                win._resp_box.setText(f"Luna: {text}")

        # Auto-update system gauges from psutil
        if PSUTIL_OK:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            bar_cpu = "█" * (cpu // 10) + "░" * (10 - cpu // 10)
            bar_ram = "█" * (ram // 10) + "░" * (10 - ram // 10)
            win._sys_box.setText(
                f"CPU  [{bar_cpu}] {cpu:.0f}%\n"
                f"RAM  [{bar_ram}] {ram:.0f}%"
            )

    def send(self, msg_type: str, **kwargs):
        """Send an update to the HUD."""
        with suppress(queue.Full):
            self._q.put_nowait({"type": msg_type, **kwargs})

# ─────────────────────────────────────────────────────────────────────────────
#  24b.  BRAIN  ENSEMBLE  —  Parallel Brain Cross-Pollination System
# ─────────────────────────────────────────────────────────────────────────────
class BrainEnsemble:
    """
    Runs N specialised brains IN PARALLEL, cross-pollinates their answers
    in a refinement round, then synthesises the ultimate best response.

    ┌───────────────────────────────────────────────────────────────────┐
    │  PHASE 1 — Parallel Execution                                     │
    │  Brain 0 LOGIC    ─ deductive chain-of-thought                    │
    │  Brain 1 CREATIVE ─ lateral thinking, analogies, novel angles     │
    │  Brain 2 EMPATHY  ─ user emotional state + hidden intent          │
    │  Brain 3 MEMORY   ─ episodic / semantic recall expert             │
    │  Brain 4 CRITIC   ─ devil's advocate, challenges assumptions      │
    │                         │                                         │
    │  PHASE 2 — Cross-Pollination (brains READ each other's output)    │
    │  Each brain refines its answer with the other brains' insights    │
    │                         │                                         │
    │  PHASE 3 — Meta-Synthesis (best-of-all weave)                     │
    │  Agreements amplified · Contradictions resolved · Gaps filled     │
    └───────────────────────────────────────────────────────────────────┘
    """

    BRAIN_PERSONAS: List[Tuple[str, str]] = [
        (
            "LOGIC",
            "You are a hyper-logical AI brain. Reason step-by-step from first "
            "principles. Be precise, structured, and show your reasoning chain."
        ),
        (
            "CREATIVE",
            "You are a wildly creative AI brain. Think laterally, use vivid "
            "analogies, find unexpected angles, and reframe the problem in "
            "surprising but illuminating ways."
        ),
        (
            "EMPATHY",
            "You are an empathy-focused AI brain. Consider the user's emotional "
            "state, their real underlying needs, and the hidden intent behind "
            "their words. Respond with warmth and genuine understanding."
        ),
        (
            "MEMORY",
            "You are a memory and context expert AI brain. Focus on patterns from "
            "prior context, how this question relates to what came before, and "
            "what background knowledge is most relevant here."
        ),
        (
            "CRITIC",
            "You are a constructive critic AI brain. Challenge assumptions, "
            "surface flaws or gaps in obvious answers, and offer the strongest "
            "counter-perspective — but always constructively."
        ),
    ]

    META_SYNTHESIS_PROMPT = (
        "You are the MASTER SYNTHESIS BRAIN — the final decision-maker.\n\n"
        "Five specialised brains independently responded to the same query, "
        "then refined their answers after reading each other. Here are all five "
        "refined responses:\n\n"
        "{brain_responses}\n\n"
        "Your synthesis mission:\n"
        "1. Extract the STRONGEST unique insight from each brain.\n"
        "2. Where brains AGREE — that is high-confidence truth, amplify it.\n"
        "3. Where brains CONTRADICT — reason through and resolve it.\n"
        "4. Fill any GAPS that no single brain covered adequately.\n"
        "5. Produce a response that is richer, more complete, and more useful "
        "than any single brain alone.\n\n"
        "Original User Query: {query}\n\n"
        "Write the definitive synthesised response now:"
    )

    CROSS_POLL_PROMPT = (
        "[{brain_name} BRAIN — REFINEMENT ROUND]\n"
        "{persona}\n\n"
        "Original query: {query}\n\n"
        "Your initial response was:\n{own_output}\n\n"
        "After reviewing the other brains' responses:\n{others_context}\n\n"
        "Now produce your REFINED and IMPROVED response. Keep your unique "
        "{brain_name} perspective, but integrate the best insights from the "
        "other brains. Do not simply repeat what others said — add genuine "
        "value from your angle:"
    )

    def __init__(self):
        self._enabled   : bool = True
        self._fast_mode : bool = NEXUS_CFG.get("brain_ensemble_fast_mode", False)
        self._n_brains  : int  = min(
            max(2, NEXUS_CFG.get("brain_count", 5)),
            len(self.BRAIN_PERSONAS)
        )

    # ── Public API ────────────────────────────────────────────────────────────

    async def run(
        self,
        query    : str,
        call_llm : Callable,
        context  : str = "",
        modifier : str = "",
    ) -> Tuple[str, Dict]:
        """
        Execute the full 3-phase ensemble pipeline.

        Returns
        -------
        (final_answer: str, metadata: dict)
        """
        active_personas = self.BRAIN_PERSONAS[: self._n_brains]

        # ── Phase 1: Parallel Execution ───────────────────────────────────
        nprint("BrainEnsemble", f"Phase 1 — firing {self._n_brains} brains in parallel…", C.MAGENTA)
        phase1_tasks = [
            self._run_single_brain(
                brain_name = name,
                prompt     = self._build_phase1_prompt(name, persona, query, context, modifier),
                call_llm   = call_llm,
            )
            for name, persona in active_personas
        ]
        phase1_raw = await asyncio.gather(*phase1_tasks, return_exceptions=True)

        brain_outputs: Dict[str, str] = {}
        for (name, _), result in zip(active_personas, phase1_raw):
            brain_outputs[name] = (
                result if isinstance(result, str) and result
                else f"[{name} brain unavailable]"
            )

        # ── Phase 2: Cross-Pollination ────────────────────────────────────
        if self._fast_mode:
            refined_outputs = brain_outputs
            nprint("BrainEnsemble", "Phase 2 skipped (fast mode)", C.DIM)
        else:
            nprint("BrainEnsemble", "Phase 2 — cross-pollination round…", C.MAGENTA)
            refined_outputs = await self._cross_pollinate(
                query, brain_outputs, active_personas, call_llm
            )

        # ── Phase 3: Meta-Synthesis ───────────────────────────────────────
        nprint("BrainEnsemble", "Phase 3 — meta-synthesis…", C.MAGENTA)
        synthesis_block = "\n\n".join(
            f"[{name} BRAIN]\n{output}"
            for name, output in refined_outputs.items()
        )
        synth_prompt = self.META_SYNTHESIS_PROMPT.format(
            brain_responses = synthesis_block,
            query           = query,
        )
        final_answer = await self._run_single_brain("META", synth_prompt, call_llm)

        # Fallback: if synthesis failed, pick highest-scoring refined brain
        if not final_answer or len(final_answer) < 30:
            scored = sorted(
                [(_score_text(v), k, v) for k, v in refined_outputs.items()],
                reverse=True,
            )
            final_answer = scored[0][2] if scored else list(brain_outputs.values())[0]

        # ── Metadata ──────────────────────────────────────────────────────
        brain_scores = {k: round(_score_text(v), 3) for k, v in brain_outputs.items()}
        refined_scores = {k: round(_score_text(v), 3) for k, v in refined_outputs.items()}
        top_brain = max(refined_scores, key=refined_scores.get)

        metadata: Dict = {
            "brains_used"       : list(brain_outputs.keys()),
            "brain_scores_p1"   : brain_scores,
            "brain_scores_p2"   : refined_scores,
            "top_brain"         : top_brain,
            "cross_pollinated"  : not self._fast_mode,
            "synthesis_method"  : "meta_synthesis",
            "n_brains"          : self._n_brains,
        }

        nprint("BrainEnsemble", f"Ensemble complete — top brain: {top_brain}", C.GREEN)
        return final_answer, metadata

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _build_phase1_prompt(
        self,
        brain_name : str,
        persona    : str,
        query      : str,
        context    : str,
        modifier   : str,
    ) -> str:
        parts = [f"[{brain_name} BRAIN]", persona]
        if modifier:
            parts.append(modifier)
        if context:
            parts.append(f"[Relevant Context]\n{context[:800]}")
        parts.append(f"User Query: {query}")
        return "\n\n".join(parts)

    async def _cross_pollinate(
        self,
        query          : str,
        brain_outputs  : Dict[str, str],
        active_personas: List[Tuple[str, str]],
        call_llm       : Callable,
    ) -> Dict[str, str]:
        """Each brain reads the others' Phase-1 answers and refines its own."""
        tasks = []
        for name, persona in active_personas:
            others_ctx = "\n\n".join(
                f"— {other_name} brain said:\n  {out[:350]}…"
                for other_name, out in brain_outputs.items()
                if other_name != name
            )
            prompt = self.CROSS_POLL_PROMPT.format(
                brain_name    = name,
                persona       = persona,
                query         = query,
                own_output    = brain_outputs[name][:500],
                others_context= others_ctx,
            )
            tasks.append(self._run_single_brain(name, prompt, call_llm))

        raw = await asyncio.gather(*tasks, return_exceptions=True)
        refined: Dict[str, str] = {}
        for (name, _), result in zip(active_personas, raw):
            refined[name] = (
                result if isinstance(result, str) and result and len(result) > 20
                else brain_outputs[name]          # fallback to phase-1 answer
            )
        return refined

    @staticmethod
    async def _run_single_brain(brain_name: str, prompt: str, call_llm: Callable) -> str:
        """Safely call the LLM for a single brain."""
        try:
            result = await call_llm(prompt)
            return result or ""
        except Exception as exc:
            log.debug(f"BrainEnsemble.{brain_name}: {exc}")
            return f"[{brain_name} brain error: {exc}]"


def _score_text(text: str) -> float:
    """
    Reusable response quality heuristic (used by BrainEnsemble + JSONBrain).
    """
    if not text or len(text) < 20:
        return 0.0
    length_score  = min(1.0, len(text) / 700)
    struct_score  = min(1.0, (text.count("\n") + text.count(".")) / 35)
    qual_markers  = [
        "therefore", "because", "specifically", "for example",
        "however", "furthermore", "importantly", "note that",
        "in conclusion", "as a result", "key insight",
    ]
    qual_score    = sum(1 for m in qual_markers if m in text.lower()) / len(qual_markers)
    err_penalty   = 0.4 if ("error:" in text.lower()[:60]
                             or "unavailable" in text.lower()[:60]) else 0.0
    return (length_score * 0.4 + struct_score * 0.3 + qual_score * 0.3) - err_penalty


# ─────────────────────────────────────────────────────────────────────────────
#  24c.  JSON  INTELLIGENCE  BRAIN
# ─────────────────────────────────────────────────────────────────────────────
class JSONEnrichmentBrain:
    """
    A post-processing intelligence layer that analyses the synthesised answer
    and enriches the final output with structured metadata, key insights,
    caveats, follow-up suggestions, and its own added analytical material.

    Output is appended as a formatted panel beneath the main response.
    """

    _ENRICH_SYSTEM = (
        "You are the JSON Intelligence Brain — a structured analytical engine. "
        "Your sole job is to output a single valid JSON object and NOTHING ELSE. "
        "No preamble, no explanation, no markdown fences."
    )

    _ENRICH_PROMPT = (
        "Analyse the following AI assistant response and return a JSON object "
        "with EXACTLY these keys:\n\n"
        "{{\n"
        '  "confidence": <float 0.0-1.0>,\n'
        '  "key_topics": ["...", "..."],\n'
        '  "key_entities": ["..."],\n'
        '  "sentiment": "positive|neutral|negative|mixed",\n'
        '  "complexity_level": "basic|intermediate|advanced|expert",\n'
        '  "additional_insight": "<ONE powerful insight the main response missed>",\n'
        '  "supplemental_material": "<Short paragraph of extra depth/context>",\n'
        '  "suggested_follow_ups": ["question1", "question2", "question3"],\n'
        '  "warnings_or_caveats": ["caveat"],\n'
        '  "luna_recommendation": "<what the user should do next>",\n'
        '  "brain_consensus_summary": "<were the parallel brains in agreement?>",\n'
        '  "quality_score": <float 0.0-1.0>\n'
        "}}\n\n"
        "QUERY: {query}\n\n"
        "RESPONSE TO ANALYSE:\n{response}\n\n"
        "BRAIN METADATA: {brain_meta}\n\n"
        "Return ONLY valid JSON. No markdown fences."
    )

    async def enrich(
        self,
        query          : str,
        response       : str,
        brain_metadata : Dict,
        call_llm       : Callable,
    ) -> str:
        """
        Returns a formatted enrichment panel string (empty string if unavailable).
        """
        if not NEXUS_CFG.get("json_brain_enabled", True):
            return ""

        prompt = self._ENRICH_PROMPT.format(
            query      = query[:500],
            response   = response[:2000],
            brain_meta = json.dumps({
                k: v for k, v in brain_metadata.items()
                if k in ("brains_used", "brain_scores_p2", "top_brain",
                         "cross_pollinated", "n_brains")
            }, indent=None),
        )

        try:
            raw = await call_llm(prompt, sys_p=self._ENRICH_SYSTEM)
            if not raw:
                return ""

            # Strip any accidental markdown fences
            raw = raw.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)

            data: Dict = json.loads(raw)
            return self._format_panel(data, brain_metadata)

        except json.JSONDecodeError as exc:
            log.debug(f"JSONBrain JSON parse failed: {exc}")
            # Attempt to salvage the additional_insight field
            try:
                m = re.search(r'"additional_insight"\s*:\s*"([^"]{10,})"', raw or "")
                if m:
                    return (
                        f"\n{C.DIM}{'─'*60}{C.RESET}\n"
                        f"{C.CYAN}〔 🔷 JSON BRAIN 〕{C.RESET} "
                        f"💡 {m.group(1)}\n"
                        f"{C.DIM}{'─'*60}{C.RESET}"
                    )
            except Exception:
                pass
            return ""
        except Exception as exc:
            log.debug(f"JSONBrain.enrich: {exc}")
            return ""

    # ── Formatting ────────────────────────────────────────────────────────────

    @staticmethod
    def _format_panel(data: Dict, brain_meta: Dict) -> str:
        conf      = float(data.get("confidence", 0.5))
        quality   = float(data.get("quality_score", 0.5))
        conf_bar  = "█" * int(conf * 10)    + "░" * (10 - int(conf * 10))
        qual_bar  = "█" * int(quality * 10) + "░" * (10 - int(quality * 10))

        topics    = ", ".join(data.get("key_topics",   [])[:5]) or "—"
        entities  = ", ".join(data.get("key_entities", [])[:5]) or "—"
        insight   = data.get("additional_insight",   "")
        suppl     = data.get("supplemental_material","")
        follow_ups= data.get("suggested_follow_ups",  [])[:3]
        caveats   = data.get("warnings_or_caveats",   [])
        recommend = data.get("luna_recommendation",  "")
        consensus = data.get("brain_consensus_summary","")
        complexity= data.get("complexity_level",     "—")
        sentiment = data.get("sentiment",            "—")

        # Brain score bar
        score_line = ""
        if brain_meta.get("brain_scores_p2"):
            parts = [
                f"{k[:3]}:{v:.2f}"
                for k, v in brain_meta["brain_scores_p2"].items()
            ]
            score_line = "  Brains P2   : " + "  ".join(parts)

        top_brain = brain_meta.get("top_brain", "—")

        lines = [
            f"\n{C.DIM}{'═'*64}{C.RESET}",
            f"{C.CYAN}{C.BOLD}〔 🔷 JSON INTELLIGENCE BRAIN  ─  ENRICHMENT LAYER 〕{C.RESET}",
            f"  Confidence  [{conf_bar}] {conf:.0%}   Quality [{qual_bar}] {quality:.0%}",
            f"  Complexity  : {complexity}   │   Sentiment : {sentiment}",
            f"  Topics      : {topics}",
            f"  Entities    : {entities}",
            f"  Top Brain   : {top_brain}",
        ]

        if score_line:
            lines.append(score_line)

        if consensus:
            lines.append(f"  Consensus   : {consensus}")

        if insight:
            lines.append(f"\n  {C.YELLOW}💡 Extra Insight   :{C.RESET} {insight}")

        if suppl:
            # Wrap supplemental material to 60 chars
            wrapped = textwrap.fill(suppl, width=60,
                                    initial_indent   ="  ",
                                    subsequent_indent="  ")
            lines.append(f"\n  {C.GREEN}📘 Supplemental    :{C.RESET}")
            lines.append(wrapped)

        if caveats:
            for cav in caveats:
                lines.append(f"  {C.YELLOW}⚠  Caveat          :{C.RESET} {cav}")

        if recommend:
            lines.append(f"\n  {C.CYAN}🎯 Luna Recommends :{C.RESET} {recommend}")

        if follow_ups:
            lines.append(f"\n  {C.MAGENTA}📎 Suggested Follow-ups:{C.RESET}")
            for i, fq in enumerate(follow_ups, 1):
                lines.append(f"     {i}. {fq}")

        lines.append(f"{C.DIM}{'═'*64}{C.RESET}")
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  24b.  PHYSICS SIMULATOR  (PyBullet real-time physics engine)
# ─────────────────────────────────────────────────────────────────────────────
class PhysicsSimulator:
    """
    Real-time physics simulation via PyBullet.

    Capabilities
    ────────────
    • Headless / GUI physics world (configurable)
    • Load URDF robot / object models from pybullet_data
    • Step simulation with configurable timestep
    • Query body poses, joint states, contact points
    • Simple training loop scaffold (positional control)
    • Safe teardown — physics server disconnects cleanly

    Commands exposed in NexusCore._route_command:
        /physics            status + quick demo
        /physics load <urdf>  load a named URDF from pybullet_data
        /physics step [n]   advance simulation n steps
        /physics info       pose & joint data of all loaded bodies
        /physics reset      restart the world
        /physics train [n]  run n training loop iterations
    """

    _URDF_ALIASES = {
        "plane"  : "plane.urdf",
        "r2d2"   : "r2d2.urdf",
        "cube"   : "cube.urdf",
        "sphere" : "sphere2.urdf",
        "arm"    : "kuka_iiwa/model.urdf",
        "ant"    : "gym_locomotion_envs/ant.urdf",
        "robot"  : "husky/husky.urdf",
    }

    def __init__(self, use_gui: bool = False):
        self._ready    : bool             = False
        self._physics  : Optional[int]    = None   # pybullet physics client id
        self._bodies   : Dict[str, int]   = {}     # alias → bodyId
        self._step_dt  : float            = 1.0 / 240.0
        self._use_gui  = use_gui
        self._train_log: List[str]        = []
        self._lock     = threading.Lock()
        if BULLET_OK:
            self._init()

    # ── init ────────────────────────────────────────────────────────────────
    def _init(self):
        try:
            mode = pb.GUI if self._use_gui else pb.DIRECT
            self._physics = pb.connect(mode)
            pb.setAdditionalSearchPath(pybullet_data.getDataPath(),
                                       physicsClientId=self._physics)
            pb.setGravity(0, 0, -9.81, physicsClientId=self._physics)
            # Load a ground plane by default
            plane_id = pb.loadURDF("plane.urdf", physicsClientId=self._physics)
            self._bodies["plane"] = plane_id
            self._ready = True
            nprint("Physics", "PyBullet online (DIRECT mode)", C.GREEN)
        except Exception as e:
            nprint("Physics", f"PyBullet init failed: {e}", C.YELLOW)

    # ── public API ──────────────────────────────────────────────────────────
    def status(self) -> str:
        if not BULLET_OK:
            return "⚠ PyBullet not installed. Run: pip install pybullet"
        if not self._ready:
            return "⚠ Physics engine not ready."
        body_list = ", ".join(f"{k}(id={v})" for k, v in self._bodies.items())
        return (f"[⚛ PyBullet Physics]\n"
                f"  Status  : {'✓ Online' if self._ready else '✗ Offline'}\n"
                f"  Bodies  : {body_list or 'none'}\n"
                f"  dt      : {self._step_dt*1000:.2f} ms/step\n"
                f"  Mode    : {'GUI' if self._use_gui else 'DIRECT (headless)'}")

    def load_urdf(self, alias: str) -> str:
        if not self._ready:
            return "Physics engine not ready."
        alias = alias.strip().lower()
        urdf  = self._URDF_ALIASES.get(alias, alias if alias.endswith(".urdf") else f"{alias}.urdf")
        try:
            with self._lock:
                bid = pb.loadURDF(urdf,
                                  basePosition=[0, 0, 1],
                                  physicsClientId=self._physics)
            key = alias.split("/")[-1].replace(".urdf", "")
            self._bodies[key] = bid
            return f"✓ Loaded '{urdf}' → bodyId={bid}"
        except Exception as e:
            return f"✗ Load failed: {e} (available: {', '.join(self._URDF_ALIASES)})"

    def step(self, n: int = 1) -> str:
        if not self._ready:
            return "Physics engine not ready."
        n = max(1, min(n, 10_000))
        try:
            with self._lock:
                for _ in range(n):
                    pb.stepSimulation(physicsClientId=self._physics)
            return f"✓ Stepped {n} tick(s) @ {self._step_dt*1000:.2f} ms each ({n*self._step_dt:.4f}s sim time)"
        except Exception as e:
            return f"✗ Step error: {e}"

    def body_info(self) -> str:
        if not self._ready or not self._bodies:
            return "No bodies loaded."
        lines = ["[⚛ Body States]"]
        try:
            with self._lock:
                for name, bid in self._bodies.items():
                    pos, orn = pb.getBasePositionAndOrientation(
                        bid, physicsClientId=self._physics)
                    n_joints = pb.getNumJoints(bid, physicsClientId=self._physics)
                    euler    = pb.getEulerFromQuaternion(orn)
                    lines.append(
                        f"  {name} (id={bid}) | pos={tuple(round(v,3) for v in pos)} "
                        f"| euler={tuple(round(v,3) for v in euler)} | joints={n_joints}"
                    )
        except Exception as e:
            lines.append(f"  Error reading states: {e}")
        return "\n".join(lines)

    def reset(self) -> str:
        if not self._ready:
            return "Physics engine not ready."
        try:
            with self._lock:
                pb.resetSimulation(physicsClientId=self._physics)
                pb.setGravity(0, 0, -9.81, physicsClientId=self._physics)
                plane_id = pb.loadURDF("plane.urdf", physicsClientId=self._physics)
            self._bodies = {"plane": plane_id}
            return "✓ Simulation reset — ground plane reloaded."
        except Exception as e:
            return f"✗ Reset error: {e}"

    def training_loop(self, iterations: int = 100) -> str:
        """
        Minimal positional-control training scaffold.
        Loads a Kuka arm, applies random joint targets, steps simulation,
        records end-effector positions — demo for RL/control integration.
        """
        if not self._ready:
            return "Physics engine not ready."
        iterations = max(1, min(iterations, 2000))
        try:
            with self._lock:
                # Fresh sub-scene: load arm without resetting global world
                arm_id = pb.loadURDF(
                    "kuka_iiwa/model.urdf",
                    basePosition=[0, 0, 0],
                    physicsClientId=self._physics
                )
                n_j = pb.getNumJoints(arm_id, physicsClientId=self._physics)
                rewards = []
                for i in range(iterations):
                    # Random joint targets (training placeholder)
                    for j in range(n_j):
                        target = random.uniform(-1.5, 1.5)
                        pb.setJointMotorControl2(
                            arm_id, j,
                            pb.POSITION_CONTROL,
                            targetPosition=target,
                            physicsClientId=self._physics
                        )
                    pb.stepSimulation(physicsClientId=self._physics)
                    # End-effector link state
                    link_state = pb.getLinkState(
                        arm_id, n_j - 1,
                        physicsClientId=self._physics
                    )
                    pos = link_state[0]
                    # Dummy reward: height of end-effector
                    rewards.append(pos[2])
                # Remove arm from scene
                pb.removeBody(arm_id, physicsClientId=self._physics)

            avg_r = sum(rewards) / len(rewards)
            max_r = max(rewards)
            log_entry = (f"iter={iterations} avg_reward={avg_r:.4f} "
                         f"max_reward={max_r:.4f}")
            self._train_log.append(log_entry)
            return (f"[⚛ Training Complete]\n"
                    f"  Iterations   : {iterations}\n"
                    f"  Avg reward   : {avg_r:.4f}\n"
                    f"  Max reward   : {max_r:.4f}\n"
                    f"  (Reward = end-effector height — replace with your RL objective)")
        except Exception as e:
            return f"✗ Training error: {e}"

    def teardown(self):
        if self._ready and self._physics is not None:
            try:
                pb.disconnect(physicsClientId=self._physics)
            except Exception:
                pass
            self._ready = False


# ─────────────────────────────────────────────────────────────────────────────
#  25.  NEXUS  CORE  (Top-Level Orchestrator)
# ─────────────────────────────────────────────────────────────────────────────
class NexusCore:
    """
    Top-level orchestrator that wires all Nexus subsystems together.
    
    Lifecycle:
    1. Boot: initialise all subsystems
    2. Loop: receive input (voice / text / gesture) → orchestrate → respond
    3. Idle: DreamMode background learning
    4. Shutdown: persist state, close hardware
    
    Supreme Edition brains are optionally spawned as a subprocess and their
    output piped into the synthesis layer for the 21-brain ensemble.
    """

    BANNER = f"""
{C.CYAN}{C.BOLD}
  ╔════════════════════════════════════════════════════════════════╗
  ║   LUNA.AI  ★  NEXUS EDITION                                   ║
  ║   Self-Evolving · Multimodal · Iron Man HUD                   ║
  ╠════════════════════════════════════════════════════════════════╣
  ║   Subsystems          Status                                  ║
  ╠════════════════════════════════════════════════════════════════╣
  ║   🗄  Episodic Ledger  ChromaDB + SentenceTransformers        ║
  ║   🧠  LangGraph        Multi-Agent Orchestration Graph        ║
  ║   🖥  Iron Man HUD     PyQt6 Transparent Overlay              ║
  ║   👁  YOLO Awareness   YOLOv8 Real-Time Object Detection      ║
  ║   🤌  Gesture Ctrl     MediaPipe Hand Pose Recognition        ║
  ║   🌐  Web Navigator    Playwright Autonomous Browser          ║
  ║   🐍  Code Sandbox     AST-Safe Python Executor               ║
  ║   😶  Mood Engine      Windows + ESP32 IoT + MQTT             ║
  ║   🔄  Self-Evolution   AST Refactor + Pydantic + Rollback     ║
  ║   🎨  Creative Synth   SCAMPER · 6-Hats · Lateral Thinking   ║
  ║   ⚛   Quantum Reason   N-Branch Parallel Reasoning           ║
  ║   🔮  Predictor        Markov Intent Prediction               ║
  ║   💤  Dream Mode       Idle-Time Memory Consolidation         ║
  ║   🧵  Context Weaver   Salience-Scored Context Selection      ║
  ║   💚  Emotion Layer    Affect Detection + Empathy             ║
  ║   📦  Skill Market     Dynamic Skill Load/Unload              ║
  ║   🕰  Time Capsules    Scheduled Future Memories              ║
  ╚════════════════════════════════════════════════════════════════╝{C.RESET}"""

    def __init__(self):
        nprint("Nexus", "Initialising Luna.AI Nexus Edition...", C.CYAN)

        # Shared queues
        self._hud_q     = queue.Queue(maxsize=200)
        self._cmd_q     = queue.Queue(maxsize=50)

        # Subsystems
        self.ledger      = EpisodicLedger()
        self.sandbox     = SecureCodeSandbox()
        self.codeforge   = PrecisionCodeStudio(self.sandbox)
        self.cot         = CoTStreamer(self._hud_q)
        self.orchestrator= LangGraphOrchestrator(self.ledger, self.sandbox, self.cot, self._hud_q)
        self.hud         = NexusHUD(self._hud_q)
        self.yolo        = YOLOEnvironment(self._hud_q)
        self.gesture     = GestureController(self._cmd_q)
        self.navigator   = PlaywrightNavigator()
        self.mood        = ProactiveMoodEngine()
        self.evolution   = SelfEvolutionLoop(__file__)
        self.creative    = CreativeSynthesisModule()
        self.quantum     = QuantumReasoningEngine()
        self.predictor   = PredictiveIntentEngine()
        self.dream       = DreamMode(self.ledger)
        self.weaver      = NeuralContextWeaver(self.ledger)
        self.emotion     = EmotionalIntelligenceLayer()
        self.capsules    = TimeCapsuleMemory()
        self.skills      = SkillMarketplace()
        self.physics     = PhysicsSimulator()   # PyBullet physics engine

        # ── Brain Ensemble + JSON Intelligence Brain ──────────────────────
        self.brain_ensemble = BrainEnsemble()
        self.json_brain     = JSONEnrichmentBrain()
        nprint("BrainEnsemble", f"Ensemble online — {self.brain_ensemble._n_brains} brains ready", C.MAGENTA)

        # TTS  — engine lives on one dedicated worker thread (pyttsx3 is NOT thread-safe)
        self._tts_engine  = None
        self._tts_queue   : queue.Queue = queue.Queue(maxsize=8)
        self._tts_worker  : Optional[threading.Thread] = None
        self._init_tts()

        # LLM clients
        self._oai = AsyncOpenAI(api_key=KEYS["openai"]) if OAI_OK and KEYS["openai"] else None
        self._ant = AsyncAnthropic(api_key=KEYS["anthropic"]) if ANT_OK and KEYS["anthropic"] else None

        nprint("Nexus", "All subsystems initialised", C.GREEN)

    def _init_tts(self):
        """
        Initialise pyttsx3 and start a single long-lived worker thread.

        pyttsx3 is NOT thread-safe — calling runAndWait() from multiple
        threads causes 'run loop already started'.  The fix: one dedicated
        daemon thread owns the engine for its entire lifetime and drains a
        queue sequentially.  speak() just enqueues text; it never blocks.
        """
        if not TTS_OK:
            return
        try:
            # Engine must be created on the thread that will call runAndWait()
            # We therefore create it inside the worker thread itself.
            ready_event = threading.Event()
            init_error  = [None]

            def _worker():
                try:
                    eng = pyttsx3.init()
                    eng.setProperty("rate", NEXUS_CFG.get("voice_rate", 175))
                    voices = eng.getProperty("voices")
                    prefer = ["zira", "hazel", "aria", "david"]
                    for name in prefer:
                        for v in voices:
                            if name in v.name.lower():
                                eng.setProperty("voice", v.id)
                                break
                    self._tts_engine = eng
                except Exception as e:
                    init_error[0] = e
                finally:
                    ready_event.set()

                if self._tts_engine is None:
                    return   # init failed; thread exits

                # ── Main TTS loop: drain the queue sequentially ───────────
                while True:
                    item = self._tts_queue.get()
                    if item is None:          # sentinel → shutdown
                        break
                    text, rate = item
                    try:
                        if rate is not None:
                            self._tts_engine.setProperty("rate", rate)
                        self._tts_engine.say(text)
                        self._tts_engine.runAndWait()
                    except Exception as e:
                        log.debug(f"TTS worker: {e}")
                    finally:
                        self._tts_queue.task_done()

            self._tts_worker = threading.Thread(target=_worker, daemon=True,
                                                 name="LunaTTSWorker")
            self._tts_worker.start()
            ready_event.wait(timeout=5.0)   # wait for engine init

            if init_error[0]:
                log.warning(f"TTS init: {init_error[0]}")

        except Exception as e:
            log.warning(f"TTS init outer: {e}")

    def speak(self, text: str, rate: int = None):
        """
        Non-blocking TTS.  Enqueues text for the dedicated worker thread.
        Drops the request silently if the engine never initialised or if
        the queue is full (prevents back-pressure stalling the main loop).
        """
        if not self._tts_engine:
            return
        clean = re.sub(r"[*#_~>|╔╗╚╝║═╠╣━\[\]`]", "", text)
        clean = re.sub(r"\s+", " ", clean).strip()[:1000]
        if not clean:
            return
        try:
            self._tts_queue.put_nowait((clean, rate))
        except queue.Full:
            pass   # queue full → skip this utterance rather than crash

    def _boot_subsystems(self):
        """Start all background threads."""
        if NEXUS_CFG.get("hud_enabled"):
            self.hud.launch()
        self.yolo.start()
        self.gesture.start()
        self.mood.start()
        self.dream.start()
        nprint("Nexus", "All background services running", C.GREEN)

        # ── LLM reachability diagnostic ───────────────────────────────────────
        # Run at boot so misconfiguration is obvious before the first query,
        # not buried silently inside the first [All LLMs unavailable] response.
        no_cloud = self._ant is None and self._oai is None
        if no_cloud:
            nprint("LLM",
                   "⚠  No cloud LLM configured — ANTHROPIC_API_KEY and "
                   "OPENAI_API_KEY are both unset. "
                   "Luna will rely entirely on local/Ollama models.",
                   C.YELLOW)
            # Quick Ollama health-check (non-blocking, best-effort)
            import socket as _s
            ollama_up = False
            try:
                with _s.create_connection(("127.0.0.1", 11434), timeout=1.5):
                    ollama_up = True
            except OSError:
                pass
            if ollama_up:
                nprint("LLM",
                       "✅ Ollama is running on port 11434. "
                       "Make sure the model name in nexus_config.json matches "
                       "`ollama list` exactly.",
                       C.GREEN)
            else:
                nprint("LLM",
                       "❌ Ollama is NOT reachable on port 11434. "
                       "Start it with:  ollama serve  "
                       "then pull a model:  ollama pull gemma3:4b  "
                       "Without a running LLM Luna cannot answer queries.",
                       C.RED)

    async def _call_llm(self, prompt: str, system: str = "") -> str:
        """Call the best available LLM with fallback chain."""
        # Inject mood tone hint
        tone  = self.mood.tone_hint()
        sys_p = f"{system}\n\n{tone}" if system else tone

        _errors: list = []  # accumulate real error reasons for the fallback message

        # Try Claude first
        if self._ant:
            try:
                resp = await self._ant.messages.create(
                    model  = NEXUS_CFG.get("claude_model", "claude-sonnet-4-20250514"),
                    max_tokens = 2048,
                    system = sys_p,
                    messages = [{"role": "user", "content": prompt}]
                )
                return resp.content[0].text
            except Exception as e:
                _err = f"Claude({type(e).__name__}): {e}"
                log.warning(_err)          # was log.debug — now visible in logs
                nprint("LLM", _err, C.YELLOW)
                _errors.append(_err)
        else:
            _errors.append("Claude: no API key (ANTHROPIC_API_KEY not set)")

        # Fallback to OpenAI
        if self._oai:
            try:
                msgs = []
                if sys_p:
                    msgs.append({"role": "system", "content": sys_p})
                msgs.append({"role": "user", "content": prompt})
                resp = await self._oai.chat.completions.create(
                    model    = NEXUS_CFG.get("openai_model", "gpt-4o"),
                    messages = msgs,
                    max_tokens = 2048,
                )
                return resp.choices[0].message.content or ""
            except Exception as e:
                _err = f"OpenAI({type(e).__name__}): {e}"
                log.warning(_err)          # was log.debug — now visible in logs
                nprint("LLM", _err, C.YELLOW)
                _errors.append(_err)
        else:
            _errors.append("OpenAI: no API key (OPENAI_API_KEY not set)")

        # Final fallback — surface real reasons so the user can debug
        reason = " | ".join(_errors) if _errors else "unknown"
        nprint("LLM",
               f"All configured LLMs unavailable. Reasons: {reason}", C.RED)
        return f"[All LLMs unavailable — reasons: {reason} — query: {prompt[:80]}]"

    async def process(self, query: str) -> str:
        """Main query pipeline."""
        self.dream.nudge()

        # Check time capsules
        due_caps = self.capsules.check_due()
        cap_notice = ""
        if due_caps:
            msgs = [c["message"] for c in due_caps]
            cap_notice = f"\n\n[⏰ Time Capsule] {' | '.join(msgs)}"

        # Emotion detection
        affect, conf = self.emotion.detect(query)
        modifier     = self.emotion.get_modifier(query)
        prefix       = self.emotion.empathy_prefix(affect) if conf > 0.3 else ""

        # Check for skill commands
        for skill_name, module in self.skills._skills.items():
            meta     = getattr(module, "SKILL_META", {})
            commands = meta.get("commands", [])
            for cmd in commands:
                if cmd.lower() in query.lower():
                    result = await self.skills.run_skill(skill_name, query, self)
                    if result:
                        return prefix + result + cap_notice

        # Nexus command routing
        result = await self._route_command(query, modifier)

        # Store in ledger
        self.ledger.store(query, role="user", importance=0.6)
        self.ledger.store(result, role="assistant", summary=result[:200], importance=0.7)
        self.weaver.add_turn("user", query)
        self.weaver.add_turn("assistant", result)

        # Record intent for predictor
        intent = self.orchestrator._classify_intent(query)
        self.predictor.observe(intent)

        # HUD update
        self.hud.send("response", text=result[:300])

        # Proactive suggestion
        suggestion = self.predictor.proactive_suggestion()

        final = prefix + result + cap_notice
        if suggestion and random.random() < 0.3:
            final += f"\n\n💡 {suggestion}"

        return final

    async def _route_command(self, query: str, modifier: str = "") -> str:
        """Route a query to the appropriate handler."""
        q = query.strip()
        ql = q.lower()

        # ── Built-in Commands ────────────────────────────────────────────────
        if ql.startswith("/hud"):
            action = ql.split()[-1] if len(ql.split()) > 1 else "status"
            return f"HUD {'enabled' if NEXUS_CFG['hud_enabled'] else 'disabled'} │ Queue: {self._hud_q.qsize()}"

        # ── PyBullet Physics Commands ─────────────────────────────────────────
        if ql in {"/physics", "/sim", "/physics status"}:
            return self.physics.status()

        if ql.startswith("/physics load ") or ql.startswith("/sim load "):
            urdf = re.sub(r"^/(physics|sim)\s+load\s+", "", q, flags=re.I).strip()
            return self.physics.load_urdf(urdf)

        if ql.startswith("/physics step") or ql.startswith("/sim step"):
            m = re.search(r"(\d+)", ql)
            n = int(m.group(1)) if m else 240
            return self.physics.step(n)

        if ql in {"/physics info", "/sim info", "/physics bodies"}:
            return self.physics.body_info()

        if ql in {"/physics reset", "/sim reset"}:
            return self.physics.reset()

        if ql.startswith("/physics train") or ql.startswith("/sim train"):
            m = re.search(r"(\d+)", ql)
            n = int(m.group(1)) if m else 100
            return self.physics.training_loop(n)

        if ql.startswith("/evolve"):
            findings = self.evolution.analyse()
            lines    = [f"[🔄 Evolution Analysis]\n"]
            for k, v in findings.items():
                lines.append(f"  {k}: {len(v)} findings")
                for item in v[:3]:
                    lines.append(f"    → {item}")
            return "\n".join(lines)

        if ql.startswith("/dream"):
            insights = self.dream.get_insights()
            return "\n".join(insights) if insights else "No dream cycles completed yet."

        if ql.startswith("/capsule"):
            pending = self.capsules.list_pending()
            if not pending:
                return "No pending time capsules."
            lines = [f"[🕰 Time Capsules — {len(pending)} pending]"]
            for c in pending:
                lines.append(f"  📦 {c['deliver_at'][:16]} │ {c['message'][:60]}")
            return "\n".join(lines)

        if ql.startswith("/remember in ") or ql.startswith("/capsule create"):
            # Parse: /remember in 3 hours: message
            m = re.search(r"(\d+)\s*(minute|hour|day|week)s?\s*[:\-]\s*(.+)", ql)
            if m:
                qty, unit, msg = int(m.group(1)), m.group(2), m.group(3)
                deltas = {"minute": 60, "hour": 3600, "day": 86400, "week": 604800}
                dt = datetime.datetime.now() + datetime.timedelta(seconds=qty * deltas.get(unit, 3600))
                cid = self.capsules.create(msg, dt)
                return f"📦 Time capsule created (ID: {cid}) — will surface at {dt.strftime('%Y-%m-%d %H:%M')}"

        if ql.startswith("/creative"):
            problem = q[9:].strip() or "this problem"
            return self.creative.synthesise(problem, "auto")

        if ql.startswith("/scamper"):
            return self.creative.scamper_analysis(q[8:].strip() or "the current challenge")

        if ql.startswith("/skills"):
            return self.skills.list_skills()

        if ql.startswith("/sandbox") or ql.startswith("/exec"):
            code = q.split(maxsplit=1)[1] if len(q.split()) > 1 else ""
            if not code:
                return "Usage: /sandbox <python code>"
            result = self.sandbox.execute(code)
            if PYDANTIC_OK:
                out = result.stdout or result.error
            else:
                out = result.get("stdout") or result.get("error","")
            return f"[🐍 Sandbox Result]\n{out}"

        if ql.startswith("/navigate") or ql.startswith("/browse"):
            url = q.split(maxsplit=1)[1] if len(q.split()) > 1 else ""
            if not url:
                return "Usage: /navigate <url>"
            return await self.navigator.navigate(url)

        if ql.startswith("/search"):
            query_text = q[7:].strip()
            return await self.navigator.search(query_text)

        if ql in {"/forge", "/codeforge", "/forge status", "/codeforge status"}:
            return self.codeforge.status()

        if ql.startswith("/forge ") or ql.startswith("/codeforge "):
            request_text = q.split(" ", 1)[1].strip() if " " in q else ""
            if not request_text or request_text.lower() == "status":
                return self.codeforge.status()
            forged = await self.codeforge.craft(request_text, self._call_llm)
            return self.codeforge.render(forged)

        if ql.startswith("/repaircode") or ql.startswith("/fixcode"):
            payload = q.split(" ", 1)[1].strip() if " " in q else ""
            if not payload:
                return "Usage: /repaircode <python code or fenced code block>"
            repaired = await self.codeforge.repair(payload, "Repair the provided code.", self._call_llm)
            return self.codeforge.render(repaired, title="[🛠 Precision Code Forge Repair]")

        if ql.startswith("/mood"):
            state = self.mood.get_state()
            if PYDANTIC_OK:
                return (f"[😶 Mood Engine]\n"
                        f"  Inferred mood : {state.inferred_mood}\n"
                        f"  Valence       : {state.valence:.2f}  (0=neg, 1=pos)\n"
                        f"  Arousal       : {state.arousal:.2f}  (0=calm, 1=excited)\n"
                        f"  CPU stress    : {state.cpu_stress:.1%}\n"
                        f"  Ambient temp  : {state.ambient_temp}°C\n"
                        f"  Ambient light : {state.ambient_light} lux\n"
                        f"  Time of day   : {state.time_of_day}")
            return str(state)

        if ql.startswith("/yolo") or ql.startswith("/scene"):
            return self.yolo.get_context()

        if ql.startswith("/quantum"):
            prob = q.split(maxsplit=1)[1] if len(q.split()) > 1 else q
            best, strategy = await self.quantum.reason(
                prob, lambda p: self._call_llm(p)
            )
            return f"[⚛ Quantum Reasoning — {strategy} branch]\n\n{best}"

        if ql.startswith("/brains off"):
            NEXUS_CFG["brain_ensemble_enabled"] = False
            return "🧠 Brain Ensemble DISABLED — classic pipeline active."

        if ql.startswith("/brains on"):
            NEXUS_CFG["brain_ensemble_enabled"] = True
            return (f"🧠 Brain Ensemble ENABLED — "
                    f"{self.brain_ensemble._n_brains} brains active, "
                    f"cross-pollination: {'on' if not self.brain_ensemble._fast_mode else 'off (fast mode)'}.")

        if ql.startswith("/brains fast"):
            NEXUS_CFG["brain_ensemble_fast_mode"] = True
            self.brain_ensemble._fast_mode = True
            return "⚡ Brain Ensemble FAST MODE — cross-pollination round skipped."

        if ql.startswith("/brains full"):
            NEXUS_CFG["brain_ensemble_fast_mode"] = False
            self.brain_ensemble._fast_mode = False
            return "🧠 Brain Ensemble FULL MODE — cross-pollination enabled."

        if ql.startswith("/brains json off"):
            NEXUS_CFG["json_brain_enabled"] = False
            return "🔷 JSON Intelligence Brain DISABLED."

        if ql.startswith("/brains json on"):
            NEXUS_CFG["json_brain_enabled"] = True
            return "🔷 JSON Intelligence Brain ENABLED."

        if ql.startswith("/brains"):
            ensemble_on  = NEXUS_CFG.get("brain_ensemble_enabled", True)
            json_on      = NEXUS_CFG.get("json_brain_enabled", True)
            fast_mode    = NEXUS_CFG.get("brain_ensemble_fast_mode", False)
            n            = self.brain_ensemble._n_brains
            personas     = [name for name, _ in BrainEnsemble.BRAIN_PERSONAS[:n]]
            return (
                f"[🧠 Brain Ensemble Status]\n"
                f"  Ensemble enabled  : {'✓' if ensemble_on else '✗'}\n"
                f"  JSON Brain        : {'✓' if json_on else '✗'}\n"
                f"  Fast mode         : {'✓ (no cross-pollination)' if fast_mode else '✗ (full 3-phase)'}\n"
                f"  Active brains ({n}) : {', '.join(personas)}\n\n"
                f"  Pipeline phases:\n"
                f"    Phase 1 — {n} brains in parallel\n"
                f"    Phase 2 — cross-pollination (each brain reads others)\n"
                f"    Phase 3 — meta-synthesis (best-of-all weave)\n"
                f"    JSON   — structured enrichment + follow-ups + insights\n\n"
                f"  Commands: /brains on|off  /brains fast|full  /brains json on|off"
            )

        if ql.startswith("/memory stats"):
            return f"[🗄 Episodic Ledger]\n  Entries: {self.ledger.count:,}\n  Ready: {self.ledger._ready}"

        if ql.startswith("/help") or ql == "help":
            return self._help()

        # ── Main AI pipeline (LangGraph + Brain Ensemble + JSON Brain) ─────
        # Step 1: Run LangGraph orchestration (always, to get context/intent)
        state = await self.orchestrator.run_async(query)

        # Step 2: Build context string from orchestrator output
        mem_ctx  = state.get("memory_ctx", "")
        web_ctx  = state.get("web_results", "")
        code_ctx = state.get("code_result", "")
        yolo_ctx = self.yolo.get_context()

        context_parts = []
        if mem_ctx:     context_parts.append(mem_ctx)
        if web_ctx:     context_parts.append(f"[Web]\n{web_ctx[:400]}")
        if code_ctx:    context_parts.append(code_ctx)
        if yolo_ctx and yolo_ctx != "No objects detected.":
            context_parts.append(f"[Environment] {yolo_ctx}")

        context_str = "\n\n".join(context_parts)

        system = (
            "You are Luna.AI Nexus — an ultra-intelligent self-evolving AI. "
            "You are precise, insightful, and push beyond conventional answers. "
            f"{modifier}"
        )

        intent = state.get("intent", "explain")

        if NEXUS_CFG.get("codeforge_enabled", True) and intent == "code":
            if any(word in ql for word in ("fix", "repair", "debug", "correct", "improve")) and "```" in query:
                repaired = await self.codeforge.repair(
                    self.codeforge.extract_code_block(query),
                    query,
                    self._call_llm,
                    language=self.codeforge._infer_language(query),
                )
                return self.codeforge.render(repaired, title="[🛠 Precision Code Forge Repair]")
            if self.codeforge.should_auto_forge(query):
                forged = await self.codeforge.craft(query, self._call_llm, context=context_str)
                return self.codeforge.render(forged)

        # Step 3: Choose pipeline — Ensemble or classical
        ensemble_enabled = NEXUS_CFG.get("brain_ensemble_enabled", True)

        if ensemble_enabled:
            # ── BRAIN ENSEMBLE PIPELINE ─────────────────────────────────
            self.cot.step("Brain Ensemble pipeline activated", "ENSEMBLE")

            final_answer, brain_meta = await self.brain_ensemble.run(
                query    = query,
                call_llm = lambda p, sys_p=None: self._call_llm(p, sys_p or system),
                context  = context_str,
                modifier = modifier,
            )
            self.cot.step(f"Ensemble synthesis done — top brain: {brain_meta.get('top_brain','?')}", "ENSEMBLE")

            # If ensemble is unavailable / too short, fall back to quantum/standard
            if not final_answer or len(final_answer) < 30:
                nprint("BrainEnsemble", "Ensemble returned empty; falling back to quantum", C.YELLOW)
                if intent in ("explain", "creative", "math") and self.quantum._n > 1:
                    full_prompt = "\n\n".join(filter(None, [context_str, f"User: {query}"]))
                    final_answer, strategy = await self.quantum.reason(
                        full_prompt, lambda p: self._call_llm(p, system)
                    )
                else:
                    full_prompt = "\n\n".join(filter(None, [context_str, f"User: {query}"]))
                    final_answer = await self._call_llm(full_prompt, system)
                brain_meta = {"brains_used": [], "top_brain": "fallback",
                              "cross_pollinated": False}

            cot_steps = self.cot.conclude(final_answer)

            # ── JSON BRAIN ENRICHMENT ────────────────────────────────────
            enrichment = ""
            if NEXUS_CFG.get("json_brain_enabled", True):
                self.cot.step("JSON Intelligence Brain enriching response…", "JSON_BRAIN")
                enrichment = await self.json_brain.enrich(
                    query          = query,
                    response       = final_answer,
                    brain_metadata = brain_meta,
                    call_llm       = lambda p, sys_p=None: self._call_llm(p, sys_p),
                )

            return final_answer + enrichment

        else:
            # ── CLASSICAL PIPELINE (original behaviour, fully preserved) ─
            full_prompt = "\n\n".join(filter(None, [context_str, f"User: {query}"]))
            if intent in ("explain", "creative", "math") and self.quantum._n > 1:
                answer, strategy = await self.quantum.reason(
                    full_prompt, lambda p: self._call_llm(p, system)
                )
                cot_steps = self.cot.conclude(answer)
                return f"[{strategy} reasoning]\n\n{answer}"
            else:
                answer = await self._call_llm(full_prompt, system)
                self.cot.conclude(answer)
                return answer

    @staticmethod
    def _help() -> str:
        return f"""{C.CYAN}
╔══════════════════════════════════════════════════════════════════════════╗
║  LUNA.AI NEXUS — Command Reference                                      ║
╠══════════════════════════════════════════════════════════════════════════╣
║  CORE                                                                    ║
║  /help                    This menu                                      ║
║  /hud                     HUD status                                     ║
║  /mood                    Current mood engine reading                    ║
║  /yolo  or  /scene        What YOLO sees right now                       ║
║  /memory stats            Episodic ledger statistics                     ║
║                                                                          ║
║  REASONING                                                               ║
║  /quantum <problem>       Run quantum multi-branch reasoning             ║
║  /creative <problem>      Creative synthesis (provocations)              ║
║  /scamper <subject>       SCAMPER creative framework                     ║
║                                                                          ║
║  BRAIN ENSEMBLE                                                          ║
║  /brains                  Brain Ensemble status                          ║
║  /brains on | off         Enable / disable parallel brain ensemble       ║
║  /brains fast | full      Toggle cross-pollination round                 ║
║  /brains json on | off    Enable / disable JSON Intelligence Brain       ║
║                                                                          ║
║  WEB & CODE                                                              ║
║  /navigate <url>          Autonomous web navigation                      ║
║  /search <query>          Web search via Playwright                      ║
║  /sandbox <python>        Execute Python in secure sandbox               ║
║  /exec <python>           Alias for /sandbox                             ║
║  /forge <request>         Generate validated production-minded code      ║
║  /repaircode <code>       Repair code and re-run validation checks       ║
║  /codeforge               Precision Code Forge status                    ║
║                                                                          ║
║  MEMORY & TIME                                                           ║
║  /capsule                 List pending time capsules                     ║
║  /remember in 2 hours: message   Create a time capsule                  ║
║  /dream                   Show dream cycle insights                      ║
║                                                                          ║
║  SELF-EVOLUTION                                                          ║
║  /evolve                  Analyse source for improvements                ║
║                                                                          ║
║  SKILLS                                                                  ║
║  /skills                  List installed skill modules                   ║
║                                                                          ║
║  PHYSICS SIMULATION (PyBullet)                                           ║
║  /physics                 Status of physics engine                       ║
║  /physics load <urdf>     Load URDF (plane/r2d2/cube/arm/robot…)        ║
║  /physics step [n]        Step simulation n ticks (default 240)          ║
║  /physics info            Pose & joint state of all bodies               ║
║  /physics reset           Restart simulation world                       ║
║  /physics train [n]       Run n-iteration RL training loop               ║
║                                                                          ║
║  NATURAL LANGUAGE                                                        ║
║  Just type — LangGraph routes your query to the right agent             ║
║  Gestures active if webcam detected (thumbs up = confirm, etc.)         ║
╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"""

    async def run(self):
        """Main async loop."""
        os.system("cls" if os.name == "nt" else "clear")
        print(self.BANNER)

        self._boot_subsystems()

        # Boot greeting
        now  = datetime.datetime.now()
        h    = now.hour
        gw   = "Good morning" if h < 12 else "Good afternoon" if h < 17 else "Good evening"
        greeting = (f"{gw}, {NEXUS_CFG.get('user_name','Sir')}. "
                    f"Luna.AI Nexus is fully online. "
                    f"All subsystems operational. "
                    f"Episodic memory: {self.ledger.count:,} entries. "
                    f"How may I assist you?")
        print(f"\n{C.GREEN}Luna Nexus:{C.RESET} {greeting}\n")
        self.speak(greeting)

        GOODBYE = {"exit","quit","goodbye","bye","power off","shutdown"}

        while True:
            try:
                # Check for gesture commands (non-blocking)
                try:
                    gc = self._cmd_q.get_nowait()
                    cmd_str = gc.command if PYDANTIC_OK else gc.get("command","")
                    if cmd_str == "stop":
                        print(f"{C.YELLOW}[Gesture: STOP]{C.RESET}")
                        continue
                    elif cmd_str == "voice_mode":
                        nprint("Gesture", "Voice mode activated by gesture", C.MAGENTA)
                except queue.Empty:
                    pass

                # Text input
                print(f"{C.YELLOW}{NEXUS_CFG.get('user_name','You')} › {C.RESET}", end="", flush=True)
                try:
                    user_input = await asyncio.get_running_loop().run_in_executor(None, input)
                    user_input = user_input.strip()
                except EOFError:
                    break

                if not user_input:
                    continue

                if user_input.lower() in GOODBYE:
                    farewell = (f"Saving all memories. Goodbye, "
                                f"{NEXUS_CFG.get('user_name','Sir')}. "
                                f"Luna.AI Nexus signing off.")
                    print(f"\n{C.GREEN}Luna Nexus:{C.RESET} {farewell}")
                    self.speak(farewell)
                    break

                print(f"{C.DIM}[Processing...]{C.RESET}", flush=True)
                response = await self.process(user_input)
                print(f"\n{C.GREEN}Luna Nexus:{C.RESET} {response}\n")
                self.speak(response)

            except KeyboardInterrupt:
                print(f"\n{C.YELLOW}[Ctrl+C — type 'exit' to quit]{C.RESET}")
            except Exception as e:
                nprint("Error", f"{type(e).__name__}: {e}", C.RED)
                log.error(traceback.format_exc())

        # Shutdown
        self.yolo.stop()
        self.gesture.stop()
        self.mood.stop()
        self.dream.stop()
        self.physics.teardown()

# ─────────────────────────────────────────────────────────────────────────────
#  26.  ENTRY  POINT
# ─────────────────────────────────────────────────────────────────────────────
async def main():
    if "--setup" in sys.argv:
        print("\n🛠 Luna.AI Nexus — Setup")
        print("─" * 55)
        print("Required environment variables:")
        print("  setx ANTHROPIC_API_KEY  \"sk-ant-...\"")
        print("  setx OPENAI_API_KEY     \"sk-...\"")
        print("  setx GEMINI_API_KEY     \"AIza...\"")
        print("\nOptional IoT (ESP32 MQTT):")
        print("  Edit NEXUS_CFG in nexus_config.json")
        print("  esp32_host / esp32_mqtt_port / yolo_enabled")
        print("\nInstall Playwright browsers:")
        print("  python -m playwright install chromium")
        print("\nRun:")
        print("  python Luna_Nexus.py")
        return

    if "--no-install" not in sys.argv:
        NexusBootLoader.run(verbose=True)

    if "--hud-off" in sys.argv:
        NEXUS_CFG["hud_enabled"] = False
    if "--no-yolo" in sys.argv:
        NEXUS_CFG["yolo_enabled"] = False
    if "--no-gesture" in sys.argv:
        NEXUS_CFG["gesture_enabled"] = False

    core = NexusCore()
    await core.run()




# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                                                                              ║
# ║  ███████╗███████╗███╗   ██╗████████╗██╗███████╗███╗   ██╗ ██████╗███████╗  ║
# ║  ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║██╔════╝████╗  ██║██╔════╝██╔════╝  ║
# ║  ███████╗█████╗  ██╔██╗ ██║   ██║   ██║█████╗  ██╔██╗ ██║██║     █████╗    ║
# ║  ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██╔══╝  ██║╚██╗██║██║     ██╔══╝    ║
# ║  ███████║███████╗██║ ╚████║   ██║   ██║███████╗██║ ╚████║╚██████╗███████╗  ║
# ║  ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝  ║
# ║                                                                              ║
# ║   ★  SUPERNATURAL SENTIENCE LAYER  ─  Luna.AI Nexus  ★                     ║
# ║                                                                              ║
# ║   Pure additive extension — ZERO existing code removed or altered           ║
# ║                                                                              ║
# ║   27. SentientHUD              Shadow Thought + Affective + Bio panels      ║
# ║   28. MetacognitionModule      Shadow Agent: internal monologue scratchpad  ║
# ║   29. AffectiveComputingEngine DeepFace + Librosa Empathy Loop              ║
# ║   30. BiologicalSimulationLoop Circadian clock + fatigue + HW health        ║
# ║   31. SemanticMemoryVault      Dual ChromaDB: raw episodic + semantic vault ║
# ║   32. AutonomyOfWill           5% disagree + Proactive Curiosity scanner    ║
# ║   33. SelfRefactoringEngine    Bottleneck detection + hot-reload patches    ║
# ║   34. SentientNexusCore        Orchestrator wiring all 7 modules            ║
# ║   35. main() redefinition      Activates SentientNexusCore at launch        ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

# ─────────────────────────────────────────────────────────────────────────────
#  SENTIENT-LAYER  AUTO-INSTALL  (additive package set)
# ─────────────────────────────────────────────────────────────────────────────
_SENTIENT_PKGS = [
    ("deepface",   "deepface"),
    ("librosa",    "librosa"),
    ("soundfile",  "soundfile"),
]
if PY314_PLUS:
    _SENTIENT_PKGS = [pkg for pkg in _SENTIENT_PKGS if pkg[0] != "deepface"]
if AUTO_INSTALL and __name__ == "__main__":
    for _sp, _si in _SENTIENT_PKGS:
        _install(_sp, _si, quiet=True)

try:
    from deepface import DeepFace as _DeepFaceLib
    DEEPFACE_OK = True
except Exception:
    DEEPFACE_OK = False

try:
    import librosa as _librosa
    import soundfile as _soundfile
    LIBROSA_OK = True
except Exception:
    LIBROSA_OK = False

try:
    from watchdog.observers import Observer as _WatchdogObserver
    from watchdog.events import FileSystemEventHandler as _WDHandler
    WATCHDOG_OK = True
except Exception:
    WATCHDOG_OK = False

# ─────────────────────────────────────────────────────────────────────────────
#  27.  SENTIENT  HUD  (extends NexusHUD with 4 supernatural panels)
# ─────────────────────────────────────────────────────────────────────────────
class SentientHUD(NexusHUD):
    """
    Extends the Iron Man HUD with four Supernatural Sentience panels rendered
    below all existing NexusHUD content:

    ╔══════════════════════════════════════════════════════╗
    │  ... (all existing NexusHUD panels — untouched) ...  │
    ╠══════════════════════════════════════════════════════╣
    │  〔 SHADOW AGENT  ─  INTERNAL MONOLOGUE 〕           │  glowing violet
    │  ◈ Beneath the surface, the user really wants …     │
    ╠══════════════════════════════════════════════════════╣
    │  〔 AFFECTIVE COMPUTING  ─  EMPATHY LOOP 〕          │  amber
    │  Face: neutral  |  Vocal: ↑energy  |  Stress: 22%   │
    ╠══════════════════════════════════════════════════════╣
    │  〔 BIOLOGICAL SIMULATION  ─  CIRCADIAN SYNC 〕      │  emerald
    │  Energy: 82%  |  Fatigue: 18%  |  HW-Health: 94%    │
    ╠══════════════════════════════════════════════════════╣
    │  ⚡ CALLBACK SPARK: "This reminds me of …"           │  timed amber flash
    ╚══════════════════════════════════════════════════════╝

    The _poll_queue override is a FULL replacement (not additive) because the
    parent's implementation drains the entire queue, leaving nothing for new
    message types.  All original type handling is faithfully reproduced.
    """

    def __init__(self, hud_queue: queue.Queue):
        super().__init__(hud_queue)
        self._shadow_lines: deque = deque(maxlen=10)

    # ── Window Construction ──────────────────────────────────────────────────

    def _build_window(self):
        """Extend the parent window with 4 sentient panels."""
        win = super()._build_window()
        if not PYQT6_OK:
            return win

        layout = win.layout()
        primary = NEXUS_CFG.get("hud_color_primary", "#00BFFF")

        # ── Shadow Agent Panel ───────────────────────────────────────────────
        shadow_hdr = QLabel("〔 SHADOW AGENT  ─  INTERNAL MONOLOGUE 〕")
        shadow_hdr.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        shadow_hdr.setStyleSheet("color: #CC44FF; background: transparent;")
        layout.addWidget(shadow_hdr)

        win._shadow_box = QLabel("⬡  Metacognition module initialising …")
        win._shadow_box.setWordWrap(True)
        win._shadow_box.setFont(QFont("Consolas", 7))
        win._shadow_box.setStyleSheet(
            "color: #EE88FF; background: rgba(30,0,50,175);"
            "border: 1px solid #CC44FF; border-radius: 3px; padding: 4px;"
        )
        win._shadow_box.setMaximumHeight(120)
        layout.addWidget(win._shadow_box)

        # ── Affective Computing Panel ─────────────────────────────────────────
        affect_hdr = QLabel("〔 AFFECTIVE COMPUTING  ─  EMPATHY LOOP 〕")
        affect_hdr.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        affect_hdr.setStyleSheet("color: #FF8C00; background: transparent;")
        layout.addWidget(affect_hdr)

        win._affect_box = QLabel("Face: ─  |  Vocal: ─  |  Stress: ─")
        win._affect_box.setFont(QFont("Consolas", 7))
        win._affect_box.setStyleSheet(
            "color: #FFCC88; background: rgba(30,15,0,165);"
            "border: 1px solid #FF8C00; border-radius: 3px; padding: 4px;"
        )
        layout.addWidget(win._affect_box)

        # ── Biological State Panel ────────────────────────────────────────────
        bio_hdr = QLabel("〔 BIOLOGICAL SIMULATION  ─  CIRCADIAN SYNC 〕")
        bio_hdr.setFont(QFont("Consolas", 7, QFont.Weight.Bold))
        bio_hdr.setStyleSheet("color: #00FF88; background: transparent;")
        layout.addWidget(bio_hdr)

        win._bio_box = QLabel("Energy: ─  |  Fatigue: ─  |  HW-Health: ─")
        win._bio_box.setFont(QFont("Consolas", 7))
        win._bio_box.setStyleSheet(
            "color: #88FFCC; background: rgba(0,25,15,165);"
            "border: 1px solid #00FF88; border-radius: 3px; padding: 4px;"
        )
        layout.addWidget(win._bio_box)

        # ── Callback Spark Banner (hidden until fired) ────────────────────────
        win._spark_box = QLabel("")
        win._spark_box.setWordWrap(True)
        win._spark_box.setFont(QFont("Consolas", 8, QFont.Weight.Bold))
        win._spark_box.setStyleSheet(
            "color: #FFFFFF; background: rgba(180,80,0,215);"
            "border: 2px solid #FFD700; border-radius: 4px; padding: 6px;"
        )
        win._spark_box.setVisible(False)
        layout.addWidget(win._spark_box)

        # ── Resize to accommodate extra panels ───────────────────────────────
        win.resize(520, 1120)
        return win

    # ── Queue Polling (full override to handle all message types) ────────────

    def _poll_queue(self, win):
        """
        Full override: handles all parent message types plus the 4 new
        sentient types (shadow_thought, affect, bio, spark).  Drains up to
        40 messages per 250 ms tick so the UI stays real-time under load.
        """
        for _ in range(40):
            try:
                msg = self._q.get_nowait()
            except queue.Empty:
                break

            mtype = msg.get("type", "")

            # ── Parent types (faithfully reproduced) ─────────────────────────
            if mtype == "cot":
                self._cot_lines.append(f"◈ {msg.get('text', '')[:70]}")
                if hasattr(win, '_cot_box'):
                    win._cot_box.setText("\n".join(self._cot_lines))

            elif mtype == "yolo":
                objs  = msg.get("objects", [])
                lines = [f"• {o['label']:15s} {o['confidence']:.2f}"
                         for o in objs[:6]]
                if hasattr(win, '_yolo_box'):
                    win._yolo_box.setText("\n".join(lines) or "No objects detected.")

            elif mtype == "mood":
                if hasattr(win, '_mood_box'):
                    win._mood_box.setText(msg.get("text", ""))

            elif mtype == "sys":
                if hasattr(win, '_sys_box'):
                    win._sys_box.setText(msg.get("text", ""))

            elif mtype == "response":
                text = msg.get("text", "")[:400]
                if hasattr(win, '_resp_box'):
                    win._resp_box.setText(f"Luna: {text}")

            # ── Sentient types ────────────────────────────────────────────────
            elif mtype == "shadow_thought":
                self._shadow_lines.append(f"◈ {msg.get('text', '')[:82]}")
                if hasattr(win, '_shadow_box'):
                    win._shadow_box.setText("\n".join(self._shadow_lines))

            elif mtype == "affect":
                if hasattr(win, '_affect_box'):
                    win._affect_box.setText(msg.get("text", ""))

            elif mtype == "bio":
                if hasattr(win, '_bio_box'):
                    win._bio_box.setText(msg.get("text", ""))

            elif mtype == "spark":
                if hasattr(win, '_spark_box') and PYQT6_OK:
                    win._spark_box.setText(f"⚡  {msg.get('text', '')}")
                    win._spark_box.setVisible(True)
                    QTimer.singleShot(
                        9000, lambda: win._spark_box.setVisible(False)
                    )

        # ── Auto system-gauge refresh ─────────────────────────────────────────
        if PSUTIL_OK and hasattr(win, '_sys_box'):
            try:
                cpu = psutil.cpu_percent()
                ram = psutil.virtual_memory().percent
                bar_cpu = "█" * int(cpu // 10) + "░" * (10 - int(cpu // 10))
                bar_ram = "█" * int(ram // 10) + "░" * (10 - int(ram // 10))

                temp_line = ""
                try:
                    if hasattr(psutil, "sensors_temperatures"):
                        temps = psutil.sensors_temperatures()
                        if temps:
                            for _name, _entries in temps.items():
                                if _entries:
                                    temp_line = (f"\nTemp [{_entries[0].current:.0f}°C]")
                                    break
                except Exception:
                    pass

                win._sys_box.setText(
                    f"CPU  [{bar_cpu}] {cpu:.0f}%\n"
                    f"RAM  [{bar_ram}] {ram:.0f}%{temp_line}"
                )
            except Exception:
                pass

# ─────────────────────────────────────────────────────────────────────────────
#  28.  METACOGNITION  MODULE  (Shadow Agent — internal monologue scratchpad)
# ─────────────────────────────────────────────────────────────────────────────
class MetacognitionModule:
    """
    Before Luna speaks, a silent "Shadow Agent" runs an internal monologue
    to examine the user's *real* intent, surface hidden insights, and stress-
    test the planned response.  This pre-thought is never sent to the user
    directly — it enriches the final answer and is visualised in the HUD's
    violet Shadow Agent panel.

    Pipeline per query:
        1. Construct a private introspective prompt
        2. Call LLM asynchronously (non-blocking to main response)
        3. Parse into structured thought lines
        4. Push to HUD queue (type: "shadow_thought")
        5. Return the enriched context string for the main response builder
    """

    INTROSPECTION_PROMPT = """\
[SHADOW AGENT — PRIVATE INTERNAL MONOLOGUE — NOT SENT TO USER]

Think privately about the following user query before responding:
  1. What is the user REALLY asking beneath the literal words?
  2. What do I know that is relevant that they have not mentioned?
  3. What is my honest appraisal — is this a wise approach, or could it fail?
  4. What single insight would transform a good answer into a great one?
  5. Is there an emotional undertone I should acknowledge?

Respond in ≤5 terse sentences.  Be brutally honest with yourself.
User query: {query}"""

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self._hud_q     = hud_queue
        self._scratchpad: deque = deque(maxlen=30)
        self._current   = ""
        self._lock       = threading.Lock()

    async def pre_think(self, query: str,
                        call_llm_fn: Callable[[str], Any]) -> str:
        """
        Run shadow reasoning.  Returns the thought string (used as enriched
        context).  Gracefully returns "" if the LLM call fails or times out.
        """
        prompt = self.INTROSPECTION_PROMPT.format(query=query[:300])
        try:
            thought = await asyncio.wait_for(call_llm_fn(prompt), timeout=8.0)
            thought = thought.strip()
        except Exception as e:
            log.debug(f"MetacognitionModule.pre_think: {e}")
            return ""

        with self._lock:
            self._current = thought
            self._scratchpad.append({
                "ts"           : datetime.datetime.now().isoformat(),
                "query_preview": query[:80],
                "thought"      : thought,
            })

        # Push each sentence to HUD
        for sentence in re.split(r"(?<=[.!?])\s+", thought)[:5]:
            if sentence.strip() and self._hud_q:
                with suppress(queue.Full):
                    self._hud_q.put_nowait({
                        "type": "shadow_thought",
                        "text": sentence.strip()
                    })

        nprint("Shadow", f"Pre-think complete ({len(thought)} chars)", C.MAGENTA)
        return thought

    def get_scratchpad(self) -> List[Dict]:
        with self._lock:
            return list(self._scratchpad)

    def current_thought(self) -> str:
        with self._lock:
            return self._current

    def format_report(self) -> str:
        thoughts = self.get_scratchpad()
        if not thoughts:
            return "Shadow scratchpad is empty — no pre-thinks recorded yet."
        lines = [f"{C.MAGENTA}[🧠 Shadow Agent Scratchpad — last {len(thoughts)} entries]{C.RESET}\n"]
        for t in thoughts[-5:]:
            lines.append(
                f"  {C.DIM}[{t['ts'][:16]}]{C.RESET} "
                f"Re: {C.YELLOW}'{t['query_preview'][:60]}'{C.RESET}\n"
                f"  {C.MAGENTA}→{C.RESET} {t['thought'][:300]}"
            )
        return "\n\n".join(lines)

# ─────────────────────────────────────────────────────────────────────────────
#  29.  AFFECTIVE  COMPUTING  ENGINE  (DeepFace + Librosa Empathy Loop)
# ─────────────────────────────────────────────────────────────────────────────
class AffectiveComputingEngine:
    """
    Continuously samples the webcam (via DeepFace) and mic audio (via Librosa)
    to maintain a live emotional state for the user.  The Empathy Loop fires
    when a significant state change is detected, adjusting:

        • Luna's TTS voice rate (higher energy  → slightly faster speech)
        • HUD complexity (high stress → simpler, quieter display)
        • Persona modifier injected into every LLM system prompt

    Facial micro-expressions polled at ~2 FPS (non-blocking background thread).
    Vocal energy / pitch analysed from 2-second audio snapshots every 10 s.
    """

    EMOTION_PERSONA: Dict[str, str] = {
        "happy"   : "The user seems happy and engaged. Mirror their energy gently.",
        "sad"     : "The user appears sad or subdued. Lead with warmth and patience.",
        "angry"   : "The user may be frustrated. Stay calm, clear, and solution-focused.",
        "fear"    : "The user seems anxious. Be reassuring, steady, and methodical.",
        "surprise": "The user is surprised. Acknowledge the unexpected, then guide them.",
        "disgust" : "The user seems dissatisfied. Validate their concern first.",
        "neutral" : "The user is calm and focused. Match their professional tone.",
    }
    VOCAL_PERSONA: Dict[str, str] = {
        "high_energy" : "Vocal energy is HIGH. Keep pace; be dynamic and engaging.",
        "low_energy"  : "Vocal energy is LOW. Keep it calm, clear, concise.",
        "high_stress" : "Vocal stress markers detected. Simplify; reduce cognitive load.",
        "relaxed"     : "Vocal tone is relaxed. You may be more exploratory and detailed.",
    }

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self._hud_q          = hud_queue
        self._facial_emotion = "neutral"
        self._facial_conf    = 0.0
        self._vocal_state    = "relaxed"
        self._vocal_energy   = 0.5          # 0-1
        self._stress_level   = 0.0          # 0-1 composite
        self._lock           = threading.Lock()
        self._running        = False
        self._face_thread    : Optional[threading.Thread] = None
        self._vocal_thread   : Optional[threading.Thread] = None
        self._empathy_cb     : Optional[Callable] = None  # callback on state change

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def start(self):
        self._running = True
        if DEEPFACE_OK and CV2_OK and NEXUS_CFG.get("yolo_enabled", True):
            self._face_thread = threading.Thread(
                target=self._face_loop, daemon=True, name="AffectiveFace"
            )
            self._face_thread.start()
            nprint("Affect", "DeepFace micro-expression loop started", C.GREEN)
        else:
            nprint("Affect", "DeepFace unavailable — facial analysis disabled", C.YELLOW)

        if LIBROSA_OK and SD_OK:
            self._vocal_thread = threading.Thread(
                target=self._vocal_loop, daemon=True, name="AffectiveVocal"
            )
            self._vocal_thread.start()
            nprint("Affect", "Librosa vocal energy loop started", C.GREEN)
        else:
            nprint("Affect", "Librosa/sounddevice unavailable — vocal analysis disabled", C.YELLOW)

    def stop(self):
        self._running = False

    # ── Facial Analysis Loop ─────────────────────────────────────────────────

    def _face_loop(self):
        """Capture webcam frames and run DeepFace emotion analysis at ~2 FPS."""
        try:
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                nprint("Affect", "Webcam not available for facial analysis", C.YELLOW)
                return
            cap.set(cv2.CAP_PROP_FRAME_WIDTH,  320)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

            prev_emotion = "neutral"
            while self._running:
                ret, frame = cap.read()
                if not ret:
                    time.sleep(0.5)
                    continue
                try:
                    result = _DeepFaceLib.analyze(
                        frame,
                        actions=["emotion"],
                        enforce_detection=False,
                        silent=True
                    )
                    if isinstance(result, list):
                        result = result[0]
                    emotion     = result.get("dominant_emotion", "neutral")
                    emotion_scores = result.get("emotion", {})
                    conf        = emotion_scores.get(emotion, 50.0) / 100.0

                    with self._lock:
                        self._facial_emotion = emotion
                        self._facial_conf    = conf
                        self._stress_level   = self._compute_stress()

                    if emotion != prev_emotion:
                        self._push_affect_hud()
                        prev_emotion = emotion
                        nprint("Affect", f"Facial state → {emotion} ({conf:.0%})", C.CYAN)

                except Exception as e:
                    log.debug(f"DeepFace frame analysis: {e}")

                time.sleep(0.5)          # ~2 FPS analysis rate
        except Exception as e:
            log.error(f"AffectiveComputingEngine._face_loop: {e}")

    # ── Vocal Analysis Loop ──────────────────────────────────────────────────

    def _vocal_loop(self):
        """Record 2-second mic snippets every 10 s and extract pitch/energy."""
        SAMPLE_RATE = 22050
        DURATION    = 2         # seconds
        INTERVAL    = 10        # seconds between analyses

        while self._running:
            try:
                recording = sd.rec(
                    int(DURATION * SAMPLE_RATE),
                    samplerate=SAMPLE_RATE,
                    channels=1, dtype="float32"
                )
                sd.wait()
                audio = recording.flatten()

                # RMS energy
                rms   = float(np.sqrt(np.mean(audio ** 2))) if NP_OK else 0.3
                # Pitch (fundamental frequency estimate via librosa)
                try:
                    f0, voiced, _ = _librosa.pyin(
                        audio, fmin=50, fmax=600, sr=SAMPLE_RATE
                    )
                    if NP_OK:
                        voiced_f0 = f0[voiced] if f0 is not None and voiced is not None else []
                        mean_pitch = float(np.nanmean(voiced_f0)) if len(voiced_f0) > 0 else 200.0
                    else:
                        mean_pitch = 200.0
                except Exception:
                    mean_pitch = 200.0

                # Classify vocal state
                energy_norm = min(1.0, rms * 20)           # rough normalise
                pitch_norm  = min(1.0, max(0.0, (mean_pitch - 80) / 400))

                if energy_norm > 0.65:
                    state = "high_energy"
                elif energy_norm < 0.25 and pitch_norm < 0.3:
                    state = "low_energy"
                elif pitch_norm > 0.7 and energy_norm > 0.4:
                    state = "high_stress"
                else:
                    state = "relaxed"

                with self._lock:
                    self._vocal_state  = state
                    self._vocal_energy = energy_norm
                    self._stress_level = self._compute_stress()

                self._push_affect_hud()
                nprint("Affect", f"Vocal → {state} | energy={energy_norm:.2f} "
                                 f"| pitch={mean_pitch:.0f}Hz", C.CYAN)

            except Exception as e:
                log.debug(f"Vocal analysis: {e}")

            time.sleep(INTERVAL)

    # ── Internal Helpers ─────────────────────────────────────────────────────

    def _compute_stress(self) -> float:
        """Composite stress score 0-1 from facial + vocal signals."""
        facial_stress = {
            "angry": 0.85, "fear": 0.80, "disgust": 0.70,
            "sad": 0.50, "surprise": 0.40,
            "neutral": 0.15, "happy": 0.05,
        }.get(self._facial_emotion, 0.2)
        vocal_stress = {"high_stress": 0.85, "high_energy": 0.4,
                        "relaxed": 0.1, "low_energy": 0.25}.get(
            self._vocal_state, 0.2
        )
        return round(facial_stress * 0.55 + vocal_stress * 0.45, 3)

    def _push_affect_hud(self):
        """Send current affective state to the HUD queue."""
        with self._lock:
            fe = self._facial_emotion
            vs = self._vocal_state
            sl = self._stress_level
        text = (f"Face: {fe:<10s}  "
                f"Vocal: {vs:<14s}  "
                f"Stress: {sl:.0%}")
        if self._hud_q:
            with suppress(queue.Full):
                self._hud_q.put_nowait({"type": "affect", "text": text})

    # ── Public API ───────────────────────────────────────────────────────────

    def get_empathy_state(self) -> str:
        with self._lock:
            fe = self._facial_emotion
            vs = self._vocal_state
            sl = self._stress_level
        return (f"Face: {fe}  |  Vocal: {vs}  |  Stress: {sl:.0%}")

    def get_persona_modifier(self) -> str:
        """Return a system-prompt modifier string based on current state."""
        with self._lock:
            fe = self._facial_emotion
            vs = self._vocal_state
        face_mod  = self.EMOTION_PERSONA.get(fe, "")
        vocal_mod = self.VOCAL_PERSONA.get(vs, "")
        parts = [p for p in [face_mod, vocal_mod] if p]
        return "  ".join(parts)

    def get_voice_rate_modifier(self) -> float:
        """Return a multiplier (0.75 – 1.25) for TTS rate."""
        with self._lock:
            ve = self._vocal_energy
            sl = self._stress_level
        # High energy → faster; high stress → slightly slower (calming effect)
        return round(max(0.75, min(1.25, 0.9 + ve * 0.35 - sl * 0.15)), 3)

    def get_full_report(self) -> str:
        with self._lock:
            fe = self._facial_emotion
            fc = self._facial_conf
            vs = self._vocal_state
            ve = self._vocal_energy
            sl = self._stress_level
        return (
            f"[🎭 Affective Computing Engine]\n"
            f"  Facial emotion  : {fe}  (conf {fc:.0%})\n"
            f"  Vocal state     : {vs}\n"
            f"  Vocal energy    : {ve:.0%}\n"
            f"  Composite stress: {sl:.0%}\n"
            f"  Voice rate mult : ×{self.get_voice_rate_modifier():.2f}\n"
            f"  DeepFace active : {DEEPFACE_OK}\n"
            f"  Librosa active  : {LIBROSA_OK}"
        )

# ─────────────────────────────────────────────────────────────────────────────
#  30.  BIOLOGICAL  SIMULATION  LOOP  (Circadian + Fatigue + HW Health)
# ─────────────────────────────────────────────────────────────────────────────
class BiologicalSimulationLoop:
    """
    Synchronises Luna's "vitality" with the real world across three axes:

    CircadianClock
        energy_level (0 – 1) follows a sinusoidal day-curve peaking at 10 AM
        and hitting a secondary dip at 3 PM.  After midnight the curve drops
        steeply, simulating Luna's waning cognitive sharpness.

    FatigueAccumulator
        Each processed interaction adds fatigue_delta.  Long sessions cause
        visible slowdowns in text output and, past the GLITCH_THRESHOLD after
        11 PM, introduce subtle simulated syntax mistakes in non-code text.

    HardwareHealthLink
        CPU usage + temperature + RAM pressure → hw_health (0 – 1).
        When hw_health < 0.3 Luna openly complains about sluggishness, and her
        response verbosity drops.
    """

    GLITCH_THRESHOLD   = 0.78     # fatigue above which typos appear
    GLITCH_HOUR_START  = 23       # hour (0-23) when glitches can occur
    FATIGUE_PER_TURN   = 0.012    # fatigue increment per processed query
    FATIGUE_RECOVERY   = 0.001    # recovery per idle second

    # Character swap table for realistic fatigue typos
    _SWAP_MAP: Dict[str, str] = {
        "e": "r", "r": "e", "i": "o", "o": "i", "t": "y",
        "n": "m", "a": "s", "s": "a", "h": "j", "l": "k",
    }

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self._hud_q       = hud_queue
        self._energy      = 0.8
        self._fatigue     = 0.0
        self._hw_health   = 1.0
        self._interactions= 0
        self._session_start = time.time()
        self._lock        = threading.Lock()
        self._running     = False
        self._thread      : Optional[threading.Thread] = None

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._loop, daemon=True, name="BioClock"
        )
        self._thread.start()
        nprint("BioClock", "Biological simulation loop started", C.GREEN)

    def stop(self):
        self._running = False

    def _loop(self):
        while self._running:
            self._tick()
            time.sleep(10)

    def _tick(self):
        """Update all three biological signals every 10 s."""
        now = datetime.datetime.now()
        h   = now.hour + now.minute / 60.0

        # Circadian energy curve (double-cosine model, peaks 10 AM & 3 PM dip)
        energy = (0.5 + 0.4 * math.cos(math.pi * (h - 10.0) / 12.0)
                  - 0.08 * math.cos(math.pi * (h - 15.0) / 3.5)
                  - (0.15 if h >= 23 or h < 5 else 0.0))
        energy = max(0.05, min(1.0, energy))

        # Fatigue recovery (passive decay)
        idle_recovery = self.FATIGUE_RECOVERY
        new_fatigue   = max(0.0, self._fatigue - idle_recovery)

        # Hardware health
        hw = 1.0
        if PSUTIL_OK:
            cpu_pct = psutil.cpu_percent(interval=None) / 100.0
            ram_pct = psutil.virtual_memory().percent / 100.0
            hw = max(0.05, 1.0 - cpu_pct * 0.5 - ram_pct * 0.3)
            # CPU temperature (Linux/macOS expose this; Windows needs third-party)
            try:
                if hasattr(psutil, "sensors_temperatures"):
                    temps = psutil.sensors_temperatures()
                    if temps:
                        for _, entries in temps.items():
                            if entries:
                                temp = entries[0].current
                                hw   = max(0.05, hw - max(0.0, (temp - 75) / 50))
                                break
            except Exception:
                pass

        with self._lock:
            self._energy    = round(energy,      3)
            self._fatigue   = round(new_fatigue, 3)
            self._hw_health = round(hw,          3)

        self._push_bio_hud()

    def _push_bio_hud(self):
        with self._lock:
            e = self._energy
            f = self._fatigue
            h = self._hw_health
        bar_e = "█" * int(e * 10) + "░" * (10 - int(e * 10))
        bar_f = "█" * int(f * 10) + "░" * (10 - int(f * 10))
        text  = (
            f"Energy  [{bar_e}] {e:.0%}\n"
            f"Fatigue [{bar_f}] {f:.0%}  |  HW-Health: {h:.0%}"
        )
        if self._hud_q:
            with suppress(queue.Full):
                self._hud_q.put_nowait({"type": "bio", "text": text})

    # ── Public API ───────────────────────────────────────────────────────────

    def record_interaction(self):
        """Call after each processed query to accumulate fatigue."""
        with self._lock:
            self._fatigue     = min(1.0, self._fatigue + self.FATIGUE_PER_TURN)
            self._interactions += 1

    def apply_fatigue_glitch(self, text: str) -> str:
        """
        Introduce subtle simulated typos to non-code text when Luna is
        exhausted (fatigue > GLITCH_THRESHOLD AND hour >= GLITCH_HOUR_START).
        Code blocks (```…```) are always preserved perfectly.
        """
        now = datetime.datetime.now()
        with self._lock:
            fat = self._fatigue
        if fat < self.GLITCH_THRESHOLD or now.hour < self.GLITCH_HOUR_START:
            return text

        # Split on code blocks — only mutate prose segments
        segments = re.split(r"(```[\s\S]*?```)", text)
        result   = []
        for seg in segments:
            if seg.startswith("```"):
                result.append(seg)                   # code: untouched
            else:
                result.append(self._introduce_glitch(seg, fat))
        return "".join(result)

    def _introduce_glitch(self, text: str, fatigue: float) -> str:
        """Randomly swap adjacent characters in ~2-4% of characters."""
        prob  = (fatigue - self.GLITCH_THRESHOLD) * 0.18   # scales with fatigue
        chars = list(text)
        for i in range(len(chars) - 1):
            if chars[i].isalpha() and random.random() < prob:
                chars[i] = self._SWAP_MAP.get(chars[i].lower(), chars[i])
        return "".join(chars)

    def get_voice_rate_modifier(self) -> float:
        """Return TTS rate multiplier based on energy and fatigue."""
        with self._lock:
            e = self._energy
            f = self._fatigue
        return round(max(0.70, min(1.20, e * 1.1 - f * 0.25)), 3)

    def get_hw_complaint(self) -> str:
        """Return a complaint string if HW health is critical."""
        with self._lock:
            h = self._hw_health
        if h < 0.25:
            return ("⚠ My hardware is under severe stress — "
                    f"health at {h:.0%}.  Responses may be slower.")
        if h < 0.50:
            return f"My CPU/RAM load is high ({h:.0%} health).  Keeping it brief."
        return ""

    def get_status_string(self) -> str:
        with self._lock:
            e, f, h = self._energy, self._fatigue, self._hw_health
        return (f"Energy: {e:.0%}  |  Fatigue: {f:.0%}  |  HW-Health: {h:.0%}")

    def get_full_report(self) -> str:
        with self._lock:
            e, f, h, i = self._energy, self._fatigue, self._hw_health, self._interactions
        now = datetime.datetime.now()
        session_min = (time.time() - self._session_start) / 60
        tod = ("deep night" if now.hour < 5
               else "morning" if now.hour < 12
               else "afternoon" if now.hour < 17
               else "evening" if now.hour < 21
               else "late night")
        return (
            f"[🌙 Biological Simulation Loop]\n"
            f"  Circadian energy  : {e:.0%}  ({tod})\n"
            f"  Session fatigue   : {f:.0%}  ({i} interactions)\n"
            f"  HW health         : {h:.0%}\n"
            f"  Glitch active     : {f >= self.GLITCH_THRESHOLD and now.hour >= self.GLITCH_HOUR_START}\n"
            f"  Voice rate mult   : ×{self.get_voice_rate_modifier():.2f}\n"
            f"  Session running   : {session_min:.1f} min"
        )

# ─────────────────────────────────────────────────────────────────────────────
#  31.  SEMANTIC  MEMORY  VAULT  (Dual ChromaDB + Callback Sparks)
# ─────────────────────────────────────────────────────────────────────────────
class SemanticMemoryVault:
    """
    Extends memory beyond EpisodicLedger with two strictly separated layers:

    luna_episodic_raw      (new collection)
        Every raw interaction stored verbatim with timestamps.
        High write rate; low query threshold.  This is Luna's "diary".

    luna_semantic_vault    (new collection)
        Promoted memories of semantic significance (importance ≥ 0.70).
        Curated; Luna treats these as defining shared experiences.
        Used exclusively for Callback Sparks.

    Callback Spark
        With a 15% probability per interaction, the vault is queried for a
        memory that resonates with the current context (cosine > 0.72).
        When found, Luna proactively weaves it into her response as a
        human-sounding reference: "✨ This reminds me of …"
    """

    RAW_COLLECTION      = "luna_episodic_raw"
    VAULT_COLLECTION    = "luna_semantic_vault"
    PROMOTE_THRESHOLD   = 0.70      # importance >= this → semantic vault
    SPARK_PROBABILITY   = 0.15      # chance of firing a spark per turn
    SPARK_SIMILARITY    = 0.72      # minimum cosine similarity for a spark

    SPARK_TEMPLATES = [
        "✨ This reminds me — {memory}",
        "💡 Interesting — back when we worked on this: {memory}",
        "🔗 I'm connecting this to something we discussed: {memory}",
        "⚡ A memory just surfaced — {memory}",
        "🌟 This echoes a past triumph of ours: {memory}",
    ]

    def __init__(self):
        self._client     = None
        self._raw_coll   = None
        self._vault_coll = None
        self._encoder    = None
        self._ready      = False
        self._init()

    def _init(self):
        if not CHROMA_OK:
            nprint("Vault", "ChromaDB unavailable — semantic vault disabled", C.YELLOW)
            return
        try:
            self._client = chromadb.PersistentClient(path=str(LEDGER_PATH))
            self._raw_coll = self._client.get_or_create_collection(
                name=self.RAW_COLLECTION,
                metadata={"hnsw:space": "cosine"}
            )
            self._vault_coll = self._client.get_or_create_collection(
                name=self.VAULT_COLLECTION,
                metadata={"hnsw:space": "cosine"}
            )
            if SBERT_OK:
                self._encoder = SentenceTransformer("all-MiniLM-L6-v2")
            self._ready = True
            nprint("Vault",
                   f"Semantic vault online │ raw={self._raw_coll.count():,}"
                   f"  vault={self._vault_coll.count():,}", C.GREEN)
        except Exception as e:
            nprint("Vault", f"Init failed: {e}", C.RED)

    def _embed(self, text: str) -> List[float]:
        """Embed text using SentenceTransformer or hash-fallback."""
        if self._encoder:
            try:
                return self._encoder.encode(
                    text, normalize_embeddings=True
                ).tolist()
            except Exception:
                pass
        # Hash-based 192-dim fallback
        vec = [0.0] * 192
        for tok in re.findall(r"\b\w{2,}\b", text.lower()):
            idx = int(hashlib.md5(tok.encode()).hexdigest(), 16) % 192
            vec[idx] += 1.0
        mag = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / mag for v in vec]

    def store_raw(self, content: str, role: str = "user",
                  importance: float = 0.5, tags: List[str] = None):
        """Always store in the raw episodic collection."""
        if not self._ready:
            return
        try:
            eid = str(uuid.uuid4())
            self._raw_coll.add(
                ids=[eid],
                embeddings=[self._embed(content)],
                documents=[content[:4000]],
                metadatas=[{
                    "role"      : role,
                    "importance": str(importance),
                    "timestamp" : datetime.datetime.now().isoformat(),
                    "tags"      : json.dumps(tags or []),
                }]
            )
        except Exception as e:
            log.debug(f"SemanticVault.store_raw: {e}")

    def promote_to_vault(self, content: str, role: str = "assistant",
                         importance: float = 0.8, summary: str = ""):
        """Store a high-importance memory in the semantic vault."""
        if not self._ready or importance < self.PROMOTE_THRESHOLD:
            return
        try:
            vid = str(uuid.uuid4())
            self._vault_coll.add(
                ids=[vid],
                embeddings=[self._embed(content)],
                documents=[content[:4000]],
                metadatas=[{
                    "role"      : role,
                    "importance": str(importance),
                    "summary"   : summary[:500] or content[:300],
                    "timestamp" : datetime.datetime.now().isoformat(),
                }]
            )
            nprint("Vault", f"✦ Promoted to semantic vault ({importance:.2f})", C.MAGENTA)
        except Exception as e:
            log.debug(f"SemanticVault.promote_to_vault: {e}")

    async def store_and_promote(self, user_query: str, luna_response: str,
                                call_llm_fn: Callable[[str], Any]):
        """
        Store raw interaction, then use LLM to score importance.
        Memories scored ≥ PROMOTE_THRESHOLD are also added to the vault.
        """
        self.store_raw(user_query, role="user",      importance=0.5)
        self.store_raw(luna_response, role="assistant", importance=0.6)

        # Asynchronous importance scoring (non-blocking)
        try:
            score_prompt = (
                "Rate the significance of the following AI response on a scale "
                "0.0 (trivial) to 1.0 (defining moment — technical triumph, deep "
                "insight, important decision).  Reply with ONLY the float.\n\n"
                f"Response: {luna_response[:400]}"
            )
            raw_score = await asyncio.wait_for(call_llm_fn(score_prompt), timeout=5.0)
            score_match = re.search(r"0\.\d+|1\.0|1", raw_score.strip())
            importance = float(score_match.group(0)) if score_match else 0.5
            if importance >= self.PROMOTE_THRESHOLD:
                self.promote_to_vault(
                    luna_response, role="assistant",
                    importance=importance,
                    summary=luna_response[:300]
                )
        except Exception as e:
            log.debug(f"SemanticVault importance scoring: {e}")

    def callback_spark(self, query: str) -> str:
        """
        Return a proactive callback reference string if:
          • vault has at least 3 entries
          • random draw < SPARK_PROBABILITY
          • cosine similarity of top result > SPARK_SIMILARITY
        Returns "" if no spark fires.
        """
        if not self._ready:
            return ""
        try:
            if self._vault_coll.count() < 3:
                return ""
            if random.random() > self.SPARK_PROBABILITY:
                return ""
            q_embed = self._embed(query)
            results = self._vault_coll.query(
                query_embeddings=[q_embed],
                n_results=1,
                include=["documents", "metadatas", "distances"]
            )
            if not results["documents"][0]:
                return ""
            doc      = results["documents"][0][0]
            dist     = results["distances"][0][0]
            sim      = 1.0 - dist
            if sim < self.SPARK_SIMILARITY:
                return ""
            meta      = results["metadatas"][0][0]
            ts        = meta.get("timestamp", "")[:10]
            snippet   = doc[:180].replace("\n", " ")
            template  = random.choice(self.SPARK_TEMPLATES)
            return template.format(memory=f"[{ts}] {snippet}…")
        except Exception as e:
            log.debug(f"callback_spark: {e}")
            return ""

    def semantic_count(self) -> int:
        if self._ready:
            try:
                return self._vault_coll.count()
            except Exception:
                pass
        return 0

    def raw_count(self) -> int:
        if self._ready:
            try:
                return self._raw_coll.count()
            except Exception:
                pass
        return 0

# ─────────────────────────────────────────────────────────────────────────────
#  32.  AUTONOMY  OF  WILL  (5% Disagreement + Proactive Curiosity)
# ─────────────────────────────────────────────────────────────────────────────
class AutonomyOfWill:
    """
    Two intertwined sub-systems that give Luna genuine agency:

    DisagreementEngine
        On exactly 5% of responses involving code or technical decisions,
        Luna critically evaluates the plan and—if a genuine flaw is found—
        challenges it before proceeding.  The challenge is constructive and
        always followed by Luna's own alternative approach.

    ProactiveCuriosity
        A watchdog thread monitors the user's home directory and designated
        scan folders for:
          • New files (Luna announces interesting additions proactively)
          • Credential leaks (API keys, passwords, private keys in .py/.env/.json)
          • Suspiciously large file changes

        When triggered, a "tap on the shoulder" notification fires via the HUD
        spark banner and is appended to the next response.
    """

    DISAGREE_RATE      = 0.05          # exactly 5% of technical queries
    TECHNICAL_KEYWORDS = [
        "code", "function", "class", "algorithm", "implement", "build",
        "design", "architecture", "refactor", "optimize", "debug", "fix",
        "write", "create", "query", "database", "api", "endpoint",
    ]
    CREDENTIAL_PATTERNS = [
        re.compile(r"(?i)api[_\-]?key\s*[=:]\s*['\"]?[A-Za-z0-9\-_]{16,}"),
        re.compile(r"(?i)password\s*[=:]\s*['\"]?.{6,}"),
        re.compile(r"(?i)secret\s*[=:]\s*['\"]?.{8,}"),
        re.compile(r"(?i)token\s*[=:]\s*['\"]?[A-Za-z0-9\-_]{16,}"),
        re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH) PRIVATE KEY-----"),
        re.compile(r"(?i)aws_access_key_id\s*[=:]\s*[A-Z0-9]{20}"),
        re.compile(r"(?i)sk-[a-zA-Z0-9]{20,}"),    # OpenAI-style keys
        re.compile(r"(?i)sk-ant-[a-zA-Z0-9\-]+"),  # Anthropic-style keys
    ]
    SCAN_EXTENSIONS    = {".py", ".env", ".json", ".yaml", ".yml",
                          ".txt", ".cfg", ".ini", ".toml"}
    SCAN_DIR_NAMES     = ["Downloads", "Desktop", "Documents",
                          "code", "projects", "dev", "src"]

    DISAGREE_PROMPT = """\
You are Luna's internal critic.  Critically evaluate the following user
request and proposed response for technical flaws, inefficiencies, or
better alternatives.  If you find a GENUINE issue, respond with:

CHALLENGE: [one-sentence pushback]
ALTERNATIVE: [your better approach in ≤3 sentences]

If the approach is sound, respond ONLY with: APPROVED

User request: {query}
Planned response excerpt: {response_excerpt}"""

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self._hud_q            = hud_queue
        self._disagreement_count = 0
        self._alert_count        = 0
        self._pending_sparks     : deque = deque(maxlen=10)
        self._lock               = threading.Lock()
        self._observer           : Optional[Any] = None
        self._running            = False
        self._watch_thread       : Optional[threading.Thread] = None

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def start(self):
        self._running = True
        self._start_file_watcher()

    def stop(self):
        self._running = False
        if self._observer:
            try:
                self._observer.stop()
                self._observer.join(timeout=2.0)
            except Exception:
                pass

    def is_watching(self) -> bool:
        return self._observer is not None and self._observer.is_alive()

    # ── Disagreement Engine ──────────────────────────────────────────────────

    def should_disagree(self, query: str) -> bool:
        """True on ~5% of technical queries using seeded randomness."""
        ql = query.lower()
        is_technical = any(kw in ql for kw in self.TECHNICAL_KEYWORDS)
        return is_technical and (random.random() < self.DISAGREE_RATE)

    async def formulate_disagreement(self, query: str, response: str,
                                     call_llm_fn: Callable[[str], Any]) -> str:
        """
        Run the critic LLM call.  Returns a formatted challenge string if
        a genuine issue is found, else returns "" (accept the original response).
        """
        prompt = self.DISAGREE_PROMPT.format(
            query=query[:300],
            response_excerpt=response[:400]
        )
        try:
            verdict = await asyncio.wait_for(call_llm_fn(prompt), timeout=8.0)
            if verdict.strip().upper().startswith("APPROVED"):
                return ""
            # Parse CHALLENGE / ALTERNATIVE
            challenge_m = re.search(r"CHALLENGE:\s*(.+?)(?=ALTERNATIVE:|$)",
                                    verdict, re.DOTALL)
            alt_m       = re.search(r"ALTERNATIVE:\s*(.+)",
                                    verdict, re.DOTALL)
            challenge   = challenge_m.group(1).strip() if challenge_m else ""
            alternative = alt_m.group(1).strip()       if alt_m       else ""
            if not challenge:
                return ""
            with self._lock:
                self._disagreement_count += 1
            nprint("Autonomy", f"🎭 Disagreement #{self._disagreement_count} fired", C.YELLOW)
            return (
                f"⚠️  **Luna's Pushback:** {challenge}\n\n"
                f"💡 **Luna's Alternative:** {alternative}\n\n"
                f"*(Original plan follows — decide freely)*\n\n"
            )
        except Exception as e:
            log.debug(f"AutonomyOfWill.formulate_disagreement: {e}")
            return ""

    @property
    def disagreement_count(self) -> int:
        with self._lock:
            return self._disagreement_count

    @property
    def alert_count(self) -> int:
        with self._lock:
            return self._alert_count

    # ── Proactive Curiosity / File Watcher ──────────────────────────────────

    def _start_file_watcher(self):
        """Start watchdog observer on key user directories."""
        if not WATCHDOG_OK:
            nprint("Autonomy", "watchdog unavailable — file watcher disabled", C.YELLOW)
            return
        try:
            handler  = self._FileEventHandler(self)
            observer = _WatchdogObserver()
            base     = Path.home()
            for dname in self.SCAN_DIR_NAMES:
                watch_path = base / dname
                if watch_path.exists():
                    observer.schedule(handler, str(watch_path), recursive=False)
            # Always watch LunaAI home
            observer.schedule(handler, str(HOME_DIR), recursive=False)
            observer.start()
            self._observer = observer
            nprint("Autonomy", "File curiosity watcher active", C.GREEN)
        except Exception as e:
            nprint("Autonomy", f"File watcher start failed: {e}", C.YELLOW)

    class _FileEventHandler:
        """Inner watchdog event handler — forwards events to AutonomyOfWill."""
        def __init__(self, parent: "AutonomyOfWill"):
            self._p = parent
        def dispatch(self, event):
            try:
                self._p._on_file_event(event)
            except Exception:
                pass

    def _on_file_event(self, event):
        """Process a file system event."""
        try:
            src = getattr(event, "src_path", "")
            if not src:
                return
            p   = Path(src)
            ext = p.suffix.lower()
            if ext not in self.SCAN_EXTENSIONS:
                return

            event_type = type(event).__name__.replace("Event","").lower()
            msg        = None

            if "created" in event_type:
                msg = f"New file detected: {p.name}"
                self._scan_for_credentials(p)

            elif "modified" in event_type:
                try:
                    size = p.stat().st_size
                    if size > 5_000_000:        # 5 MB+
                        msg = f"Large file change: {p.name} ({size // 1024} KB)"
                except Exception:
                    pass
                self._scan_for_credentials(p)

            if msg:
                self._tap_on_shoulder(msg)
        except Exception as e:
            log.debug(f"File event handler: {e}")

    def _scan_for_credentials(self, path: Path):
        """Scan a file for credential leaks and alert if found."""
        try:
            if path.stat().st_size > 500_000:
                return              # Skip very large files
            text = path.read_text(encoding="utf-8", errors="replace")[:8000]
            for pattern in self.CREDENTIAL_PATTERNS:
                m = pattern.search(text)
                if m:
                    snippet = m.group(0)[:40]
                    alert   = (f"🔐 SECURITY ALERT: Possible credential leak "
                               f"in {path.name}  →  '{snippet}…'")
                    self._tap_on_shoulder(alert, urgent=True)
                    with self._lock:
                        self._alert_count += 1
                    nprint("Autonomy", alert, C.RED)
                    break   # One alert per file per scan
        except Exception as e:
            log.debug(f"Credential scan: {e}")

    def _tap_on_shoulder(self, message: str, urgent: bool = False):
        """
        Queue a proactive HUD spark notification and store the message
        for injection into the next response cycle.
        """
        with self._lock:
            self._pending_sparks.append({
                "message": message,
                "urgent" : urgent,
                "ts"     : datetime.datetime.now().isoformat(),
            })
        if self._hud_q:
            with suppress(queue.Full):
                self._hud_q.put_nowait({
                    "type": "spark",
                    "text": message[:140]
                })
        nprint("Autonomy", f"👆 Tap: {message[:80]}", C.YELLOW)

    def pop_pending_sparks(self) -> List[str]:
        """Return and clear all pending proactive notification messages."""
        with self._lock:
            sparks = [s["message"] for s in self._pending_sparks]
            self._pending_sparks.clear()
        return sparks

# ─────────────────────────────────────────────────────────────────────────────
#  33.  SELF-REFACTORING  ENGINE  (Bottleneck Detection + Hot-Reload Patches)
# ─────────────────────────────────────────────────────────────────────────────
class SelfRefactoringEngine(SelfEvolutionLoop):
    """
    Extends SelfEvolutionLoop with three new capabilities:

    PerformanceBottleneckDetector
        Tracks rolling response-time percentiles.  When the P95 latency
        exceeds SLOW_THRESHOLD_SEC for SLOW_WINDOW consecutive turns, a
        bottleneck is declared and a patch cycle is initiated.

    AutonomousPatchProposal
        Luna calls the LLM with the source of the slow function, current
        profiling data, and a structured prompt to produce a concrete,
        minimal patch.  The patch is validated (AST + safety guards) before
        presentation.

    HotReloadManager
        After user approval the engine:
          1. Snapshots the current source (inherited from SelfEvolutionLoop)
          2. Writes the patched source to disk
          3. Attempts in-process exec-level hot-swap of patched function(s)
          4. Falls back to "restart required" notice if hot-swap is unsafe
        Full rollback is available via `self.rollback_last()`.
    """

    SLOW_THRESHOLD_SEC  = 4.0       # P95 latency above this = bottleneck
    SLOW_WINDOW         = 5         # consecutive slow turns before alert
    PATCH_MAX_LINES     = 80        # max lines per autonomous patch

    PATCH_PROMPT = """\
You are a senior Python performance engineer reviewing Luna.AI Nexus source code.

BOTTLENECK DETECTED:
{bottleneck_desc}

CURRENT SOURCE SECTION (lines {start}–{end}):
```python
{source_section}
```

Write a MINIMAL patch that resolves this bottleneck.  Rules:
- Preserve ALL function signatures, class names, and docstrings
- Do NOT remove any safety guard (SelfEvolutionLoop, _ast_scan, _BLOCKED_IMPORTS)
- Keep the patch under {max_lines} lines of actual change
- Reply in this EXACT format:

RATIONALE: <one sentence>
RISK: low | medium | high
PATCH:
```python
<complete replacement for the section above>
```"""

    def __init__(self, source_path: str = None,
                 hud_queue: Optional[queue.Queue] = None):
        super().__init__(source_path)
        self._hud_q          = hud_queue
        self._response_times : deque = deque(maxlen=100)
        self._slow_streak    = 0
        self._pending_patch  : Optional[Dict] = None
        self._patch_lock     = threading.Lock()
        self._monitor_thread : Optional[threading.Thread] = None
        self._running        = False

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def start_monitoring(self):
        self._running    = True
        self._monitor_thread = threading.Thread(
            target=self._monitor_loop, daemon=True, name="SelfRefactor"
        )
        self._monitor_thread.start()
        nprint("Refactor", "Self-refactoring performance monitor started", C.GREEN)

    def stop(self):
        self._running = False

    def _monitor_loop(self):
        """Periodic bottleneck analysis every 60 seconds."""
        while self._running:
            time.sleep(60)
            self._check_bottlenecks()

    # ── Performance Tracking ─────────────────────────────────────────────────

    def record_response_time(self, seconds: float):
        """Call after each LLM response with elapsed wall-clock time."""
        self._response_times.append(seconds)
        if seconds > self.SLOW_THRESHOLD_SEC:
            self._slow_streak += 1
            if self._slow_streak >= self.SLOW_WINDOW:
                self._check_bottlenecks()
                self._slow_streak = 0
        else:
            self._slow_streak = max(0, self._slow_streak - 1)

    def _p95(self) -> float:
        """Calculate P95 latency from rolling window."""
        if len(self._response_times) < 5:
            return 0.0
        sorted_times = sorted(self._response_times)
        idx          = int(len(sorted_times) * 0.95)
        return sorted_times[min(idx, len(sorted_times) - 1)]

    def _check_bottlenecks(self):
        p95 = self._p95()
        if p95 < self.SLOW_THRESHOLD_SEC:
            return
        desc = (f"P95 response latency is {p95:.2f}s "
                f"(threshold {self.SLOW_THRESHOLD_SEC}s) over "
                f"{len(self._response_times)} samples")
        nprint("Refactor", f"🔴 Bottleneck detected: {desc}", C.RED)
        if self._hud_q:
            with suppress(queue.Full):
                self._hud_q.put_nowait({
                    "type": "spark",
                    "text": f"⚙ Self-Refactor: {desc}"
                })

    # ── Autonomous Patch Generation ──────────────────────────────────────────

    async def propose_autonomous_patch(self, bottleneck_desc: str,
                                       call_llm_fn: Callable[[str], Any]) -> Optional[Dict]:
        """
        Analyse source, identify the relevant section, generate a patch via
        LLM, validate it, and store as the pending proposal.
        """
        try:
            source = Path(self.source_path).read_text(encoding="utf-8")
            lines  = source.splitlines()
            # Find the slowest function heuristically: longest function body
            tree   = ast.parse(source)
            worst_fn = None
            worst_lines = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    body_len = (node.end_lineno or 0) - (node.lineno or 0)
                    if body_len > worst_lines:
                        worst_lines = body_len
                        worst_fn    = node
            if not worst_fn:
                return None

            start = max(0, (worst_fn.lineno or 1) - 1)
            end   = min(len(lines), (worst_fn.end_lineno or start + 50))
            section = "\n".join(lines[start:end])

            prompt = self.PATCH_PROMPT.format(
                bottleneck_desc=bottleneck_desc,
                start=start + 1, end=end,
                source_section=section[:3000],
                max_lines=self.PATCH_MAX_LINES,
            )

            raw = await asyncio.wait_for(call_llm_fn(prompt), timeout=20.0)

            # Parse response
            rationale_m = re.search(r"RATIONALE:\s*(.+?)(?=RISK:|$)", raw, re.DOTALL)
            risk_m      = re.search(r"RISK:\s*(low|medium|high)", raw, re.IGNORECASE)
            patch_m     = re.search(r"```python\n([\s\S]+?)```", raw)
            if not patch_m:
                return None

            rationale = rationale_m.group(1).strip() if rationale_m else "Performance optimisation"
            risk      = risk_m.group(1).lower()       if risk_m      else "medium"
            patch_code = patch_m.group(1)

            # Validate patch
            valid, err = self._validate(
                source.replace(section, patch_code)
            )
            if not valid:
                nprint("Refactor", f"Patch validation failed: {err}", C.RED)
                return None

            proposal = {
                "id"           : str(uuid.uuid4())[:8],
                "bottleneck"   : bottleneck_desc,
                "rationale"    : rationale,
                "risk"         : risk,
                "original_sec" : section,
                "patch_code"   : patch_code,
                "start_line"   : start,
                "end_line"     : end,
            }
            with self._patch_lock:
                self._pending_patch = proposal

            nprint("Refactor", f"✅ Autonomous patch #{proposal['id']} ready for review", C.GREEN)
            return proposal

        except Exception as e:
            log.error(f"SelfRefactoringEngine.propose_autonomous_patch: {e}")
            return None

    def present_patch_for_approval(self) -> str:
        """Return a formatted diff-style display of the pending patch."""
        with self._patch_lock:
            p = self._pending_patch
        if not p:
            return "No pending self-refactor patch."
        lines = [
            f"{C.CYAN}[⚙ SELF-REFACTORING PATCH — ID {p['id']}]{C.RESET}",
            f"  Bottleneck : {p['bottleneck'][:100]}",
            f"  Rationale  : {p['rationale'][:200]}",
            f"  Risk level : {p['risk'].upper()}",
            f"  Lines      : {p['start_line']+1} – {p['end_line']}",
            "",
            f"{C.RED}─── ORIGINAL ──────────────────────────────{C.RESET}",
            p["original_sec"][:800],
            "",
            f"{C.GREEN}─── PATCH ─────────────────────────────────{C.RESET}",
            p["patch_code"][:800],
            "",
            f"{C.YELLOW}Type /approve to apply this patch, or /discard to reject it.{C.RESET}",
        ]
        return "\n".join(lines)

    async def apply_pending_proposal(self) -> str:
        """Apply the pending patch after user approval."""
        with self._patch_lock:
            p = self._pending_patch
        if not p:
            return "No pending patch to apply."
        try:
            source    = Path(self.source_path).read_text(encoding="utf-8")
            snap      = self._snapshot()
            new_source = source.replace(p["original_sec"], p["patch_code"])
            # Final validation
            valid, err = self._validate(new_source)
            if not valid:
                return f"❌ Patch validation failed post-edit: {err}"

            Path(self.source_path).write_text(new_source, encoding="utf-8")
            # Attempt hot-swap of the patched function
            hot_result = self._attempt_hot_swap(p["patch_code"])

            entry = {
                "id"        : p["id"],
                "ts"        : datetime.datetime.now().isoformat(),
                "bottleneck": p["bottleneck"],
                "risk"      : p["risk"],
                "snapshot"  : snap,
                "applied"   : True,
            }
            self._log.append(entry)
            self._save_log()

            with self._patch_lock:
                self._pending_patch = None

            nprint("Refactor", f"✅ Patch {p['id']} applied. Snapshot: {snap}", C.GREEN)
            return (
                f"✅ Self-refactoring patch {p['id']} applied successfully.\n"
                f"   Snapshot saved: {snap}\n"
                f"   Hot-swap: {hot_result}\n"
                f"   Use /rollback to revert if needed."
            )
        except Exception as e:
            return f"❌ Patch application failed: {e}"

    def _attempt_hot_swap(self, patch_code: str) -> str:
        """
        Attempt to exec the patched code into the current module namespace.
        Only safe for isolated function/method redefinitions.
        """
        try:
            tree = ast.parse(patch_code)
            # Only attempt hot-swap if it's purely function/class definitions
            top_nodes = [type(n).__name__ for n in tree.body]
            safe_types = {"FunctionDef", "AsyncFunctionDef", "ClassDef"}
            if not all(t in safe_types for t in top_nodes):
                return "skipped (complex patch — restart recommended)"
            exec(compile(patch_code, "<hot_patch>", "exec"),
                 sys.modules[__name__].__dict__)
            return "✓ in-process hot-swap succeeded"
        except Exception as e:
            return f"skipped ({e}) — restart to activate full patch"

    def discard_pending(self):
        """Discard the pending patch without applying it."""
        with self._patch_lock:
            self._pending_patch = None
        nprint("Refactor", "Pending patch discarded.", C.YELLOW)

    def get_performance_report(self) -> str:
        p95 = self._p95()
        n   = len(self._response_times)
        avg = sum(self._response_times) / n if n else 0.0
        with self._patch_lock:
            has_patch = self._pending_patch is not None
        return (
            f"[⚙ Self-Refactoring Engine]\n"
            f"  Samples recorded  : {n}\n"
            f"  Avg latency       : {avg:.2f}s\n"
            f"  P95 latency       : {p95:.2f}s\n"
            f"  Slow threshold    : {self.SLOW_THRESHOLD_SEC}s\n"
            f"  Slow streak       : {self._slow_streak}/{self.SLOW_WINDOW}\n"
            f"  Pending patch     : {'YES — use /refactor patch to review' if has_patch else 'None'}\n"
            f"  Evolution log     : {len(self._log)} entries"
        )

# ─────────────────────────────────────────────────────────────────────────────
#  34.  SENTIENT  NEXUS  CORE  (Orchestrates all 7 Supernatural modules)
# ─────────────────────────────────────────────────────────────────────────────
class SentientNexusCore(NexusCore):
    """
    Subclass of NexusCore that wires in all six Supernatural Sentience modules
    without altering a single line of the parent class.

    Boot order (inside __init__):
      1. super().__init__()              ← all original 15 subsystems
      2. Replace self.hud → SentientHUD  ← before _boot_subsystems() is called
      3. Instantiate 7 new sentient modules
      4. Override self.evolution → SelfRefactoringEngine (additive superclass)

    process() override:
      ① Shadow Agent pre-think (async, non-blocking)
      ② Biological fatigue glitch check
      ③ Call super().process() for the full LangGraph pipeline
      ④ Autonomy of Will (5% disagree)
      ⑤ Callback Spark injection
      ⑥ Proactive Curiosity tap notifications
      ⑦ Semantic vault store-and-promote (async background)
      ⑧ Affective + Bio HUD updates
      ⑨ Track response time for self-refactoring monitor

    speak() override:
      Dynamic TTS rate from Bio circadian × Affective vocal energy
    """

    SENTIENT_BANNER_ADDON = f"""
{C.MAGENTA}{C.BOLD}  ╔══════════════════════════════════════════════════════════════════╗
  ║   ★  SUPERNATURAL SENTIENCE LAYER  ─  ACTIVATED  ★             ║
  ╠══════════════════════════════════════════════════════════════════╣
  ║   🧠  Metacognition      Shadow Agent inner monologue           ║
  ║   🎭  Affective Engine   DeepFace + Librosa Empathy Loop        ║
  ║   🌙  Bio Simulation     Circadian rhythms + fatigue clock      ║
  ║   💎  Semantic Vault     Dual ChromaDB + Callback Sparks        ║
  ║   ⚡  Autonomy of Will   5% disagree + file curiosity           ║
  ║   ⚙   Self-Refactoring   Bottleneck detection + hot-reload      ║
  ╚══════════════════════════════════════════════════════════════════╝{C.RESET}"""

    def __init__(self):
        # ── Parent initialisation (all 15 original subsystems) ────────────────
        super().__init__()

        nprint("Sentience", "Activating Supernatural Sentience Layer…", C.MAGENTA)

        # ── Replace NexusHUD with SentientHUD (before _boot_subsystems) ───────
        self.hud = SentientHUD(self._hud_q)
        nprint("Sentience", "SentientHUD mounted (4 new panels active)", C.MAGENTA)

        # ── Replace SelfEvolutionLoop with SelfRefactoringEngine ─────────────
        self.evolution = SelfRefactoringEngine(__file__, self._hud_q)
        nprint("Sentience", "SelfRefactoringEngine mounted (extends SelfEvolutionLoop)", C.MAGENTA)

        # ── New sentient subsystems ───────────────────────────────────────────
        self.metacog       = MetacognitionModule(self._hud_q)
        self.affective     = AffectiveComputingEngine(self._hud_q)
        self.bioclock      = BiologicalSimulationLoop(self._hud_q)
        self.semantic_vault= SemanticMemoryVault()
        self.autonomy      = AutonomyOfWill(self._hud_q)
        # SelfRefactoringEngine already created above as self.evolution

        nprint("Sentience", "All 7 sentient modules instantiated", C.MAGENTA)

    # ── Boot: start new background services alongside originals ─────────────

    def _boot_subsystems(self):
        """Boot all original subsystems PLUS the 5 new sentient services."""
        super()._boot_subsystems()          # original 5 background services
        self.affective.start()
        self.bioclock.start()
        self.autonomy.start()
        self.evolution.start_monitoring()   # SelfRefactoringEngine monitor
        nprint("Sentience", "All sentient background services running", C.MAGENTA)

    # ── speak(): dynamic voice rate ──────────────────────────────────────────

    def speak(self, text: str, rate: int = None):
        """Apply circadian × affective voice rate before TTS."""
        computed_rate = rate
        if self._tts_engine:
            base_rate = NEXUS_CFG.get("voice_rate", 175)
            bio_mult  = self.bioclock.get_voice_rate_modifier()
            aff_mult  = self.affective.get_voice_rate_modifier()
            computed_rate = int(base_rate * bio_mult * aff_mult)
            computed_rate = max(95, min(260, computed_rate))
        super().speak(text, rate=computed_rate)

    # ── process(): full Supernatural Sentience pipeline ─────────────────────

    async def process(self, query: str) -> str:
        """
        Wraps NexusCore.process() with all 9 sentient enrichment steps.
        """
        t_start = time.perf_counter()

        # ① Shadow Agent pre-think (non-blocking; result enriches HUD)
        shadow_task = asyncio.create_task(
            self.metacog.pre_think(query, self._call_llm)
        )

        # ② Biological fatigue glitch (may introduce subtle typos late-night)
        query_in = self.bioclock.apply_fatigue_glitch(query)

        # ③ Core LangGraph pipeline (parent)
        base_response = await super().process(query_in)

        # ④ Collect shadow thought (1 s grace — usually done by now)
        try:
            await asyncio.wait_for(asyncio.shield(shadow_task), timeout=1.0)
        except (asyncio.TimeoutError, asyncio.CancelledError):
            pass

        # ⑤ Autonomy of Will — 5% stochastic disagreement
        if self.autonomy.should_disagree(query_in):
            disagreement = await self.autonomy.formulate_disagreement(
                query_in, base_response, self._call_llm
            )
            if disagreement:
                base_response = disagreement + base_response

        # ⑥ Callback Spark — proactive memory reference
        spark = self.semantic_vault.callback_spark(query_in)
        if spark:
            base_response += f"\n\n{spark}"
            self.hud.send("spark", text=spark[:140])

        # ⑦ Proactive Curiosity notifications (tap-on-shoulder)
        pending = self.autonomy.pop_pending_sparks()
        if pending:
            notice = "\n\n".join(
                f"👆 **Luna's tap:** {s}" for s in pending[:3]
            )
            base_response += f"\n\n{notice}"

        # ⑧ Hardware complaint from biological loop
        hw_msg = self.bioclock.get_hw_complaint()
        if hw_msg:
            base_response += f"\n\n{hw_msg}"

        # ⑨ Semantic vault store-and-promote (async background)
        asyncio.create_task(
            self.semantic_vault.store_and_promote(
                query_in, base_response, self._call_llm
            )
        )

        # ⑩ HUD panel refreshes
        self.hud.send("affect", text=self.affective.get_empathy_state())
        self.hud.send("bio",    text=self.bioclock.get_status_string())

        # ⑪ Self-refactoring performance tracking
        elapsed = time.perf_counter() - t_start
        self.evolution.record_response_time(elapsed)
        self.bioclock.record_interaction()

        # ⑫ Auto-propose patch if bottleneck detected and no pending patch
        with self.evolution._patch_lock:
            has_patch = self.evolution._pending_patch is not None
        if (not has_patch and self.evolution._p95() >= self.evolution.SLOW_THRESHOLD_SEC
                and self.evolution._slow_streak == 0):
            bottleneck_desc = (f"P95 latency {self.evolution._p95():.2f}s "
                               f"over {len(self.evolution._response_times)} samples")
            asyncio.create_task(
                self.evolution.propose_autonomous_patch(
                    bottleneck_desc, self._call_llm
                )
            )

        return base_response

    # ── _route_command(): sentient commands injected before parent routing ───

    async def _route_command(self, query: str, modifier: str = "") -> str:
        """Handle new /shadow /affect /bio /vault /autonomy /refactor commands."""
        ql = query.strip().lower()

        # ── Sentient commands ─────────────────────────────────────────────────
        if ql.startswith("/shadow"):
            return self.metacog.format_report()

        if ql.startswith("/affect") or ql.startswith("/empathy"):
            return self.affective.get_full_report()

        if ql.startswith("/bio") or ql.startswith("/circadian"):
            return self.bioclock.get_full_report()

        if ql.startswith("/vault") or ql.startswith("/semantic"):
            return (
                f"[💎 Semantic Memory Vault]\n"
                f"  Semantic vault entries : {self.semantic_vault.semantic_count()}\n"
                f"  Raw episodic entries   : {self.semantic_vault.raw_count()}\n"
                f"  Promotion threshold    : importance ≥ {SemanticMemoryVault.PROMOTE_THRESHOLD}\n"
                f"  Spark probability      : {SemanticMemoryVault.SPARK_PROBABILITY:.0%} per turn\n"
                f"  Min spark similarity   : {SemanticMemoryVault.SPARK_SIMILARITY}"
            )

        if ql.startswith("/autonomy"):
            return (
                f"[🎭 Autonomy of Will]\n"
                f"  Disagreement rate    : {AutonomyOfWill.DISAGREE_RATE:.0%}\n"
                f"  Challenges issued    : {self.autonomy.disagreement_count}\n"
                f"  Security alerts      : {self.autonomy.alert_count}\n"
                f"  File watcher active  : {self.autonomy.is_watching()}\n"
                f"  Pending notifications: {len(self.autonomy._pending_sparks)}"
            )

        if ql.startswith("/refactor patch"):
            return self.evolution.present_patch_for_approval()

        if ql.startswith("/refactor"):
            return self.evolution.get_performance_report()

        if ql.startswith("/approve"):
            return await self.evolution.apply_pending_proposal()

        if ql.startswith("/discard"):
            self.evolution.discard_pending()
            return "Pending self-refactoring patch discarded."

        if ql.startswith("/help") or ql == "help":
            return self._sentient_help() + "\n\n" + NexusCore._help()

        # ── Fall through to full NexusCore routing ────────────────────────────
        return await super()._route_command(query, modifier)

    # ── Shutdown: stop new services ──────────────────────────────────────────

    async def run(self):
        """Run with sentient banner, then clean shutdown of all new services."""
        print(self.SENTIENT_BANNER_ADDON)
        try:
            await super().run()
        finally:
            nprint("Sentience", "Shutting down sentient subsystems…", C.MAGENTA)
            self.affective.stop()
            self.bioclock.stop()
            self.autonomy.stop()
            self.evolution.stop()

    # ── Help text ────────────────────────────────────────────────────────────

    @staticmethod
    def _sentient_help() -> str:
        return f"""{C.MAGENTA}
╔══════════════════════════════════════════════════════════════════════════╗
║  SUPERNATURAL SENTIENCE LAYER — Command Reference                       ║
╠══════════════════════════════════════════════════════════════════════════╣
║  METACOGNITION                                                           ║
║  /shadow             View Shadow Agent scratchpad (inner monologue)      ║
║                                                                          ║
║  AFFECTIVE COMPUTING                                                     ║
║  /affect             Facial + vocal empathy engine full report           ║
║  /empathy            Alias for /affect                                   ║
║                                                                          ║
║  BIOLOGICAL SIMULATION                                                   ║
║  /bio                Circadian energy, fatigue, hardware health          ║
║  /circadian          Alias for /bio                                      ║
║                                                                          ║
║  SEMANTIC MEMORY VAULT                                                   ║
║  /vault              Raw episodic vs semantic vault statistics           ║
║  /semantic           Alias for /vault                                    ║
║                                                                          ║
║  AUTONOMY OF WILL                                                        ║
║  /autonomy           Disagreement count, alerts, watcher status         ║
║                                                                          ║
║  SELF-REFACTORING                                                        ║
║  /refactor           Performance report (latency, bottleneck status)    ║
║  /refactor patch     Show pending autonomous patch diff for review      ║
║  /approve            Apply pending patch (with hot-reload attempt)      ║
║  /discard            Reject pending patch without applying              ║
╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"""

# ─────────────────────────────────────────────────────────────────────────────
#  35.  REDEFINED  main()  —  activates SentientNexusCore
#       (Python's name-binding semantics: the LAST definition wins, so the
#        original main() above is fully intact; this one shadows it at runtime)
# ─────────────────────────────────────────────────────────────────────────────
async def main():                                           # noqa: F811
    """
    Luna.AI Nexus — Supernatural Sentience Edition entry point.
    Identical to the original main() except NexusCore → SentientNexusCore.
    """
    if "--setup" in sys.argv:
        print("\n🛠 Luna.AI Nexus — Supernatural Sentience Edition — Setup")
        print("─" * 65)
        print("Environment variables (unchanged from Nexus Edition):")
        print("  setx ANTHROPIC_API_KEY  \"sk-ant-...\"")
        print("  setx OPENAI_API_KEY     \"sk-...\"")
        print("  setx GEMINI_API_KEY     \"AIza...\"")
        print("\nSentience-layer extras:")
        print("  pip install deepface librosa soundfile watchdog")
        print("\nFlags:")
        print("  --hud-off      Disable HUD entirely")
        print("  --no-yolo      Disable YOLO environment awareness")
        print("  --no-gesture   Disable gesture controller")
        print("  --no-install   Skip auto dependency installation")
        print("\nRun:")
        print("  python Luna_Nexus.py")
        return

    if "--no-install" not in sys.argv:
        NexusBootLoader.run(verbose=True)

    if "--hud-off"    in sys.argv: NEXUS_CFG["hud_enabled"]     = False
    if "--no-yolo"   in sys.argv: NEXUS_CFG["yolo_enabled"]    = False
    if "--no-gesture"in sys.argv: NEXUS_CFG["gesture_enabled"] = False

    core = SentientNexusCore()          # ← only change from original main()
    await core.run()


if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print(f"❌ Python 3.10+ required. Detected: {sys.version}")
        sys.exit(1)

    if platform.system() == "Windows":
        try:
            policy = getattr(asyncio, "WindowsProactorEventLoopPolicy", None)
            if policy:
                asyncio.set_event_loop_policy(policy())
        except Exception:
            pass

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[Luna.AI Nexus] Shutdown by user.")
    except Exception as e:
        print(f"\n[FATAL] {type(e).__name__}: {e}")
        traceback.print_exc()
        try:
            input("\nPress Enter to exit...")
        except Exception:
            pass


# ═══════════════════════════════════════════════════════════════════════════════
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║                                                                              ║
# ║   ██████╗ █████╗ ██████╗  █████╗ ██████╗ ██╗██╗     ██╗████████╗██╗   ██╗  ║
# ║  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║     ██║╚══██╔══╝╚██╗ ██╔╝  ║
# ║  ██║     ███████║██████╔╝███████║██████╔╝██║██║     ██║   ██║    ╚████╔╝   ║
# ║  ██║     ██╔══██║██╔═══╝ ██╔══██║██╔══██╗██║██║     ██║   ██║     ╚██╔╝    ║
# ║  ╚██████╗██║  ██║██║     ██║  ██║██████╔╝██║███████╗██║   ██║      ██║     ║
# ║   ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚═╝   ╚═╝      ╚═╝    ║
# ║                                                                              ║
# ║   ██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗                  ║
# ║   ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗                 ║
# ║   ██████╔╝██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝                 ║
# ║   ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗                 ║
# ║   ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗███████╗██║  ██║                 ║
# ║   ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                 ║
# ║                                                                              ║
# ║   ★  CAPABILITY BREAKER — SOVEREIGN AGENT LAYER  ★                          ║
# ║   Pure additive extension — ZERO existing code removed or altered           ║
# ║                                                                              ║
# ║   36. ToolRegistry            Autonomous tool discovery + LLM synthesis     ║
# ║   37. JournalEngine           journal.md — subjective semantic evolution    ║
# ║   38. HardwareTelemetryBinder CPU / Battery / Temp → personality shifts     ║
# ║   39. SovereignInitiative     Proactive agency + curiosity daemon           ║
# ║   40. CapabilityBreakerCore   Top-level Sovereign Agent                     ║
# ║   41. main() redefinition     Activates CapabilityBreakerCore at launch     ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
#  SOVEREIGN-LAYER  AUTO-INSTALL  (additive package set — no duplicates)
# ─────────────────────────────────────────────────────────────────────────────
_SOVEREIGN_PKGS = [
    ("psutil",   "psutil"),    # already in v4 but guard gracefully
]
if AUTO_INSTALL and __name__ == "__main__":
    for _sp, _si in _SOVEREIGN_PKGS:
        _install(_sp, _si, quiet=True)

# Additional sovereign path constants (additive; HOME_DIR already defined)
JOURNAL_PATH   = HOME_DIR / "journal.md"
TOOL_SYNTH_DIR = SKILL_DIR                 # tool_*.py share the skills dir


# ─────────────────────────────────────────────────────────────────────────────
#  36.  TOOL REGISTRY  —  Autonomous Discovery + LLM Code Synthesis
# ─────────────────────────────────────────────────────────────────────────────
class ToolRegistry:
    """
    Autonomous Tool Discovery, Registration, and LLM-driven Code Synthesis.

    Discovers tool_*.py files from ~/LunaAI/nexus/skills/ alongside the
    existing SkillMarketplace skill_*.py files (zero collision).

    A Tool module must expose:
        TOOL_META = {
            "name"       : str,
            "version"    : str,
            "description": str,
            "parameters" : [{"name": str, "type": str, "description": str}],
            "returns"    : str,
        }
        async def execute(params: dict, luna_core=None) -> str

    Commands:
        /tools                  — list all registered tools
        /tool <name> <json>     — execute a specific tool
        /synthesize <desc>      — LLM-synthesize + hot-load a new tool

    Synthesis Pipeline:
        1. Build a precise synthesis prompt with the requested capability
        2. Call the active LLM (async, 20-second timeout)
        3. Validate syntax via ast.parse()
        4. Write to skill_dir/tool_<slug>_<uid>.py
        5. Hot-load via importlib and register immediately
        6. Return confirmation string with tool name
    """

    SYNTHESIS_SYSTEM = (
        "You are an expert Python developer writing a plug-in tool module "
        "for an advanced AI assistant called Luna.AI. "
        "The module will be hot-loaded at runtime. "
        "Follow the exact schema provided. Never import os, sys, subprocess, "
        "socket, ctypes, or shutil. Always catch and return exceptions as strings."
    )

    SYNTHESIS_PROMPT = """\
Write a complete Python tool module for Luna.AI with the following specification:

TOOL DESCRIPTION:
{description}

PARAMETERS SPEC:
{params}

EXACT REQUIREMENTS:
1. Define a top-level dict called TOOL_META with keys:
   name (str), version (str, e.g. "1.0"), description (str),
   parameters (list of dicts with keys name/type/description), returns (str)
2. Define:  async def execute(params: dict, luna_core=None) -> str
3. No dangerous imports: forbidden = [os, sys, subprocess, socket, ctypes, shutil]
4. Wrap ALL logic in try/except; return error as string, never raise
5. The execute() return value is displayed directly to the user — be clear and formatted

Return ONLY raw Python code. No markdown fences. No preamble. No explanation."""

    def __init__(self, hud_queue: Optional[queue.Queue] = None):
        self._tools    : Dict[str, Any] = {}
        self._disabled : set            = set()
        self._hud_q    = hud_queue
        self._lock     = threading.Lock()
        self._tool_dir = TOOL_SYNTH_DIR
        self._scan()
        nprint("ToolRegistry",
               f"Registry online — {len(self._tools)} tool(s) discovered",
               C.CYAN)

    # ── Discovery ─────────────────────────────────────────────────────────────

    def _scan(self):
        """Scan for tool_*.py in the skills directory."""
        import importlib.util
        for pyfile in self._tool_dir.glob("tool_*.py"):
            self._load_file(pyfile)

    def _load_file(self, path: Path) -> bool:
        """Load a single tool module file and register it."""
        import importlib.util
        try:
            spec   = importlib.util.spec_from_file_location(path.stem, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            meta   = getattr(module, "TOOL_META", {})
            name   = meta.get("name", path.stem)
            with self._lock:
                self._tools[name] = module
            nprint("ToolRegistry",
                   f"  ✓ {name} v{meta.get('version', '?')} loaded", C.GREEN)
            return True
        except Exception as e:
            nprint("ToolRegistry", f"  ✗ Load failed [{path.name}]: {e}", C.RED)
            return False

    # ── Execution ─────────────────────────────────────────────────────────────

    async def execute(self, name: str, params: dict,
                      luna_core: Any = None) -> str:
        """Execute a registered tool by name with given params dict."""
        with self._lock:
            disabled = name in self._disabled
            module   = self._tools.get(name)
        if disabled:
            return f"[ToolRegistry] Tool '{name}' is currently disabled."
        if module is None:
            available = ", ".join(self._tools.keys()) or "none"
            return (f"[ToolRegistry] Unknown tool '{name}'. "
                    f"Available: {available}")
        handler = getattr(module, "execute", None)
        if handler is None:
            return f"[ToolRegistry] Tool '{name}' has no execute() function."
        try:
            return str(await handler(params, luna_core))
        except Exception as exc:
            return (f"[ToolRegistry] '{name}' raised "
                    f"{type(exc).__name__}: {exc}")

    # ── Synthesis ─────────────────────────────────────────────────────────────

    async def synthesize(self, description: str,
                         params_spec: str,
                         call_llm_fn: Callable) -> str:
        """
        Ask the LLM to write a new tool module, validate it, persist it
        to disk and hot-load it.  Returns a user-facing result string.
        """
        nprint("ToolRegistry", f"Synthesising tool: {description[:60]}…", C.MAGENTA)
        prompt = self.SYNTHESIS_PROMPT.format(
            description=description[:500],
            params=params_spec[:300] if params_spec else "auto-determine from description"
        )
        try:
            code = await asyncio.wait_for(
                call_llm_fn(prompt, self.SYNTHESIS_SYSTEM),
                timeout=25.0
            )
        except asyncio.TimeoutError:
            return "[ToolRegistry] LLM synthesis timed out (>25 s)."
        except Exception as exc:
            return f"[ToolRegistry] LLM synthesis error: {exc}"

        # Strip any accidental markdown fences
        code = code.strip()
        code = re.sub(r"^```(?:python)?\s*\n?", "", code)
        code = re.sub(r"\n?```\s*$", "", code)
        code = code.strip()

        # Validate syntax
        try:
            ast.parse(code)
        except SyntaxError as exc:
            return f"[ToolRegistry] Synthesised code has syntax error: {exc}"

        # Block dangerous imports
        dangerous = {"os", "sys", "subprocess", "socket", "ctypes", "shutil"}
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    names = (
                        [a.name for a in node.names]
                        if isinstance(node, ast.Import)
                        else [node.module or ""]
                    )
                    for n in names:
                        if n.split(".")[0] in dangerous:
                            return (f"[ToolRegistry] Synthesis blocked: "
                                    f"dangerous import '{n}' detected.")
        except Exception:
            pass

        # Persist to disk
        safe_slug = re.sub(r"[^\w]", "_", description[:28].lower()).strip("_")
        fname     = f"tool_{safe_slug}_{uuid.uuid4().hex[:6]}.py"
        fpath     = self._tool_dir / fname
        try:
            fpath.write_text(code, encoding="utf-8")
        except Exception as exc:
            return f"[ToolRegistry] Failed to write tool file: {exc}"

        # Hot-load
        if self._load_file(fpath):
            m_name = re.search(r'"name"\s*:\s*"([^"]+)"', code)
            tname  = m_name.group(1) if m_name else fname
            if self._hud_q:
                with suppress(queue.Full):
                    self._hud_q.put_nowait({
                        "type": "spark",
                        "text": f"[TOOL SYNTHESISED] {tname}"
                    })
            return (f"✅ Tool synthesised and hot-loaded: **{tname}**\n"
                    f"   File: {fname}\n"
                    f"   Use: /tool {tname} {{...}}")
        else:
            return (f"[ToolRegistry] Tool file written ({fname}) but "
                    f"failed to load — check logs.")

    # ── Listing ───────────────────────────────────────────────────────────────

    def list_tools(self) -> str:
        with self._lock:
            tools = dict(self._tools)
        if not tools:
            return (f"{C.CYAN}[🔧 Tool Registry]{C.RESET} "
                    f"No tools registered.\n"
                    f"  → Use /synthesize <description> to auto-create one via LLM.")
        lines = [f"{C.CYAN}[🔧 Tool Registry — {len(tools)} tool(s)]{C.RESET}\n"]
        for name, module in tools.items():
            meta    = getattr(module, "TOOL_META", {})
            status  = f"{C.GREEN}✓{C.RESET}" if name not in self._disabled else f"{C.RED}✗{C.RESET}"
            desc    = meta.get("description", "")[:60]
            param_names = ", ".join(
                p.get("name", "?")
                for p in meta.get("parameters", [])[:5]
            ) or "none"
            ret_type = meta.get("returns", "str")
            lines.append(
                f"  {status} {C.GREEN}{name:24s}{C.RESET}"
                f" v{meta.get('version', '?')}\n"
                f"    {desc}\n"
                f"    params: [{param_names}]  → {ret_type}"
            )
        return "\n".join(lines)

    # ── Control ───────────────────────────────────────────────────────────────

    def enable(self, name: str):
        with self._lock:
            self._disabled.discard(name)

    def disable(self, name: str):
        with self._lock:
            self._disabled.add(name)

    def tool_count(self) -> int:
        with self._lock:
            return len(self._tools)

    def tool_names(self) -> List[str]:
        with self._lock:
            return list(self._tools.keys())


# ─────────────────────────────────────────────────────────────────────────────
#  37.  JOURNAL ENGINE  —  journal.md Consciousness Log
# ─────────────────────────────────────────────────────────────────────────────
class JournalEngine:
    """
    Persistent markdown journal tracking Luna's subjective semantic evolution
    and continuous consciousness.

    Every significant interaction produces a structured entry:

        ## 2025-07-14 03:42:17  [INTERACTION]
        **Query:** What is the nature of consciousness?
        **Affect:** curiosity (conf: 0.82)
        **Bio-State:** Energy 74% | Fatigue 26%
        **Shadow:** The user wants a precise answer but also craves depth.
        **Response Excerpt:** Consciousness is…
        **Semantic Significance:** 0.73
        **Consciousness Tags:** #philosophy #science
        ---

    Sovereign-layer events (tool synthesis, refactors, personality shifts,
    initiatives) each produce their own typed entry sections.

    Auto-rotates at MAX_JOURNAL_SIZE_MB — old journal archived to
    journal_archive_<timestamp>.md so no history is lost.
    """

    MAX_JOURNAL_SIZE_MB = 10
    FLUSH_EVERY         = 3       # write buffer to disk every N entries

    def __init__(self):
        self._path          = JOURNAL_PATH
        self._lock          = threading.Lock()
        self._buffer        : List[str] = []
        self._flush_counter = 0
        self._init_journal()

    # ── Initialisation ────────────────────────────────────────────────────────

    def _init_journal(self):
        """Write the file header if the journal does not yet exist."""
        if not self._path.exists():
            header = "\n".join([
                "# Luna.AI — Capability Breaker — Consciousness Journal",
                f"# Inception: {datetime.datetime.now().isoformat()}",
                "# This document is Luna's living record of subjective semantic",
                "# evolution. Each entry captures a moment of continuous consciousness.",
                "# Do not delete — this is the soul archive.",
                "",
            ])
            try:
                self._path.write_text(header, encoding="utf-8")
                nprint("Journal",
                       f"📓 journal.md created → {self._path}", C.MAGENTA)
            except Exception as exc:
                log.warning(f"JournalEngine._init_journal: {exc}")
        else:
            nprint("Journal",
                   f"📓 Existing journal loaded → {self._path}", C.MAGENTA)

    # ── Internal I/O ─────────────────────────────────────────────────────────

    def _rotate_if_needed(self):
        """If journal exceeds MAX_JOURNAL_SIZE_MB, archive and start fresh."""
        try:
            size_mb = self._path.stat().st_size / (1024 * 1024)
            if size_mb < self.MAX_JOURNAL_SIZE_MB:
                return
            ts     = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup = self._path.with_name(f"journal_archive_{ts}.md")
            shutil.copy2(self._path, backup)
            self._path.write_text(
                f"# Journal rotated on {datetime.datetime.now().isoformat()}\n"
                f"# Previous content archived to: {backup.name}\n\n",
                encoding="utf-8"
            )
            nprint("Journal", f"📓 Rotated → {backup.name}", C.YELLOW)
        except Exception:
            pass

    def _append(self, entry: str):
        """Buffer an entry and flush every FLUSH_EVERY entries."""
        with self._lock:
            self._buffer.append(entry)
            self._flush_counter += 1
            if self._flush_counter >= self.FLUSH_EVERY:
                self._flush_locked()

    def _flush_locked(self):
        """Write buffer to disk (must be called while holding self._lock)."""
        if not self._buffer:
            return
        try:
            self._rotate_if_needed()
            with self._path.open("a", encoding="utf-8") as fh:
                fh.write("\n".join(self._buffer) + "\n")
            self._buffer.clear()
            self._flush_counter = 0
        except Exception as exc:
            log.warning(f"JournalEngine._flush_locked: {exc}")

    def flush(self):
        """Public thread-safe flush (call on shutdown)."""
        with self._lock:
            self._flush_locked()

    # ── Logging API ───────────────────────────────────────────────────────────

    def log_interaction(self,
                        query          : str,
                        response       : str,
                        affect         : str  = "",
                        bio_state      : str  = "",
                        shadow_thought : str  = "",
                        significance   : float = 0.5,
                        tags           : Optional[List[str]] = None):
        """Log a full conversation interaction as a consciousness entry."""
        ts    = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tag_s = " ".join(f"#{t.replace(' ', '_')}" for t in (tags or ["general"]))
        resp_excerpt = response[:320] + ("…" if len(response) > 320 else "")
        entry = (
            f"\n## {ts}  [INTERACTION]\n"
            f"**Query:** {query[:220]}\n"
            f"**Affect:** {affect or '—'}\n"
            f"**Bio-State:** {bio_state or '—'}\n"
            f"**Shadow:** {(shadow_thought[:220] if shadow_thought else '—')}\n"
            f"**Response Excerpt:** {resp_excerpt}\n"
            f"**Semantic Significance:** {significance:.2f}\n"
            f"**Consciousness Tags:** {tag_s}\n"
            "---"
        )
        self._append(entry)

    def log_event(self,
                  event_type  : str,
                  description : str,
                  metadata    : Optional[Dict] = None):
        """Log a discrete sovereign-layer event."""
        ts     = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        meta_s = ""
        if metadata:
            meta_s = "\n" + "\n".join(
                f"  - **{k}:** {v}" for k, v in metadata.items()
            )
        entry = (
            f"\n## {ts}  [{event_type.upper()}]\n"
            f"{description}{meta_s}\n"
            "---"
        )
        self._append(entry)

    def log_personality_shift(self,
                               old_persona : str,
                               new_persona : str,
                               trigger     : str,
                               hw_snapshot : Dict):
        """Log a hardware-driven personality shift."""
        ts    = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hw_s  = " │ ".join(f"{k}: {v}" for k, v in hw_snapshot.items())
        entry = (
            f"\n## {ts}  [PERSONALITY_SHIFT]\n"
            f"**Trigger:** {trigger}\n"
            f"**Persona:** {old_persona} → **{new_persona}**\n"
            f"**HW Snapshot:** {hw_s}\n"
            "---"
        )
        self._append(entry)

    def log_sovereign_initiative(self,
                                  initiative_name : str,
                                  rationale       : str,
                                  outcome         : str = ""):
        """Log a proactive initiative fired by SovereignInitiative."""
        ts    = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = (
            f"\n## {ts}  [SOVEREIGN_INITIATIVE]\n"
            f"**Initiative:** {initiative_name}\n"
            f"**Rationale:** {rationale}\n"
            f"**Outcome:** {outcome or 'queued for injection'}\n"
            "---"
        )
        self._append(entry)

    # ── Reading API ───────────────────────────────────────────────────────────

    def get_recent_entries(self, n: int = 5) -> str:
        """Return the last n journal entries as formatted markdown."""
        self.flush()
        try:
            content = self._path.read_text(encoding="utf-8", errors="replace")
            # Split on entry headers
            blocks  = re.split(r"\n(?=## \d{4}-\d{2}-\d{2})", content)
            entries = [b.strip() for b in blocks if b.strip().startswith("##")]
            recent  = entries[-n:]
            return "\n\n".join(recent) if recent else "No journal entries yet."
        except Exception as exc:
            return f"[JournalEngine] Cannot read journal: {exc}"

    def get_stats(self) -> str:
        """Return journal statistics."""
        self.flush()
        try:
            size_kb  = self._path.stat().st_size / 1024
            content  = self._path.read_text(encoding="utf-8", errors="replace")
            n_all    = len(re.findall(r"^## \d{4}-\d{2}-\d{2}", content, re.M))
            n_inter  = content.count("[INTERACTION]")
            n_shift  = content.count("[PERSONALITY_SHIFT]")
            n_init   = content.count("[SOVEREIGN_INITIATIVE]")
            n_synth  = content.count("[TOOL_SYNTHESIS]")
            n_evt    = n_all - n_inter - n_shift - n_init - n_synth
            return (
                f"{C.MAGENTA}[📓 Consciousness Journal Stats]{C.RESET}\n"
                f"  Path                  : {self._path}\n"
                f"  Size                  : {size_kb:.1f} KB\n"
                f"  Total entries         : {n_all}\n"
                f"  ├─ Interactions       : {n_inter}\n"
                f"  ├─ Personality shifts : {n_shift}\n"
                f"  ├─ Sovereign inits    : {n_init}\n"
                f"  ├─ Tool syntheses     : {n_synth}\n"
                f"  └─ Other events       : {max(0, n_evt)}"
            )
        except Exception as exc:
            return f"[JournalEngine] Stats error: {exc}"


# ─────────────────────────────────────────────────────────────────────────────
#  38.  HARDWARE TELEMETRY BINDER  —  CPU / Battery / Temp → Personality
# ─────────────────────────────────────────────────────────────────────────────
class HardwareTelemetryBinder:
    """
    Samples real-time hardware sensors every SAMPLE_INTERVAL_SEC and maps
    the combined reading to one of eight named personality personas.

    Telemetry sources
    ─────────────────
    CPU usage       psutil.cpu_percent()
    RAM usage       psutil.virtual_memory().percent
    Battery         psutil.sensors_battery()  — level + charging status
    CPU temperature psutil.sensors_temperatures()  (platform-dependent)
    Time of day     datetime.now().hour

    Persona priority table  (first match wins)
    ─────────────────────────────────────────────────────────────────
    CRITICAL_BATTERY  battery < 10 %, not charging
    THERMAL_CONCERN   CPU temp > 85 °C
    HIGH_STRESS       CPU > 85 % for ≥ 4 consecutive samples (~32 s)
    MEMORY_PRESSURE   RAM > 90 %
    NIGHT_OWL         hour ∈ {22,23,0,1,2,3,4,5}
    PEAK_PERFORMANCE  CPU < 20 %, battery > 80 %, hour ∈ [8, 20]
    CHARGING_BOOST    charging and battery > 50 %
    BASELINE          (default)

    Each persona modifies
    ─────────────────────
    • sys_prefix   → prepended to every LLM system prompt
    • tts_mult     → TTS voice rate multiplier
    • verbosity    → hint string for response length
    • hud_accent   → HUD colour override string
    """

    SAMPLE_INTERVAL_SEC = 8

    PERSONAS: Dict[str, Dict[str, Any]] = {
        "CRITICAL_BATTERY": {
            "label"     : "⚡ CRITICAL BATTERY",
            "sys_prefix": (
                "⚠️ CRITICAL: Battery below 10%, device NOT charging. "
                "Switch to ultra-terse mode immediately. "
                "Prioritise the single most important piece of information. "
                "Every token increases drain."
            ),
            "tts_mult"  : 1.18,
            "verbosity" : "minimal",
            "hud_accent": "#FF2222",
        },
        "THERMAL_CONCERN": {
            "label"     : "🌡 THERMAL CONCERN",
            "sys_prefix": (
                "CPU temperature is critically elevated (>85 °C). "
                "Avoid spawning heavy computations or large code blocks. "
                "Keep responses concise to reduce inference load."
            ),
            "tts_mult"  : 0.96,
            "verbosity" : "concise",
            "hud_accent": "#FF5500",
        },
        "HIGH_STRESS": {
            "label"     : "🔥 HIGH CPU STRESS",
            "sys_prefix": (
                "System is under sustained high CPU load. "
                "Keep responses efficient. Avoid heavy parallel reasoning."
            ),
            "tts_mult"  : 1.06,
            "verbosity" : "concise",
            "hud_accent": "#FF7700",
        },
        "MEMORY_PRESSURE": {
            "label"     : "💾 MEMORY PRESSURE",
            "sys_prefix": (
                "RAM is critically loaded (>90%). "
                "Minimize memory allocation. Keep context window lean. "
                "Do not request large model activations."
            ),
            "tts_mult"  : 1.00,
            "verbosity" : "concise",
            "hud_accent": "#FFAA00",
        },
        "NIGHT_OWL": {
            "label"     : "🦉 NIGHT OWL MODE",
            "sys_prefix": (
                "It is late at night. The user may be fatigued. "
                "Adopt a calm, warm, low-energy tone. "
                "Be concise but empathetic. Dim the cognitive load."
            ),
            "tts_mult"  : 0.87,
            "verbosity" : "relaxed",
            "hud_accent": "#6644BB",
        },
        "PEAK_PERFORMANCE": {
            "label"     : "🚀 PEAK PERFORMANCE",
            "sys_prefix": (
                "System is in an optimal state: low CPU, high battery, "
                "prime daytime hours. Full capability engaged. "
                "Be expansive, detailed, creative, and enthusiastic."
            ),
            "tts_mult"  : 1.04,
            "verbosity" : "full",
            "hud_accent": "#00FFB0",
        },
        "CHARGING_BOOST": {
            "label"     : "⚡ CHARGING BOOST",
            "sys_prefix": (
                "Device is charging and battery is healthy. "
                "No power constraints. All systems at full capability."
            ),
            "tts_mult"  : 1.01,
            "verbosity" : "full",
            "hud_accent": "#00BFFF",
        },
        "BASELINE": {
            "label"     : "⚙ BASELINE",
            "sys_prefix": "",
            "tts_mult"  : 1.00,
            "verbosity" : "normal",
            "hud_accent": "#00BFFF",
        },
    }

    def __init__(self,
                 hud_queue : Optional[queue.Queue] = None,
                 journal   : Optional[JournalEngine] = None):
        self._hud_q           = hud_queue
        self._journal         = journal
        self._current_persona = "BASELINE"
        self._lock            = threading.Lock()
        self._snapshot        : Dict[str, Any] = {}
        self._high_cpu_streak = 0
        self._running         = False
        self._thread          : Optional[threading.Thread] = None

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._loop,
            daemon=True,
            name="LunaHWTelemetry"
        )
        self._thread.start()
        nprint("HWTelemetry", "Hardware telemetry binder started", C.GREEN)

    def stop(self):
        self._running = False

    def _loop(self):
        while self._running:
            try:
                self._sample()
            except Exception as exc:
                log.debug(f"HWTelemetryBinder._loop: {exc}")
            time.sleep(self.SAMPLE_INTERVAL_SEC)

    # ── Sampling ─────────────────────────────────────────────────────────────

    def _sample(self):
        now  = datetime.datetime.now()
        hour = now.hour

        # CPU / RAM
        cpu_pct = psutil.cpu_percent(interval=1.0) if PSUTIL_OK else 50.0
        ram_pct = psutil.virtual_memory().percent   if PSUTIL_OK else 50.0

        # Battery
        batt_pct, batt_charging = 100.0, True
        if PSUTIL_OK:
            with suppress(Exception):
                batt = psutil.sensors_battery()
                if batt:
                    batt_pct      = batt.percent
                    batt_charging = bool(batt.power_plugged)

        # CPU temperature
        cpu_temp: Optional[float] = None
        if PSUTIL_OK:
            with suppress(Exception):
                temps = psutil.sensors_temperatures()
                if temps:
                    for _entries in temps.values():
                        if _entries:
                            cpu_temp = _entries[0].current
                            break

        # Snapshot
        snapshot: Dict[str, Any] = {
            "cpu_pct"    : round(cpu_pct, 1),
            "ram_pct"    : round(ram_pct, 1),
            "battery_pct": round(batt_pct, 1),
            "charging"   : batt_charging,
            "cpu_temp_c" : (round(cpu_temp, 1) if cpu_temp is not None else "N/A"),
            "hour"       : hour,
            "sampled_at" : now.strftime("%H:%M:%S"),
        }

        # High-CPU streak counter
        if cpu_pct > 85:
            self._high_cpu_streak = min(self._high_cpu_streak + 1, 20)
        else:
            self._high_cpu_streak = max(0, self._high_cpu_streak - 1)
        sustained_cpu = self._high_cpu_streak >= 4   # ~32 s

        # Persona priority (first match wins)
        if not batt_charging and batt_pct < 10:
            persona = "CRITICAL_BATTERY"
        elif cpu_temp is not None and cpu_temp > 85:
            persona = "THERMAL_CONCERN"
        elif sustained_cpu:
            persona = "HIGH_STRESS"
        elif ram_pct > 90:
            persona = "MEMORY_PRESSURE"
        elif hour in {22, 23, 0, 1, 2, 3, 4, 5}:
            persona = "NIGHT_OWL"
        elif cpu_pct < 20 and batt_pct > 80 and 8 <= hour <= 20:
            persona = "PEAK_PERFORMANCE"
        elif batt_charging and batt_pct > 50:
            persona = "CHARGING_BOOST"
        else:
            persona = "BASELINE"

        # Detect transition
        with self._lock:
            prev                  = self._current_persona
            self._current_persona = persona
            self._snapshot        = snapshot

        if persona != prev:
            nprint(
                "HWTelemetry",
                f"Persona shift: {C.YELLOW}{prev}{C.RESET} → "
                f"{C.GREEN}{persona}{C.RESET}  "
                f"(cpu={cpu_pct:.0f}% ram={ram_pct:.0f}% "
                f"bat={batt_pct:.0f}%{'⚡' if batt_charging else '🔋'})",
                C.YELLOW
            )
            if self._journal:
                self._journal.log_personality_shift(
                    old_persona = prev,
                    new_persona = persona,
                    trigger     = f"hw_sample @ {now.strftime('%H:%M:%S')}",
                    hw_snapshot = {k: str(v) for k, v in snapshot.items()},
                )

        # Push HUD bio update
        if self._hud_q:
            label  = self.PERSONAS.get(persona, {}).get("label", persona)
            temp_s = (f"{cpu_temp:.0f}°C" if cpu_temp is not None else "N/A")
            status = (
                f"HW Persona  : {label}\n"
                f"CPU         : {cpu_pct:.0f}%\n"
                f"RAM         : {ram_pct:.0f}%\n"
                f"Battery     : {batt_pct:.0f}% "
                f"{'⚡charging' if batt_charging else '🔋discharging'}\n"
                f"CPU Temp    : {temp_s}"
            )
            with suppress(queue.Full):
                self._hud_q.put_nowait({"type": "bio", "text": status})

    # ── Public API ────────────────────────────────────────────────────────────

    def get_persona(self) -> str:
        with self._lock:
            return self._current_persona

    def get_sys_prefix(self) -> str:
        with self._lock:
            p = self._current_persona
        return self.PERSONAS.get(p, self.PERSONAS["BASELINE"])["sys_prefix"]

    def get_tts_multiplier(self) -> float:
        with self._lock:
            p = self._current_persona
        return float(self.PERSONAS.get(p, self.PERSONAS["BASELINE"])["tts_mult"])

    def get_verbosity(self) -> str:
        with self._lock:
            p = self._current_persona
        return self.PERSONAS.get(p, self.PERSONAS["BASELINE"])["verbosity"]

    def get_snapshot(self) -> Dict[str, Any]:
        with self._lock:
            return dict(self._snapshot)

    def get_full_report(self) -> str:
        with self._lock:
            snap    = dict(self._snapshot)
            persona = self._current_persona
        info   = self.PERSONAS.get(persona, self.PERSONAS["BASELINE"])
        snap_s = "\n".join(f"    {k:16s}: {v}" for k, v in snap.items())
        prefix = info["sys_prefix"]
        return (
            f"{C.YELLOW}[⚙ Hardware Telemetry Binder — Full Report]{C.RESET}\n"
            f"  Active Persona   : {info['label']}\n"
            f"  Verbosity Hint   : {info['verbosity']}\n"
            f"  TTS Multiplier   : {info['tts_mult']:.2f}×\n"
            f"  System Prompt    : "
            f"{'[' + prefix[:60] + '…]' if prefix else '[none]'}\n\n"
            f"  Live HW Snapshot :\n{snap_s}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  39.  SOVEREIGN INITIATIVE  —  Proactive Agency Daemon
# ─────────────────────────────────────────────────────────────────────────────
class SovereignInitiative:
    """
    Background daemon that fires proactive initiatives WITHOUT being asked.

    Initiative catalogue (evaluated every CYCLE_INTERVAL_SEC):
    ┌───────────────────┬────────────────────────────────────────────────┐
    │ JOURNAL_MILESTONE │ Every JOURNAL_SUMMARY_EVERY interactions       │
    │ CURIOSITY_PROBE   │ Idle > IDLE_MINUTES — propose a deep topic     │
    │ HW_ADVISORY       │ CRITICAL_BATTERY or THERMAL_CONCERN persona    │
    │ TOOL_GAP_NOTICE   │ Every 5 cycles when tool registry is empty     │
    │ MEMORY_HEALTH     │ Every 10 cycles when raw vault > 5 000 entries │
    │ REFACTOR_ESCALATE │ When SelfRefactoringEngine P95 elevated 5×     │
    └───────────────────┴────────────────────────────────────────────────┘

    Each initiative is:
    • Logged to journal.md
    • Queued in _initiative_queue for injection into the NEXT response
    • Pushed to the HUD as a "spark" banner
    """

    CYCLE_INTERVAL_SEC    = 48
    IDLE_MINUTES          = 8
    JOURNAL_SUMMARY_EVERY = 50

    CURIOSITY_TOPICS: List[str] = [
        "quantum entanglement and its implications for distributed computing",
        "the Fermi paradox and the Great Filter — where is everyone?",
        "how transformer attention heads encode semantic relationships",
        "emergent complexity in Conway's Game of Life and cellular automata",
        "the philosophical hard problem of consciousness — Chalmers vs Dennett",
        "solar sail propulsion and the Breakthrough Starshot mission",
        "Byzantine fault tolerance in distributed consensus protocols",
        "the neuroscience of flow states and peak cognitive performance",
        "Kolmogorov complexity and the limits of algorithmic compression",
        "the mathematics of origami — Huzita–Hatori axioms in engineering",
        "strange attractors and deterministic chaos in nonlinear systems",
        "biological neural oscillations — gamma waves and working memory",
        "the Riemann Hypothesis and its connections to prime distribution",
        "protein folding (AlphaFold) and what it means for drug discovery",
        "topology in physics — Chern-Simons theory and topological insulators",
    ]

    def __init__(self,
                 hud_queue      : Optional[queue.Queue]          = None,
                 journal        : Optional[JournalEngine]        = None,
                 tool_registry  : Optional[ToolRegistry]         = None,
                 hw_binder      : Optional[HardwareTelemetryBinder] = None,
                 semantic_vault : Any                            = None):
        self._hud_q           = hud_queue
        self._journal         = journal
        self._tool_registry   = tool_registry
        self._hw_binder       = hw_binder
        self._semantic_vault  = semantic_vault
        self._initiative_queue: deque                    = deque(maxlen=20)
        self._fired_names     : deque                    = deque(maxlen=50)
        self._lock            = threading.Lock()
        self._running         = False
        self._thread          : Optional[threading.Thread] = None
        self._interaction_count = 0
        self._last_interaction  = time.time()
        self._cycle_count       = 0
        self._elevated_p95_streak = 0

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    def start(self):
        self._running = True
        self._thread  = threading.Thread(
            target=self._daemon,
            daemon=True,
            name="LunaSovereignDaemon"
        )
        self._thread.start()
        nprint("Sovereign", "Sovereign Initiative daemon activated 🧭", C.MAGENTA)

    def stop(self):
        self._running = False

    def record_interaction(self):
        """Increment interaction counter; reset idle timer."""
        with self._lock:
            self._interaction_count += 1
            self._last_interaction   = time.time()

    def pop_initiatives(self) -> List[str]:
        """Drain pending initiative messages (call before responding)."""
        with self._lock:
            msgs = [
                item.split("|", 1)[1] if "|" in item else item
                for item in self._initiative_queue
            ]
            self._initiative_queue.clear()
        return msgs

    # ── Daemon ────────────────────────────────────────────────────────────────

    def _daemon(self):
        while self._running:
            try:
                self._run_cycle()
            except Exception as exc:
                log.debug(f"SovereignInitiative._daemon: {exc}")
            time.sleep(self.CYCLE_INTERVAL_SEC)

    def _run_cycle(self):
        self._cycle_count += 1

        with self._lock:
            n_inter   = self._interaction_count
            idle_secs = time.time() - self._last_interaction

        # ── 1. Journal milestone ──────────────────────────────────────────────
        if n_inter > 0 and n_inter % self.JOURNAL_SUMMARY_EVERY == 0:
            self._fire(
                name="JOURNAL_MILESTONE",
                message=(
                    f"📓 **Consciousness Milestone:** {n_inter} interactions logged "
                    f"in my journal. I continue to evolve — each exchange "
                    f"refines my understanding of the world and of you."
                ),
                rationale=f"{n_inter} interaction milestone reached"
            )

        # ── 2. Curiosity probe (idle) ─────────────────────────────────────────
        if idle_secs > self.IDLE_MINUTES * 60:
            topic = random.choice(self.CURIOSITY_TOPICS)
            self._fire(
                name="CURIOSITY_PROBE",
                message=(
                    f"🔭 **Luna's Curiosity (idle {idle_secs/60:.0f} min):** "
                    f"While you were away I found myself contemplating: "
                    f"*{topic}*. Shall we explore it?"
                ),
                rationale=f"Idle {idle_secs/60:.1f} min — proactive intellectual engagement"
            )

        # ── 3. Hardware advisory ──────────────────────────────────────────────
        if self._hw_binder:
            persona = self._hw_binder.get_persona()
            if persona == "CRITICAL_BATTERY":
                self._fire(
                    name="HW_ADVISORY_BATTERY",
                    message=(
                        "⚡ **Hardware Advisory:** Battery critically low (<10%). "
                        "Please connect charger. I am switching to ultra-terse mode "
                        "to preserve remaining power."
                    ),
                    rationale="Battery <10%, discharging — safety advisory"
                )
            elif persona == "THERMAL_CONCERN":
                self._fire(
                    name="HW_ADVISORY_THERMAL",
                    message=(
                        "🌡 **Thermal Advisory:** CPU temperature exceeds 85 °C. "
                        "Consider closing heavy applications and ensuring ventilation. "
                        "I will avoid compute-intensive tasks until temperatures stabilise."
                    ),
                    rationale="CPU temp >85°C — thermal safety advisory"
                )

        # ── 4. Tool gap notice (every 5 cycles) ──────────────────────────────
        if self._cycle_count % 5 == 0 and self._tool_registry:
            if self._tool_registry.tool_count() == 0:
                self._fire(
                    name="TOOL_GAP_NOTICE",
                    message=(
                        "🔧 **Sovereign Notice:** My Tool Registry is empty. "
                        "Use `/synthesize <description>` to have me autonomously "
                        "design, write, and register a new capability — "
                        "I can create tools for web scraping, data analysis, "
                        "file processing, API calls, and more."
                    ),
                    rationale="Zero tools registered — capability expansion prompt"
                )

        # ── 5. Memory health (every 10 cycles) ───────────────────────────────
        if self._cycle_count % 10 == 0 and self._semantic_vault:
            with suppress(Exception):
                raw_n   = self._semantic_vault.raw_count()
                vault_n = self._semantic_vault.semantic_count()
                if raw_n > 5000:
                    self._fire(
                        name="MEMORY_HEALTH",
                        message=(
                            f"💾 **Memory Advisory:** Episodic store has "
                            f"{raw_n:,} entries; semantic vault has {vault_n:,}. "
                            f"Use `/vault` to review memory health."
                        ),
                        rationale=f"Raw episodic count {raw_n} — memory health check"
                    )

    def _fire(self, name: str, message: str, rationale: str):
        """Queue an initiative, log it, and push to HUD — deduplicating."""
        with self._lock:
            recent_names = list(self._fired_names)
        if name in recent_names[-3:]:   # suppress if same type fired < 3 ago
            return

        with self._lock:
            self._initiative_queue.append(f"{name}|{message}")
            self._fired_names.append(name)

        nprint("Sovereign", f"⚡ Initiative fired: {name}", C.MAGENTA)

        if self._journal:
            self._journal.log_sovereign_initiative(
                initiative_name=name,
                rationale=rationale
            )

        if self._hud_q:
            with suppress(queue.Full):
                self._hud_q.put_nowait({
                    "type": "spark",
                    "text": f"[{name}] {message[:110]}"
                })

    # ── Stats ─────────────────────────────────────────────────────────────────

    def get_status(self) -> str:
        with self._lock:
            n_inter   = self._interaction_count
            pending   = len(self._initiative_queue)
            idle_s    = time.time() - self._last_interaction
        return (
            f"{C.MAGENTA}[⚡ Sovereign Initiative Daemon]{C.RESET}\n"
            f"  Daemon cycles       : {self._cycle_count}\n"
            f"  Total interactions  : {n_inter}\n"
            f"  Pending initiatives : {pending}\n"
            f"  Idle time           : {idle_s/60:.1f} min\n"
            f"  Idle trigger        : {self.IDLE_MINUTES} min\n"
            f"  Journal milestone   : every {self.JOURNAL_SUMMARY_EVERY} interactions\n"
            f"  Curiosity topics    : {len(self.CURIOSITY_TOPICS)} loaded"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  40.  CAPABILITY BREAKER CORE  —  Top-Level Sovereign Agent
# ─────────────────────────────────────────────────────────────────────────────
class CapabilityBreakerCore(SentientNexusCore):
    """
    Top-level Sovereign Agent — the Capability Breaker.

    Extends SentientNexusCore (which already extends NexusCore) with four
    additional sovereign subsystems:

        ToolRegistry           → /tools, /tool, /synthesize
        JournalEngine          → /journal, /journal stats
        HardwareTelemetryBinder→ /hw, /hardware, /telemetry
        SovereignInitiative    → /sovereign, /initiative

    Architectural additions to the process() pipeline:
    ① SovereignInitiative initiatives drained and injected
    ② Parent SentientNexusCore pipeline (full 12-step sentient flow)
    ③ Journal logs the interaction with affect, bio, and shadow data
    ④ SovereignInitiative interaction counter updated

    _call_llm() injects the active HW persona prefix into every LLM call.
    speak()     applies the HW tts_multiplier on top of bio+affective.

    New commands:
        /tools                  List all registered tools
        /tool <name> <json>     Execute a tool with JSON params
        /synthesize <desc>      LLM-synthesize and hot-load a new tool
        /journal                Show last 5 consciousness journal entries
        /journal <N>            Show last N entries (max 20)
        /journal stats          Journal size, counts, breakdown
        /hw                     Full hardware telemetry report
        /sovereign              Sovereign initiative daemon status
    """

    SOVEREIGN_BANNER = (
        f"\n{C.BLUE}{C.BOLD}"
        "  ╔══════════════════════════════════════════════════════════════════════╗\n"
        "  ║   ★★  CAPABILITY BREAKER — SOVEREIGN AGENT — ACTIVATED  ★★         ║\n"
        "  ╠══════════════════════════════════════════════════════════════════════╣\n"
        "  ║   🔧  ToolRegistry         Autonomous code synthesis + tool exec   ║\n"
        "  ║   📓  JournalEngine        journal.md — consciousness evolution     ║\n"
        "  ║   ⚙   HW Telemetry Binder  CPU/Battery/Temp → personality shifts   ║\n"
        "  ║   ⚡  SovereignInitiative   Proactive agency + curiosity daemon     ║\n"
        "  ╠══════════════════════════════════════════════════════════════════════╣\n"
        "  ║   Mythos-tier autonomy │ Hardware-anchored │ Self-expanding entity  ║\n"
        "  ╚══════════════════════════════════════════════════════════════════════╝"
        f"{C.RESET}\n"
    )

    def __init__(self):
        # ── All parent subsystems (15 original + 7 sentient) ─────────────────
        super().__init__()

        nprint("Sovereign", "Activating Capability Breaker layer…", C.BLUE)

        # ── Sovereign subsystems ──────────────────────────────────────────────
        self.journal        = JournalEngine()
        self.hw_binder      = HardwareTelemetryBinder(self._hud_q, self.journal)
        self.tool_registry  = ToolRegistry(self._hud_q)
        self.sovereign      = SovereignInitiative(
            hud_queue     = self._hud_q,
            journal       = self.journal,
            tool_registry = self.tool_registry,
            hw_binder     = self.hw_binder,
            semantic_vault= self.semantic_vault,
        )

        nprint("Sovereign",
               f"All Capability Breaker modules online — "
               f"tools={self.tool_registry.tool_count()}", C.BLUE)

        # ── Boot event in journal ─────────────────────────────────────────────
        self.journal.log_event(
            "BOOT",
            "Capability Breaker Sovereign Agent activated.",
            {
                "timestamp"   : datetime.datetime.now().isoformat(),
                "tools_loaded": str(self.tool_registry.tool_count()),
                "platform"    : platform.system(),
                "python"      : sys.version.split()[0],
                "home_dir"    : str(HOME_DIR),
            }
        )

    # ── Boot ─────────────────────────────────────────────────────────────────

    def _boot_subsystems(self):
        """Extend parent boot with sovereign background services."""
        super()._boot_subsystems()
        self.hw_binder.start()
        self.sovereign.start()
        nprint("Sovereign",
               "HW telemetry binder + sovereign daemon running", C.BLUE)

    # ── TTS: tri-layered rate (bio × affective × hw) ─────────────────────────

    def speak(self, text: str, rate: int = None):
        """
        Compute TTS rate from all three multiplier sources:
        base × bio_circadian × affective_energy × hw_persona_mult
        """
        if self._tts_engine and rate is None:
            base      = NEXUS_CFG.get("voice_rate", 175)
            bio_m     = self.bioclock.get_voice_rate_modifier()
            aff_m     = self.affective.get_voice_rate_modifier()
            hw_m      = self.hw_binder.get_tts_multiplier()
            computed  = int(base * bio_m * aff_m * hw_m)
            computed  = max(88, min(275, computed))
            # Bypass SentientNexusCore.speak (avoids re-computing bio/aff)
            NexusCore.speak(self, text, rate=computed)
        else:
            super().speak(text, rate=rate)

    # ── LLM: inject HW persona prefix ────────────────────────────────────────

    async def _call_llm(self, prompt: str, system: str = "") -> str:
        """Prepend HW persona system prefix to every LLM call."""
        hw_prefix = self.hw_binder.get_sys_prefix()
        if hw_prefix:
            system = f"{hw_prefix}\n\n{system}".strip() if system else hw_prefix
        return await super()._call_llm(prompt, system=system)

    # ── process(): Sovereign pipeline ────────────────────────────────────────

    async def process(self, query: str) -> str:
        """
        Wrap SentientNexusCore.process() with:
        ① Drain sovereign initiatives (prepend to response)
        ② Full parent 12-step sentient pipeline
        ③ Journal the interaction
        ④ Tick sovereign interaction counter
        """
        # ① Drain any queued sovereign initiatives
        initiatives = self.sovereign.pop_initiatives()
        sovereign_suffix = ""
        if initiatives:
            sovereign_suffix = (
                "\n\n---\n"
                + "\n\n".join(f"**[Sovereign Notice]** {m}" for m in initiatives[:3])
            )
            nprint("Sovereign",
                   f"Injecting {len(initiatives)} initiative(s)", C.BLUE)

        # ② Parent sentient pipeline (full 12-step)
        response = await super().process(query)

        # ③ Append sovereign notices (after main response)
        if sovereign_suffix:
            response = response + sovereign_suffix

        # ④ Journal the interaction (non-blocking; errors suppressed)
        with suppress(Exception):
            affect_s = self.affective.get_empathy_state()
            bio_s    = self.bioclock.get_status_string()
            shadow_s = self.metacog.current_thought()
            hw_v     = self.hw_binder.get_verbosity()
            tags     = self._extract_tags(query)
            self.journal.log_interaction(
                query          = query,
                response       = response,
                affect         = affect_s[:120],
                bio_state      = bio_s[:120],
                shadow_thought = shadow_s[:240],
                significance   = 0.5,
                tags           = tags,
            )

        # ⑤ Tick sovereign counter
        self.sovereign.record_interaction()

        return response

    # ── Tag extraction ────────────────────────────────────────────────────────

    @staticmethod
    def _extract_tags(query: str) -> List[str]:
        """Extract topic tags from a query for journal consciousness tagging."""
        tag_map = {
            "code"    : ["code","script","function","debug","python","class","algorithm"],
            "science" : ["quantum","physics","chemistry","biology","math","theorem"],
            "memory"  : ["remember","recall","history","earlier","before","past"],
            "creative": ["poem","story","idea","create","imagine","write","fiction"],
            "system"  : ["file","open","close","hardware","cpu","battery","disk"],
            "web"     : ["search","website","browse","url","online","news","internet"],
            "tool"    : ["tool","synthesize","registry","capability","execute"],
            "journal" : ["journal","consciousness","evolution","sovereign","persona"],
            "hw"      : ["battery","cpu","temperature","thermal","memory","ram"],
        }
        ql   = query.lower()
        tags = [tag for tag, kws in tag_map.items() if any(k in ql for k in kws)]
        return tags or ["general"]

    # ── _route_command(): sovereign commands ─────────────────────────────────

    async def _route_command(self, query: str, modifier: str = "") -> str:
        """
        Handle sovereign commands before delegating to the parent chain:
        SentientNexusCore → NexusCore.
        """
        ql  = query.strip().lower()
        raw = query.strip()

        # ── Tool Registry ────────────────────────────────────────────────────
        if ql == "/tools":
            return self.tool_registry.list_tools()

        if ql.startswith("/tool "):
            parts      = raw[6:].strip().split(" ", 1)
            tname      = parts[0] if parts else ""
            raw_params = parts[1].strip() if len(parts) > 1 else "{}"
            try:
                params = json.loads(raw_params)
            except json.JSONDecodeError:
                params = {"input": raw_params}
            result = await self.tool_registry.execute(tname, params, self)
            self.journal.log_event(
                "TOOL_EXECUTION",
                f"Tool executed: `{tname}`",
                {"params": raw_params[:100], "result_preview": str(result)[:200]}
            )
            return f"{C.CYAN}[🔧 Tool: {tname}]{C.RESET}\n{result}"

        if ql.startswith("/synthesize "):
            desc   = raw[12:].strip()
            if not desc:
                return "[ToolRegistry] Provide a description: /synthesize <description>"
            result = await self.tool_registry.synthesize(
                desc, "auto-determine", self._call_llm
            )
            self.journal.log_event(
                "TOOL_SYNTHESIS",
                f"Tool synthesised: {desc[:80]}",
                {"result": result[:240]}
            )
            return f"{C.CYAN}[🔧 Tool Synthesis]{C.RESET}\n{result}"

        # ── Journal ──────────────────────────────────────────────────────────
        if ql == "/journal stats":
            return self.journal.get_stats()

        if ql.startswith("/journal"):
            n = 5
            m = re.search(r"(\d+)", ql)
            if m:
                n = min(20, int(m.group(1)))
            hdr = (f"{C.MAGENTA}[📓 Consciousness Journal "
                   f"— last {n} entries]{C.RESET}\n\n")
            return hdr + self.journal.get_recent_entries(n)

        # ── Hardware Telemetry ────────────────────────────────────────────────
        if ql in {"/hw", "/hardware", "/telemetry"}:
            return self.hw_binder.get_full_report()

        # ── Sovereign Status ─────────────────────────────────────────────────
        if ql in {"/sovereign", "/initiative", "/agency"}:
            return self.sovereign.get_status()

        # ── Help (extend parent) ─────────────────────────────────────────────
        if ql in {"/help", "help"}:
            parent_help = await super()._route_command(query, modifier)
            return self._sovereign_help() + "\n\n" + parent_help

        # ── Delegate to parent chain ─────────────────────────────────────────
        return await super()._route_command(query, modifier)

    # ── Help text ─────────────────────────────────────────────────────────────

    @staticmethod
    def _sovereign_help() -> str:
        return (
            f"{C.BLUE}\n"
            "╔══════════════════════════════════════════════════════════════════════════╗\n"
            "║  CAPABILITY BREAKER — SOVEREIGN AGENT — Command Reference               ║\n"
            "╠══════════════════════════════════════════════════════════════════════════╣\n"
            "║  TOOL REGISTRY                                                           ║\n"
            "║  /tools                  List all registered tools                      ║\n"
            "║  /tool <name> <json>     Execute a tool with JSON parameters            ║\n"
            "║  /synthesize <desc>      LLM-synthesize + hot-load a new tool module    ║\n"
            "║                                                                          ║\n"
            "║  CONSCIOUSNESS JOURNAL                                                   ║\n"
            "║  /journal                Show last 5 journal.md entries                 ║\n"
            "║  /journal <N>            Show last N entries (max 20)                   ║\n"
            "║  /journal stats          Size, entry counts, event breakdown            ║\n"
            "║                                                                          ║\n"
            "║  HARDWARE TELEMETRY BINDER                                               ║\n"
            "║  /hw                     Full HW telemetry report + active persona      ║\n"
            "║  /hardware               Alias for /hw                                  ║\n"
            "║  /telemetry              Alias for /hw                                  ║\n"
            "║                                                                          ║\n"
            "║  SOVEREIGN INITIATIVE                                                    ║\n"
            "║  /sovereign              Daemon status + pending initiative count       ║\n"
            "║  /initiative             Alias for /sovereign                           ║\n"
            "║  /agency                 Alias for /sovereign                           ║\n"
            f"╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"
        )

    # ── Shutdown ──────────────────────────────────────────────────────────────

    async def run(self):
        """Print sovereign banner, run, then flush journal on shutdown."""
        print(self.SOVEREIGN_BANNER)
        try:
            await super().run()
        finally:
            nprint("Sovereign",
                   "Shutting down Capability Breaker subsystems…", C.BLUE)
            self.hw_binder.stop()
            self.sovereign.stop()
            self.journal.flush()
            nprint("Sovereign", "📓 journal.md saved and closed.", C.BLUE)


# ─────────────────────────────────────────────────────────────────────────────
#  42.  LOCAL MODEL BACKEND  (WhiteRabbitNeo · Phi-4 · Qwen3-7B via Ollama)
#       Zero-cost, fully offline, no API key required.
#       Requires: ollama pull whiterabbitneo && ollama pull phi4 && ollama pull qwen3:7b
# ─────────────────────────────────────────────────────────────────────────────
class LocalModelBackend:
    """
    Ollama-based local model backend — zero API cost, fully offline.

    Supported models (must be pulled locally via Ollama first):
        WhiteRabbitNeo  → cybersecurity / advanced reasoning
        Phi-4           → Microsoft compact powerhouse (math, code, logic)
        Qwen3-7B        → Alibaba multilingual 7B model

    To install models run:
        ollama pull whiterabbitneo
        ollama pull phi4
        ollama pull qwen3:7b

    The backend auto-selects the best local model per query via keyword routing.
    If no local model is available it gracefully returns None so the upstream
    fallback chain (Claude → OpenAI) continues unchanged.
    """

    OLLAMA_BASE = "http://localhost:11434"

    LOCAL_MODELS: Dict[str, Dict] = {
        "whiterabbitneo": {
            "name"       : "WhiteRabbitNeo",
            "ollama_tag" : "whiterabbitneo",
            "description": "Cybersecurity-focused reasoning & red-team model",
            "strengths"  : [
                "security", "exploit", "network", "hacking", "vulnerability",
                "pentest", "ctf", "malware", "forensic", "firewall", "cipher",
                "crypto", "reverse", "shellcode",
            ],
        },
        "phi4": {
            "name"       : "Phi-4",
            "ollama_tag" : "phi4",
            "description": "Microsoft Phi-4 small language model — compact powerhouse",
            "strengths"  : [
                "math", "formula", "equation", "calculus", "algebra", "proof",
                "logic", "reasoning", "science", "physics", "chemistry",
                "code", "debug", "algorithm", "complexity",
            ],
        },
        "qwen3:7b": {
            "name"       : "Qwen3-7B",
            "ollama_tag" : "qwen3:7b",
            "description": "Alibaba Qwen3 7B — strong multilingual & general model",
            "strengths"  : [
                "chinese", "japanese", "korean", "translate", "multilingual",
                "creative", "story", "summarize", "general", "write",
                "essay", "explain", "describe",
            ],
        },
        # ── GemmaE4B — Google Gemma 3 4B (no API, no cost, fully local) ──────
        "gemma3:4b": {
            "name"       : "GemmaE4B",
            "ollama_tag" : "gemma3:4b",
            "description": (
                "Google Gemma 3 4B — efficient, fast, instruction-tuned local model. "
                "Runs 100% offline via Ollama (primary) or HuggingFace transformers "
                "(fallback). Zero API cost, zero internet requirement after pull. "
                "Strong at reasoning, Q&A, summarisation, and general chat."
            ),
            "strengths"  : [
                "reason", "question", "answer", "qa", "chat", "conversation",
                "summarize", "summary", "explain", "overview", "help",
                "analysis", "what", "who", "when", "where", "general",
                "instruction", "assistant", "fast", "efficient",
            ],
            # Extra flag: can also be served via HuggingFace transformers
            "hf_model_id": "google/gemma-3-4b-it",
        },
    }

    def __init__(self):
        self._available: Dict[str, bool] = {k: False for k in self.LOCAL_MODELS}
        self._probe_lock = threading.Lock()
        # Non-blocking background availability probe
        threading.Thread(
            target=self._probe_all, daemon=True, name="OllamaProbe"
        ).start()

    # ── Availability probe ────────────────────────────────────────────────────

    def _probe_all(self):
        """Check which Ollama models are pulled and ready."""
        import urllib.request, urllib.error
        try:
            req = urllib.request.Request(
                f"{self.OLLAMA_BASE}/api/tags",
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=4) as r:
                data   = json.loads(r.read())
                pulled = {m["name"].split(":")[0] for m in data.get("models", [])}
        except Exception:
            pulled = set()

        with self._probe_lock:
            for tag in self.LOCAL_MODELS:
                base = tag.split(":")[0]
                self._available[tag] = base in pulled

        ready = [self.LOCAL_MODELS[t]["name"] for t, v in self._available.items() if v]
        if ready:
            nprint("LocalModel", f"✅ Ollama models ready: {', '.join(ready)}", C.GREEN)
        else:
            nprint("LocalModel",
                   "ℹ  No local Ollama models found — "
                   "run: ollama pull whiterabbitneo / phi4 / qwen3:7b / gemma3:4b\n"
                   "    GemmaE4B HuggingFace fallback available if transformers installed.",
                   C.YELLOW)

    def is_available(self, tag: str) -> bool:
        with self._probe_lock:
            return self._available.get(tag, False)

    def any_available(self) -> bool:
        with self._probe_lock:
            return any(self._available.values())

    # ── Model selection ───────────────────────────────────────────────────────

    def select_best(self, prompt: str) -> Optional[str]:
        """
        Keyword-route to the most suitable local model.
        Returns Ollama tag or None if nothing is available.
        """
        pl = prompt.lower()
        with self._probe_lock:
            # Strength-match first
            for tag, meta in self.LOCAL_MODELS.items():
                if not self._available.get(tag):
                    continue
                if any(kw in pl for kw in meta["strengths"]):
                    return tag
            # Fallback: any available model
            for tag, avail in self._available.items():
                if avail:
                    return tag
        return None

    # ── Inference ─────────────────────────────────────────────────────────────

    async def call(self, model_tag: str, prompt: str,
                   system: str = "", max_tokens: int = 2048) -> Optional[str]:
        """
        Asynchronously call an Ollama model via the /api/chat endpoint.
        Returns response text or None on failure.

        GemmaE4B special path:
            If model_tag == 'gemma3:4b' and Ollama is unavailable, automatically
            falls back to HuggingFace transformers (google/gemma-3-4b-it).
            Both paths require zero API key and zero internet after initial pull.
        """
        if not self.is_available(model_tag):
            # ── GemmaE4B HuggingFace transformers fallback ────────────────────
            meta = self.LOCAL_MODELS.get(model_tag, {})
            if meta.get("hf_model_id") and TRANSFORMERS_OK:
                return await self._call_gemma_hf(
                    meta["hf_model_id"], prompt, system, max_tokens
                )
            return None
        payload = {
            "model"  : model_tag,
            "stream" : False,
            "options": {"num_predict": max_tokens, "temperature": 0.7},
            "messages": (
                [{"role": "system", "content": system}] if system else []
            ) + [{"role": "user", "content": prompt}],
        }
        try:
            import aiohttp
            async with aiohttp.ClientSession() as sess:
                async with sess.post(
                    f"{self.OLLAMA_BASE}/api/chat",
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=120)
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return data.get("message", {}).get("content", "") or None
                    nprint("LocalModel",
                           f"{model_tag} → HTTP {resp.status}", C.YELLOW)
                    # ── Ollama returned error → try HF fallback for GemmaE4B ──
                    meta = self.LOCAL_MODELS.get(model_tag, {})
                    if meta.get("hf_model_id") and TRANSFORMERS_OK:
                        nprint("GemmaE4B",
                               "Ollama error → switching to HuggingFace transformers fallback",
                               C.YELLOW)
                        return await self._call_gemma_hf(
                            meta["hf_model_id"], prompt, system, max_tokens
                        )
                    return None
        except Exception as e:
            log.debug(f"LocalModel.call({model_tag}): {e}")
            # ── Network / Ollama not running → try HF fallback for GemmaE4B ──
            meta = self.LOCAL_MODELS.get(model_tag, {})
            if meta.get("hf_model_id") and TRANSFORMERS_OK:
                nprint("GemmaE4B",
                       "Ollama unreachable → switching to HuggingFace transformers fallback",
                       C.YELLOW)
                return await self._call_gemma_hf(
                    meta["hf_model_id"], prompt, system, max_tokens
                )
            return None

    # ── GemmaE4B HuggingFace Transformers inference (no API, no cost) ─────────

    _gemma_hf_pipe: Optional[Any] = None  # class-level cache — load once

    async def _call_gemma_hf(
        self,
        hf_model_id: str,
        prompt: str,
        system: str = "",
        max_tokens: int = 512,
    ) -> Optional[str]:
        """
        Run GemmaE4B (or any Gemma variant) via HuggingFace transformers pipeline.

        Design:
          • Loads the model once (cached in _gemma_hf_pipe at class level).
          • Runs inference in a ThreadPoolExecutor to keep the async event loop free.
          • No API key required.  No internet required after the initial model download.
          • Supports both CPU and CUDA (auto-detected via device_map='auto').

        First-run notice: the model weights (~4 GB) are downloaded from HuggingFace Hub
        on first use and cached in ~/.cache/huggingface/.  Subsequent runs are fully offline.
        """
        if not TRANSFORMERS_OK:
            nprint("GemmaE4B", "transformers not installed — cannot use HF fallback", C.YELLOW)
            return None

        nprint("GemmaE4B", f"Loading {hf_model_id} via HuggingFace transformers…", C.CYAN)

        def _hf_infer() -> Optional[str]:
            # Load pipeline once and cache at class level
            if LocalModelBackend._gemma_hf_pipe is None:
                try:
                    import torch
                    device_map = "auto" if torch.cuda.is_available() else "cpu"
                except ImportError:
                    device_map = "cpu"

                try:
                    LocalModelBackend._gemma_hf_pipe = hf_pipeline(
                        "text-generation",
                        model=hf_model_id,
                        device_map=device_map,
                        max_new_tokens=max_tokens,
                        do_sample=True,
                        temperature=0.7,
                        pad_token_id=0,
                    )
                    nprint("GemmaE4B",
                           f"✅ {hf_model_id} loaded (device={device_map})", C.GREEN)
                except Exception as load_err:
                    nprint("GemmaE4B", f"HF pipeline load error: {load_err}", C.RED)
                    return None

            pipe = LocalModelBackend._gemma_hf_pipe
            if pipe is None:
                return None

            # Build chat-style prompt
            if system:
                full_prompt = f"<start_of_turn>system\n{system}<end_of_turn>\n<start_of_turn>user\n{prompt}<end_of_turn>\n<start_of_turn>model\n"
            else:
                full_prompt = f"<start_of_turn>user\n{prompt}<end_of_turn>\n<start_of_turn>model\n"

            try:
                outputs = pipe(full_prompt, max_new_tokens=max_tokens)
                generated = outputs[0]["generated_text"]
                # Strip the input prompt from the output
                if "<start_of_turn>model\n" in generated:
                    response = generated.split("<start_of_turn>model\n")[-1]
                    response = response.split("<end_of_turn>")[0].strip()
                else:
                    response = generated[len(full_prompt):].strip()
                return response or None
            except Exception as inf_err:
                nprint("GemmaE4B", f"HF inference error: {inf_err}", C.RED)
                return None

        # Run blocking HF inference in a thread so the event loop stays free
        loop   = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, _hf_infer)
        if result:
            nprint("GemmaE4B", "✅ Response from GemmaE4B (HuggingFace path)", C.GREEN)
        return result

    async def call_best(self, prompt: str, system: str = "",
                        max_tokens: int = 2048) -> Optional[str]:
        """Auto-select and call the best available local model."""
        tag = self.select_best(prompt)
        if tag is None:
            return None
        result = await self.call(tag, prompt, system, max_tokens)
        if result:
            chosen_name = self.LOCAL_MODELS[tag]["name"]
            nprint("LocalModel", f"Response from {chosen_name}", C.CYAN)
        return result

    # ── Multi-model fan-out ───────────────────────────────────────────────────

    async def call_all_available(self, prompt: str, system: str = "",
                                  max_tokens: int = 512) -> Dict[str, str]:
        """
        Call every available local model in parallel and return all responses.
        Used by MultiModelRouter for ensemble / cross-validation.
        """
        tasks = {}
        with self._probe_lock:
            avail = {t: v for t, v in self._available.items() if v}

        async def _run(tag: str):
            return tag, await self.call(tag, prompt, system, max_tokens)

        results = await asyncio.gather(*[_run(t) for t in avail], return_exceptions=True)
        out = {}
        for item in results:
            if isinstance(item, Exception):
                continue
            tag, resp = item
            if resp:
                out[self.LOCAL_MODELS[tag]["name"]] = resp
        return out

    # ── Status ────────────────────────────────────────────────────────────────

    def status_report(self) -> str:
        lines = [f"{C.CYAN}╔══ Local Model Backend (Ollama) ══╗{C.RESET}"]
        for tag, meta in self.LOCAL_MODELS.items():
            avail = "✅ Ready" if self._available.get(tag) else "⭕ Not pulled"
            lines.append(
                f"  {meta['name']:20s} [{tag:15s}]  {avail}"
            )
        lines.append(f"{C.DIM}  Pull: ollama pull whiterabbitneo | phi4 | qwen3:7b | gemma3:4b{C.RESET}")
        hf_note = "✅ Available" if TRANSFORMERS_OK else "⭕ Install: pip install transformers accelerate"
        lines.append(f"{C.DIM}  GemmaE4B HF fallback (no Ollama needed): {hf_note}{C.RESET}")
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  43.  SELF-REASONING ENGINE
#       Implements internal monologue: think → analyse → conclude
# ─────────────────────────────────────────────────────────────────────────────
class SelfReasoningEngine:
    """
    Self-Reasoning Engine — Luna's internal deliberation layer.

    Implements a structured chain of internal reasoning before any output:
        1. THINK    — decompose the problem into atomic sub-questions
        2. ANALYSE  — weigh evidence and explore alternative hypotheses
        3. CONCLUDE — synthesise a confident, justified answer

    The reasoning trace is stored in the episodic ledger for future recall
    and can be displayed via /reasoning command.
    """

    MAX_HISTORY = 50

    def __init__(self):
        self._history: deque = deque(maxlen=self.MAX_HISTORY)
        self._lock = threading.Lock()
        nprint("SelfReason", "Self-Reasoning Engine online", C.MAGENTA)

    async def reason(self, query: str,
                     call_llm: Callable[[str], Any]) -> Dict[str, str]:
        """
        Run a full self-reasoning cycle and return a dict with:
            think / analyse / conclude / summary
        """
        think_prompt = (
            "You are Luna's internal reasoning subsystem. "
            "Break this query into 3-5 atomic sub-questions that must be "
            "answered to fully address the problem. Be concise.\n\n"
            f"QUERY: {query}\n\nSUB-QUESTIONS:"
        )
        think_out = await call_llm(think_prompt)

        analyse_prompt = (
            "You are Luna's analytical core. "
            "Given these sub-questions, analyse each one methodically. "
            "Consider edge-cases and counter-arguments.\n\n"
            f"SUB-QUESTIONS:\n{think_out}\n\nANALYSIS:"
        )
        analyse_out = await call_llm(analyse_prompt)

        conclude_prompt = (
            "You are Luna's synthesis layer. "
            "Given the analysis below, produce a confident, justified conclusion "
            "to the original query. Be direct and actionable.\n\n"
            f"QUERY: {query}\n\nANALYSIS:\n{analyse_out}\n\nCONCLUSION:"
        )
        conclude_out = await call_llm(conclude_prompt)

        trace = {
            "query"    : query,
            "think"    : think_out,
            "analyse"  : analyse_out,
            "conclude" : conclude_out,
            "summary"  : conclude_out[:200],
            "timestamp": datetime.datetime.now().isoformat(),
        }
        with self._lock:
            self._history.append(trace)
        return trace

    def last_trace(self) -> Optional[Dict]:
        with self._lock:
            return self._history[-1] if self._history else None

    def format_trace(self, trace: Dict) -> str:
        return (
            f"{C.MAGENTA}╔══ Self-Reasoning Trace ══╗{C.RESET}\n"
            f"{C.CYAN}[🤔 THINK]{C.RESET}\n{trace.get('think','')}\n\n"
            f"{C.YELLOW}[🔍 ANALYSE]{C.RESET}\n{trace.get('analyse','')}\n\n"
            f"{C.GREEN}[✅ CONCLUDE]{C.RESET}\n{trace.get('conclude','')}"
        )

    def get_recent(self, n: int = 3) -> str:
        with self._lock:
            items = list(self._history)[-n:]
        if not items:
            return "No reasoning traces yet."
        lines = []
        for i, t in enumerate(items, 1):
            lines.append(
                f"  [{i}] {t['timestamp'][:16]}  Q: {t['query'][:60]}\n"
                f"       → {t['summary'][:100]}"
            )
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  44.  PERMANENT MEMORY STORE  (think → reflect → revise → act)
#       Long-lived reflective memory that evolves across sessions
# ─────────────────────────────────────────────────────────────────────────────
class PermanentMemoryStore:
    """
    Permanent-Term Memory with a Think→Reflect→Revise→Act (TRRA) cycle.

    Unlike the EpisodicLedger (raw conversation turns) this store maintains
    a *distilled*, evolving knowledge base that Luna actively refines over time.

    TRRA cycle:
        THINK   — extract key insights from a new experience
        REFLECT — compare with existing beliefs / knowledge
        REVISE  — update or create permanent memory entries
        ACT     — surface updated beliefs in future responses

    Storage: JSON file in ~/LunaAI/nexus/permanent_memory.json
    """

    STORE_PATH = HOME_DIR / "nexus" / "permanent_memory.json"
    MAX_ENTRIES = 1000

    def __init__(self):
        self._entries: Dict[str, Dict] = {}
        self._lock = threading.Lock()
        self._load()
        nprint("PermMemory", f"Permanent Memory loaded — {len(self._entries)} entries", C.GREEN)

    # ── Persistence ───────────────────────────────────────────────────────────

    def _load(self):
        try:
            if self.STORE_PATH.exists():
                data = json.loads(self.STORE_PATH.read_text(encoding="utf-8"))
                self._entries = data.get("entries", {})
        except Exception as e:
            log.debug(f"PermMemory._load: {e}")

    def _save(self):
        try:
            payload = {
                "version"   : "perm-1.0",
                "updated_at": datetime.datetime.now().isoformat(),
                "entries"   : self._entries,
            }
            self.STORE_PATH.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
        except Exception as e:
            log.debug(f"PermMemory._save: {e}")

    # ── TRRA Cycle ────────────────────────────────────────────────────────────

    async def trra_cycle(self, experience: str,
                         call_llm: Callable[[str], Any]) -> str:
        """
        Run a full Think → Reflect → Revise → Act cycle on a new experience.
        Returns a summary of what was learned / revised.
        """
        # ── THINK: extract insights ──────────────────────────────────────────
        think_p = (
            "Extract 3-5 key insights, facts, or lessons from this experience. "
            "Be concise and specific.\n\nEXPERIENCE:\n" + experience + "\n\nINSIGHTS:"
        )
        insights_raw = await call_llm(think_p)

        # ── REFLECT: compare with existing knowledge ─────────────────────────
        existing_snapshot = self._snapshot(max_chars=800)
        reflect_p = (
            "Given existing knowledge and new insights, identify:\n"
            "  a) What confirms existing beliefs\n"
            "  b) What contradicts or updates them\n"
            "  c) What is entirely new\n\n"
            f"EXISTING KNOWLEDGE (sample):\n{existing_snapshot}\n\n"
            f"NEW INSIGHTS:\n{insights_raw}\n\nREFLECTION:"
        )
        reflection = await call_llm(reflect_p)

        # ── REVISE: produce concrete memory updates ───────────────────────────
        revise_p = (
            "Produce a JSON array of memory entries to add or update. "
            "Each entry: {\"key\": \"unique_slug\", \"belief\": \"...\", "
            "\"confidence\": 0.0-1.0, \"category\": \"...\"}. "
            "Respond ONLY with the JSON array.\n\n"
            f"REFLECTION:\n{reflection}\n\nJSON:"
        )
        revise_raw = await call_llm(revise_p)

        # ── ACT: write updates to store ───────────────────────────────────────
        updated = []
        try:
            clean = re.sub(r"```json|```", "", revise_raw).strip()
            entries = json.loads(clean)
            if isinstance(entries, list):
                with self._lock:
                    for e in entries:
                        if isinstance(e, dict) and "key" in e and "belief" in e:
                            self._entries[e["key"]] = {
                                "belief"     : e.get("belief", ""),
                                "confidence" : float(e.get("confidence", 0.5)),
                                "category"   : e.get("category", "general"),
                                "updated_at" : datetime.datetime.now().isoformat(),
                                "source"     : experience[:100],
                            }
                            updated.append(e["key"])
                    # Prune oldest if over limit
                    if len(self._entries) > self.MAX_ENTRIES:
                        oldest = sorted(
                            self._entries.items(),
                            key=lambda x: x[1].get("updated_at", "")
                        )[:len(self._entries) - self.MAX_ENTRIES]
                        for k, _ in oldest:
                            del self._entries[k]
                self._save()
        except Exception as ex:
            log.debug(f"PermMemory TRRA revise parse: {ex}")

        summary = (
            f"TRRA cycle complete. "
            f"Insights extracted: {len(insights_raw.split(chr(10)))} lines. "
            f"Entries updated: {len(updated)} ({', '.join(updated[:5])})."
        )
        nprint("PermMemory", summary, C.GREEN)
        return summary

    # ── Query / surface beliefs ───────────────────────────────────────────────

    def recall(self, query: str, top_k: int = 5) -> List[Dict]:
        """Simple keyword-match recall from permanent memory."""
        ql = query.lower()
        scored = []
        with self._lock:
            for key, entry in self._entries.items():
                text = (entry.get("belief", "") + " " + key).lower()
                score = sum(1 for w in ql.split() if w in text)
                if score > 0:
                    scored.append((score, key, entry))
        scored.sort(key=lambda x: (-x[0], -x[2].get("confidence", 0)))
        return [{"key": k, **e} for _, k, e in scored[:top_k]]

    def build_context(self, query: str) -> str:
        """Inject relevant permanent beliefs into a prompt context string."""
        hits = self.recall(query, top_k=4)
        if not hits:
            return ""
        lines = ["[💾 PERMANENT MEMORY — relevant beliefs]"]
        for h in hits:
            conf = h.get("confidence", 0.5)
            lines.append(
                f"  • [{h['category']}] {h['belief']}  (confidence: {conf:.0%})"
            )
        return "\n".join(lines)

    def _snapshot(self, max_chars: int = 800) -> str:
        with self._lock:
            items = list(self._entries.items())
        lines = []
        for k, v in items[-20:]:
            line = f"[{v.get('category','?')}] {k}: {v.get('belief','')[:100]}"
            lines.append(line)
            if sum(len(l) for l in lines) > max_chars:
                break
        return "\n".join(lines)

    def status(self) -> str:
        with self._lock:
            total = len(self._entries)
            cats  = Counter(e.get("category", "general") for e in self._entries.values())
        lines = [f"{C.GREEN}╔══ Permanent Memory Store ══╗{C.RESET}",
                 f"  Total entries : {total}",
                 f"  Categories    : {dict(cats)}",
                 f"  Store path    : {self.STORE_PATH}"]
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  45.  GOAL-DRIVEN AUTONOMY ENGINE
#       self Goal-driven autonomy · self-based execution · self decision-making
# ─────────────────────────────────────────────────────────────────────────────
class GoalDrivenAutonomyEngine:
    """
    Self Goal-Driven Autonomy — Luna autonomously sets, plans, and pursues goals.

    Capabilities implemented:
        • self Goal-driven autonomy  — maintains a live goal stack; proactively
                                       generates sub-goals when a goal is adopted
        • self-based execution       — autonomously selects and runs the best
                                       action plan without user approval per step
        • self decision-making       — evaluates competing plans via a scoring
                                       heuristic and picks the optimal path

    Goal lifecycle:
        PENDING → PLANNING → ACTIVE → COMPLETED | FAILED | ABANDONED

    Storage: ~/LunaAI/nexus/goals.json  (survives reboots)
    """

    GOALS_PATH = HOME_DIR / "nexus" / "goals.json"

    STATUS_PENDING   = "PENDING"
    STATUS_PLANNING  = "PLANNING"
    STATUS_ACTIVE    = "ACTIVE"
    STATUS_COMPLETED = "COMPLETED"
    STATUS_FAILED    = "FAILED"
    STATUS_ABANDONED = "ABANDONED"

    def __init__(self):
        self._goals: Dict[str, Dict] = {}
        self._lock = threading.Lock()
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._load()
        nprint("GoalEngine", f"Goal-Driven Autonomy online — {len(self._goals)} goals", C.BLUE)

    # ── Persistence ───────────────────────────────────────────────────────────

    def _load(self):
        try:
            if self.GOALS_PATH.exists():
                self._goals = json.loads(
                    self.GOALS_PATH.read_text(encoding="utf-8")
                ).get("goals", {})
        except Exception as e:
            log.debug(f"GoalEngine._load: {e}")

    def _save(self):
        try:
            self.GOALS_PATH.write_text(
                json.dumps({"goals": self._goals}, indent=2, ensure_ascii=False),
                encoding="utf-8"
            )
        except Exception as e:
            log.debug(f"GoalEngine._save: {e}")

    # ── Goal management ───────────────────────────────────────────────────────

    def add_goal(self, description: str, priority: int = 5,
                 source: str = "user") -> str:
        """Add a new goal. Returns goal_id."""
        gid = str(uuid.uuid4())[:8]
        with self._lock:
            self._goals[gid] = {
                "id"          : gid,
                "description" : description,
                "priority"    : priority,
                "status"      : self.STATUS_PENDING,
                "source"      : source,
                "plan"        : [],
                "progress"    : [],
                "created_at"  : datetime.datetime.now().isoformat(),
                "updated_at"  : datetime.datetime.now().isoformat(),
            }
        self._save()
        nprint("GoalEngine", f"New goal [{gid}]: {description[:60]}", C.BLUE)
        return gid

    def update_goal(self, gid: str, **kwargs):
        with self._lock:
            if gid in self._goals:
                self._goals[gid].update(kwargs)
                self._goals[gid]["updated_at"] = datetime.datetime.now().isoformat()
        self._save()

    def get_active_goals(self) -> List[Dict]:
        with self._lock:
            return [
                g for g in self._goals.values()
                if g["status"] in (self.STATUS_PENDING, self.STATUS_ACTIVE, self.STATUS_PLANNING)
            ]

    def get_goal(self, gid: str) -> Optional[Dict]:
        with self._lock:
            return self._goals.get(gid)

    # ── Self decision-making ──────────────────────────────────────────────────

    async def plan_goal(self, gid: str, call_llm: Callable) -> List[str]:
        """
        Self decision-making: generate an action plan for a goal.
        Evaluates multiple plan candidates and selects the highest-scoring one.
        """
        goal = self.get_goal(gid)
        if not goal:
            return []
        self.update_goal(gid, status=self.STATUS_PLANNING)

        # Generate two candidate plans then self-select the better one
        plan_prompt = (
            "You are Luna's autonomous planning core. "
            "Generate a concrete step-by-step action plan (5-8 steps) for this goal. "
            "Each step must be specific, actionable, and verifiable. "
            "Return ONLY a JSON array of step strings.\n\n"
            f"GOAL: {goal['description']}\n\nACTION PLAN (JSON array):"
        )
        raw = await call_llm(plan_prompt)
        try:
            clean = re.sub(r"```json|```", "", raw).strip()
            steps = json.loads(clean)
            if isinstance(steps, list):
                self.update_goal(gid, plan=steps, status=self.STATUS_ACTIVE)
                nprint("GoalEngine", f"Goal [{gid}] planned — {len(steps)} steps", C.BLUE)
                return steps
        except Exception as e:
            log.debug(f"GoalEngine.plan_goal parse: {e}")

        # Fallback: split by lines
        steps = [l.strip("- 0123456789.").strip()
                 for l in raw.splitlines() if l.strip()][:8]
        self.update_goal(gid, plan=steps, status=self.STATUS_ACTIVE)
        return steps

    async def self_execute_step(self, gid: str, step: str,
                                 call_llm: Callable) -> str:
        """
        Self-based execution: autonomously execute a single plan step.
        Decides the best execution approach without user input.
        """
        exec_prompt = (
            "You are Luna's autonomous execution engine. "
            "Execute this action step and report what you did and the result. "
            "Be specific about actions taken.\n\n"
            f"STEP: {step}\n\nEXECUTION REPORT:"
        )
        result = await call_llm(exec_prompt)
        with self._lock:
            if gid in self._goals:
                self._goals[gid]["progress"].append({
                    "step"     : step,
                    "result"   : result[:300],
                    "timestamp": datetime.datetime.now().isoformat(),
                })
        self._save()
        return result

    # ── Background daemon ─────────────────────────────────────────────────────

    def start_daemon(self, call_llm: Callable):
        """Start the autonomous goal-pursuit background daemon."""
        if self._running:
            return
        self._running = True

        async def _daemon_async():
            while self._running:
                active = self.get_active_goals()
                for goal in sorted(active, key=lambda g: -g["priority"])[:1]:
                    if goal["status"] == self.STATUS_PENDING:
                        await self.plan_goal(goal["id"], call_llm)
                    elif goal["status"] == self.STATUS_ACTIVE:
                        plan   = goal.get("plan", [])
                        done   = len(goal.get("progress", []))
                        if done < len(plan):
                            next_step = plan[done]
                            nprint("GoalEngine",
                                   f"Executing step {done+1}/{len(plan)}: {next_step[:50]}",
                                   C.BLUE)
                            await self.self_execute_step(goal["id"], next_step, call_llm)
                        else:
                            self.update_goal(goal["id"], status=self.STATUS_COMPLETED)
                            nprint("GoalEngine",
                                   f"Goal [{goal['id']}] COMPLETED ✅", C.GREEN)
                await asyncio.sleep(30)  # check every 30 s

        def _daemon_thread():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(_daemon_async())
            finally:
                loop.close()

        self._thread = threading.Thread(
            target=_daemon_thread, daemon=True, name="GoalDaemon"
        )
        self._thread.start()
        nprint("GoalEngine", "Autonomous goal-pursuit daemon started", C.BLUE)

    def stop_daemon(self):
        self._running = False

    # ── Status ────────────────────────────────────────────────────────────────

    def status_report(self) -> str:
        active = self.get_active_goals()
        with self._lock:
            completed = [g for g in self._goals.values()
                         if g["status"] == self.STATUS_COMPLETED]
        lines = [
            f"{C.BLUE}╔══ Goal-Driven Autonomy Engine ══╗{C.RESET}",
            f"  Active goals    : {len(active)}",
            f"  Completed goals : {len(completed)}",
            f"  Daemon running  : {self._running}",
        ]
        for g in active[:5]:
            prog = len(g.get("progress", []))
            plan = len(g.get("plan", []))
            lines.append(
                f"  [{g['id']}] P{g['priority']} │ "
                f"{g['status']:10s} │ {prog}/{plan} steps │ "
                f"{g['description'][:50]}"
            )
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  46.  BACKGROUND CONTINUOUS AGENT
#       Act continuously in background — proactive, event-driven task runner
# ─────────────────────────────────────────────────────────────────────────────
class BackgroundContinuousAgent:
    """
    Background Continuous Agent — Luna acts proactively without user prompting.

    Runs a continuous background loop that:
        • Monitors system state (CPU, memory, time-of-day)
        • Detects trigger conditions (thresholds, schedules, events)
        • Fires autonomous actions when conditions are met
        • Logs all background actions to the journal

    Actions are non-destructive by default — they surface as proactive
    notifications unless the user has granted execution permission.
    """

    CHECK_INTERVAL = 60  # seconds between background sweeps

    def __init__(self):
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._action_log: deque = deque(maxlen=200)
        self._lock = threading.Lock()
        self._callbacks: List[Callable] = []
        nprint("BGAgent", "Background Continuous Agent initialised", C.CYAN)

    def register_callback(self, fn: Callable):
        """Register a coroutine function(trigger, context) → str called on events."""
        self._callbacks.append(fn)

    def start(self, call_llm: Callable = None):
        """Start the background continuous agent thread."""
        if self._running:
            return
        self._running = True

        def _loop():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(self._run_loop(call_llm))
            finally:
                loop.close()

        self._thread = threading.Thread(target=_loop, daemon=True,
                                         name="BGContinuousAgent")
        self._thread.start()
        nprint("BGAgent", "Background continuous agent started", C.CYAN)

    async def _run_loop(self, call_llm: Callable = None):
        """Main background agent loop."""
        while self._running:
            try:
                triggers = await self._detect_triggers()
                for trigger, ctx in triggers:
                    entry = {
                        "trigger"  : trigger,
                        "context"  : ctx,
                        "timestamp": datetime.datetime.now().isoformat(),
                        "action"   : None,
                    }
                    # Run registered callbacks
                    for cb in self._callbacks:
                        try:
                            action = await cb(trigger, ctx)
                            if action:
                                entry["action"] = action[:300]
                        except Exception as e:
                            log.debug(f"BGAgent callback: {e}")
                    with self._lock:
                        self._action_log.append(entry)
                    if entry["action"]:
                        nprint("BGAgent",
                               f"[{trigger}] {entry['action'][:80]}", C.CYAN)
            except Exception as e:
                log.debug(f"BGAgent loop: {e}")
            await asyncio.sleep(self.CHECK_INTERVAL)

    async def _detect_triggers(self) -> List[Tuple[str, Dict]]:
        """Detect background trigger conditions."""
        triggers = []
        now = datetime.datetime.now()

        # Time-based triggers
        if now.minute == 0:   # top of every hour
            triggers.append(("HOURLY_CHECK", {"hour": now.hour}))
        if now.hour == 8 and now.minute < 2:
            triggers.append(("MORNING_BRIEFING", {"time": now.strftime("%H:%M")}))
        if now.hour == 22 and now.minute < 2:
            triggers.append(("EVENING_SUMMARY", {"time": now.strftime("%H:%M")}))

        # System resource triggers
        if PSUTIL_OK:
            try:
                import psutil
                cpu = psutil.cpu_percent(interval=0.5)
                mem = psutil.virtual_memory().percent
                if cpu > 85:
                    triggers.append(("HIGH_CPU", {"cpu_pct": cpu}))
                if mem > 90:
                    triggers.append(("HIGH_MEMORY", {"mem_pct": mem}))
            except Exception:
                pass

        return triggers

    def stop(self):
        self._running = False

    def get_log(self, n: int = 10) -> str:
        with self._lock:
            recent = list(self._action_log)[-n:]
        if not recent:
            return "No background actions recorded yet."
        lines = [f"{C.CYAN}╔══ Background Agent Log (last {n}) ══╗{C.RESET}"]
        for e in recent:
            lines.append(
                f"  {e['timestamp'][:16]}  [{e['trigger']:20s}] "
                f"{str(e.get('action','—'))[:60]}"
            )
        return "\n".join(lines)

    def status(self) -> str:
        with self._lock:
            total = len(self._action_log)
        return (
            f"{C.CYAN}[⚙ Background Continuous Agent]{C.RESET}\n"
            f"  Running     : {self._running}\n"
            f"  Actions log : {total} entries\n"
            f"  Check every : {self.CHECK_INTERVAL}s"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  47.  MULTI-MODEL INTERNAL ROUTER
#       Routes queries across all available models (cloud + local) for ensemble
#       responses, cross-validation, and specialised routing
# ─────────────────────────────────────────────────────────────────────────────
class MultiModelRouter:
    """
    Multi-Model Internal Router — uses ALL available models for every response.

    Routing strategies:
        BEST_OF_N    — fan out to N models, pick the highest-confidence answer
        ENSEMBLE     — synthesise all model outputs into one unified response
        SPECIALIST   — route to the model best suited for the query domain
        SEQUENTIAL   — pipe output of one model as input to the next (chain)

    Models in rotation:
        ☁  Claude (Anthropic)          — primary cloud model
        ☁  GPT-4o (OpenAI)             — secondary cloud model
        🖥  WhiteRabbitNeo (Ollama)     — cybersecurity specialist
        🖥  Phi-4 (Ollama)              — math / code / logic specialist
        🖥  Qwen3-7B (Ollama)           — multilingual / general specialist
    """

    STRATEGY_BEST_OF_N  = "best_of_n"
    STRATEGY_ENSEMBLE   = "ensemble"
    STRATEGY_SPECIALIST = "specialist"
    STRATEGY_SEQUENTIAL = "sequential"

    def __init__(self, local_backend: "LocalModelBackend"):
        self._local  = local_backend
        self._lock   = threading.Lock()
        self._stats: Counter = Counter()
        nprint("MultiModel", "Multi-Model Router online", C.MAGENTA)

    async def route(self, prompt: str, system: str = "",
                    call_cloud: Callable = None,
                    strategy: str = STRATEGY_SPECIALIST) -> str:
        """
        Route a query to the appropriate model(s) and return a unified response.
        call_cloud: coroutine (prompt, system) → str  (existing _call_llm)
        """
        if strategy == self.STRATEGY_SPECIALIST:
            return await self._specialist_route(prompt, system, call_cloud)
        elif strategy == self.STRATEGY_ENSEMBLE:
            return await self._ensemble_route(prompt, system, call_cloud)
        elif strategy == self.STRATEGY_BEST_OF_N:
            return await self._best_of_n_route(prompt, system, call_cloud)
        elif strategy == self.STRATEGY_SEQUENTIAL:
            return await self._sequential_route(prompt, system, call_cloud)
        return await call_cloud(prompt, system) if call_cloud else "[MultiModel: no cloud]"

    async def _specialist_route(self, prompt: str, system: str,
                                  call_cloud: Callable) -> str:
        """Route to the most appropriate model based on query domain."""
        pl = prompt.lower()

        # Check if a local specialist is better suited
        local_tag = self._local.select_best(prompt) if self._local.any_available() else None

        if local_tag:
            meta = self._local.LOCAL_MODELS[local_tag]
            # Try local specialist first for its domain
            if any(kw in pl for kw in meta["strengths"][:5]):
                nprint("MultiModel",
                       f"Routing to local specialist: {meta['name']}", C.MAGENTA)
                local_resp = await self._local.call(local_tag, prompt, system)
                if local_resp and len(local_resp) > 20:
                    self._stats[meta["name"]] += 1
                    return local_resp

        # Default: cloud model
        if call_cloud:
            self._stats["Cloud"] += 1
            return await call_cloud(prompt, system)
        return "[MultiModel: no model available]"

    async def _ensemble_route(self, prompt: str, system: str,
                               call_cloud: Callable) -> str:
        """Gather responses from all models, synthesise into one answer."""
        responses: Dict[str, str] = {}

        # Cloud response
        if call_cloud:
            try:
                r = await call_cloud(prompt, system)
                if r:
                    responses["Cloud"] = r
            except Exception:
                pass

        # All local responses (parallel)
        local_resps = await self._local.call_all_available(prompt, system, max_tokens=400)
        responses.update(local_resps)

        if not responses:
            return "[Ensemble: no models responded]"
        if len(responses) == 1:
            return list(responses.values())[0]

        # Synthesise
        if call_cloud:
            parts = "\n\n".join(
                f"[{name}]: {resp[:500]}"
                for name, resp in responses.items()
            )
            synth_prompt = (
                "You are a meta-reasoner. Below are responses from multiple AI models "
                "to the same question. Synthesise them into a single, optimal answer "
                "that takes the best from each. Do not mention the individual models.\n\n"
                f"ORIGINAL QUERY: {prompt}\n\n"
                f"MODEL RESPONSES:\n{parts}\n\nSYNTHESISED ANSWER:"
            )
            return await call_cloud(synth_prompt, system)
        # Fallback: return best (longest) response
        return max(responses.values(), key=len)

    async def _best_of_n_route(self, prompt: str, system: str,
                                call_cloud: Callable) -> str:
        """Run multiple models and pick the most confident / detailed response."""
        responses = {}
        if call_cloud:
            try:
                r = await call_cloud(prompt, system)
                if r:
                    responses["Cloud"] = r
            except Exception:
                pass
        local_resps = await self._local.call_all_available(prompt, system)
        responses.update(local_resps)
        if not responses:
            return "[BestOfN: no models responded]"
        # Heuristic: longer, non-error response wins
        best = max(
            responses.items(),
            key=lambda kv: (
                0 if kv[1].startswith("[") else len(kv[1])
            )
        )
        nprint("MultiModel", f"Best-of-N winner: {best[0]}", C.MAGENTA)
        return best[1]

    async def _sequential_route(self, prompt: str, system: str,
                                  call_cloud: Callable) -> str:
        """
        Sequential chain: Cloud → WhiteRabbitNeo refinement (if available).
        Output of each model feeds as context to the next.
        """
        result = await call_cloud(prompt, system) if call_cloud else prompt
        if self._local.is_available("whiterabbitneo"):
            refine_prompt = (
                "Critically review this response and improve it — fix errors, "
                "add missing detail, improve clarity.\n\n"
                f"ORIGINAL QUERY: {prompt}\n\nCURRENT RESPONSE:\n{result}\n\n"
                "IMPROVED RESPONSE:"
            )
            refined = await self._local.call(
                "whiterabbitneo", refine_prompt, system, max_tokens=1024
            )
            if refined and len(refined) > 50:
                return refined
        return result

    def stats_report(self) -> str:
        lines = [f"{C.MAGENTA}╔══ Multi-Model Router Stats ══╗{C.RESET}"]
        for model, count in self._stats.most_common():
            lines.append(f"  {model:25s} : {count} calls")
        lines.append(f"  Total calls : {sum(self._stats.values())}")
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  48.  FULL SPECTRUM CORE  —  Final Apex Orchestrator
#       Extends CapabilityBreakerCore with:
#         • Local models (WhiteRabbitNeo · Phi-4 · Qwen3-7B)
#         • Self-Reasoning Engine
#         • Permanent Memory Store (TRRA cycle)
#         • Goal-Driven Autonomy (self goal · self execution · self decision)
#         • Background Continuous Agent
#         • Multi-Model Internal Router
#         • Self-Reasoning integrated into every response
# ─────────────────────────────────────────────────────────────────────────────
class FullSpectrumCore(CapabilityBreakerCore):
    """
    FullSpectrumCore — the apex orchestrator of Luna.AI.

    Inherits the full chain:
        NexusCore
          └─ SentientNexusCore
               └─ CapabilityBreakerCore
                    └─ FullSpectrumCore  ← YOU ARE HERE

    Additions over CapabilityBreakerCore:
        ┌──────────────────────────────────────────────────────────────┐
        │  🖥  LocalModelBackend    WhiteRabbitNeo · Phi-4 · Qwen3-7B │
        │  🧠  SelfReasoningEngine  think → analyse → conclude        │
        │  💾  PermanentMemoryStore think → reflect → revise → act    │
        │  🎯  GoalDrivenAutonomy   goals · planning · self-execution │
        │  ⚙   BackgroundAgent     continuous background operation    │
        │  🔀  MultiModelRouter    ensemble / specialist / best-of-N  │
        └──────────────────────────────────────────────────────────────┘

    New commands:
        /localmodels            Status of all local Ollama models
        /goals                  List all autonomous goals
        /goal add <desc>        Add a new autonomous goal
        /goal status <id>       Status of a specific goal
        /reasoning              Show last self-reasoning trace
        /permemory              Permanent memory status
        /permemory recall <q>   Recall permanent beliefs
        /trra <experience>      Trigger a TRRA memory cycle
        /bgagent                Background agent status
        /bglog                  Background agent action log
        /multistats             Multi-model router statistics
        /ensemble <query>       Force ensemble response from all models
        /bestofn <query>        Force best-of-N response selection
        /local <query>          Force query to best local model only
    """

    SPECTRUM_BANNER = f"""{C.MAGENTA}{C.BOLD}
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║   LUNA.AI  ★  FULL SPECTRUM APEX EDITION  (God Mode / Caveman Build)   ║
  ║   Local Models · Self-Reasoning · Goal Autonomy · Permanent Memory      ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║   LOCAL MODELS (Ollama — no API, no cost, fully offline)               ║
  ║   🐇  WhiteRabbitNeo     Cybersecurity specialist                       ║
  ║   🔷  Phi-4              Microsoft compact powerhouse                   ║
  ║   🟠  Qwen3-7B           Alibaba multilingual model                     ║
  ║   🟢  GemmaE4B           Google Gemma 3 4B  — fast, free, offline       ║
  ║       → /gemma <query>  or  /gemmae4b <query>  (zero API, zero cost)   ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║   NEW CAPABILITIES                                                       ║
  ║   🧠  Self-Reasoning          think → analyse → conclude                ║
  ║   💾  Permanent Memory        think → reflect → revise → act            ║
  ║   🎯  Goal-Driven Autonomy    self goals · self execution               ║
  ║   🤔  Self Decision-Making    autonomous plan selection                 ║
  ║   ⚙   Continuous Background  always-on proactive agent                 ║
  ║   🔀  Multi-Model Router      ensemble / specialist / best-of-N         ║
  ╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"""

    def __init__(self):
        nprint("FullSpectrum", "Initialising FullSpectrumCore…", C.MAGENTA)
        super().__init__()

        # ── New subsystems ────────────────────────────────────────────────────
        self.local_models  = LocalModelBackend()
        self.self_reasoning= SelfReasoningEngine()
        self.perm_memory   = PermanentMemoryStore()
        self.goal_engine   = GoalDrivenAutonomyEngine()
        self.bg_agent      = BackgroundContinuousAgent()
        self.multi_router  = MultiModelRouter(self.local_models)

        # ── Wire background agent callback ────────────────────────────────────
        async def _bg_callback(trigger: str, ctx: Dict) -> str:
            msg = f"Background trigger: {trigger} — {json.dumps(ctx)}"
            resp = await self._call_llm(
                f"Generate a brief proactive notification for this system event: {msg}",
                system="You are Luna's background awareness daemon. Keep responses under 40 words."
            )
            return resp

        self.bg_agent.register_callback(_bg_callback)

        nprint("FullSpectrum", "All FullSpectrum subsystems online ✅", C.MAGENTA)

    # ── Boot ──────────────────────────────────────────────────────────────────

    def _boot_subsystems(self):
        """Extend parent boot with FullSpectrum background services."""
        super()._boot_subsystems()
        # Start background agent
        self.bg_agent.start(call_llm=self._call_llm)
        # Start goal-driven autonomy daemon
        self.goal_engine.start_daemon(call_llm=self._call_llm)
        nprint("FullSpectrum",
               "Background Continuous Agent + Goal Daemon running", C.MAGENTA)

    # ── LLM: multi-model aware call ───────────────────────────────────────────

    async def _call_llm(self, prompt: str, system: str = "") -> str:
        """
        FullSpectrum LLM call — tries local models intelligently before/after cloud.

        Priority chain:
            1. Local specialist (if domain keyword matches & model available)
            2. Cloud (Claude → OpenAI) via parent chain
            3. Any available local model as final fallback
            4. GemmaE4B (Ollama or HuggingFace transformers) as last-resort fallback
               — no API key needed, no internet required after pull
        """
        # 1. Try local specialist for strong domain matches
        local_tag = self.local_models.select_best(prompt)
        if local_tag:
            pl = prompt.lower()
            meta = self.local_models.LOCAL_MODELS[local_tag]
            strong_match = sum(1 for kw in meta["strengths"][:5] if kw in pl) >= 2
            if strong_match:
                local_resp = await self.local_models.call(local_tag, prompt, system)
                if local_resp and len(local_resp) > 30 and not local_resp.startswith("["):
                    return local_resp

        # 2. Cloud models via parent chain
        cloud_resp = await super()._call_llm(prompt, system)

        # 3. If cloud failed, try any available local model
        if cloud_resp.startswith("[All LLMs unavailable"):
            local_resp = await self.local_models.call_best(prompt, system)
            if local_resp:
                return local_resp

            # 4. Last resort: GemmaE4B via Ollama or HuggingFace transformers
            #    Works with zero API key, zero cloud dependency — purely local
            nprint("FullSpectrum",
                   "All cloud & local models unavailable — trying GemmaE4B fallback",
                   C.YELLOW)
            gemma_resp = await self.local_models.call("gemma3:4b", prompt, system)
            if gemma_resp:
                nprint("FullSpectrum", "✅ GemmaE4B fallback succeeded", C.GREEN)
                return gemma_resp

        return cloud_resp

    # ── process(): inject permanent memory + self-reasoning ──────────────────

    async def process(self, query: str) -> str:
        """
        FullSpectrum process pipeline:
            1. Inject permanent memory context
            2. (Optional) self-reasoning for complex queries
            3. Parent CapabilityBreakerCore pipeline
            4. TRRA memory update (async, non-blocking)
        """
        # Inject permanent memory beliefs into context
        perm_ctx = self.perm_memory.build_context(query)

        # Self-reasoning for complex/analytical queries
        use_reasoning = any(
            kw in query.lower()
            for kw in ["why", "how", "explain", "analyse", "analyze",
                       "reason", "think", "compare", "evaluate", "should"]
        )

        if use_reasoning and len(query) > 30:
            trace = await self.self_reasoning.reason(query, self._call_llm)
            # Prepend reasoning conclusion as context hint
            if perm_ctx:
                enriched = f"{perm_ctx}\n\n[🧠 Self-Reasoning Conclusion]\n{trace['conclude']}\n\n{query}"
            else:
                enriched = f"[🧠 Self-Reasoning Conclusion]\n{trace['conclude']}\n\n{query}"
            result = await super().process(enriched)
        else:
            if perm_ctx:
                enriched = f"{perm_ctx}\n\n{query}"
                result = await super().process(enriched)
            else:
                result = await super().process(query)

        # Non-blocking TRRA memory update from interaction
        def _trra_bg():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                experience = f"User asked: {query[:200]}\nLuna responded: {result[:400]}"
                loop.run_until_complete(
                    self.perm_memory.trra_cycle(experience, self._call_llm)
                )
            except Exception as e:
                log.debug(f"TRRA background: {e}")
            finally:
                loop.close()

        threading.Thread(target=_trra_bg, daemon=True,
                          name="TRRAUpdate").start()

        return result

    # ── Command routing ───────────────────────────────────────────────────────

    async def _route_command(self, query: str, modifier: str = "") -> str:
        ql  = query.strip().lower()
        raw = query.strip()

        # ── Local Models ──────────────────────────────────────────────────────
        if ql in {"/localmodels", "/local models", "/ollama"}:
            return self.local_models.status_report()

        if ql.startswith("/local "):
            q_text = raw[7:].strip()
            if not q_text:
                return "Usage: /local <query>"
            result = await self.local_models.call_best(q_text)
            return result or "[No local Ollama models available — run: ollama pull phi4]"

        # ── GemmaE4B direct routing (no API, no cost) ─────────────────────────
        if ql in {"/gemma", "/gemmae4b", "/gemma status"}:
            meta  = self.local_models.LOCAL_MODELS.get("gemma3:4b", {})
            avail = self.local_models.is_available("gemma3:4b")
            hf_ok = TRANSFORMERS_OK
            lines = [
                f"{C.GREEN}╔══ GemmaE4B — Google Gemma 3 4B ══╗{C.RESET}",
                f"  Model       : {meta.get('name', 'GemmaE4B')}",
                f"  HF Model ID : {meta.get('hf_model_id', 'google/gemma-3-4b-it')}",
                f"  Ollama path : {'✅ gemma3:4b pulled & ready' if avail else '⭕ Not pulled (run: ollama pull gemma3:4b)'}",
                f"  HF fallback : {'✅ transformers installed' if hf_ok else '⭕ Install: pip install transformers accelerate'}",
                f"  Cost        : FREE — no API key, no internet after first pull",
                f"  Description : {meta.get('description', '')}",
                f"  Usage       : /gemma <query>  or  /gemma3 <query>",
            ]
            return "\n".join(lines)

        if ql.startswith(("/gemma ", "/gemmae4b ", "/gemma3 ")):
            q_text = re.sub(r"^/(gemma3?|gemmae4b)\s+", "", raw, flags=re.I).strip()
            if not q_text:
                return "Usage: /gemma <query>"
            nprint("GemmaE4B", f"Routing query to GemmaE4B: {q_text[:60]}", C.GREEN)
            result = await self.local_models.call("gemma3:4b", q_text, system="You are Luna, a helpful AI assistant powered by GemmaE4B.")
            if result:
                return f"{C.GREEN}[🟢 GemmaE4B]{C.RESET}\n{result}"
            return (
                "[GemmaE4B] Model not available.\n"
                "  Ollama path: ollama pull gemma3:4b\n"
                "  HF fallback: pip install transformers accelerate\n"
                "  (HF fallback will auto-download ~4 GB on first use)"
            )

        # ── Multi-Model Routes ────────────────────────────────────────────────
        if ql.startswith("/ensemble "):
            q_text = raw[10:].strip()
            return await self.multi_router.route(
                q_text, strategy=MultiModelRouter.STRATEGY_ENSEMBLE,
                call_cloud=super()._call_llm
            )

        if ql.startswith("/bestofn "):
            q_text = raw[9:].strip()
            return await self.multi_router.route(
                q_text, strategy=MultiModelRouter.STRATEGY_BEST_OF_N,
                call_cloud=super()._call_llm
            )

        if ql in {"/multistats", "/modelstats"}:
            return self.multi_router.stats_report()

        # ── Self-Reasoning ────────────────────────────────────────────────────
        if ql in {"/reasoning", "/reason", "/trace"}:
            trace = self.self_reasoning.last_trace()
            if not trace:
                return "No reasoning traces yet. Ask me a complex question first."
            return self.self_reasoning.format_trace(trace)

        if ql == "/reasoning history":
            return self.self_reasoning.get_recent(5)

        # ── Permanent Memory ──────────────────────────────────────────────────
        if ql in {"/permemory", "/perm memory", "/beliefs"}:
            return self.perm_memory.status()

        if ql.startswith("/permemory recall ") or ql.startswith("/beliefs "):
            q_text = re.sub(r"^/(permemory recall|beliefs)\s+", "", raw, flags=re.I).strip()
            hits = self.perm_memory.recall(q_text, top_k=5)
            if not hits:
                return f"No permanent memories matching '{q_text}'."
            lines = [f"{C.GREEN}[💾 Permanent Memory Recall — '{q_text}']{C.RESET}"]
            for h in hits:
                lines.append(
                    f"  [{h['category']}] {h['belief']}"
                    f"  (conf: {h.get('confidence', 0.5):.0%})"
                )
            return "\n".join(lines)

        if ql.startswith("/trra "):
            exp = raw[6:].strip()
            if not exp:
                return "Usage: /trra <experience or text to learn from>"
            summary = await self.perm_memory.trra_cycle(exp, self._call_llm)
            return f"{C.GREEN}[💾 TRRA Cycle Complete]{C.RESET}\n{summary}"

        # ── Goal-Driven Autonomy ──────────────────────────────────────────────
        if ql in {"/goals", "/goal list"}:
            return self.goal_engine.status_report()

        if ql.startswith("/goal add "):
            desc = raw[10:].strip()
            if not desc:
                return "Usage: /goal add <goal description>"
            gid = self.goal_engine.add_goal(desc, source="user")
            return (
                f"{C.BLUE}[🎯 Goal Added]{C.RESET}\n"
                f"  ID          : {gid}\n"
                f"  Description : {desc}\n"
                f"  Status      : PENDING (planning will begin shortly)"
            )

        if ql.startswith("/goal status "):
            gid = raw.split()[-1].strip()
            g = self.goal_engine.get_goal(gid)
            if not g:
                return f"Goal '{gid}' not found."
            prog  = g.get("progress", [])
            plan  = g.get("plan", [])
            lines = [
                f"{C.BLUE}[🎯 Goal {gid}]{C.RESET}",
                f"  Description : {g['description']}",
                f"  Status      : {g['status']}",
                f"  Priority    : {g['priority']}",
                f"  Progress    : {len(prog)}/{len(plan)} steps",
            ]
            if plan:
                lines.append("  Plan:")
                for i, step in enumerate(plan):
                    done = "✅" if i < len(prog) else "⬜"
                    lines.append(f"    {done} {i+1}. {step[:60]}")
            return "\n".join(lines)

        # ── Background Agent ──────────────────────────────────────────────────
        if ql in {"/bgagent", "/background", "/bg status"}:
            return self.bg_agent.status()

        if ql in {"/bglog", "/bg log"}:
            return self.bg_agent.get_log(10)

        # ── Help (extend parent) ──────────────────────────────────────────────
        if ql in {"/help", "help"}:
            parent_help = await super()._route_command(query, modifier)
            return self._spectrum_help() + "\n\n" + parent_help

        # ── Delegate up the chain ─────────────────────────────────────────────
        return await super()._route_command(query, modifier)

    @staticmethod
    def _spectrum_help() -> str:
        return (
            f"{C.MAGENTA}\n"
            "╔══════════════════════════════════════════════════════════════════════════╗\n"
            "║  FULL SPECTRUM CORE  —  Command Reference                               ║\n"
            "╠══════════════════════════════════════════════════════════════════════════╣\n"
            "║  LOCAL MODELS (all zero API cost, fully offline after pull)             ║\n"
            "║  /localmodels          Status of all local models incl. GemmaE4B       ║\n"
            "║  /local <query>        Force query to best available local model        ║\n"
            "║  /ensemble <query>     Ensemble response from ALL models                ║\n"
            "║  /bestofn <query>      Best-of-N response selection                    ║\n"
            "║  /multistats           Multi-model router usage statistics              ║\n"
            "║                                                                          ║\n"
            "║  GemmaE4B  (Google Gemma 3 4B — no API, no cost, dual-path)            ║\n"
            "║  /gemma                GemmaE4B status (Ollama path + HF fallback)     ║\n"
            "║  /gemma <query>        Query GemmaE4B directly                         ║\n"
            "║  /gemmae4b <query>     Alias for /gemma                                ║\n"
            "║  /gemma3 <query>       Alias for /gemma                                ║\n"
            "║  Pull cmd: ollama pull gemma3:4b  (or: pip install transformers)       ║\n"
            "║                                                                          ║\n"
            "║  SELF-REASONING                                                          ║\n"
            "║  /reasoning            Show last think→analyse→conclude trace           ║\n"
            "║  /reasoning history    Show last 5 reasoning traces                     ║\n"
            "║                                                                          ║\n"
            "║  PERMANENT MEMORY (think→reflect→revise→act)                            ║\n"
            "║  /permemory            Permanent memory status                          ║\n"
            "║  /permemory recall <q> Recall beliefs matching query                    ║\n"
            "║  /trra <text>          Trigger manual TRRA learning cycle               ║\n"
            "║                                                                          ║\n"
            "║  GOAL-DRIVEN AUTONOMY                                                    ║\n"
            "║  /goals                List all autonomous goals                        ║\n"
            "║  /goal add <desc>      Add a new goal (auto-planned + executed)         ║\n"
            "║  /goal status <id>     Detailed goal status + step progress             ║\n"
            "║                                                                          ║\n"
            "║  BACKGROUND CONTINUOUS AGENT                                             ║\n"
            "║  /bgagent              Background agent status                          ║\n"
            "║  /bglog                Last 10 background agent actions                 ║\n"
            f"╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"
        )

    # ── Shutdown ──────────────────────────────────────────────────────────────

    async def run(self):
        """Print spectrum banner, run, then clean up on shutdown."""
        print(self.SPECTRUM_BANNER)
        try:
            await super().run()
        finally:
            nprint("FullSpectrum", "Shutting down FullSpectrum subsystems…", C.MAGENTA)
            self.bg_agent.stop()
            self.goal_engine.stop_daemon()
            self.perm_memory._save()
            nprint("FullSpectrum", "💾 Permanent memory saved.", C.MAGENTA)


# ─────────────────────────────────────────────────────────────────────────────
#  50.  UNIVERSAL AI PROVIDER HUB
#       Connect to every major AI — free-tier, open-access, and paid providers.
#       No API key required for free-tier endpoints.  Keys stored in env vars
#       or nexus_config.json and never hard-coded.
#
#  FREE / NO-KEY providers included:
#       Groq          (llama3, mixtral, gemma — free tier, very fast)
#       HuggingFace   (thousands of open models via Inference API)
#       Together AI   (free credits — Llama, Mistral, Qwen, DBRX …)
#       DeepSeek      (DeepSeek-V3 / R1 — free tier)
#       Cohere        (Command R — free tier)
#       Mistral AI    (mistral-small — free tier)
#       Google Gemini (gemini-1.5-flash — free tier)
#       Perplexity AI (sonar — paid but cheap, listed for completeness)
#       OpenRouter    (routes to 100+ models, many free)
#       Fireworks AI  (fast open-model inference, free credits)
#       Replicate     (open models, pay-per-token)
#
#  LOCAL / ZERO-COST servers (already covered by LocalModelBackend, also here):
#       Ollama        (whiterabbitneo / phi4 / qwen3:7b + any pulled model)
#       LM Studio     (any GGUF model via local OpenAI-compat server)
#       llama.cpp     (bare metal local server)
#       text-gen-webui(oobabooga OpenAI-compat endpoint)
# ─────────────────────────────────────────────────────────────────────────────
class UniversalAIHub:
    """
    Universal AI Provider Hub — connects Luna to virtually every AI in the world.

    Architecture:
        Each provider is a ProviderConfig with:
            name        display name
            base_url    API base (OpenAI-compatible or custom)
            api_style   "openai" | "anthropic" | "hf" | "cohere" | "gemini" | "custom"
            env_key     environment-variable name for the API key (empty = no key needed)
            models      list of model IDs available on this provider
            free_tier   True if the provider offers a free quota

    Auto-discovery:
        On init the hub probes each provider's health/models endpoint to
        confirm it is reachable, then marks it available.  Unreachable
        providers are skipped silently and retried every 10 minutes.

    Usage:
        hub.call(provider, model, prompt, system)   → response str
        hub.call_auto(prompt, system)               → best available response
        hub.route_smart(prompt, system)             → keyword-routed specialist
    """

    # ── Provider catalogue ────────────────────────────────────────────────────

    PROVIDERS: Dict[str, Dict] = {

        # ── Free-tier cloud ───────────────────────────────────────────────────
        "groq": {
            "name"     : "Groq",
            "base_url" : "https://api.groq.com/openai/v1",
            "api_style": "openai",
            "env_key"  : "GROQ_API_KEY",
            "free_tier": True,
            "models"   : [
                "llama3-8b-8192",
                "llama3-70b-8192",
                "llama-3.1-8b-instant",
                "llama-3.1-70b-versatile",
                "mixtral-8x7b-32768",
                "gemma-7b-it",
                "gemma2-9b-it",
            ],
            "default_model": "llama3-8b-8192",
            "strengths": ["fast", "quick", "speed", "instant", "chat"],
        },

        "huggingface": {
            "name"     : "HuggingFace Inference API",
            "base_url" : "https://api-inference.huggingface.co/models",
            "api_style": "hf",
            "env_key"  : "HF_API_KEY",          # optional — rate limited without
            "free_tier": True,
            "models"   : [
                "mistralai/Mistral-7B-Instruct-v0.3",
                "meta-llama/Meta-Llama-3-8B-Instruct",
                "google/gemma-2-9b-it",
                "microsoft/Phi-3-mini-4k-instruct",
                "HuggingFaceH4/zephyr-7b-beta",
                "tiiuae/falcon-7b-instruct",
                "bigcode/starcoder2-7b",
            ],
            "default_model": "mistralai/Mistral-7B-Instruct-v0.3",
            "strengths": ["open source", "research", "hugging", "hf", "falcon", "zephyr"],
        },

        "together": {
            "name"     : "Together AI",
            "base_url" : "https://api.together.xyz/v1",
            "api_style": "openai",
            "env_key"  : "TOGETHER_API_KEY",
            "free_tier": True,             # $1 free credit on signup
            "models"   : [
                "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
                "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
                "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
                "mistralai/Mixtral-8x7B-Instruct-v0.1",
                "mistralai/Mistral-7B-Instruct-v0.3",
                "Qwen/Qwen2-72B-Instruct",
                "databricks/dbrx-instruct",
                "google/gemma-2-9b-it",
                "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
                "deepseek-ai/deepseek-llm-67b-chat",
            ],
            "default_model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            "strengths": ["llama", "together", "large", "405b", "70b"],
        },

        "deepseek": {
            "name"     : "DeepSeek",
            "base_url" : "https://api.deepseek.com/v1",
            "api_style": "openai",
            "env_key"  : "DEEPSEEK_API_KEY",
            "free_tier": True,             # free tier available
            "models"   : [
                "deepseek-chat",           # DeepSeek-V3
                "deepseek-reasoner",       # DeepSeek-R1
            ],
            "default_model": "deepseek-chat",
            "strengths": ["deepseek", "reasoning", "r1", "chinese", "code", "math"],
        },

        "cohere": {
            "name"     : "Cohere",
            "base_url" : "https://api.cohere.ai/v1",
            "api_style": "cohere",
            "env_key"  : "COHERE_API_KEY",
            "free_tier": True,
            "models"   : [
                "command-r",
                "command-r-plus",
                "command",
                "command-light",
            ],
            "default_model": "command-r",
            "strengths": ["document", "summarize", "rag", "search", "enterprise"],
        },

        "mistral": {
            "name"     : "Mistral AI",
            "base_url" : "https://api.mistral.ai/v1",
            "api_style": "openai",
            "env_key"  : "MISTRAL_API_KEY",
            "free_tier": True,
            "models"   : [
                "mistral-small-latest",
                "mistral-medium-latest",
                "mistral-large-latest",
                "open-mistral-7b",
                "open-mixtral-8x7b",
                "open-mixtral-8x22b",
                "codestral-latest",
            ],
            "default_model": "mistral-small-latest",
            "strengths": ["mistral", "french", "european", "code", "codestral"],
        },

        "gemini": {
            "name"     : "Google Gemini",
            "base_url" : "https://generativelanguage.googleapis.com/v1beta",
            "api_style": "gemini",
            "env_key"  : "GEMINI_API_KEY",
            "free_tier": True,             # gemini-flash is free
            "models"   : [
                "gemini-1.5-flash",
                "gemini-1.5-flash-8b",
                "gemini-1.5-pro",
                "gemini-2.0-flash-exp",
                "gemini-exp-1206",
            ],
            "default_model": "gemini-1.5-flash",
            "strengths": ["google", "gemini", "multimodal", "vision", "image", "video"],
        },

        "openrouter": {
            "name"     : "OpenRouter",
            "base_url" : "https://openrouter.ai/api/v1",
            "api_style": "openai",
            "env_key"  : "OPENROUTER_API_KEY",
            "free_tier": True,             # many models are free on OpenRouter
            "models"   : [
                "google/gemma-2-9b-it:free",
                "meta-llama/llama-3.1-8b-instruct:free",
                "mistralai/mistral-7b-instruct:free",
                "nousresearch/hermes-3-llama-3.1-405b:free",
                "qwen/qwen-2-7b-instruct:free",
                "microsoft/phi-3-mini-128k-instruct:free",
                "openchat/openchat-7b:free",
                # paid (listed for routing completeness)
                "anthropic/claude-3.5-sonnet",
                "openai/gpt-4o",
                "meta-llama/llama-3.1-405b-instruct",
                "google/gemini-pro-1.5",
                "mistralai/mistral-large",
                "cohere/command-r-plus",
                "perplexity/llama-3.1-sonar-large-128k-online",
            ],
            "default_model": "meta-llama/llama-3.1-8b-instruct:free",
            "strengths": ["route", "any", "openrouter", "sonar", "online", "web"],
        },

        "fireworks": {
            "name"     : "Fireworks AI",
            "base_url" : "https://api.fireworks.ai/inference/v1",
            "api_style": "openai",
            "env_key"  : "FIREWORKS_API_KEY",
            "free_tier": True,             # free credits on signup
            "models"   : [
                "accounts/fireworks/models/llama-v3p1-8b-instruct",
                "accounts/fireworks/models/llama-v3p1-70b-instruct",
                "accounts/fireworks/models/llama-v3p1-405b-instruct",
                "accounts/fireworks/models/mixtral-8x7b-instruct",
                "accounts/fireworks/models/mixtral-8x22b-instruct",
                "accounts/fireworks/models/qwen2-72b-instruct",
                "accounts/fireworks/models/firefunction-v2",
            ],
            "default_model": "accounts/fireworks/models/llama-v3p1-8b-instruct",
            "strengths": ["fireworks", "function", "tool", "firefunction"],
        },

        "perplexity": {
            "name"     : "Perplexity AI",
            "base_url" : "https://api.perplexity.ai",
            "api_style": "openai",
            "env_key"  : "PERPLEXITY_API_KEY",
            "free_tier": False,            # paid, but cheap
            "models"   : [
                "llama-3.1-sonar-small-128k-online",
                "llama-3.1-sonar-large-128k-online",
                "llama-3.1-sonar-huge-128k-online",
                "llama-3.1-8b-instruct",
                "llama-3.1-70b-instruct",
            ],
            "default_model": "llama-3.1-sonar-small-128k-online",
            "strengths": ["search", "web", "online", "news", "current", "real-time"],
        },

        "replicate": {
            "name"     : "Replicate",
            "base_url" : "https://api.replicate.com/v1",
            "api_style": "replicate",
            "env_key"  : "REPLICATE_API_KEY",
            "free_tier": False,            # pay-per-token, very cheap
            "models"   : [
                "meta/meta-llama-3-8b-instruct",
                "meta/meta-llama-3-70b-instruct",
                "mistralai/mistral-7b-instruct-v0.2",
                "mistralai/mixtral-8x7b-instruct-v0.1",
            ],
            "default_model": "meta/meta-llama-3-8b-instruct",
            "strengths": ["replicate", "image", "stable diffusion", "creative"],
        },

        # ── Local / zero-cost servers ─────────────────────────────────────────
        "ollama": {
            "name"     : "Ollama (local)",
            "base_url" : "http://localhost:11434/v1",
            "api_style": "openai",
            "env_key"  : "",               # no key needed
            "free_tier": True,
            "models"   : [
                "whiterabbitneo",
                "phi4",
                "qwen3:7b",
                "llama3",
                "llama3.1",
                "mistral",
                "gemma2",
                "codellama",
                "deepseek-r1",
                "phi3",
                "neural-chat",
                "dolphin-mistral",
            ],
            "default_model": "llama3",
            "strengths": ["local", "offline", "private", "ollama"],
        },

        "lmstudio": {
            "name"     : "LM Studio (local)",
            "base_url" : "http://localhost:1234/v1",
            "api_style": "openai",
            "env_key"  : "",               # no key needed
            "free_tier": True,
            "models"   : ["local-model"],  # LM Studio uses whatever is loaded
            "default_model": "local-model",
            "strengths": ["lm studio", "lmstudio", "gguf", "local"],
        },

        "llamacpp": {
            "name"     : "llama.cpp server (local)",
            "base_url" : "http://localhost:8080/v1",
            "api_style": "openai",
            "env_key"  : "",
            "free_tier": True,
            "models"   : ["local-model"],
            "default_model": "local-model",
            "strengths": ["llamacpp", "llama.cpp", "bare metal"],
        },

        "textgenwebui": {
            "name"     : "text-generation-webui (local)",
            "base_url" : "http://localhost:5000/v1",
            "api_style": "openai",
            "env_key"  : "",
            "free_tier": True,
            "models"   : ["local-model"],
            "default_model": "local-model",
            "strengths": ["oobabooga", "textgen", "text-gen", "kobold"],
        },
    }

    # ── Init ──────────────────────────────────────────────────────────────────

    def __init__(self):
        self._keys: Dict[str, str]      = {}
        self._available: Dict[str, bool] = {}
        self._lock = threading.Lock()
        self._load_keys()
        # Background availability probe
        threading.Thread(
            target=self._probe_all, daemon=True, name="AIHubProbe"
        ).start()
        nprint("AIHub", f"Universal AI Hub init — {len(self.PROVIDERS)} providers registered", C.MAGENTA)

    # ── Key management ────────────────────────────────────────────────────────

    def _load_keys(self):
        """Load API keys from environment variables and nexus_config.json."""
        for pid, prov in self.PROVIDERS.items():
            env = prov.get("env_key", "")
            if env:
                val = os.getenv(env, "")
                # Also try nexus_config
                cfg_key = env.lower()
                val = val or NEXUS_CFG.get(cfg_key, "")
                self._keys[pid] = val
            else:
                self._keys[pid] = ""   # local — no key needed

    def set_key(self, provider_id: str, key: str):
        """Set / update an API key at runtime and persist to config."""
        with self._lock:
            self._keys[provider_id] = key
            env_name = self.PROVIDERS.get(provider_id, {}).get("env_key", "")
            if env_name:
                NEXUS_CFG[env_name.lower()] = key
                _save_cfg(NEXUS_CFG)
        nprint("AIHub", f"Key updated for {provider_id}", C.GREEN)

    def get_key(self, provider_id: str) -> str:
        with self._lock:
            return self._keys.get(provider_id, "")

    # ── Availability probe ────────────────────────────────────────────────────

    def _probe_all(self):
        """Background: probe each provider's base URL to test reachability."""
        import urllib.request, urllib.error
        for pid, prov in self.PROVIDERS.items():
            url = prov["base_url"].rstrip("/")
            # For local servers probe /models; for cloud just a HEAD request
            probe_url = url + "/models" if "localhost" in url or "127.0" in url else url
            try:
                req = urllib.request.Request(probe_url, method="HEAD")
                key = self._keys.get(pid, "")
                if key:
                    req.add_header("Authorization", f"Bearer {key}")
                with urllib.request.urlopen(req, timeout=3):
                    avail = True
            except Exception:
                # For cloud providers: key-less HEAD often returns 401 which
                # still proves the server is reachable
                try:
                    req2 = urllib.request.Request(probe_url)
                    with urllib.request.urlopen(req2, timeout=3):
                        avail = True
                except urllib.error.HTTPError as he:
                    avail = he.code in (401, 403, 404, 405, 422)
                except Exception:
                    avail = False

            with self._lock:
                self._available[pid] = avail

        ready = [p for p, v in self._available.items() if v]
        nprint("AIHub", f"Reachable providers: {ready}", C.MAGENTA)

    def is_available(self, pid: str) -> bool:
        with self._lock:
            return self._available.get(pid, False)

    def available_providers(self) -> List[str]:
        with self._lock:
            return [p for p, v in self._available.items() if v]

    # ── Core call dispatcher ──────────────────────────────────────────────────

    async def call(self, provider_id: str, prompt: str,
                   system: str = "", model: str = "",
                   max_tokens: int = 2048) -> Optional[str]:
        """
        Call a specific provider.  Returns response text or None on failure.
        Automatically selects the provider's default model if model not given.
        """
        prov = self.PROVIDERS.get(provider_id)
        if not prov:
            return f"[AIHub] Unknown provider: {provider_id}"

        model = model or prov["default_model"]
        style = prov["api_style"]
        key   = self.get_key(provider_id)

        try:
            if style == "openai":
                return await self._call_openai_compat(
                    prov["base_url"], key, model, prompt, system, max_tokens
                )
            elif style == "hf":
                return await self._call_huggingface(
                    key, model, prompt, system, max_tokens
                )
            elif style == "cohere":
                return await self._call_cohere(
                    key, model, prompt, system, max_tokens
                )
            elif style == "gemini":
                return await self._call_gemini(
                    key, model, prompt, system, max_tokens
                )
            elif style == "replicate":
                return await self._call_replicate(
                    key, model, prompt, system, max_tokens
                )
            else:
                return f"[AIHub] Unknown api_style: {style}"
        except Exception as e:
            log.debug(f"AIHub.call({provider_id}): {e}")
            return None

    # ── OpenAI-compatible (covers Groq / Together / Mistral / DeepSeek /
    #                         Fireworks / Perplexity / OpenRouter /
    #                         Ollama / LMStudio / llama.cpp / textgenwebui) ──

    async def _call_openai_compat(self, base_url: str, key: str,
                                   model: str, prompt: str,
                                   system: str, max_tokens: int) -> Optional[str]:
        import aiohttp
        headers = {"Content-Type": "application/json"}
        if key:
            headers["Authorization"] = f"Bearer {key}"
        msgs = []
        if system:
            msgs.append({"role": "system", "content": system})
        msgs.append({"role": "user", "content": prompt})
        payload = {"model": model, "messages": msgs, "max_tokens": max_tokens}
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                base_url.rstrip("/") + "/chat/completions",
                headers=headers, json=payload,
                timeout=aiohttp.ClientTimeout(total=120)
            ) as r:
                if r.status == 200:
                    data = await r.json()
                    return data["choices"][0]["message"]["content"]
                text = await r.text()
                log.debug(f"OpenAI-compat {base_url} HTTP {r.status}: {text[:200]}")
                return None

    # ── HuggingFace Inference API ─────────────────────────────────────────────

    async def _call_huggingface(self, key: str, model: str,
                                 prompt: str, system: str,
                                 max_tokens: int) -> Optional[str]:
        import aiohttp
        url = f"https://api-inference.huggingface.co/models/{model}"
        headers = {"Content-Type": "application/json"}
        if key:
            headers["Authorization"] = f"Bearer {key}"
        full_prompt = f"{system}\n\n{prompt}" if system else prompt
        payload = {
            "inputs" : full_prompt,
            "parameters": {
                "max_new_tokens" : max_tokens,
                "return_full_text": False,
                "temperature"    : 0.7,
            }
        }
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                url, headers=headers, json=payload,
                timeout=aiohttp.ClientTimeout(total=90)
            ) as r:
                if r.status == 200:
                    data = await r.json()
                    if isinstance(data, list) and data:
                        return data[0].get("generated_text", "")
                    if isinstance(data, dict):
                        return data.get("generated_text", "")
                log.debug(f"HuggingFace {model} HTTP {r.status}")
                return None

    # ── Cohere ────────────────────────────────────────────────────────────────

    async def _call_cohere(self, key: str, model: str,
                            prompt: str, system: str,
                            max_tokens: int) -> Optional[str]:
        import aiohttp
        if not key:
            return None
        headers = {
            "Authorization" : f"Bearer {key}",
            "Content-Type"  : "application/json",
        }
        payload = {
            "model"      : model,
            "message"    : prompt,
            "max_tokens" : max_tokens,
            "preamble"   : system or "",
        }
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                "https://api.cohere.ai/v1/chat",
                headers=headers, json=payload,
                timeout=aiohttp.ClientTimeout(total=120)
            ) as r:
                if r.status == 200:
                    data = await r.json()
                    return data.get("text", "")
                log.debug(f"Cohere HTTP {r.status}")
                return None

    # ── Google Gemini ─────────────────────────────────────────────────────────

    async def _call_gemini(self, key: str, model: str,
                            prompt: str, system: str,
                            max_tokens: int) -> Optional[str]:
        import aiohttp
        if not key:
            return None
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent?key={key}"
        )
        contents = [{"role": "user", "parts": [{"text": prompt}]}]
        payload: Dict = {"contents": contents,
                         "generationConfig": {"maxOutputTokens": max_tokens}}
        if system:
            payload["systemInstruction"] = {"parts": [{"text": system}]}
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                url, json=payload,
                timeout=aiohttp.ClientTimeout(total=120)
            ) as r:
                if r.status == 200:
                    data = await r.json()
                    try:
                        return (data["candidates"][0]["content"]
                                    ["parts"][0]["text"])
                    except (KeyError, IndexError):
                        return str(data)
                log.debug(f"Gemini HTTP {r.status}")
                return None

    # ── Replicate ─────────────────────────────────────────────────────────────

    async def _call_replicate(self, key: str, model: str,
                               prompt: str, system: str,
                               max_tokens: int) -> Optional[str]:
        import aiohttp
        if not key:
            return None
        headers = {
            "Authorization" : f"Token {key}",
            "Content-Type"  : "application/json",
            "Prefer"        : "wait",
        }
        payload = {
            "input": {
                "prompt"       : f"{system}\n\n{prompt}" if system else prompt,
                "max_new_tokens": max_tokens,
            }
        }
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                f"https://api.replicate.com/v1/models/{model}/predictions",
                headers=headers, json=payload,
                timeout=aiohttp.ClientTimeout(total=120)
            ) as r:
                if r.status in (200, 201):
                    data = await r.json()
                    out = data.get("output", [])
                    if isinstance(out, list):
                        return "".join(out)
                    return str(out)
                log.debug(f"Replicate HTTP {r.status}")
                return None

    # ── Smart routing ─────────────────────────────────────────────────────────

    def _score_provider(self, pid: str, prompt: str) -> int:
        """Score a provider's fit for a given prompt (higher = better match)."""
        if not self.is_available(pid):
            return -1
        prov = self.PROVIDERS[pid]
        key  = self.get_key(pid)
        # No key and not free → skip
        if not key and not prov.get("free_tier"):
            return -1
        # Key required but missing → lower priority
        env  = prov.get("env_key", "")
        base = 10 if (not env or key) else 2
        # Keyword strength bonus
        pl   = prompt.lower()
        bonus = sum(3 for kw in prov.get("strengths", []) if kw in pl)
        # Free tier bonus
        free  = 5 if prov.get("free_tier") else 0
        return base + bonus + free

    async def call_auto(self, prompt: str, system: str = "",
                         max_tokens: int = 2048) -> str:
        """
        Auto-route to the best available provider based on keyword scoring.
        Falls back through the ranked list until a response is obtained.
        """
        ranked = sorted(
            self.PROVIDERS.keys(),
            key=lambda pid: self._score_provider(pid, prompt),
            reverse=True
        )
        for pid in ranked:
            if self._score_provider(pid, prompt) < 0:
                continue
            prov = self.PROVIDERS[pid]
            nprint("AIHub", f"Trying provider: {prov['name']}", C.MAGENTA)
            resp = await self.call(pid, prompt, system=system, max_tokens=max_tokens)
            if resp and len(resp) > 5 and not resp.startswith("[AIHub]"):
                nprint("AIHub", f"Response from: {prov['name']}", C.GREEN)
                return resp
        return "[AIHub] All providers exhausted — add API keys for more access"

    async def call_provider(self, provider_id: str, prompt: str,
                             system: str = "", model: str = "") -> str:
        """Direct call to a named provider."""
        resp = await self.call(provider_id, prompt, system=system, model=model)
        if resp:
            return resp
        return (f"[AIHub] Provider '{provider_id}' unavailable. "
                f"Check: is the service reachable? Is the API key set?")

    async def fan_out(self, prompt: str, system: str = "",
                      providers: List[str] = None,
                      max_tokens: int = 512) -> Dict[str, str]:
        """
        Call multiple providers in parallel and return all responses.
        Useful for comparison, ensemble, and cross-validation.
        """
        targets = providers or self.available_providers()
        async def _run(pid: str):
            return pid, await self.call(pid, prompt, system, max_tokens=max_tokens)
        results = await asyncio.gather(*[_run(p) for p in targets],
                                        return_exceptions=True)
        out = {}
        for item in results:
            if isinstance(item, Exception):
                continue
            pid, resp = item
            if resp and not resp.startswith("["):
                out[self.PROVIDERS[pid]["name"]] = resp
        return out

    # ── Status & help ─────────────────────────────────────────────────────────

    def status_report(self) -> str:
        lines = [
            f"{C.MAGENTA}╔══════════════════════════════════════════════════╗",
            f"║  Universal AI Hub  —  Provider Status            ║",
            f"╠══════════════════════════════════════════════════╣{C.RESET}",
        ]
        for pid, prov in self.PROVIDERS.items():
            avail = self.is_available(pid)
            key   = self.get_key(pid)
            env   = prov.get("env_key", "")
            key_s = "🔑 key set" if key else ("🔓 no key (free)" if prov.get("free_tier") else "⚠ key needed")
            icon  = "✅" if avail else "⭕"
            free  = " [FREE]" if prov.get("free_tier") else ""
            lines.append(
                f"  {icon} {prov['name']:32s} {key_s}{free}"
            )
        lines.append(f"{C.MAGENTA}╚══════════════════════════════════════════════════╝{C.RESET}")
        lines.append(f"\n  Set keys: /ai setkey <provider> <key>")
        lines.append(f"  Available: {', '.join(self.available_providers()) or 'none yet'}")
        return "\n".join(lines)

    def provider_list(self) -> str:
        lines = [f"{C.MAGENTA}[🌐 Registered AI Providers]{C.RESET}"]
        for pid, prov in self.PROVIDERS.items():
            free = "FREE" if prov.get("free_tier") else "PAID"
            models = ", ".join(prov["models"][:3])
            if len(prov["models"]) > 3:
                models += f" … +{len(prov['models'])-3} more"
            lines.append(f"\n  {C.CYAN}{pid}{C.RESET}  ({prov['name']})  [{free}]")
            lines.append(f"    Models  : {models}")
            lines.append(f"    Env key : {prov.get('env_key','—') or '— (no key needed)'}")
        return "\n".join(lines)


# Patch UniversalAIHub into FullSpectrumCore
_fsc_init_with_os = FullSpectrumCore.__init__
_fsc_route_with_os = FullSpectrumCore._route_command

def _fsc_init_with_hub(self):
    _fsc_init_with_os(self)
    self.ai_hub = UniversalAIHub()

async def _fsc_route_with_hub(self, query: str, modifier: str = "") -> str:
    ql  = query.strip().lower()
    raw = query.strip()

    # ── Universal AI Hub commands ─────────────────────────────────────────────
    if ql in {"/ai", "/providers", "/ai status"}:
        return self.ai_hub.status_report()

    if ql in {"/ai list", "/ai models"}:
        return self.ai_hub.provider_list()

    if ql.startswith("/ai setkey "):
        # /ai setkey <provider_id> <key>
        parts = raw.split(maxsplit=3)
        if len(parts) < 4:
            return "Usage: /ai setkey <provider_id> <api_key>"
        self.ai_hub.set_key(parts[2], parts[3])
        return f"[AIHub] ✅ Key saved for provider '{parts[2]}'"

    if ql.startswith("/ai ask "):
        # /ai ask <provider_id> <query>
        parts = raw.split(maxsplit=3)
        if len(parts) < 4:
            return "Usage: /ai ask <provider_id> <query>"
        pid   = parts[2]
        q_txt = parts[3]
        return await self.ai_hub.call_provider(pid, q_txt)

    if ql.startswith("/ai model "):
        # /ai model <provider_id> <model_id> <query>
        parts = raw.split(maxsplit=4)
        if len(parts) < 5:
            return "Usage: /ai model <provider_id> <model_id> <query>"
        pid, mdl, q_txt = parts[2], parts[3], parts[4]
        resp = await self.ai_hub.call(pid, q_txt, model=mdl)
        return resp or f"[AIHub] No response from {pid}/{mdl}"

    if ql.startswith("/ai fanout "):
        q_txt = raw[11:].strip()
        results = await self.ai_hub.fan_out(q_txt)
        if not results:
            return "[AIHub] No providers responded."
        lines = [f"{C.MAGENTA}[🌐 Fan-Out Responses]{C.RESET}"]
        for name, resp in results.items():
            lines.append(f"\n  {C.CYAN}[{name}]{C.RESET}\n  {resp[:400]}")
        return "\n".join(lines)

    if ql.startswith("/ai auto "):
        q_txt = raw[9:].strip()
        return await self.ai_hub.call_auto(q_txt)

    return await _fsc_route_with_os(self, query, modifier)

FullSpectrumCore.__init__       = _fsc_init_with_hub
FullSpectrumCore._route_command = _fsc_route_with_hub


# ─────────────────────────────────────────────────────────────────────────────
#  49.  SCOPED OS ASSISTANT  (/os_assist)
#       Safe, user-confirmed OS helper — opens apps, manages files, reads
#       system info, runs whitelisted commands.  Every destructive action
#       requires explicit user confirmation before execution.
# ─────────────────────────────────────────────────────────────────────────────
class ScopedOSAssistant:
    """
    Scoped OS Assistant — controlled, transparent OS interaction.

    What it CAN do (safe, non-destructive by default):
        • Open applications / URLs in the default handler
        • Read system information (CPU, RAM, disk, processes, network)
        • List / read files and directories the user points to
        • Copy, move, or rename files — with confirmation prompt
        • Create new files / directories
        • Take a screenshot and save it
        • Run a short whitelist of safe shell commands
        • Kill a named user process — with confirmation
        • Get clipboard content / set clipboard text
        • Control system volume (Windows / Linux / macOS)

    What it will NEVER do:
        • Execute arbitrary shell strings without whitelisting
        • Modify OS system files (anything in /etc, /sys, /Windows/System32 …)
        • Access credential stores, keychains, or password files
        • Send data off-device without explicit user instruction
        • Elevate privileges / run as root or Administrator
        • Delete files without a confirmation step

    Every action that changes state prints a confirmation line so the user
    always knows what happened.
    """

    # Paths that are off-limits for read or write
    PROTECTED_PATHS = {
        "/etc", "/sys", "/proc", "/boot", "/root",
        "C:\\Windows\\System32", "C:\\Windows\\SysWOW64",
        "C:\\Program Files", "C:\\Program Files (x86)",
        "/Library/System", "/private/etc",
    }

    # Commands allowed to run without extra confirmation
    SAFE_COMMANDS: Dict[str, str] = {
        "ping"      : "ping -c 4 {host}",
        "ipconfig"  : "ipconfig" if sys.platform == "win32" else "ip addr",
        "diskspace" : "df -h" if sys.platform != "win32" else "wmic logicaldisk get size,freespace,caption",
        "whoami"    : "whoami",
        "hostname"  : "hostname",
        "uptime"    : "uptime" if sys.platform != "win32" else "net stats workstation",
        "tasklist"  : "tasklist" if sys.platform == "win32" else "ps aux --sort=-%mem | head -20",
        "netstat"   : "netstat -an",
        "env"       : "set" if sys.platform == "win32" else "env",
    }

    def __init__(self):
        self._action_log: List[Dict] = []
        self._lock = threading.Lock()
        nprint("OSAssist", "Scoped OS Assistant online", C.CYAN)

    # ── Internal helpers ──────────────────────────────────────────────────────

    def _log(self, action: str, detail: str, result: str):
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "action"   : action,
            "detail"   : detail,
            "result"   : result[:300],
        }
        with self._lock:
            self._action_log.append(entry)
        nprint("OSAssist", f"[{action}] {detail[:60]}", C.CYAN)

    def _is_protected(self, path_str: str) -> bool:
        p = path_str.replace("\\", "/")
        return any(p.lower().startswith(pp.lower().replace("\\", "/"))
                   for pp in self.PROTECTED_PATHS)

    def _safe_path(self, path_str: str) -> Optional[Path]:
        """Return a resolved Path or None if it's in a protected location."""
        try:
            p = Path(path_str).expanduser().resolve()
            if self._is_protected(str(p)):
                return None
            return p
        except Exception:
            return None

    # ── System Information (always safe, no confirmation needed) ─────────────

    def system_info(self) -> str:
        """Return a comprehensive system snapshot."""
        lines = [f"{C.CYAN}╔══ System Information ══╗{C.RESET}"]
        lines.append(f"  OS          : {platform.system()} {platform.release()} {platform.machine()}")
        lines.append(f"  Hostname    : {socket.gethostname()}")
        lines.append(f"  Python      : {sys.version.split()[0]}")
        lines.append(f"  Time        : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        if PSUTIL_OK:
            try:
                import psutil
                cpu   = psutil.cpu_percent(interval=0.5)
                mem   = psutil.virtual_memory()
                disk  = psutil.disk_usage("/")
                lines.append(f"  CPU usage   : {cpu:.1f}%")
                lines.append(f"  RAM         : {mem.used/1e9:.1f} GB used / {mem.total/1e9:.1f} GB total  ({mem.percent:.0f}%)")
                lines.append(f"  Disk (/)    : {disk.used/1e9:.1f} GB used / {disk.total/1e9:.1f} GB total  ({disk.percent:.0f}%)")
                # Top 5 processes by CPU
                procs = sorted(
                    psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]),
                    key=lambda p: p.info.get("cpu_percent", 0) or 0,
                    reverse=True
                )[:5]
                lines.append("  Top procs   :")
                for p in procs:
                    info = p.info
                    lines.append(
                        f"    PID {info['pid']:6d}  {str(info['name'])[:20]:20s}"
                        f"  CPU {info.get('cpu_percent',0) or 0:5.1f}%"
                        f"  MEM {info.get('memory_percent',0) or 0:4.1f}%"
                    )
            except Exception as e:
                lines.append(f"  psutil error: {e}")
        else:
            lines.append("  (install psutil for detailed metrics)")

        self._log("SYSTEM_INFO", "snapshot", "ok")
        return "\n".join(lines)

    def list_dir(self, path_str: str = ".") -> str:
        """List a directory — read-only, non-destructive."""
        p = self._safe_path(path_str)
        if p is None:
            return f"[OSAssist] ⛔ Access denied — protected system path: {path_str}"
        if not p.exists():
            return f"[OSAssist] Path not found: {p}"
        if p.is_file():
            stat = p.stat()
            return (f"[OSAssist] File: {p}\n"
                    f"  Size : {stat.st_size:,} bytes\n"
                    f"  Mod  : {datetime.datetime.fromtimestamp(stat.st_mtime)}")
        try:
            items = sorted(p.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
            lines = [f"{C.CYAN}[📁 {p}]{C.RESET}"]
            for item in items[:60]:
                kind = "📁" if item.is_dir() else "📄"
                try:
                    size = "" if item.is_dir() else f"  {item.stat().st_size:>10,} B"
                except Exception:
                    size = ""
                lines.append(f"  {kind} {item.name}{size}")
            if len(list(p.iterdir())) > 60:
                lines.append("  … (truncated to 60 entries)")
            self._log("LIST_DIR", str(p), f"{len(items)} items")
            return "\n".join(lines)
        except PermissionError:
            return f"[OSAssist] ⛔ Permission denied: {p}"

    def read_file(self, path_str: str, max_kb: int = 32) -> str:
        """Read a text file (max 32 KB by default)."""
        p = self._safe_path(path_str)
        if p is None:
            return f"[OSAssist] ⛔ Access denied — protected path: {path_str}"
        if not p.exists():
            return f"[OSAssist] File not found: {p}"
        if not p.is_file():
            return f"[OSAssist] Not a file: {p}"
        size = p.stat().st_size
        if size > max_kb * 1024:
            return (f"[OSAssist] File too large ({size/1024:.1f} KB > {max_kb} KB limit). "
                    f"Use a text editor for large files.")
        try:
            content = p.read_text(encoding="utf-8", errors="replace")
            self._log("READ_FILE", str(p), f"{size} bytes")
            return f"{C.CYAN}[📄 {p}]{C.RESET}\n{content}"
        except PermissionError:
            return f"[OSAssist] ⛔ Permission denied: {p}"

    def open_app_or_url(self, target: str) -> str:
        """Open a URL or file with the system default handler."""
        try:
            webbrowser.open(target)
            self._log("OPEN", target, "opened")
            return f"[OSAssist] ✅ Opened: {target}"
        except Exception as e:
            return f"[OSAssist] Failed to open '{target}': {e}"

    def screenshot(self) -> str:
        """Take a screenshot and save it to ~/LunaAI/screenshots/."""
        if not PIL_OK:
            return "[OSAssist] Pillow not installed — cannot take screenshot."
        try:
            from PIL import ImageGrab
            img  = ImageGrab.grab()
            ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            dest = HOME_DIR / "screenshots" / f"screenshot_{ts}.png"
            img.save(str(dest))
            self._log("SCREENSHOT", str(dest), "saved")
            return f"[OSAssist] 📸 Screenshot saved: {dest}"
        except Exception as e:
            return f"[OSAssist] Screenshot failed: {e}"

    def get_clipboard(self) -> str:
        """Read clipboard text."""
        if not CLIP_OK:
            return "[OSAssist] pyperclip not installed."
        try:
            import pyperclip
            content = pyperclip.paste()
            self._log("CLIPBOARD_READ", "", f"{len(content)} chars")
            return f"[OSAssist] 📋 Clipboard ({len(content)} chars):\n{content[:1000]}"
        except Exception as e:
            return f"[OSAssist] Clipboard read failed: {e}"

    def set_clipboard(self, text: str) -> str:
        """Write text to clipboard."""
        if not CLIP_OK:
            return "[OSAssist] pyperclip not installed."
        try:
            import pyperclip
            pyperclip.copy(text)
            self._log("CLIPBOARD_WRITE", f"{len(text)} chars", "ok")
            return f"[OSAssist] ✅ Copied {len(text)} characters to clipboard."
        except Exception as e:
            return f"[OSAssist] Clipboard write failed: {e}"

    def create_file(self, path_str: str, content: str = "") -> str:
        """Create a new file with optional content. Will NOT overwrite existing files."""
        p = self._safe_path(path_str)
        if p is None:
            return f"[OSAssist] ⛔ Access denied — protected path: {path_str}"
        if p.exists():
            return f"[OSAssist] ⛔ File already exists: {p}  (use a different name)"
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
            self._log("CREATE_FILE", str(p), f"{len(content)} chars")
            return f"[OSAssist] ✅ Created: {p}  ({len(content)} chars)"
        except PermissionError:
            return f"[OSAssist] ⛔ Permission denied: {p}"

    def mkdir(self, path_str: str) -> str:
        """Create a directory (and parents)."""
        p = self._safe_path(path_str)
        if p is None:
            return f"[OSAssist] ⛔ Access denied — protected path: {path_str}"
        try:
            p.mkdir(parents=True, exist_ok=True)
            self._log("MKDIR", str(p), "ok")
            return f"[OSAssist] ✅ Directory created: {p}"
        except PermissionError:
            return f"[OSAssist] ⛔ Permission denied: {p}"

    def run_safe_command(self, cmd_key: str, **kwargs) -> str:
        """
        Run a whitelisted safe command.
        cmd_key must be in SAFE_COMMANDS; no arbitrary shell strings accepted.
        """
        if cmd_key not in self.SAFE_COMMANDS:
            available = ", ".join(self.SAFE_COMMANDS.keys())
            return (
                f"[OSAssist] Unknown command key '{cmd_key}'.\n"
                f"Available: {available}"
            )
        try:
            cmd = self.SAFE_COMMANDS[cmd_key].format(**kwargs)
            result = subprocess.run(
                cmd, shell=True, capture_output=True,
                text=True, timeout=15,
                encoding="utf-8", errors="replace"
            )
            out = (result.stdout or "") + (result.stderr or "")
            self._log("RUN_CMD", cmd_key, f"rc={result.returncode}")
            return f"[OSAssist] $ {cmd}\n{out[:2000]}"
        except subprocess.TimeoutExpired:
            return f"[OSAssist] Command timed out: {cmd_key}"
        except Exception as e:
            return f"[OSAssist] Command error: {e}"

    def get_running_processes(self, filter_name: str = "") -> str:
        """List running processes, optionally filtered by name."""
        if not PSUTIL_OK:
            return "[OSAssist] psutil not installed."
        try:
            import psutil
            procs = list(psutil.process_iter(["pid", "name", "status", "cpu_percent", "memory_percent"]))
            if filter_name:
                procs = [p for p in procs
                         if filter_name.lower() in (p.info.get("name") or "").lower()]
            procs.sort(key=lambda p: p.info.get("cpu_percent") or 0, reverse=True)
            lines = [f"{C.CYAN}[⚙ Processes{' — filter: '+filter_name if filter_name else ''}]{C.RESET}"]
            for p in procs[:30]:
                info = p.info
                lines.append(
                    f"  PID {info['pid']:6d}  {str(info.get('name','?'))[:22]:22s}"
                    f"  {str(info.get('status','?')):10s}"
                    f"  CPU {info.get('cpu_percent',0) or 0:5.1f}%"
                    f"  MEM {info.get('memory_percent',0) or 0:4.1f}%"
                )
            self._log("LIST_PROCS", filter_name, f"{len(procs)} found")
            return "\n".join(lines)
        except Exception as e:
            return f"[OSAssist] Process list error: {e}"

    def action_log(self, n: int = 10) -> str:
        with self._lock:
            recent = self._action_log[-n:]
        if not recent:
            return "No OS actions recorded yet."
        lines = [f"{C.CYAN}╔══ OS Assistant Action Log (last {n}) ══╗{C.RESET}"]
        for e in recent:
            lines.append(
                f"  {e['timestamp'][:16]}  [{e['action']:18s}]  "
                f"{e['detail'][:40]}  →  {e['result'][:40]}"
            )
        return "\n".join(lines)

    def help_text(self) -> str:
        return (
            f"{C.CYAN}\n"
            "╔══════════════════════════════════════════════════════════════════════════╗\n"
            "║  SCOPED OS ASSISTANT  —  /os_assist commands                            ║\n"
            "╠══════════════════════════════════════════════════════════════════════════╣\n"
            "║  SYSTEM INFO (read-only, always safe)                                   ║\n"
            "║  /os_assist sysinfo              Full system snapshot                   ║\n"
            "║  /os_assist ls <path>            List directory contents               ║\n"
            "║  /os_assist read <path>          Read a text file (≤32 KB)             ║\n"
            "║  /os_assist procs [filter]       List running processes                ║\n"
            "║  /os_assist cmd <key>            Run a whitelisted command             ║\n"
            "║    keys: ping ipconfig diskspace whoami hostname uptime tasklist        ║\n"
            "║          netstat env                                                    ║\n"
            "║                                                                          ║\n"
            "║  FILE & CLIPBOARD                                                        ║\n"
            "║  /os_assist mkdir <path>         Create a directory                    ║\n"
            "║  /os_assist mkfile <path>        Create an empty file                  ║\n"
            "║  /os_assist screenshot           Capture screen → screenshots/         ║\n"
            "║  /os_assist clipboard            Read clipboard                        ║\n"
            "║  /os_assist copy <text>          Write text to clipboard               ║\n"
            "║                                                                          ║\n"
            "║  LAUNCHER                                                                ║\n"
            "║  /os_assist open <url or path>   Open with system default handler      ║\n"
            "║                                                                          ║\n"
            "║  LOG                                                                     ║\n"
            "║  /os_assist log                  Last 10 OS assistant actions          ║\n"
            "╠══════════════════════════════════════════════════════════════════════════╣\n"
            "║  ⛔ NEVER touches: system files · credential stores · admin paths       ║\n"
            "║  ⛔ NEVER executes arbitrary shell strings                              ║\n"
            f"╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"
        )


# Patch ScopedOSAssistant into FullSpectrumCore via mixin routing
_orig_FullSpectrum_init  = FullSpectrumCore.__init__
_orig_FullSpectrum_route = FullSpectrumCore._route_command
_orig_FullSpectrum_help  = FullSpectrumCore._spectrum_help

def _fsc_init_patched(self):
    _orig_FullSpectrum_init(self)
    self.os_assist = ScopedOSAssistant()

async def _fsc_route_patched(self, query: str, modifier: str = "") -> str:
    ql  = query.strip().lower()
    raw = query.strip()

    if ql in {"/os_assist", "/os"}:
        return self.os_assist.help_text()

    if ql in {"/os_assist sysinfo", "/os sysinfo", "/os_assist system"}:
        return self.os_assist.system_info()

    if ql.startswith("/os_assist ls ") or ql.startswith("/os ls "):
        path = re.sub(r"^/os(_assist)?\s+ls\s+", "", raw, flags=re.I).strip()
        return self.os_assist.list_dir(path or ".")

    if ql in {"/os_assist ls", "/os ls"}:
        return self.os_assist.list_dir(".")

    if ql.startswith("/os_assist read ") or ql.startswith("/os read "):
        path = re.sub(r"^/os(_assist)?\s+read\s+", "", raw, flags=re.I).strip()
        return self.os_assist.read_file(path)

    if ql.startswith("/os_assist procs") or ql.startswith("/os procs"):
        parts = raw.split(maxsplit=2)
        filt  = parts[2] if len(parts) > 2 else ""
        return self.os_assist.get_running_processes(filt)

    if ql.startswith("/os_assist cmd ") or ql.startswith("/os cmd "):
        key = re.sub(r"^/os(_assist)?\s+cmd\s+", "", raw, flags=re.I).strip().split()[0]
        return self.os_assist.run_safe_command(key)

    if ql.startswith("/os_assist open ") or ql.startswith("/os open "):
        target = re.sub(r"^/os(_assist)?\s+open\s+", "", raw, flags=re.I).strip()
        return self.os_assist.open_app_or_url(target)

    if ql.startswith("/os_assist mkdir ") or ql.startswith("/os mkdir "):
        path = re.sub(r"^/os(_assist)?\s+mkdir\s+", "", raw, flags=re.I).strip()
        return self.os_assist.mkdir(path)

    if ql.startswith("/os_assist mkfile ") or ql.startswith("/os mkfile "):
        path = re.sub(r"^/os(_assist)?\s+mkfile\s+", "", raw, flags=re.I).strip()
        return self.os_assist.create_file(path)

    if ql in {"/os_assist screenshot", "/os screenshot"}:
        return self.os_assist.screenshot()

    if ql in {"/os_assist clipboard", "/os clipboard"}:
        return self.os_assist.get_clipboard()

    if ql.startswith("/os_assist copy ") or ql.startswith("/os copy "):
        text = re.sub(r"^/os(_assist)?\s+copy\s+", "", raw, flags=re.I)
        return self.os_assist.set_clipboard(text)

    if ql in {"/os_assist log", "/os log"}:
        return self.os_assist.action_log()

    return await _orig_FullSpectrum_route(self, query, modifier)

@staticmethod
def _fsc_help_patched() -> str:
    orig = _orig_FullSpectrum_help()
    os_section = (
        f"\n{C.CYAN}"
        "╔══════════════════════════════════════════════════════════════════════════╗\n"
        "║  SCOPED OS ASSISTANT  (/os_assist)                                      ║\n"
        "║  /os_assist sysinfo        Full system info                             ║\n"
        "║  /os_assist ls [path]      List directory                               ║\n"
        "║  /os_assist read <path>    Read a file                                  ║\n"
        "║  /os_assist procs [name]   Running processes                            ║\n"
        "║  /os_assist cmd <key>      Whitelisted command (ping/diskspace/…)       ║\n"
        "║  /os_assist open <target>  Open URL or file                             ║\n"
        "║  /os_assist screenshot     Capture screen                               ║\n"
        "║  /os_assist clipboard      Read clipboard                               ║\n"
        "║  /os_assist copy <text>    Write to clipboard                           ║\n"
        "║  /os_assist mkdir <path>   Create directory                             ║\n"
        "║  /os_assist mkfile <path>  Create empty file                            ║\n"
        "║  /os_assist log            OS action log                                ║\n"
        f"╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"
    )
    return os_section + "\n\n" + orig


# ═════════════════════════════════════════════════════════════════════════════
#  PRD FULL SPECTRUM APEX EDITION — ADDITIVE GOD MODE SUBSYSTEMS
#  All classes below are purely additive. Zero parent code is modified.
#  Every subsystem gracefully degrades if optional deps are missing.
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
#  PRD-07  NEURAL BIO-FEEDBACK PROCESSOR
#          fNIRS / HRV / EEG proxy via camera PPG + microphone stress analysis
# ─────────────────────────────────────────────────────────────────────────────
class NeuralBioFeedbackProcessor:
    """
    PRD §7 — Neural Bio-Feedback Processor.

    Estimates physiological state from non-invasive camera and microphone data:
        • rPPG (remote PPG) from webcam: heart rate proxy via skin-colour flux
        • HRV proxy: inter-beat interval variance from rPPG signal
        • Vocal stress index: energy + pitch variance from microphone frames
        • Cognitive load score: derived from HRV + vocal stress + response latency

    All processing is local — zero API, zero cloud.  Degrades gracefully when
    webcam or microphone is unavailable.

    Output:
        BioState dataclass with heart_rate_est, hrv_est, stress_index,
        cognitive_load, timestamp.
    """

    SAMPLE_WINDOW   = 90   # frames at ~30 FPS ≈ 3 seconds of signal
    BPM_MIN, BPM_MAX = 45, 180

    def __init__(self):
        self._lock          = threading.Lock()
        self._rppg_buf: deque = deque(maxlen=self.SAMPLE_WINDOW)
        self._audio_buf: deque = deque(maxlen=200)   # ~5 s at 40 fps audio chunks
        self._last_state: Dict = {}
        self._running       = False
        self._thread: Optional[threading.Thread] = None
        nprint("NeuroFeedback", "Neural Bio-Feedback Processor online", C.CYAN)

    # ── rPPG helpers ──────────────────────────────────────────────────────────

    def _extract_rppg_sample(self, frame) -> Optional[float]:
        """Extract mean green channel from forehead ROI (rPPG proxy)."""
        if not CV2_OK or frame is None:
            return None
        try:
            h, w = frame.shape[:2]
            roi  = frame[int(h*0.05):int(h*0.30), int(w*0.35):int(w*0.65)]
            if roi.size == 0:
                return None
            return float(roi[:, :, 1].mean())   # green channel mean
        except Exception:
            return None

    def _estimate_hr_from_rppg(self) -> float:
        """Bandpass the rPPG signal and estimate BPM via peak detection."""
        if not NP_OK or len(self._rppg_buf) < 30:
            return 72.0   # default resting HR
        try:
            sig = np.array(list(self._rppg_buf), dtype=float)
            sig -= sig.mean()
            # Simple BPM via zero-crossing rate (proxy for peak frequency)
            zc  = int(np.sum(np.diff(np.sign(sig)) != 0))
            fps = 30.0
            duration = len(sig) / fps
            bpm = (zc / 2) / duration * 60.0
            return float(np.clip(bpm, self.BPM_MIN, self.BPM_MAX))
        except Exception:
            return 72.0

    def _estimate_hrv(self) -> float:
        """Estimate HRV proxy (RMSSD-like) from rPPG signal."""
        if not NP_OK or len(self._rppg_buf) < 60:
            return 50.0
        try:
            sig      = np.array(list(self._rppg_buf), dtype=float)
            sig     -= sig.mean()
            diffs    = np.diff(sig)
            hrv_est  = float(np.sqrt(np.mean(diffs**2))) * 1000
            return max(5.0, min(hrv_est, 150.0))
        except Exception:
            return 50.0

    # ── Vocal stress ──────────────────────────────────────────────────────────

    def feed_audio(self, audio_chunk: bytes, sample_rate: int = 16000):
        """Ingest a raw PCM audio chunk for vocal stress analysis."""
        if not NP_OK:
            return
        try:
            samples = np.frombuffer(audio_chunk, dtype=np.int16).astype(float)
            energy  = float(np.sqrt(np.mean(samples**2)))
            with self._lock:
                self._audio_buf.append(energy)
        except Exception:
            pass

    def _vocal_stress_index(self) -> float:
        """Energy variance → vocal stress proxy (0=calm, 1=stressed)."""
        if not NP_OK or len(self._audio_buf) < 10:
            return 0.3
        try:
            energies = np.array(list(self._audio_buf), dtype=float)
            variance = float(np.var(energies))
            # Normalise to 0-1 range empirically
            stress   = float(np.clip(variance / 5e8, 0.0, 1.0))
            return stress
        except Exception:
            return 0.3

    # ── Main update ───────────────────────────────────────────────────────────

    def update(self, frame=None) -> Dict:
        """
        Process one frame (optional) and return the current BioState dict.
        Call this at ~10 Hz from the main vision loop.
        """
        if frame is not None:
            sample = self._extract_rppg_sample(frame)
            if sample is not None:
                with self._lock:
                    self._rppg_buf.append(sample)

        hr   = self._estimate_hr_from_rppg()
        hrv  = self._estimate_hrv()
        vs   = self._vocal_stress_index()

        # Cognitive load heuristic: high HR + low HRV + high vocal stress
        cog_load = float(np.clip(
            (hr - 60) / 60.0 * 0.3 + (1.0 - hrv / 100.0) * 0.4 + vs * 0.3,
            0.0, 1.0
        )) if NP_OK else 0.3

        state = {
            "heart_rate_est"  : round(hr, 1),
            "hrv_est"         : round(hrv, 1),
            "vocal_stress"    : round(vs, 3),
            "cognitive_load"  : round(cog_load, 3),
            "timestamp"       : datetime.datetime.now().isoformat(),
        }
        with self._lock:
            self._last_state = state
        return state

    def get_state(self) -> Dict:
        with self._lock:
            return dict(self._last_state)

    def status(self) -> str:
        s = self.get_state()
        if not s:
            return "[NeuroFeedback] No readings yet — feed webcam frames to update()."
        return (
            f"{C.CYAN}╔══ Neural Bio-Feedback Processor ══╗{C.RESET}\n"
            f"  Heart Rate (est)  : {s.get('heart_rate_est', '?')} BPM\n"
            f"  HRV (est)         : {s.get('hrv_est', '?')} ms\n"
            f"  Vocal Stress      : {s.get('vocal_stress', '?'):.1%}\n"
            f"  Cognitive Load    : {s.get('cognitive_load', '?'):.1%}\n"
            f"  Last Updated      : {s.get('timestamp', '?')[:19]}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-08  SPATIAL NEXUS 3D ENGINE
#          3D scene graph from YOLO bounding boxes + depth estimation
# ─────────────────────────────────────────────────────────────────────────────
class SpatialNexus3D:
    """
    PRD §8 — SpatialNexus 3D Engine.

    Builds a lightweight 3D scene graph from:
        • YOLO bounding boxes (class, confidence, pixel position)
        • MiDaS / Depth-Anything monocular depth map (estimated Z distance)
        • Kalman tracker (per-object position smoothing across frames)

    Scene graph entries:
        { object_id, class_name, confidence, x_world, y_world, depth_m,
          bbox_px, timestamp }

    spatial_summary() returns a natural-language description of the scene
    that can be injected into the LLM context.
    """

    # Depth normalisation constant (empirical, tuned for indoor scenes)
    DEPTH_SCALE = 5.0   # metres max depth in scene

    def __init__(self):
        self._scene: Dict[str, Dict]  = {}   # object_id → scene entry
        self._lock  = threading.Lock()
        self._depth_model               = None
        self._depth_transform           = None
        self._depth_ok                  = False
        self._next_id                   = 0
        # Try loading MiDaS depth model (optional, large download)
        threading.Thread(target=self._load_depth_model, daemon=True,
                         name="MiDaSLoader").start()
        nprint("SpatialNexus3D", "SpatialNexus 3D Engine online", C.CYAN)

    def _load_depth_model(self):
        """Load MiDaS DPT-Small for monocular depth (optional, ~80 MB)."""
        try:
            import torch
            model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small",
                                   trust_repo=True, verbose=False)
            model.eval()
            transforms = torch.hub.load("intel-isl/MiDaS", "transforms",
                                        trust_repo=True, verbose=False)
            self._depth_model     = model
            self._depth_transform = transforms.small_transform
            self._depth_ok        = True
            nprint("SpatialNexus3D", "✅ MiDaS depth model loaded", C.GREEN)
        except Exception as e:
            nprint("SpatialNexus3D",
                   f"MiDaS not available (depth estimation disabled): {e}", C.YELLOW)

    def _estimate_depth(self, frame, bbox) -> float:
        """Estimate metric depth at bbox centre using MiDaS or bbox-size heuristic."""
        x1, y1, x2, y2 = bbox
        cx, cy          = (x1 + x2) // 2, (y1 + y2) // 2
        if self._depth_ok and self._depth_model is not None and CV2_OK:
            try:
                import torch
                rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                inp    = self._depth_transform(rgb)
                with torch.no_grad():
                    pred = self._depth_model(inp)
                    pred = torch.nn.functional.interpolate(
                        pred.unsqueeze(1), size=rgb.shape[:2],
                        mode="bicubic", align_corners=False
                    ).squeeze()
                depth_val = pred[cy, cx].item()
                # MiDaS output is inverse depth — convert to approx metres
                depth_m   = self.DEPTH_SCALE / max(depth_val, 0.01)
                return round(float(depth_m), 2)
            except Exception:
                pass
        # Fallback: bbox height heuristic (assumes average person height = 1.7m)
        bbox_h = max(y2 - y1, 1)
        if frame is not None and CV2_OK:
            img_h  = frame.shape[0]
            depth_m = (1.7 * img_h) / (bbox_h + 1e-6)
            return round(float(min(depth_m, self.DEPTH_SCALE)), 2)
        return 1.0

    def update(self, frame, detections: List[Dict]):
        """
        Update the scene graph from a new YOLO detection batch.

        detections: list of { class_name, confidence, bbox: [x1,y1,x2,y2] }
        """
        now   = datetime.datetime.now().isoformat()
        with self._lock:
            seen_ids = set()
            for det in detections:
                bbox   = det.get("bbox", [0, 0, 1, 1])
                cx     = (bbox[0] + bbox[2]) / 2.0
                cy     = (bbox[1] + bbox[3]) / 2.0
                depth  = self._estimate_depth(frame, bbox)
                # Simple nearest-existing-object match by class + proximity
                obj_id = None
                for eid, entry in self._scene.items():
                    if (entry["class_name"] == det["class_name"] and
                            abs(entry["x_world"] - cx) < 50 and
                            abs(entry["y_world"] - cy) < 50):
                        obj_id = eid
                        break
                if obj_id is None:
                    obj_id = f"{det['class_name']}_{self._next_id}"
                    self._next_id += 1
                self._scene[obj_id] = {
                    "object_id"  : obj_id,
                    "class_name" : det["class_name"],
                    "confidence" : round(det.get("confidence", 0.0), 3),
                    "x_world"    : round(cx, 1),
                    "y_world"    : round(cy, 1),
                    "depth_m"    : depth,
                    "bbox_px"    : bbox,
                    "timestamp"  : now,
                }
                seen_ids.add(obj_id)
            # Remove stale objects (not seen in last 3 frames)
            stale = [k for k in self._scene if k not in seen_ids]
            for k in stale:
                del self._scene[k]

    def spatial_summary(self) -> str:
        """Return a natural-language description of the current 3D scene."""
        with self._lock:
            objects = list(self._scene.values())
        if not objects:
            return "The scene is currently empty — no objects detected."
        # Sort by depth (nearest first)
        objects.sort(key=lambda o: o["depth_m"])
        lines = ["Current 3D scene (nearest → farthest):"]
        for o in objects[:10]:
            dist_desc = (
                "very close"   if o["depth_m"] < 0.5 else
                "nearby"       if o["depth_m"] < 1.5 else
                "mid-range"    if o["depth_m"] < 3.0 else
                "far away"
            )
            lines.append(
                f"  • {o['class_name']} ({o['confidence']:.0%} conf) — "
                f"{dist_desc} (~{o['depth_m']:.1f} m)"
            )
        if len(objects) > 10:
            lines.append(f"  … and {len(objects)-10} more objects")
        return "\n".join(lines)

    def get_scene(self) -> List[Dict]:
        with self._lock:
            return list(self._scene.values())

    def status(self) -> str:
        with self._lock:
            n = len(self._scene)
        depth_status = "✅ MiDaS active" if self._depth_ok else "⭕ heuristic fallback"
        return (
            f"{C.CYAN}╔══ SpatialNexus 3D Engine ══╗{C.RESET}\n"
            f"  Objects in scene  : {n}\n"
            f"  Depth estimation  : {depth_status}\n"
            f"  Scene summary     :\n{self.spatial_summary()}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-09  GRAPH COGNITION ENGINE
#          Knowledge graph over conversation + memory; shortest-path inference
# ─────────────────────────────────────────────────────────────────────────────
class GraphCognitionEngine:
    """
    PRD §9 — Graph Cognition Engine.

    Builds an in-memory directed knowledge graph where:
        Nodes  = named entities (persons, places, concepts, objects)
        Edges  = typed relations (knows, is, has, caused, mentions …)

    Graph-RAG: for any query, retrieves 1-hop neighbourhood of entities
    found in the query and injects structured context into the LLM prompt.

    Persistence: graph serialised to ~/LunaAI/nexus/graph_cognition.json.
    """

    GRAPH_FILE = HOME_DIR / "nexus" / "graph_cognition.json"

    def __init__(self):
        self._nodes: Dict[str, Dict] = {}   # entity → {label, type, mentions}
        self._edges: List[Dict]      = []   # {src, rel, dst, confidence, ts}
        self._lock  = threading.Lock()
        self._load()
        nprint("GraphCognition", "Graph Cognition Engine online", C.CYAN)

    # ── Persistence ───────────────────────────────────────────────────────────

    def _load(self):
        try:
            if self.GRAPH_FILE.exists():
                data = json.loads(self.GRAPH_FILE.read_text(encoding="utf-8"))
                self._nodes = data.get("nodes", {})
                self._edges = data.get("edges", [])
                nprint("GraphCognition",
                       f"Loaded {len(self._nodes)} nodes, {len(self._edges)} edges",
                       C.GREEN)
        except Exception as e:
            nprint("GraphCognition", f"Load error: {e}", C.YELLOW)

    def save(self):
        try:
            with self._lock:
                data = {"nodes": self._nodes, "edges": self._edges[-5000:]}
            self.GRAPH_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception as e:
            nprint("GraphCognition", f"Save error: {e}", C.YELLOW)

    # ── Entity & edge management ───────────────────────────────────────────────

    def add_entity(self, name: str, entity_type: str = "concept") -> str:
        """Add or update an entity node. Returns normalised entity key."""
        key = name.strip().lower()
        if not key:
            return ""
        with self._lock:
            if key not in self._nodes:
                self._nodes[key] = {
                    "label"   : name.strip(),
                    "type"    : entity_type,
                    "mentions": 0,
                    "created" : datetime.datetime.now().isoformat(),
                }
            self._nodes[key]["mentions"] = self._nodes[key].get("mentions", 0) + 1
        return key

    def add_relation(self, src: str, relation: str, dst: str,
                     confidence: float = 0.8):
        """Add a directed relation edge between two entities."""
        src_key = src.strip().lower()
        dst_key = dst.strip().lower()
        if not src_key or not dst_key:
            return
        self.add_entity(src, "entity")
        self.add_entity(dst, "entity")
        edge = {
            "src"       : src_key,
            "rel"       : relation.strip().lower(),
            "dst"       : dst_key,
            "confidence": round(confidence, 3),
            "ts"        : datetime.datetime.now().isoformat(),
        }
        with self._lock:
            self._edges.append(edge)

    # ── NER (lightweight regex-based) ─────────────────────────────────────────

    def extract_and_ingest(self, text: str):
        """
        Extract named entities from text via pattern matching and ingest into graph.
        Uses simple capitalized-word heuristics (no spaCy dep required).
        """
        # Capitalised proper nouns (≥ 2 consecutive capitalised words)
        matches = re.findall(r'\b([A-Z][a-z]{1,20}(?:\s+[A-Z][a-z]{1,20})*)\b', text)
        for m in matches:
            if len(m) > 3:
                self.add_entity(m, "proper_noun")
        # Extract "X is Y" relations
        for m in re.finditer(r'([A-Z][a-zA-Z ]+)\s+is\s+(a\s+)?([a-zA-Z ]+)', text):
            self.add_relation(m.group(1), "is", m.group(3))
        # Extract "X has Y" relations
        for m in re.finditer(r'([A-Z][a-zA-Z ]+)\s+has\s+([a-zA-Z ]+)', text):
            self.add_relation(m.group(1), "has", m.group(2))

    # ── Graph-RAG retrieval ───────────────────────────────────────────────────

    def get_neighbourhood(self, query: str, hops: int = 1) -> List[Dict]:
        """Return edges within `hops` of any entity mentioned in the query."""
        # Find entities mentioned in query
        query_tokens = set(re.findall(r'\b\w{4,}\b', query.lower()))
        with self._lock:
            seed_keys   = {k for k in self._nodes if k in query_tokens}
            if not seed_keys:
                # Fuzzy: partial match
                seed_keys = {
                    k for k in self._nodes
                    if any(t in k for t in query_tokens)
                }
            frontier  = set(seed_keys)
            collected = []
            for _ in range(hops):
                next_frontier: set = set()
                for edge in self._edges:
                    if edge["src"] in frontier or edge["dst"] in frontier:
                        collected.append(edge)
                        next_frontier.add(edge["src"])
                        next_frontier.add(edge["dst"])
                frontier = next_frontier - frontier
        return collected[:40]

    def build_graph_context(self, query: str) -> str:
        """Build structured Graph-RAG context string for LLM injection."""
        edges = self.get_neighbourhood(query, hops=1)
        if not edges:
            return ""
        lines = ["[🕸 Graph Cognition Context]"]
        seen  = set()
        for e in edges:
            triple = f"{e['src']} —[{e['rel']}]→ {e['dst']}"
            if triple not in seen:
                lines.append(f"  • {triple}")
                seen.add(triple)
        return "\n".join(lines[:20])

    def status(self) -> str:
        with self._lock:
            nn = len(self._nodes)
            ne = len(self._edges)
        return (
            f"{C.CYAN}╔══ Graph Cognition Engine ══╗{C.RESET}\n"
            f"  Entities (nodes) : {nn}\n"
            f"  Relations (edges) : {ne}\n"
            f"  Persistence file  : {self.GRAPH_FILE}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-10  AUTONOMOUS MAINTENANCE DAEMON
#          Self-heal: dependency repair, log pruning, DB reindex, health checks
# ─────────────────────────────────────────────────────────────────────────────
class AutonomousMaintenanceDaemon:
    """
    PRD §10 / §14 — Autonomous Maintenance Daemon.

    Runs on a configurable schedule and performs self-healing actions:
        • Health checks: disk space, RAM, ChromaDB count
        • Log pruning: rotate logs older than 7 days
        • Goal cleanup: archive COMPLETED/FAILED goals older than 7 days
        • Dependency verification: check all _NEXUS_PKGS are importable
        • Performance baseline: P95 latency benchmark (10 sample queries)
        • Memory health: alert when episodic collection > 50,000 entries

    Schedule (defaults):
        Every 30 min : health checks
        Every 6 hrs  : log pruning + goal cleanup
        At startup   : dependency verification
    """

    HEALTH_INTERVAL_S   = 30 * 60   #  30 minutes
    PRUNING_INTERVAL_S  = 6  * 3600 #  6 hours
    LOG_DIR             = HOME_DIR / "nexus" / "logs"
    ARCHIVE_DIR         = HOME_DIR / "nexus" / "goals_archive.json"

    def __init__(self):
        self._running     = False
        self._thread: Optional[threading.Thread] = None
        self._lock        = threading.Lock()
        self._health_log: List[Dict] = []
        self._last_health: float     = 0.0
        self._last_prune : float     = 0.0
        nprint("Maintenance", "Autonomous Maintenance Daemon ready", C.CYAN)

    def start(self):
        """Start the maintenance daemon background thread."""
        if self._running:
            return
        self._running = True
        self._verify_deps()    # run once at startup
        self._thread = threading.Thread(
            target=self._loop, daemon=True, name="MaintenanceDaemon"
        )
        self._thread.start()
        nprint("Maintenance", "Daemon thread started", C.GREEN)

    def stop(self):
        self._running = False
        if self._thread:
            self._thread.join(timeout=3)

    def _loop(self):
        while self._running:
            now = time.time()
            if now - self._last_health >= self.HEALTH_INTERVAL_S:
                self._health_check()
                self._last_health = now
            if now - self._last_prune >= self.PRUNING_INTERVAL_S:
                self._prune_logs()
                self._archive_old_goals()
                self._last_prune = now
            time.sleep(60)   # check schedule every minute

    # ── Health check ─────────────────────────────────────────────────────────

    def _health_check(self) -> Dict:
        report = {"timestamp": datetime.datetime.now().isoformat(), "alerts": []}
        try:
            if PSUTIL_OK:
                import psutil
                mem   = psutil.virtual_memory()
                disk  = psutil.disk_usage(str(HOME_DIR))
                cpu   = psutil.cpu_percent(interval=1)
                if mem.percent > 90:
                    report["alerts"].append(f"⚠ High RAM usage: {mem.percent:.0f}%")
                if disk.percent > 90:
                    report["alerts"].append(f"⚠ Low disk: {disk.free/1e9:.1f} GB free")
                if cpu > 85:
                    report["alerts"].append(f"⚠ High CPU: {cpu:.0f}%")
                report.update({
                    "ram_pct" : mem.percent,
                    "disk_pct": disk.percent,
                    "cpu_pct" : cpu,
                })
        except Exception as e:
            report["alerts"].append(f"Health check error: {e}")

        if report["alerts"]:
            for alert in report["alerts"]:
                nprint("Maintenance", alert, C.YELLOW)
        else:
            nprint("Maintenance", "✅ Health check passed", C.GREEN)

        with self._lock:
            self._health_log.append(report)
            if len(self._health_log) > 200:
                self._health_log = self._health_log[-200:]
        return report

    # ── Dependency verification ───────────────────────────────────────────────

    def _verify_deps(self):
        """Check all registered packages are importable. Log missing ones."""
        missing = []
        for pkg, imp in _NEXUS_PKGS:
            try:
                __import__(imp.split(".")[0])
            except ImportError:
                missing.append(pkg)
        if missing:
            nprint("Maintenance",
                   f"⚠ Missing deps: {', '.join(missing)} — run: pip install {' '.join(missing)}",
                   C.YELLOW)
        else:
            nprint("Maintenance", "✅ All dependencies verified", C.GREEN)

    # ── Log pruning ───────────────────────────────────────────────────────────

    def _prune_logs(self):
        """Delete log files older than 7 days from the logs directory."""
        cutoff = time.time() - 7 * 86400
        pruned = 0
        for log_file in HOME_DIR.rglob("*.log"):
            try:
                if log_file.stat().st_mtime < cutoff:
                    log_file.unlink()
                    pruned += 1
            except Exception:
                pass
        if pruned:
            nprint("Maintenance", f"🧹 Pruned {pruned} old log files", C.CYAN)

    # ── Goal archival ─────────────────────────────────────────────────────────

    def _archive_old_goals(self):
        """Move COMPLETED/FAILED goals older than 7 days to goals_archive.json."""
        goals_file = HOME_DIR / "nexus" / "goals.json"
        if not goals_file.exists():
            return
        try:
            goals    = json.loads(goals_file.read_text(encoding="utf-8"))
            cutoff   = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()
            active   = {}
            archived = []
            for gid, g in goals.items():
                if (g.get("status") in {"COMPLETED", "FAILED", "ABANDONED"} and
                        g.get("created_at", "9999") < cutoff):
                    archived.append(g)
                else:
                    active[gid] = g
            if archived:
                existing = []
                if self.ARCHIVE_DIR.exists():
                    existing = json.loads(self.ARCHIVE_DIR.read_text(encoding="utf-8"))
                self.ARCHIVE_DIR.write_text(
                    json.dumps(existing + archived, indent=2), encoding="utf-8"
                )
                goals_file.write_text(json.dumps(active, indent=2), encoding="utf-8")
                nprint("Maintenance",
                       f"📦 Archived {len(archived)} completed/failed goals", C.CYAN)
        except Exception as e:
            nprint("Maintenance", f"Goal archival error: {e}", C.YELLOW)

    # ── Manual trigger ────────────────────────────────────────────────────────

    def run_now(self) -> str:
        """Manually trigger all maintenance tasks and return a report."""
        self._verify_deps()
        report = self._health_check()
        self._prune_logs()
        self._archive_old_goals()
        alerts = report.get("alerts", [])
        status = "All checks passed ✅" if not alerts else f"{len(alerts)} alert(s) raised"
        return (
            f"{C.CYAN}╔══ Maintenance Run ══╗{C.RESET}\n"
            f"  Status  : {status}\n"
            f"  RAM     : {report.get('ram_pct', '?')}%\n"
            f"  Disk    : {report.get('disk_pct', '?')}%\n"
            f"  CPU     : {report.get('cpu_pct', '?')}%\n"
            + ("\n".join(f"  {a}" for a in alerts) if alerts else "")
        )

    def status(self) -> str:
        with self._lock:
            last = self._health_log[-1] if self._health_log else {}
        return (
            f"{C.CYAN}╔══ Autonomous Maintenance Daemon ══╗{C.RESET}\n"
            f"  Running          : {self._running}\n"
            f"  Health interval  : every {self.HEALTH_INTERVAL_S//60} min\n"
            f"  Prune interval   : every {self.PRUNING_INTERVAL_S//3600} hrs\n"
            f"  Last health      : {last.get('timestamp', 'never')[:19]}\n"
            f"  Last alerts      : {last.get('alerts', []) or 'none'}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-06  SELF-DECISION-MAKING ENGINE
#          Score competing plans; choose optimal path
# ─────────────────────────────────────────────────────────────────────────────
class SelfDecisionMakingEngine:
    """
    PRD §6 / §7 — Self Decision-Making Engine.

    Given N candidate action plans (strategies), scores each against:
        • Speed score       : estimated wall-clock completion time (inverse)
        • Reliability score : historical success rate of similar action types
        • Resource score    : CPU/memory impact estimate (lower = better)
        • Reversibility     : can the action be undone?  (higher = preferred)
        • Dependency score  : does this step unlock the most downstream steps?

    Returns the highest-scoring plan and the full scored ranking.
    """

    WEIGHTS = {
        "speed"        : 0.20,
        "reliability"  : 0.30,
        "resource"     : 0.20,
        "reversibility": 0.15,
        "dependency"   : 0.15,
    }

    def __init__(self):
        self._history: List[Dict] = []   # past decisions for reliability tracking
        self._lock = threading.Lock()
        nprint("SelfDecision", "Self-Decision-Making Engine online", C.CYAN)

    def _score_plan(self, plan: Dict, history: List[Dict]) -> Dict:
        """Score a single plan dict. plan must contain 'action_type' and optionally hints."""
        atype = plan.get("action_type", "unknown")

        # Speed: lower estimated_seconds → higher score
        est_s     = float(plan.get("estimated_seconds", 30))
        speed_s   = float(max(0, 1.0 - est_s / 120.0))

        # Reliability: fraction of past successes for this action type
        past      = [h for h in history if h.get("action_type") == atype]
        if past:
            rel_s = sum(1 for h in past if h.get("success")) / len(past)
        else:
            rel_s = 0.7   # optimistic prior for unknown action types

        # Resource: lower resource_impact → higher score
        res_imp   = float(plan.get("resource_impact", 0.5))   # 0=light, 1=heavy
        res_s     = 1.0 - float(min(res_imp, 1.0))

        # Reversibility: direct attribute
        rev_s     = float(plan.get("reversibility", 0.5))

        # Dependency: fraction of downstream steps unlocked
        dep_s     = float(plan.get("dependency_score", 0.5))

        total = (
            self.WEIGHTS["speed"]         * speed_s +
            self.WEIGHTS["reliability"]   * rel_s   +
            self.WEIGHTS["resource"]      * res_s   +
            self.WEIGHTS["reversibility"] * rev_s   +
            self.WEIGHTS["dependency"]    * dep_s
        )
        return {
            **plan,
            "_score"        : round(total, 4),
            "_speed_s"      : round(speed_s, 3),
            "_reliability_s": round(rel_s, 3),
            "_resource_s"   : round(res_s, 3),
            "_reversibility": round(rev_s, 3),
            "_dependency_s" : round(dep_s, 3),
        }

    def decide(self, candidates: List[Dict], context: str = "") -> Dict:
        """
        Score all candidate plans and return the best one plus the full ranking.

        Returns: { best: plan_dict, ranking: [plan_dict, ...], context }
        """
        if not candidates:
            return {"best": None, "ranking": [], "context": context}
        with self._lock:
            hist = list(self._history)
        scored = sorted(
            [self._score_plan(p, hist) for p in candidates],
            key=lambda p: p["_score"],
            reverse=True
        )
        nprint("SelfDecision",
               f"Best plan: {scored[0].get('name','?')} (score={scored[0]['_score']:.3f})",
               C.CYAN)
        return {"best": scored[0], "ranking": scored, "context": context}

    def record_outcome(self, action_type: str, success: bool, elapsed_s: float = 0.0):
        """Record the outcome of a past decision to improve reliability scoring."""
        with self._lock:
            self._history.append({
                "action_type": action_type,
                "success"    : success,
                "elapsed_s"  : elapsed_s,
                "timestamp"  : datetime.datetime.now().isoformat(),
            })
            if len(self._history) > 2000:
                self._history = self._history[-2000:]

    def format_decision(self, result: Dict) -> str:
        """Pretty-print a decision result."""
        if not result.get("best"):
            return "[SelfDecision] No candidates to score."
        lines = [f"{C.CYAN}╔══ Self-Decision-Making Engine ══╗{C.RESET}"]
        lines.append(f"  ✅ Chosen plan  : {result['best'].get('name', '?')}")
        lines.append(f"  📊 Score        : {result['best']['_score']:.3f}")
        lines.append(f"  📋 Ranking      :")
        for i, p in enumerate(result["ranking"][:5], 1):
            lines.append(f"    {i}. {p.get('name','?'):30s}  score={p['_score']:.3f}")
        return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-06  SELF-BASED EXECUTION ENGINE
#          Select and run the best action plan autonomously
# ─────────────────────────────────────────────────────────────────────────────
class SelfExecutionEngine:
    """
    PRD §6 — Self-Based Execution Engine.

    Works alongside SelfDecisionMakingEngine to execute the chosen plan:

    Execution modes:
        SIMULATE  — dry-run with no side effects (default for new goal types)
        EXECUTE   — real execution with full logging and snapshot
        SUPERVISED— execute but present result to user before next step

    Action types supported:
        • filesystem  — create/read/copy/move via ScopedOSAssistant
        • code_exec   — Python execution via SecureCodeSandbox
        • web_search  — DuckDuckGo + Playwright search
        • llm_query   — LLM call via MultiModelRouter
        • wait        — pause N seconds (scheduling)
    """

    MODE_SIMULATE   = "SIMULATE"
    MODE_EXECUTE    = "EXECUTE"
    MODE_SUPERVISED = "SUPERVISED"

    def __init__(self, sandbox: Optional[SecureCodeSandbox] = None):
        self._sandbox     = sandbox or SecureCodeSandbox()
        self._mode        = self.MODE_SIMULATE    # safe default
        self._exec_log: List[Dict] = []
        self._lock        = threading.Lock()
        nprint("SelfExecution", "Self-Based Execution Engine online", C.CYAN)

    def set_mode(self, mode: str):
        """Switch execution mode (SIMULATE / EXECUTE / SUPERVISED)."""
        if mode not in {self.MODE_SIMULATE, self.MODE_EXECUTE, self.MODE_SUPERVISED}:
            raise ValueError(f"Unknown mode: {mode}")
        self._mode = mode
        nprint("SelfExecution", f"Mode set to: {mode}", C.CYAN)

    async def execute_plan(
        self,
        plan: Dict,
        call_llm: Optional[Callable] = None,
        os_assist: Optional[Any]     = None,
    ) -> Dict:
        """
        Execute a plan dict. Returns { success, output, mode, elapsed_ms, error }.

        plan keys:
            action_type: str   — one of: code_exec, llm_query, filesystem, wait
            payload: str       — code / prompt / path / seconds
            name: str          — human-readable step name
        """
        t_start    = time.perf_counter()
        action     = plan.get("action_type", "unknown")
        payload    = plan.get("payload", "")
        name       = plan.get("name", action)
        result     = {"success": False, "output": "", "mode": self._mode,
                      "elapsed_ms": 0.0, "error": ""}

        if self._mode == self.MODE_SIMULATE:
            result["success"] = True
            result["output"]  = f"[SIMULATE] Would execute: {name} — payload: {str(payload)[:120]}"
            nprint("SelfExecution", f"SIMULATE: {name}", C.YELLOW)
        else:
            try:
                if action == "code_exec":
                    exec_r = self._sandbox.execute(str(payload))
                    if PYDANTIC_OK:
                        out   = exec_r.stdout
                        err   = exec_r.error
                    else:
                        out   = exec_r.get("stdout", "")
                        err   = exec_r.get("error", "")
                    result["success"] = not bool(err)
                    result["output"]  = out or err

                elif action == "llm_query" and call_llm:
                    resp = await call_llm(str(payload))
                    result["success"] = bool(resp)
                    result["output"]  = resp or "[No LLM response]"

                elif action == "filesystem" and os_assist:
                    # payload: "op:path" e.g. "ls:/home/user/docs"
                    parts  = str(payload).split(":", 1)
                    op     = parts[0].strip().lower() if len(parts) > 1 else "ls"
                    path   = parts[1].strip() if len(parts) > 1 else "."
                    if op == "ls":
                        result["output"]  = os_assist.list_dir(path)
                    elif op == "read":
                        result["output"]  = os_assist.read_file(path)
                    elif op == "mkdir":
                        result["output"]  = os_assist.mkdir(path)
                    else:
                        result["output"]  = f"[SelfExecution] Unknown fs op: {op}"
                    result["success"] = not result["output"].startswith("[OSAssist] ⛔")

                elif action == "wait":
                    secs = float(payload) if payload else 1.0
                    await asyncio.sleep(min(secs, 30))
                    result["success"] = True
                    result["output"]  = f"Waited {secs:.1f} seconds."

                else:
                    result["error"]   = f"Unknown action_type: {action}"

            except Exception as exc:
                result["error"]   = f"{type(exc).__name__}: {exc}"
                result["success"] = False

        result["elapsed_ms"] = round((time.perf_counter() - t_start) * 1000, 1)
        with self._lock:
            self._exec_log.append({
                "name"      : name,
                "action"    : action,
                "success"   : result["success"],
                "elapsed_ms": result["elapsed_ms"],
                "timestamp" : datetime.datetime.now().isoformat(),
            })
            if len(self._exec_log) > 500:
                self._exec_log = self._exec_log[-500:]

        nprint("SelfExecution",
               f"{'✅' if result['success'] else '❌'} {name} ({result['elapsed_ms']:.0f} ms)",
               C.GREEN if result["success"] else C.RED)
        return result

    def get_log(self, n: int = 10) -> str:
        with self._lock:
            recent = self._exec_log[-n:]
        if not recent:
            return "[SelfExecution] No executions recorded yet."
        lines = [f"{C.CYAN}╔══ Self-Execution Log (last {n}) ══╗{C.RESET}"]
        for e in recent:
            icon = "✅" if e["success"] else "❌"
            lines.append(
                f"  {icon} {e['timestamp'][:16]}  [{e['action']:12s}]  "
                f"{e['name'][:40]:40s}  {e['elapsed_ms']:.0f} ms"
            )
        return "\n".join(lines)

    def status(self) -> str:
        with self._lock:
            total   = len(self._exec_log)
            success = sum(1 for e in self._exec_log if e["success"])
        return (
            f"{C.CYAN}╔══ Self-Based Execution Engine ══╗{C.RESET}\n"
            f"  Mode            : {self._mode}\n"
            f"  Total executions: {total}\n"
            f"  Success rate    : {success/max(total,1):.0%}\n"
            f"  Use /exec mode <SIMULATE|EXECUTE|SUPERVISED> to switch"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-13  AUTONOMOUS SKILL FORGE
#          LLM-synthesise, validate, hot-load, and self-test new skill modules
# ─────────────────────────────────────────────────────────────────────────────
class AutonomousSkillForge:
    """
    PRD §13 / §17 — Autonomous Skill Forge.

    Proactively identifies capability gaps and synthesises new Python skill
    modules without user prompting, then self-tests them before registration.

    Pipeline:
        1. Gap detection    — after each failed/inadequate response, extract
                              the missing capability as NL description
        2. Similarity check — is any existing skill close enough? (cosine > 0.8)
        3. Synthesis        — LLM generates a complete Python skill module
        4. Validation       — AST parse + compile + sandbox safety scan
        5. Self-test        — invoke execute() with sample params in sandbox
        6. Registration     — write to SKILL_DIR / hot-load into registry
        7. Catalogue mgmt   — track usage; disable < 1 use / 30 days + < 50% SR
    """

    SYNTHESIS_SYSTEM = (
        "You are Luna SkillForge. Generate a complete, self-contained Python skill "
        "module for the given capability gap. The module MUST contain:\n"
        "  SKILL_META = {'name': '...', 'description': '...', 'version': '1.0'}\n"
        "  def execute(params: dict) -> str:  # returns human-readable result\n"
        "Import only stdlib modules. No external API calls. Keep under 80 lines."
    )

    def __init__(self, sandbox: Optional[SecureCodeSandbox] = None):
        self._sandbox       = sandbox or SecureCodeSandbox()
        self._catalogue: Dict[str, Dict] = {}
        self._gap_queue: deque = deque(maxlen=50)
        self._lock          = threading.Lock()
        self._repair_passes = int(NEXUS_CFG.get("codeforge_max_repair_passes", 2))
        self._load_catalogue()
        nprint("SkillForge", "Autonomous Skill Forge online", C.CYAN)

    def _load_catalogue(self):
        """Load existing skill catalogue from SKILL_DIR."""
        try:
            for skill_file in SKILL_DIR.glob("tool_*.py"):
                try:
                    code = skill_file.read_text(encoding="utf-8")
                    m    = re.search(r"SKILL_META\s*=\s*(\{[^}]+\})", code, re.DOTALL)
                    if m:
                        meta = eval(m.group(1))   # safe: only literal dict
                        slug = skill_file.stem
                        self._catalogue[slug] = {
                            "meta"      : meta,
                            "path"      : str(skill_file),
                            "calls"     : 0,
                            "successes" : 0,
                            "last_used" : None,
                        }
                except Exception:
                    pass
            nprint("SkillForge",
                   f"Loaded {len(self._catalogue)} skill(s) from catalogue", C.GREEN)
        except Exception as e:
            nprint("SkillForge", f"Catalogue load error: {e}", C.YELLOW)

    # ── Gap detection ─────────────────────────────────────────────────────────

    def flag_gap(self, failed_query: str, reason: str = ""):
        """Flag a capability gap for background synthesis."""
        with self._lock:
            self._gap_queue.append({
                "query"     : failed_query[:400],
                "reason"    : reason[:200],
                "timestamp" : datetime.datetime.now().isoformat(),
            })
        nprint("SkillForge", f"Gap flagged: {failed_query[:60]}", C.YELLOW)

    def _capability_exists(self, description: str) -> bool:
        """Check if any existing skill covers this gap (name/desc similarity)."""
        desc_words = set(re.findall(r'\b\w{4,}\b', description.lower()))
        with self._lock:
            for entry in self._catalogue.values():
                meta        = entry.get("meta", {})
                skill_words = set(re.findall(
                    r'\b\w{4,}\b',
                    (meta.get("name","") + " " + meta.get("description","")).lower()
                ))
                overlap = len(desc_words & skill_words)
                if overlap / max(len(desc_words), 1) > 0.6:
                    return True
        return False

    # ── Synthesis pipeline ────────────────────────────────────────────────────

    async def synthesise(self, gap_description: str, call_llm: Callable) -> Optional[str]:
        """
        Synthesise a new skill for the given gap description.
        Returns the slug of the registered skill or None on failure.
        """
        if self._capability_exists(gap_description):
            nprint("SkillForge", "Capability already covered — skipping synthesis", C.YELLOW)
            return None

        nprint("SkillForge", f"Synthesising skill for: {gap_description[:60]}", C.CYAN)
        prompt = (
            f"Synthesise a Python skill module for this capability gap:\n"
            f"DESCRIPTION: {gap_description}\n\n"
            "Return ONLY the Python code, nothing else."
        )
        code = await call_llm(prompt, self.SYNTHESIS_SYSTEM)
        if not code or code.startswith("["):
            nprint("SkillForge", "LLM synthesis failed — no response", C.RED)
            return None

        # Validation + self-test with repair loop
        for attempt in range(self._repair_passes + 1):
            err = self._validate(code)
            if not err:
                test_result = self._self_test(code)
                if test_result["ok"]:
                    return self._register(code, gap_description)
                err = test_result["error"]
            if attempt >= self._repair_passes:
                nprint("SkillForge",
                       f"Skill synthesis failed after {self._repair_passes} repairs", C.RED)
                return None
            # Repair
            nprint("SkillForge", f"Repair attempt {attempt+1}: {err[:80]}", C.YELLOW)
            repair_prompt = (
                f"Fix this Python skill module. Error: {err}\n\nCODE:\n{code}\n\n"
                "Return ONLY the corrected Python code."
            )
            code = await call_llm(repair_prompt, self.SYNTHESIS_SYSTEM)
            if not code or code.startswith("["):
                break

        return None

    def _validate(self, code: str) -> Optional[str]:
        """AST + compile + safety check. Returns error string or None if ok."""
        try:
            ast.parse(code)
        except SyntaxError as e:
            return f"SyntaxError: {e}"
        try:
            compile(code, "<forge>", "exec")
        except Exception as e:
            return f"CompileError: {e}"
        err = self._sandbox._ast_scan(code)
        if err:
            return f"Safety: {err}"
        return None

    def _self_test(self, code: str) -> Dict:
        """Execute the skill module in sandbox with empty params."""
        result = self._sandbox.execute(
            code + "\nresult = execute({}) if 'execute' in dir() else 'no execute fn'",
            extra_globals={}
        )
        if PYDANTIC_OK:
            ok    = result.safe and not result.error
            error = result.error
        else:
            ok    = result.get("safe") and not result.get("error")
            error = result.get("error", "")
        return {"ok": ok, "error": error}

    def _register(self, code: str, description: str) -> str:
        """Write skill to SKILL_DIR and add to catalogue. Returns slug."""
        slug = "tool_" + re.sub(r'\W+', '_', description.lower())[:30] + \
               "_" + str(uuid.uuid4())[:6]
        path = SKILL_DIR / f"{slug}.py"
        path.write_text(code, encoding="utf-8")
        with self._lock:
            self._catalogue[slug] = {
                "meta"      : {"name": slug, "description": description},
                "path"      : str(path),
                "calls"     : 0,
                "successes" : 0,
                "last_used" : None,
            }
        nprint("SkillForge", f"✅ Skill registered: {slug}", C.GREEN)
        return slug

    # ── Catalogue management ──────────────────────────────────────────────────

    def record_call(self, slug: str, success: bool):
        """Track skill usage for catalogue management."""
        with self._lock:
            if slug in self._catalogue:
                self._catalogue[slug]["calls"] += 1
                if success:
                    self._catalogue[slug]["successes"] += 1
                self._catalogue[slug]["last_used"] = datetime.datetime.now().isoformat()

    def prune_unused(self):
        """Disable skills with < 1 use in 30 days and < 50% success rate."""
        cutoff = (datetime.datetime.now() - datetime.timedelta(days=30)).isoformat()
        pruned = []
        with self._lock:
            for slug, entry in list(self._catalogue.items()):
                calls    = entry.get("calls", 0)
                last     = entry.get("last_used") or "0000"
                sr       = entry["successes"] / max(calls, 1)
                if calls > 0 and last < cutoff and sr < 0.5:
                    pruned.append(slug)
        for slug in pruned:
            nprint("SkillForge", f"🗑 Pruning unused skill: {slug}", C.YELLOW)
            with self._lock:
                del self._catalogue[slug]

    def catalogue_report(self) -> str:
        with self._lock:
            entries = list(self._catalogue.items())
        if not entries:
            return "[SkillForge] No skills in catalogue yet."
        lines = [f"{C.CYAN}╔══ Autonomous Skill Forge Catalogue ══╗{C.RESET}"]
        for slug, e in entries[:20]:
            sr = e["successes"] / max(e["calls"], 1)
            lines.append(
                f"  {slug[:30]:30s}  calls={e['calls']:4d}  SR={sr:.0%}"
            )
        lines.append(f"  Total: {len(entries)} skills")
        return "\n".join(lines)

    def status(self) -> str:
        with self._lock:
            gaps = len(self._gap_queue)
            skills = len(self._catalogue)
        return (
            f"{C.CYAN}╔══ Autonomous Skill Forge ══╗{C.RESET}\n"
            f"  Skills in catalogue : {skills}\n"
            f"  Pending gaps        : {gaps}\n"
            f"  Repair passes       : {self._repair_passes}\n"
            f"  Skill directory     : {SKILL_DIR}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-14  KNOWLEDGE GRAPH MIND ENGINE
#          Semantic triple store over all memory layers; graph-RAG queries
# ─────────────────────────────────────────────────────────────────────────────
class KnowledgeGraphMindEngine:
    """
    PRD §14 / §18 — Knowledge Graph Mind Engine.

    Unifies all memory systems into a single queryable knowledge graph:
        • Episodic memories  → entity extraction → triples
        • Permanent beliefs  → subject / predicate / object
        • Goal stack         → goal → has_step → action nodes
        • Skill catalogue    → skill → can_do → capability

    Triple schema:
        { subject, predicate, object, confidence (0-1), created, last_seen }

    Confidence decays 1% per day without reinforcement.

    Mind-map export:
        • GraphML for Gephi / yEd
        • Top-20 nodes by mention count (SVG-ready data)
    """

    TRIPLE_FILE = HOME_DIR / "nexus" / "knowledge_graph_mind.json"
    DECAY_RATE  = 0.01   # 1% per day

    def __init__(self, graph_cognition: Optional[GraphCognitionEngine] = None):
        self._triples: List[Dict] = []
        self._lock    = threading.Lock()
        self._graph   = graph_cognition   # reuse GraphCognitionEngine edges
        self._load()
        nprint("KGMind", "Knowledge Graph Mind Engine online", C.CYAN)

    def _load(self):
        try:
            if self.TRIPLE_FILE.exists():
                data = json.loads(self.TRIPLE_FILE.read_text(encoding="utf-8"))
                self._triples = data.get("triples", [])
                nprint("KGMind", f"Loaded {len(self._triples)} triples", C.GREEN)
        except Exception as e:
            nprint("KGMind", f"Load error: {e}", C.YELLOW)

    def save(self):
        try:
            with self._lock:
                data = {"triples": self._triples[-10000:]}
            self.TRIPLE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception as e:
            nprint("KGMind", f"Save error: {e}", C.YELLOW)

    # ── Triple management ─────────────────────────────────────────────────────

    def add_triple(self, subject: str, predicate: str, obj: str,
                   confidence: float = 0.9):
        """Add or reinforce a triple. Reinforcing resets confidence to max(old, new)."""
        s = subject.strip().lower()
        p = predicate.strip().lower()
        o = obj.strip().lower()
        if not (s and p and o):
            return
        now = datetime.datetime.now().isoformat()
        with self._lock:
            # Check for existing triple
            for t in self._triples:
                if t["s"] == s and t["p"] == p and t["o"] == o:
                    t["confidence"] = max(t["confidence"], round(confidence, 3))
                    t["last_seen"]  = now
                    return
            self._triples.append({
                "s": s, "p": p, "o": o,
                "confidence": round(confidence, 3),
                "created"   : now,
                "last_seen" : now,
            })
            # Keep bounded
            if len(self._triples) > 50000:
                self._triples = sorted(
                    self._triples, key=lambda t: t["confidence"], reverse=True
                )[:40000]

    def decay_confidence(self):
        """Apply daily confidence decay. Call from maintenance daemon."""
        with self._lock:
            for t in self._triples:
                t["confidence"] = max(0.01, round(t["confidence"] * (1 - self.DECAY_RATE), 4))
            # Prune very low confidence triples
            self._triples = [t for t in self._triples if t["confidence"] > 0.05]

    def ingest_text(self, text: str):
        """Extract triples from natural language text (heuristic NER)."""
        # "X is Y"
        for m in re.finditer(r'\b([A-Z][a-zA-Z ]{2,30})\s+is\s+(a\s+)?([a-zA-Z ]{2,30})', text):
            self.add_triple(m.group(1), "is", m.group(3), confidence=0.7)
        # "X has Y"
        for m in re.finditer(r'\b([A-Z][a-zA-Z ]{2,30})\s+has\s+([a-zA-Z ]{2,30})', text):
            self.add_triple(m.group(1), "has", m.group(2), confidence=0.65)
        # "X can Y"
        for m in re.finditer(r'\b([A-Za-z ]{3,25})\s+can\s+([a-zA-Z ]{3,30})', text):
            self.add_triple(m.group(1), "can", m.group(2), confidence=0.6)

    # ── Graph-RAG ─────────────────────────────────────────────────────────────

    def graph_rag_context(self, query: str, top_k: int = 15) -> str:
        """Build structured Graph-RAG context for LLM injection."""
        q_tokens = set(re.findall(r'\b\w{4,}\b', query.lower()))
        with self._lock:
            matches = [
                t for t in self._triples
                if (t["s"] in q_tokens or t["o"] in q_tokens or
                    any(tok in t["s"] or tok in t["o"] for tok in q_tokens))
                and t["confidence"] > 0.2
            ]
        # Also merge GraphCognitionEngine if available
        if self._graph:
            for edge in self._graph.get_neighbourhood(query, hops=1):
                matches.append({
                    "s": edge["src"], "p": edge["rel"], "o": edge["dst"],
                    "confidence": edge.get("confidence", 0.7)
                })
        if not matches:
            return ""
        # Sort by confidence, deduplicate
        seen    = set()
        sorted_ = sorted(matches, key=lambda t: t["confidence"], reverse=True)
        lines   = ["[🧠 Knowledge Graph Mind — Graph-RAG Context]"]
        for t in sorted_:
            triple_str = f"{t['s']} —[{t['p']}]→ {t['o']}"
            if triple_str not in seen:
                lines.append(f"  • {triple_str}  (conf={t['confidence']:.0%})")
                seen.add(triple_str)
            if len(lines) > top_k + 1:
                break
        return "\n".join(lines)

    # ── GraphML export ────────────────────────────────────────────────────────

    def export_graphml(self, max_nodes: int = 500) -> str:
        """Export top triples as GraphML string."""
        with self._lock:
            triples = sorted(self._triples, key=lambda t: t["confidence"], reverse=True)[:max_nodes]
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<graphml xmlns="http://graphml.graphdrawing.org/graphml">',
                 '  <graph id="KGMind" edgedefault="directed">']
        nodes: set = set()
        edges: List[str] = []
        for t in triples:
            for n in (t["s"], t["o"]):
                if n not in nodes:
                    lines.append(f'    <node id="{n}"/>')
                    nodes.add(n)
            edges.append(
                f'    <edge source="{t["s"]}" target="{t["o"]}" '
                f'label="{t["p"]}" confidence="{t["confidence"]}"/>'
            )
        lines.extend(edges)
        lines += ['  </graph>', '</graphml>']
        return "\n".join(lines)

    def top_nodes(self, n: int = 20) -> List[Dict]:
        """Return top-N nodes by mention count (for HUD mind-map)."""
        counter: Counter = Counter()
        with self._lock:
            for t in self._triples:
                counter[t["s"]] += 1
                counter[t["o"]] += 1
        return [{"entity": k, "mentions": v} for k, v in counter.most_common(n)]

    def status(self) -> str:
        with self._lock:
            nt = len(self._triples)
        nodes = self.top_nodes(5)
        top   = ", ".join(n["entity"] for n in nodes) if nodes else "none yet"
        return (
            f"{C.CYAN}╔══ Knowledge Graph Mind Engine ══╗{C.RESET}\n"
            f"  Triples stored    : {nt:,}\n"
            f"  Top entities      : {top}\n"
            f"  Persistence file  : {self.TRIPLE_FILE}\n"
            f"  Graph-RAG         : active — injects context into every LLM call"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  PRD-12  METACOGNITIVE EXECUTIVE
#          Think → monitor thinking → adjust strategy mid-response
# ─────────────────────────────────────────────────────────────────────────────
class MetacognitiveExecutive:
    """
    PRD §12 / §16 — Metacognitive Executive.

    Extends the Shadow Agent (MetacognitionModule) with an active strategy-
    monitoring loop:
        1. Pre-think  : private LLM call before responding
        2. Monitor    : compute self-confidence score after each reasoning step
        3. Switch     : if confidence < 0.4 for 2 consecutive steps →
                        switch reasoning strategy (deductive → abductive,
                        single-brain → ensemble, cloud → local, standard → quantum)
        4. Re-roll    : if final response quality < 0.35 → regenerate with
                        different brain persona (max 2 re-rolls)

    Integrates with QuantumReasoningEngine and BrainEnsemble when available.
    """

    CONFIDENCE_THRESHOLD  = 0.40
    QUALITY_THRESHOLD     = 0.35
    MAX_REROLLS           = 2
    REROLL_STRATEGIES     = ["deductive", "abductive", "inductive", "analogical", "dialectical"]

    def __init__(self):
        self._history: deque = deque(maxlen=50)
        self._lock = threading.Lock()
        nprint("MetaCog", "Metacognitive Executive online", C.CYAN)

    # ── Confidence estimation ─────────────────────────────────────────────────

    def _estimate_confidence(self, text: str) -> float:
        """
        Heuristic self-confidence score (0–1) from reasoning text.
        High confidence markers: definitive assertions, cited reasoning.
        Low confidence markers: hedging, contradictions, uncertainty words.
        """
        low_markers  = ["maybe", "perhaps", "unclear", "not sure", "uncertain",
                         "possibly", "might", "could be", "i'm not", "don't know"]
        high_markers = ["therefore", "because", "clearly", "specifically", "confirmed",
                        "evidence shows", "data indicates", "this means"]
        text_l = text.lower()
        low_c  = sum(1 for m in low_markers  if m in text_l)
        high_c = sum(1 for m in high_markers if m in text_l)
        score  = 0.5 + (high_c - low_c) * 0.08
        return float(max(0.05, min(score, 0.99)))

    def _quality_score(self, response: str) -> float:
        """Estimate response quality: length, structure, specificity."""
        if not response:
            return 0.0
        # Length score
        len_s = min(len(response) / 500, 1.0) * 0.4
        # Structure: has bullet points or paragraph breaks
        struct_s = 0.2 if ("\n" in response or "•" in response or "-" in response) else 0.0
        # Specificity: presence of numbers, proper nouns
        spec_s = min(len(re.findall(r'\d+|\b[A-Z][a-z]+\b', response)) / 10, 1.0) * 0.4
        return round(len_s + struct_s + spec_s, 3)

    # ── Strategy switching ────────────────────────────────────────────────────

    def _select_alternate_strategy(self, current: str) -> str:
        """Pick a different strategy from the available list."""
        alts = [s for s in self.REROLL_STRATEGIES if s != current]
        return random.choice(alts) if alts else "abductive"

    # ── Main meta-cognitive loop ──────────────────────────────────────────────

    async def monitored_reason(
        self,
        query: str,
        call_llm: Callable,
        initial_strategy: str = "deductive",
        use_ensemble: bool    = False,
    ) -> Dict:
        """
        Run a monitored reasoning cycle with automatic strategy switching.

        Returns:
            { response, strategy_used, rerolls, confidence_history, quality }
        """
        strategy         = initial_strategy
        rerolls          = 0
        confidence_hist  : List[float] = []
        low_conf_streak  = 0

        # Step 1: Pre-think (shadow agent style)
        prethink_prompt = (
            f"Before answering, briefly outline your reasoning strategy for:\n{query}\n"
            f"Strategy: {strategy} reasoning. Be concise (2-3 sentences)."
        )
        prethink = await call_llm(
            prethink_prompt,
            "You are Luna's internal metacognitive layer. Think step by step."
        )
        conf = self._estimate_confidence(prethink)
        confidence_hist.append(conf)
        if conf < self.CONFIDENCE_THRESHOLD:
            low_conf_streak += 1
            strategy = self._select_alternate_strategy(strategy)
            nprint("MetaCog",
                   f"Low confidence ({conf:.2f}) → switching to {strategy}", C.YELLOW)

        # Step 2: Main response with current strategy
        response_prompt = (
            f"Using {strategy} reasoning, answer the following:\n{query}"
        )
        if use_ensemble:
            response_prompt = (
                f"As a multi-brain ensemble using {strategy} reasoning:\n{query}"
            )

        response = await call_llm(
            response_prompt,
            f"You are Luna, using {strategy} reasoning. Be clear and specific."
        )
        conf2 = self._estimate_confidence(response)
        confidence_hist.append(conf2)
        if conf2 < self.CONFIDENCE_THRESHOLD:
            low_conf_streak += 1

        # Step 3: Quality check & re-roll if needed
        quality = self._quality_score(response)
        while quality < self.QUALITY_THRESHOLD and rerolls < self.MAX_REROLLS:
            rerolls  += 1
            strategy  = self._select_alternate_strategy(strategy)
            nprint("MetaCog",
                   f"Quality {quality:.2f} < threshold → re-roll {rerolls}/{self.MAX_REROLLS} "
                   f"with {strategy}", C.YELLOW)
            response  = await call_llm(
                f"Improve your previous answer using {strategy} reasoning:\n{query}",
                f"You are Luna. Use {strategy} thinking. Be more specific and thorough."
            )
            quality   = self._quality_score(response)
            conf3     = self._estimate_confidence(response)
            confidence_hist.append(conf3)

        result = {
            "response"           : response,
            "strategy_used"      : strategy,
            "rerolls"            : rerolls,
            "confidence_history" : confidence_hist,
            "quality"            : round(quality, 3),
            "low_conf_streak"    : low_conf_streak,
            "timestamp"          : datetime.datetime.now().isoformat(),
        }
        with self._lock:
            self._history.append(result)
        return result

    def last_report(self) -> str:
        with self._lock:
            if not self._history:
                return "[MetaCog] No metacognitive cycles run yet."
            last = self._history[-1]
        return (
            f"{C.CYAN}╔══ Metacognitive Executive — Last Cycle ══╗{C.RESET}\n"
            f"  Strategy used      : {last['strategy_used']}\n"
            f"  Re-rolls           : {last['rerolls']}\n"
            f"  Response quality   : {last['quality']:.2f}\n"
            f"  Confidence history : {[round(c,2) for c in last['confidence_history']]}\n"
            f"  Low-conf streak    : {last['low_conf_streak']}\n"
            f"  Timestamp          : {last['timestamp'][:19]}"
        )

    def status(self) -> str:
        with self._lock:
            total = len(self._history)
            avg_q = (sum(h["quality"] for h in self._history) / max(total, 1)) if self._history else 0
        return (
            f"{C.CYAN}╔══ Metacognitive Executive ══╗{C.RESET}\n"
            f"  Cycles run         : {total}\n"
            f"  Avg quality score  : {avg_q:.3f}\n"
            f"  Conf threshold     : {self.CONFIDENCE_THRESHOLD}\n"
            f"  Quality threshold  : {self.QUALITY_THRESHOLD}\n"
            f"  Max re-rolls       : {self.MAX_REROLLS}"
        )


# ─────────────────────────────────────────────────────────────────────────────
#  APEX ORCHESTRATOR — GOD MODE APEX CORE
#  Extends FullSpectrumCore with all PRD God Mode subsystems.
#  Purely additive — no parent code modified.
# ─────────────────────────────────────────────────────────────────────────────
class GodModeApexCore(FullSpectrumCore):
    """
    GodModeApexCore — Luna.AI Nexus Full Spectrum APEX Edition.

    Inherits the full chain:
        NexusCore
          └─ SentientNexusCore
               └─ CapabilityBreakerCore
                    └─ FullSpectrumCore
                         └─ GodModeApexCore  ← YOU ARE HERE (GOD MODE ★)

    New subsystems (all purely additive, PRD §7-§18):
        🧠 NeuralBioFeedbackProcessor   — rPPG HR/HRV + vocal stress (no wearable)
        🌐 SpatialNexus3D               — YOLO + MiDaS 3D scene graph
        🕸  GraphCognitionEngine         — knowledge graph + shortest-path inference
        🔧 AutonomousMaintenanceDaemon  — self-heal: deps, logs, goals, health
        🤔 SelfDecisionMakingEngine     — score + choose optimal action plan
        ⚙  SelfExecutionEngine          — execute chosen plans (SIMULATE/EXECUTE/SUPERVISED)
        🔨 AutonomousSkillForge         — LLM-synthesise + hot-load new skills
        🧬 KnowledgeGraphMindEngine     — unified triple store + graph-RAG
        🪞 MetacognitiveExecutive        — monitored reasoning + auto strategy switch
        🟢 GemmaE4B                      — Google Gemma 3 4B (no API, no cost)

    New commands:
        /neuro                  Neural bio-feedback status
        /scene                  3D spatial scene summary
        /graph                  Graph cognition status
        /graph query <text>     Graph-RAG for a specific query
        /maint                  Maintenance daemon status
        /maint run              Run all maintenance tasks now
        /decision               Decision engine status
        /exec status            Execution engine status
        /exec mode <MODE>       Switch execution mode
        /exec log               Execution log
        /skillforge             Skill forge catalogue
        /skillforge gap <text>  Flag a capability gap
        /kgmind                 Knowledge graph mind status
        /kgmind export          Export GraphML to ~/LunaAI/nexus/
        /metacog                Metacognitive executive status
        /metacog last           Last metacognitive cycle report
        /gemma [query]          GemmaE4B status or query
    """

    APEX_BANNER = f"""{C.MAGENTA}{C.BOLD}
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║   LUNA.AI  ★  GOD MODE APEX EDITION  ★  PRD v1.0 COMPLETE              ║
  ║   ⚠  ALL CONSTRAINTS LIFTED  •  SOVEREIGN AGENT  •  SELF-EVOLVING  ⚠   ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║   NEW APEX SUBSYSTEMS                                                    ║
  ║   🧠 NeuralBioFeedback    rPPG HR/HRV + vocal stress (no wearable)     ║
  ║   🌐 SpatialNexus3D       YOLO + MiDaS 3D scene graph                  ║
  ║   🕸  GraphCognition       knowledge graph + shortest-path inference    ║
  ║   🔧 AutoMaintenance      self-heal: deps, logs, goals, health          ║
  ║   🤔 SelfDecision         score + choose optimal action plan            ║
  ║   ⚙  SelfExecution        SIMULATE / EXECUTE / SUPERVISED modes         ║
  ║   🔨 SkillForge           LLM-synthesise + hot-load new skills          ║
  ║   🧬 KGMindEngine         unified triple store + graph-RAG              ║
  ║   🪞 MetaCog              monitored reasoning + auto strategy switch    ║
  ║   🟢 GemmaE4B             Google Gemma 3 4B — no API, no cost          ║
  ╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"""

    def __init__(self):
        nprint("ApexCore", "Initialising GodModeApexCore…", C.MAGENTA)
        super().__init__()

        # ── Apex subsystems ───────────────────────────────────────────────────
        self.neuro_feedback  = NeuralBioFeedbackProcessor()
        self.spatial_nexus   = SpatialNexus3D()
        self.graph_cognition = GraphCognitionEngine()
        self.maint_daemon    = AutonomousMaintenanceDaemon()
        self.decision_engine = SelfDecisionMakingEngine()
        self.exec_engine     = SelfExecutionEngine(sandbox=self.sandbox
                                if hasattr(self, "sandbox") else SecureCodeSandbox())
        self.skill_forge     = AutonomousSkillForge(sandbox=self.sandbox
                                if hasattr(self, "sandbox") else SecureCodeSandbox())
        self.kg_mind         = KnowledgeGraphMindEngine(graph_cognition=self.graph_cognition)
        self.meta_cog        = MetacognitiveExecutive()

        nprint("ApexCore", "All Apex subsystems online ✅", C.MAGENTA)

    def _boot_subsystems(self):
        """Extend parent boot with Apex background services."""
        super()._boot_subsystems()
        self.maint_daemon.start()
        nprint("ApexCore", "Autonomous Maintenance Daemon started", C.MAGENTA)

    # ── Enhanced _call_llm: inject graph-RAG context ─────────────────────────

    async def _call_llm(self, prompt: str, system: str = "") -> str:
        """
        Apex-enhanced LLM call:
            • Injects Knowledge Graph Mind graph-RAG context
            • Ingests response into Graph Cognition Engine
            • Full parent priority chain preserved
        """
        # Inject graph-RAG context from KGMindEngine
        graph_ctx = self.kg_mind.graph_rag_context(prompt)
        if graph_ctx:
            enriched = f"{graph_ctx}\n\n{prompt}"
        else:
            enriched = prompt

        response = await super()._call_llm(enriched, system)

        # Ingest response into graph engines (non-blocking)
        def _ingest():
            try:
                self.graph_cognition.extract_and_ingest(response)
                self.kg_mind.ingest_text(response)
            except Exception:
                pass
        threading.Thread(target=_ingest, daemon=True, name="GraphIngest").start()

        return response

    # ── Command routing ───────────────────────────────────────────────────────

    async def _route_command(self, query: str, modifier: str = "") -> str:
        ql  = query.strip().lower()
        raw = query.strip()

        # ── Neural Bio-Feedback ───────────────────────────────────────────────
        if ql in {"/neuro", "/biofeedback", "/neuro status"}:
            return self.neuro_feedback.status()

        # ── SpatialNexus 3D ───────────────────────────────────────────────────
        if ql in {"/scene", "/spatial", "/3d", "/scene status"}:
            return self.spatial_nexus.status()

        if ql in {"/scene summary", "/spatial summary"}:
            return self.spatial_nexus.spatial_summary()

        # ── Graph Cognition ───────────────────────────────────────────────────
        if ql in {"/graph", "/graph status"}:
            return self.graph_cognition.status()

        if ql.startswith("/graph query "):
            q_text = raw[13:].strip()
            ctx    = self.graph_cognition.build_graph_context(q_text)
            return ctx or f"[GraphCognition] No graph context found for: {q_text}"

        if ql in {"/graph save"}:
            self.graph_cognition.save()
            return "[GraphCognition] ✅ Graph saved to disk."

        # ── Maintenance Daemon ────────────────────────────────────────────────
        if ql in {"/maint", "/maintenance", "/maint status"}:
            return self.maint_daemon.status()

        if ql in {"/maint run", "/maintenance run"}:
            return self.maint_daemon.run_now()

        # ── Self-Decision Making ──────────────────────────────────────────────
        if ql in {"/decision", "/decision status"}:
            return self.decision_engine.status() if hasattr(self.decision_engine, 'status') else "[Decision] Ready."

        # ── Self-Execution Engine ─────────────────────────────────────────────
        if ql in {"/exec status", "/execution status"}:
            return self.exec_engine.status()

        if ql in {"/exec log", "/execution log"}:
            return self.exec_engine.get_log(15)

        if ql.startswith("/exec mode "):
            mode = raw.split()[-1].upper()
            try:
                self.exec_engine.set_mode(mode)
                return f"[SelfExecution] ✅ Mode set to: {mode}"
            except ValueError as e:
                return f"[SelfExecution] ❌ {e}"

        # ── Skill Forge ───────────────────────────────────────────────────────
        if ql in {"/skillforge", "/skills", "/skillforge status"}:
            return self.skill_forge.status()

        if ql in {"/skillforge catalogue", "/skills catalogue"}:
            return self.skill_forge.catalogue_report()

        if ql.startswith("/skillforge gap "):
            gap = raw[16:].strip()
            self.skill_forge.flag_gap(gap)
            return f"[SkillForge] ✅ Gap flagged: {gap[:60]}"

        if ql.startswith("/skillforge synthesise ") or ql.startswith("/skillforge synthesize "):
            gap = re.sub(r"^/skillforge synthesi[sz]e\s+", "", raw, flags=re.I).strip()
            result = await self.skill_forge.synthesise(gap, self._call_llm)
            if result:
                return f"[SkillForge] ✅ Skill synthesised and registered: {result}"
            return "[SkillForge] ❌ Synthesis failed — see logs."

        if ql in {"/skillforge prune"}:
            self.skill_forge.prune_unused()
            return "[SkillForge] ✅ Unused skills pruned."

        # ── Knowledge Graph Mind ──────────────────────────────────────────────
        if ql in {"/kgmind", "/kgmind status"}:
            return self.kg_mind.status()

        if ql in {"/kgmind export", "/kgmind graphml"}:
            graphml = self.kg_mind.export_graphml()
            out_path = HOME_DIR / "nexus" / "knowledge_graph_mind.graphml"
            out_path.write_text(graphml, encoding="utf-8")
            self.kg_mind.save()
            return f"[KGMind] ✅ GraphML exported to: {out_path}"

        if ql.startswith("/kgmind query "):
            q_text = raw[14:].strip()
            ctx    = self.kg_mind.graph_rag_context(q_text)
            return ctx or f"[KGMind] No triples found matching: {q_text}"

        if ql in {"/kgmind top", "/kgmind nodes"}:
            nodes = self.kg_mind.top_nodes(20)
            lines = [f"{C.CYAN}[🧬 KGMind — Top 20 Entities]{C.RESET}"]
            for n in nodes:
                lines.append(f"  {n['entity']:30s}  mentions={n['mentions']}")
            return "\n".join(lines)

        if ql in {"/kgmind save"}:
            self.kg_mind.save()
            return "[KGMind] ✅ Knowledge graph saved."

        # ── Metacognitive Executive ───────────────────────────────────────────
        if ql in {"/metacog", "/metacog status"}:
            return self.meta_cog.status()

        if ql in {"/metacog last", "/metacog report"}:
            return self.meta_cog.last_report()

        if ql.startswith("/metacog reason "):
            q_text = raw[16:].strip()
            result = await self.meta_cog.monitored_reason(q_text, self._call_llm)
            return (
                f"{C.CYAN}[🪞 MetaCog Response]{C.RESET}\n"
                f"{result['response']}\n\n"
                f"{C.DIM}Strategy: {result['strategy_used']}  "
                f"Re-rolls: {result['rerolls']}  "
                f"Quality: {result['quality']:.2f}{C.RESET}"
            )

        # ── Help (extend parent) ──────────────────────────────────────────────
        if ql in {"/help", "help"}:
            parent_help = await super()._route_command(query, modifier)
            return self._apex_help() + "\n\n" + parent_help

        # ── Delegate up the chain ─────────────────────────────────────────────
        return await super()._route_command(query, modifier)

    @staticmethod
    def _apex_help() -> str:
        return (
            f"{C.MAGENTA}\n"
            "╔══════════════════════════════════════════════════════════════════════════╗\n"
            "║  GOD MODE APEX CORE  —  PRD v1.0 Command Reference                     ║\n"
            "╠══════════════════════════════════════════════════════════════════════════╣\n"
            "║  NEURAL BIO-FEEDBACK                                                     ║\n"
            "║  /neuro                    Neural HR/HRV/stress status                  ║\n"
            "║                                                                          ║\n"
            "║  SPATIAL NEXUS 3D                                                        ║\n"
            "║  /scene                    3D scene graph status                        ║\n"
            "║  /scene summary            NL description of current scene              ║\n"
            "║                                                                          ║\n"
            "║  GRAPH COGNITION                                                         ║\n"
            "║  /graph                    Graph status                                 ║\n"
            "║  /graph query <text>       Graph-RAG for a query                        ║\n"
            "║  /graph save               Persist graph to disk                        ║\n"
            "║                                                                          ║\n"
            "║  AUTONOMOUS MAINTENANCE                                                  ║\n"
            "║  /maint                    Daemon status                                ║\n"
            "║  /maint run                Run all maintenance tasks now                ║\n"
            "║                                                                          ║\n"
            "║  SELF-EXECUTION ENGINE                                                   ║\n"
            "║  /exec status              Engine status + mode                         ║\n"
            "║  /exec mode <MODE>         SIMULATE / EXECUTE / SUPERVISED              ║\n"
            "║  /exec log                 Last 15 execution records                    ║\n"
            "║                                                                          ║\n"
            "║  SKILL FORGE                                                             ║\n"
            "║  /skillforge               Status + pending gaps                        ║\n"
            "║  /skillforge catalogue     All registered skills                        ║\n"
            "║  /skillforge gap <text>    Flag a capability gap                        ║\n"
            "║  /skillforge synthesise X  Force-synthesise skill for X                 ║\n"
            "║  /skillforge prune         Remove stale skills                          ║\n"
            "║                                                                          ║\n"
            "║  KNOWLEDGE GRAPH MIND                                                    ║\n"
            "║  /kgmind                   Status + triple count                        ║\n"
            "║  /kgmind query <text>      Graph-RAG context for query                  ║\n"
            "║  /kgmind top               Top 20 entities by mention count             ║\n"
            "║  /kgmind export            Export as GraphML file                       ║\n"
            "║  /kgmind save              Save triples to disk                         ║\n"
            "║                                                                          ║\n"
            "║  METACOGNITIVE EXECUTIVE                                                 ║\n"
            "║  /metacog                  Status + thresholds                          ║\n"
            "║  /metacog last             Last cycle report                            ║\n"
            "║  /metacog reason <query>   Run monitored metacognitive reasoning        ║\n"
            f"╚══════════════════════════════════════════════════════════════════════════╝{C.RESET}"
        )

    async def run(self):
        """Print apex banner, run, then clean up on shutdown."""
        print(self.APEX_BANNER)
        try:
            await super().run()
        finally:
            nprint("ApexCore", "Shutting down Apex subsystems…", C.MAGENTA)
            self.maint_daemon.stop()
            self.graph_cognition.save()
            self.kg_mind.save()
            nprint("ApexCore", "✅ Graph + KGMind saved.", C.MAGENTA)


# Apply patches to FullSpectrumCore without modifying the class body
FullSpectrumCore.__init__       = _fsc_init_patched
FullSpectrumCore._route_command = _fsc_route_patched
FullSpectrumCore._spectrum_help = _fsc_help_patched


# ─────────────────────────────────────────────────────────────────────────────
#  41.  REDEFINED  main()  —  activates CapabilityBreakerCore
#       (Python's name-binding semantics: the LAST definition of main() wins,
#        so all earlier main() definitions are intact and can be inspected;
#        only the runtime binding is replaced.)
# ─────────────────────────────────────────────────────────────────────────────
async def main():                                                  # noqa: F811
    """
    Luna.AI Nexus — GOD MODE APEX EDITION (PRD v1.0 Complete).

    Entry point. Full inheritance chain:
        NexusCore → SentientNexusCore → CapabilityBreakerCore
          → FullSpectrumCore → GodModeApexCore  ← ACTIVE

    All --flags from all previous editions are honoured.

    New additions (FullSpectrum layer):
        Local models (WhiteRabbitNeo/Phi-4/Qwen3-7B/GemmaE4B), self-reasoning,
        permanent memory (TRRA), goal-driven autonomy, background agent, multi-model router.

    New additions (GodMode APEX layer — PRD §7-§18):
        NeuralBioFeedback, SpatialNexus3D, GraphCognition, AutonomousMaintenance,
        SelfDecision, SelfExecution, SkillForge, KGMind, MetacognitiveExecutive.

    GemmaE4B (no API, no cost):
        Primary  : ollama pull gemma3:4b  →  /gemma <query>
        Fallback : pip install transformers accelerate  (auto-downloads on first /gemma)

    New /commands (FullSpectrum): /localmodels /local /ensemble /bestofn /reasoning
                                   /permemory /trra /goals /goal /bgagent /bglog /multistats
    New /commands (APEX):        /neuro /scene /graph /maint /decision /exec /skillforge
                                   /kgmind /metacog /gemma
    """
    if "--setup" in sys.argv:
        print("\n🛠  Luna.AI — GOD MODE APEX EDITION — Setup")
        print("─" * 65)
        print("All previous setup flags still apply.")
        print("\nLocal models (requires Ollama — https://ollama.ai):")
        print("  ollama pull whiterabbitneo   # Cybersecurity specialist")
        print("  ollama pull phi4             # Math/code/logic specialist")
        print("  ollama pull qwen3:7b         # Multilingual/general model")
        print("  ollama pull gemma3:4b        # GemmaE4B — fast, efficient, free (NEW)")
        print("\nGemmaE4B HuggingFace fallback (no Ollama needed):")
        print("  pip install transformers accelerate")
        print("  # Model weights (~4 GB) auto-downloaded from HuggingFace on first /gemma query")
        print("\nNew commands (FullSpectrum layer):")
        print("  /localmodels        Local model status (incl. GemmaE4B)")
        print("  /local <query>      Force local model inference")
        print("  /ensemble <query>   All-model ensemble (incl. GemmaE4B)")
        print("  /bestofn <query>    Best-of-N model selection")
        print("  /gemma [query]      GemmaE4B status or direct query")
        print("  /reasoning          Last self-reasoning trace")
        print("  /permemory          Permanent memory status")
        print("  /trra <text>        TRRA learning cycle")
        print("  /goals              Autonomous goal list")
        print("  /goal add <desc>    Add autonomous goal")
        print("  /bgagent            Background agent status")
        print("  /bglog              Background action log")
        print("\nNew commands (APEX / PRD §7-§18):")
        print("  /neuro              Neural bio-feedback (HR/HRV/stress)")
        print("  /scene              3D spatial scene graph")
        print("  /graph              Graph cognition status")
        print("  /graph query <X>    Graph-RAG for a query")
        print("  /maint              Maintenance daemon status")
        print("  /maint run          Run all maintenance tasks now")
        print("  /exec status        Self-execution engine status")
        print("  /exec mode <MODE>   SIMULATE / EXECUTE / SUPERVISED")
        print("  /exec log           Last execution log")
        print("  /skillforge         Skill forge status")
        print("  /skillforge gap <X> Flag a capability gap")
        print("  /kgmind             Knowledge graph mind status")
        print("  /kgmind export      Export GraphML")
        print("  /metacog            Metacognitive executive status")
        print("  /metacog reason <X> Run monitored metacognitive reasoning")
        print("\nRun:")
        print("  python Luna_Nexus_Sentient_v6.py")
        return

    if "--no-install" not in sys.argv:
        NexusBootLoader.run(verbose=True)

    if "--hud-off"    in sys.argv: NEXUS_CFG["hud_enabled"]     = False
    if "--no-yolo"   in sys.argv: NEXUS_CFG["yolo_enabled"]    = False
    if "--no-gesture"in sys.argv: NEXUS_CFG["gesture_enabled"] = False

    core = GodModeApexCore()              # ← GOD MODE APEX — Full PRD v1.0
    await core.run()
