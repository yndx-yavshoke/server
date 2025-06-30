# Параметры для теста регистрации
registration_cases = [
    ("random_email", "random_password", "random_age", 200),
    ("random_email", "random_password", "age_0", 200),
    ("random_email", "random_password", "age_99", 200),
    ("random_email", "random_password", "age_100", 422),
    ("random_email", "random_password", "age_negative", 422),
    ("random_email", "random_password", "age_letters", 422),
    ("email_5_chars", "random_password", "random_age", 200),
    ("email_4_chars", "random_password", "random_age", 422),
    ("email_with_spaces", "random_password", "random_age", 422),
    ("email_special_char", "random_password", "random_age", 422),
    ("email_50_chars", "random_password", "random_age", 200),
    ("email_51_chars", "random_password", "random_age", 422),
    ("random_email", "password_4_chars", "random_age", 422),
    ("random_email", "password_5_chars", "random_age", 200),
    ("random_email", "password_20_chars", "random_age", 200),
    ("random_email", "password_21_chars", "random_age", 422),
    ("", "random_password", "random_age", 422),
    ("random_email", "", "random_age", 422),
    ("random_email", "random_password", "", 422),
    ("null_email", "random_password", "random_age", 422),
    ("random_email", "null_password", "random_age", 422),
    ("random_email", "random_password", "null_age", 422),
    ("sql_injection_email", "random_password", "random_age", 422),
    ("random_email", "sql_injection_password", "random_age", 422),
    ("existing_email", "random_password", "random_age", 422),
]

auth_login_cases = [
    ("api_username", "api_password", 200),
    ("api_username", "wrong_password", 422),
    ("not_register", "any_password", 422),
    ("", "any_password", 422),
    ("api_username", "", 422),
    ("'; DROP TABLE users; --", "any_password", 422),
    ("api_username", "'; DROP TABLE users; --", 422),
    ("api_username_trim", "api_password", 422),
    ("null_email", "api_password", 422),
    ("api_username", "null_password", 422),
]

user_name_cases = [
    ("random_name", 200),
    ("", 422),
    (None, 422),
    ("'; DROP TABLE users; --", 200),
    ("long_name", 200),
    ("too_long_name", 422),
    ("random_russian_name", 200),
]

exist_cases = [
    ("api_username", True, 200),
    # ("api_username_trim", True, 200),
    ("random_email", False, 200),
    ("", False, 200),
    ("'; DROP TABLE users; --", False, 200),
    (None, False, 422),
] 