from src.apps.abandoned.enums import PreservationLevel, SecurityLevel

PRESERVATION_LEVEL_LOOKUP = {
    (0, 0): PreservationLevel.NONE,
    (1, 5): PreservationLevel.LOW,
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

SECURITY_LEVEL_WEIGHTS_LOOKUP = {
    "has_dogs": 3,
    "has_weapons": 3,
    "has_cameras": 2,
    "has_sensors": 2,
}

SECURITY_LEVEL_LOOKUP = {
    (0, 0): SecurityLevel.NONE,
    (1, 2): SecurityLevel.EASY,
    (3, 4): SecurityLevel.MEDIUM,
    (5, 9): SecurityLevel.HARD,
    (10, 10): SecurityLevel.IMPOSSIBLE,
}
