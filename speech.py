import subprocess

def main_function():
    my_text_input = str(input("\n\nWrite your own text\n\n"))
    if(my_text_input.lower() != "" and my_text_input.lower() != "exit" and my_text_input.lower() != "end"):
        print("\n\nYour text input was: \n\n{}".format(my_text_input))
        model = "en_US-amy-medium.onnx"
        command = "cd ./venv/piper && echo '{}' | \
  ./piper --model {} --output-raw | \
  aplay -r 22050 -f S16_LE -t raw -".format(my_text_input,model)
        result = subprocess.run(command, shell=True, check=True, text=True)
        main_function()
    else:
        quit()

main_function()