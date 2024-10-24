# Clevrr Computer

Clevrr Computer, inpired by  is an automation agent designed to perform precise and efficient system actions on behalf of the user using the PyAutoGUI library. It can automate keyboard, mouse, and screen interactions while ensuring safety and accuracy in every task.

## Features

- Automate mouse movements, clicks, and keyboard inputs.
- Take screenshots and manage windows.
- Handle errors gracefully and provide feedback.
- Execute tasks with maximum precision to avoid unintentional actions.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Clevrr-AI/Clevrr-Computer.git
   cd Clevrr-Computer
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Rename the `.env_dev` file to `.env` and add your API keys and other configurations:

   ```plaintext
   AZURE_OPENAI_API_KEY=<YOUR_AZURE_API_KEY>
   AZURE_OPENAI_ENDPOINT=<YOUR_AZURE_ENDPOINT_URL>
   AZURE_OPENAI_API_VERSION=<YOUR_AZURE_API_VERSION>
   AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=<YOUR_AZURE_DEPLOYMENT_NAME>
   GOOGLE_API_KEY=<YOUR_GEMINI_API_KEY>
   ```

## Usage

1. **Run the Application:**

   You can run the application using the following command:

   ```bash
   python main.py
   ```

   By default, this will use the `gemini` model and enable the floating UI.

2. **Optional Arguments:**

    - **Choose a Model:**
    You can specify which model to use by passing the `--model` argument. Only acceptable args are `gemini` or `openai`.

    ```bash
    python main.py --model openai
    ```

    - **Floating UI:**
    The TKinter UI will be floating and remain on top of the screen by default. You can disable this behavior by passing the `--float-ui` flag as `0`. By default it will be `1`.

    ```bash
    python main.py --float-ui 0
    ```


## Examples

### Move Mouse to Specific Coordinates and Click

```python
pyautogui.moveTo(500, 300)
pyautogui.click()
```

### Take a Screenshot

```python
screenshot = pyautogui.screenshot()
screenshot.save("screen.png")
```

### Type a Message in Notepad

```python
pyautogui.press('win')
pyautogui.write('Notepad')
pyautogui.press('enter')
pyautogui.write('Hello, World!')
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact [your-email@example.com](mailto:your-email@example.com).

