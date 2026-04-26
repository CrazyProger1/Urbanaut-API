from decouple import config

INITIAL_SIGNATURE = config(
    "INITIAL_SIGNATURE", cast=str, default="INSECURE_DEBUG_SIGNATURE"
)

REWARDS = {
    "NEW_USER": 10,
    "PLACE_CREATION": 10,
}
