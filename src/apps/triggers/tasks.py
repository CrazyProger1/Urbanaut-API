import logging

from src.config.celery import celery

logger = logging.getLogger(__name__)


@celery.task
def trigger():
    logger.critical("TRIGGERED")
    raise RuntimeError("Test error")
