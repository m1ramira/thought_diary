from datetime import datetime

test_add_entry_data = [
    # positive test
    (
        {
            "date": str(datetime.now()),
            "situation": "test_1",
            "thoughts_at_moment": "thoughts_at_moment_1",
            "helped_thoughts": "helped_thoughts_1",
            "reaction": "reaction_1",
            "emotions": [
                {
                    "emotion": "IRRITATION",
                    "rate_at_moment": 8,
                    "rate_after": 5,
                },
                {
                    "emotion": "SORROW",
                    "rate_at_moment": 4,
                    "rate_after": 2,
                },
            ],
        },
        201,
    ),
    # negative test -> incorrect emotion name
    (
        {
            "date": str(datetime.now()),
            "situation": "test_2",
            "thoughts_at_moment": "thoughts_at_moment_2",
            "helped_thoughts": "helped_thoughts_2",
            "reaction": "reaction_2",
            "emotions": [
                {
                    "emotion": "HAPPINESS",
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
            "situation": "test_3",
            "thoughts_at_moment": "thoughts_at_moment_3",
            "helped_thoughts": "helped_thoughts_3",
            "reaction": "reaction_3",
            "emotions": [
                {
                    "emotion": "IRRITATION",
                    "rate_at_moment": 11,
                    "rate_after": 0,
                }
            ],
        },
        409,
    ),
]

test_update_entry_data = [
    # positive test
    (
        4,
        {
            "id": 4,
            "user_id": 3,
            "date": str(datetime.now()),
            "situation": "test_1",
            "thoughts_at_moment": "thoughts_at_moment_1",
            "helped_thoughts": "helped_thoughts_1",
            "reaction": "new_reaction_1",
            "emotions": [
                {
                    "id": 6,
                    "entry_id": 4,
                    "emotion": "irritation",
                    "rate_at_moment": 8,
                    "rate_after": 5,
                },
                {
                    "id": 7,
                    "entry_id": 4,
                    "emotion": "sorrow",
                    "rate_at_moment": 4,
                    "rate_after": 2,
                },
            ],
        },
        202,
    )
]
