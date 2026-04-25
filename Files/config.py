"""
config.py - SKT OMNI-ARC V49 Configuration
Central place for all settings, API keys, and environment variables.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Config:
    # API Keys
    GEMINI_KEY = os.getenv("GEMINI_KEY")
    ASSEMBLY_KEY = os.getenv("ASSEMBLY_KEY")
    CIRCLE_API_KEY = os.getenv("CIRCLE_API_KEY")
    CIRCLE_ENTITY_SECRET = os.getenv("CIRCLE_ENTITY_SECRET")
    AIML_API_KEY = os.getenv("AIML_API_KEY")
    FEATHERLESS_KEY = os.getenv("FEATHERLESS_KEY")
    
    # Arc Network Settings
    ARC_TESTNET_RPC = "https://rpc.testnet.arc.network"
    ARC_EXPLORER = "https://testnet.arcscan.app"
    ARC_CHAIN_ID = 5042002
    
    # Application Settings
    APP_NAME = "SKT OMNI-ARC V49"
    DEBUG_MODE = os.getenv("DEBUG_MODE", "True").lower() == "true"
    MAX_IMAGE_SIZE_MB = 10
    CONSENSUS_THRESHOLD = 0.85  # For future multi-model consensus
    
    # Pricing (USDC per inference)
    USDC_PRICING = {
        "gemini-3.1-flash-lite": 0.0001,
        "gemini-2.5-flash": 0.0003,
        "moondream2": 0.0000,   # Local = Free
        "default": 0.00025
    }
    
    @classmethod
    def is_production_ready(cls):
        return bool(cls.CIRCLE_ENTITY_SECRET and cls.CIRCLE_API_KEY)
    
    @classmethod
    def print_status(cls):
        print("📋 Configuration Status:")
        print(f"   Arc Testnet : {cls.ARC_EXPLORER}")
        print(f"   Circle Ready: {'✅' if cls.is_production_ready() else '⚠️ Demo Mode'}")
        print(f"   Debug Mode  : {cls.DEBUG_MODE}")

config = Config()
config.print_status()
