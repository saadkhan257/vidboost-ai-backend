import os
import subprocess
import shutil


# === CONFIGURATION ===
REAL_ESRGAN_DIR = os.path.abspath("third_party/Real-ESRGAN")
MODEL_NAME = "RealESRGAN_x4plus"
INFERENCE_SCRIPT = os.path.join(REAL_ESRGAN_DIR, "inference_realesrgan.py")


def enhance_image(input_path, output_dir="outputs"):
    print("🔥 [ENHANCE STARTED]")
    
    try:
        # Normalize paths (Windows/Linux safe)
        input_path = os.path.abspath(input_path).replace("\\", "/")
        output_dir = os.path.abspath(output_dir).replace("\\", "/")
        os.makedirs(output_dir, exist_ok=True)

        print(f"📂 Input: {input_path}")
        print(f"📁 Output Dir: {output_dir}")

        # Snapshot files before
        before_files = set(f for f in os.listdir(output_dir) if f.endswith(".png"))
        print(f"📦 Files before: {before_files}")

        # Build the subprocess command
        command = [
            "python", INFERENCE_SCRIPT,
            "-n", MODEL_NAME,
            "-i", input_path,
            "-o", output_dir,
            "--fp32"
        ]
        print(f"🚀 Command: {' '.join(command)}")

        # Run enhancement
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print(f"✅ Subprocess Output:\n{result.stdout}")
        if result.stderr:
            print(f"⚠️ Subprocess Warnings:\n{result.stderr}")

        # Snapshot files after
        after_files = set(f for f in os.listdir(output_dir) if f.endswith(".png"))
        new_files = after_files - before_files
        print(f"📦 Files after: {after_files}")
        print(f"🆕 New Files: {new_files}")

        if not new_files:
            print("❌ No output file was created.")
            return None

        # Rename output to a branded filename
        generated_file = new_files.pop()
        original_name = os.path.splitext(os.path.basename(input_path))[0]
        branded_filename = f"{original_name}_vidboost-ai.png"
        final_path = os.path.join(output_dir, branded_filename)

        shutil.move(os.path.join(output_dir, generated_file), final_path)
        print(f"✅ Enhanced image saved as: {final_path}")
        return final_path

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Enhancement failed:\n{e.stderr}")
        return None

    except Exception as ex:
        print(f"[FATAL] Unexpected Error: {ex}")
        return None
