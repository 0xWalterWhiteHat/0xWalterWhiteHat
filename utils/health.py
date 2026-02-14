"""Health check utility for service monitoring."""

import json
import time
from typing import Any, Dict


# Service start time (can be set when service starts)
_service_start_time: float = time.time()

# Service version (can be set from config or version file)
SERVICE_VERSION: str = "1.0.0"


def check_service() -> Dict[str, Any]:
    """
    Check if the service is running and return a JSON status object.
    
    Returns:
        Dict containing:
            - uptime: Service uptime in seconds (number)
            - version: Service version (string)
            - timestamp: Current Unix timestamp (number)
    """
    current_time = time.time()
    uptime = current_time - _service_start_time
    
    return {
        "uptime": uptime,
        "version": SERVICE_VERSION,
        "timestamp": current_time
    }


def get_health_json() -> str:
    """
    Get the health check result as a JSON string.
    
    Returns:
        JSON string of the health status
    """
    return json.dumps(check_service())


if __name__ == "__main__":
    # CLI usage
    print(get_health_json())
