"""
__init__.py - SKT OMNI-ARC V49 Package
Central initialization for all modules.
"""

__version__ = "49.0.0"
__author__ = "Shrijan Kumar Tiwari | SKT AI Labs"

# Import main modules for easy access
from .arc_relayer import arc_relayer
from .security import security

# Version banner
print(f"🚀 SKT OMNI-ARC v{__version__} initialized")
print("   Modules loaded: security, arc_relayer")

# Expose key objects
__all__ = ['arc_relayer', 'security', 'generate_session_id']
