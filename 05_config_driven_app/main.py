from config_loader import load_config
import features

def main():
    config = load_config()

    app_name = config["app"]["name"]
    version = config["app"]["version"]
    feature_flags = config["features"]

    if feature_flags.get("show_welcome"):
        features.show_welcome(app_name)

    if feature_flags.get("enable_discount"):
        features.apply_discount()

    if feature_flags.get("debug_mode"):
        features.show_debug(version)

if __name__ == "__main__":
    main()
