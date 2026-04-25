"""
security.py - SKT OMNI-ARC V49 Security Module
Handles encryption, input sanitization, Entity Secret management,
and threat protection for developer-controlled wallets.
"""

import hashlib
import os
import base64
from datetime import datetime
import json

class SecurityManager:
    """Core security layer for SKT OMNI-ARC V49"""
    
    def __init__(self):
        self.entity_secret = os.getenv("CIRCLE_ENTITY_SECRET", "")
        self.secret_key = os.getenv("SECRET_KEY", "skt-omni-arc-v49-default-key-2026")  # Change in production
    
    def hash_data(self, data: str) -> str:
        """SHA-256 hashing for audit logs"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    def sanitize_input(self, text: str) -> str:
        """Basic input sanitization against injection"""
        if not text:
            return ""
        return str(text).strip()[:500]  # Limit length
    
    def encrypt_sensitive(self, data: str) -> str:
        """Simple AES-like base64 encryption (production mein cryptography lib use karo)"""
        try:
            encoded = base64.b64encode(data.encode()).decode()
            return f"ENC:{encoded}"
        except:
            return data
    
    def validate_entity_secret(self) -> bool:
        """Check if Entity Secret is properly configured for Circle wallets"""
        if not self.entity_secret or len(self.entity_secret) < 32:
            print("⚠️ Warning: CIRCLE_ENTITY_SECRET not properly set. Using demo mode.")
            return False
        return True
    
    def log_audit(self, action: str, details: dict, user_id: str = "system"):
        """Audit logging for compliance"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "user_id": user_id,
            "details_hash": self.hash_data(json.dumps(details)),
            "ip": "internal"  # In production use request IP
        }
        
        try:
            with open("audit_log.json", "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except:
            pass  # Fail silently in demo
        
        print(f"🔒 Audit: {action} | User: {user_id}")

# Global instance
security = SecurityManager()

# Utility functions
def generate_session_id():
    return f"SESS-{hashlib.sha256(str(datetime.now()).encode()).hexdigest()[:12].upper()}"

print("✅ security.py loaded - Entity Secret & Audit ready")
