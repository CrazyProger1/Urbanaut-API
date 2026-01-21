import logging
import os

logger = logging.getLogger(__name__)


def switch_maintenance(maintenance: bool):
    try:
        if maintenance:
            open("/var/www/maintenance_on.flag", "w")
            logger.info("Maintenance mode enabled")
        else:
            os.remove("/var/www/maintenance_on.flag")
            logger.info("Maintenance mode disabled")
    except FileNotFoundError:
        logger.warning("Maintenance flag not found")
    except Exception as e:
        logger.error(f"An error occurred while switching maintenance: {e}", exc_info=e)
