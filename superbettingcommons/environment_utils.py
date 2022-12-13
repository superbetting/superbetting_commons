def load_env_var(var: str):
    import os
    from dotenv import load_dotenv
    if not os.getenv("PROD") == "True":
        load_dotenv("env_var")
        os.environ['PROD'] = "True"
    value = os.getenv(var)
    if value is None:
        raise Exception(f"Missing {var} in environmental variables")
    return value
