import subprocess, sys


def run(cmd):
    print(">", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main():
    run([sys.executable, "/app/app/load_input.py"])
    run([sys.executable, "/app/app/preprocess.py"])
    run([sys.executable, "/app/app/predict.py"])
    run([sys.executable, "/app/app/save_output.py"])


if __name__ == "__main__":
    main()
