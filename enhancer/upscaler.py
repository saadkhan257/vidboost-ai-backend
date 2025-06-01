import os
import subprocess
import shutil

REAL_ESRGAN_DIR = os.path.abspath("third_party/Real-ESRGAN")
MODEL_NAME = "RealESRGAN_x4plus"
INFERENCE_SCRIPT = os.path.join(REAL_ESRGAN_DIR, "inference_realesrgan.py")

def enhance_image(input_path, output_dir="outputs"):
    try:
        input_path = os.path.abspath(input_path).replace("\\", "/")
        output_dir = os.path.abspath(output_dir).replace("\\", "/")
        os.makedirs(output_dir, exist_ok=True)

        name = os.path.splitext(os.path.basename(input_path))[0]
        expected_output = os.path.join(output_dir, f"{name}_out.png")

        command = [
            "python", INFERENCE_SCRIPT,
            "-n", MODEL_NAME,
            "-i", input_path,
            "-o", output_dir,
            "--fp32"
        ]
        subprocess.run(command, check=True)

        if os.path.exists(expected_output):
            branded_output = os.path.join(output_dir, f"{name}_vidboost-ai.png")
            shutil.move(expected_output, branded_output)
            print(f"✅ Enhanced image saved as: {branded_output}")
            return branded_output
        else:
            print(f"❌ Expected output not found: {expected_output}")
            return None

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Enhancement failed:\n{e}")
        return None

    except Exception as ex:
        print(f"[FATAL] Unexpected error: {ex}")
        return None
