"""
utils.py - SKT OMNI-ARC V49 Utilities
Common helper functions for formatting, timing, and logging.
"""

import time
from datetime import datetime

def format_usdc(amount: float) -> str:
    """Format amount as USDC with 4 decimals"""
    return f"{amount:.4f} USDC"

def get_elapsed_time(start_time: float) -> str:
    """Calculate and format elapsed time"""
    elapsed = round((time.time() - start_time) * 1000)
    return f"{elapsed}ms"

def log_step(step_name: str, details: str = ""):
    """Beautiful console logging"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] 🔹 {step_name} {details}")

def generate_tx_reference():
    """Unique transaction reference"""
    import uuid
    return f"TX-{uuid.uuid4().hex[:12].upper()}"

# Future: Add rate limiting, input validation helpers here
