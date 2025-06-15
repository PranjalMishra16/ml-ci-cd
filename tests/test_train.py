import subprocess


def test_model_train():
    result = subprocess.run(["python", "train.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"Training Script failed!\n{result.stderr}"

