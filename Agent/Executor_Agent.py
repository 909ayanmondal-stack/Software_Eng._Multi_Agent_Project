import tempfile
import subprocess
import os
import shutil

def executor(code: str, language: str = "python",thread_id: str = "default") -> dict:
    """Runs code in multiple languages and returns output or error"""

    try:
        temp_path = None
        result = None

        # =========================
        # 1. CREATE TEMP FILE
        # =========================
        if language == "python":
            suffix = ".py"
        elif language == "javascript":
            suffix = ".js"
        elif language == "java":
            suffix = ".java"
        elif language == "cpp":
            suffix = ".cpp"
        else:
            return {"status": "error", "output": "Unsupported language"}

        with tempfile.NamedTemporaryFile(mode="w", suffix=suffix, delete=False) as f:
            f.write(code)
            temp_path = f.name

        # =========================
        # 2. PYTHON
        # =========================
        if language == "python":
            result = subprocess.run(
                ["python3", temp_path],
                capture_output=True,
                text=True,
                timeout=10
            )

        # =========================
        # 3. JAVASCRIPT
        # =========================
        elif language == "javascript":
            result = subprocess.run(
                ["node", temp_path],
                capture_output=True,
                text=True,
                timeout=10
            )

        # =========================
        # 4. JAVA
        # =========================
        elif language == "java":
            class_name = "Main"

            # Rename file properly
            folder = tempfile.mkdtemp()
            java_file = os.path.join(folder, f"{class_name}.java")
            shutil.move(temp_path, java_file)

            # Compile
            compile_res = subprocess.run(
                ["javac", java_file],
                capture_output=True,
                text=True,
                timeout=10
            )

            if compile_res.returncode != 0:
                return {"status": "error", "output": compile_res.stderr}

            # Run
            result = subprocess.run(
                ["java", "-cp", folder, class_name],
                capture_output=True,
                text=True,
                timeout=10
            )

            # Cleanup compiled file
            shutil.rmtree(folder)

        # =========================
        # 5. C++
        # =========================
        elif language == "cpp":
            exe_path = temp_path.replace(".cpp", "")

            # Compile
            compile_res = subprocess.run(
                ["g++", temp_path, "-o", exe_path],
                capture_output=True,
                text=True,
                timeout=10
            )

            if compile_res.returncode != 0:
                return {"status": "error", "output": compile_res.stderr}

            # Run
            result = subprocess.run(
                [exe_path],
                capture_output=True,
                text=True,
                timeout=10
            )

            # Cleanup executable
            if os.path.exists(exe_path):
                os.unlink(exe_path)

        # =========================
        # 6. DELETE SOURCE FILE
        # =========================
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)

        # =========================
        # 7. RETURN RESULT
        # =========================
        if result.returncode == 0:
            return {"status": "success", "output": result.stdout}
        else:
            return {"status": "error", "output": result.stderr}

    except Exception as e:
        return {"status": "error", "output": str(e)}
    
#just for testing bro
if __name__ == "__main__":
    print(executor("print('Hello World')", "python"))
    