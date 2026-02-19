from src.apps.abandoned.enums import PreservationLevel

PRESERVATION_LEVEL_LOOKUP = {
    (0, 2): PreservationLevel.NONE,
    (3, 5): PreservationLevel.LOW,
    (6, 8): PreservationLevel.MEDIUM,
    (9, 10): PreservationLevel.HIGH,
    (11, 11): PreservationLevel.AWESOME,
}

PRESERVATION_LEVEL_WEIGHTS_LOOKUP = {
    "has_roof": 3,
    "has_floor": 2,
    "has_walls": 2,
    "has_doors": 1,
    "has_windows": 1,
    "has_internal_ceilings": 2,
}
