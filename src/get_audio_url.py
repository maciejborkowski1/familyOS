import sys

import storage


def main() -> None:
    path = sys.argv[1]
    expires_in = int(sys.argv[2]) if len(sys.argv) > 2 else 3600
    print(storage.get_signed_audio_url(path, expires_in))


if __name__ == "__main__":
    main()
