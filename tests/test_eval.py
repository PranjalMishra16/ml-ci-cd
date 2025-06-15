import subprocess


def test_model_eval():
    result = subprocess.run(["python","evaluate.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"Evaluation Script failed!\n{result.stderr}"

    