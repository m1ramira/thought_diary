from datetime import datetime

test_add_entry_data = [
    # positive test
    (
        {
            "date": str(datetime.now()),
            "situation": "situation_1",
            "thoughts_at_moment": "thoughts_at_moment_1",
            "helped_thoughts": "helped_thoughts_1",
            "reaction": "reaction_1",
            "emotions": [
                {
                    "emotion_name": "IRRITATION",
                    "rate_at_moment": 8,
                    "rate_after": 5,
                },
                {
                    "emotion_name": "SORROW",
                    "rate_at_moment": 4,
                    "rate_after": 2,
                },
            ],
        },
        200,
    ),
    # negative test -> incorrect emotion name
    (
        {
            "date": str(datetime.now()),
            "situation": "situation_2",
            "thoughts_at_moment": "thoughts_at_moment_2",
            "helped_thoughts": "helped_thoughts_2",
            "reaction": "reaction_2",
            "emotions": [
                {
                    "emotion_name": "HAPPINESS",
                    "rate_at_moment": 10,
                    "rate_after": 9,
                }
            ],
        },
        409,
    ),
    # negative test -> incorrect emotion rate
    (
        {
            "date": str(datetime.now()),
            "situation": "situation_3",
            "thoughts_at_moment": "thoughts_at_moment_3",
            "helped_thoughts": "helped_thoughts_3",
            "reaction": "reaction_3",
            "emotions": [
                {
                    "emotion_name": "IRRITATION",
                    "rate_at_moment": 11,
                    "rate_after": 0,
                }
            ],
        },
        409,
    ),
]
