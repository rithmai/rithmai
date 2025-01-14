import openai
import time

class RithmAI:
    def __init__(self, openai_api_key, name="Rithm AI"):
        self.api_key = openai_api_key
        self.name = name
        openai.api_key = self.api_key

    def generate_response(self, prompt, model="gpt-4"):
        """
        Generates a response using the OpenAI GPT model.
        """
        try:
            print(f"{self.name} is thinking...")
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"You are {self.name}, an advanced AI assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=300,
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"

    def run_chat(self):
        """
        Continuously runs a chat session with the user.
        """
        print(f"Welcome to {self.name}! Type 'exit' to end the chat.")
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print(f"Goodbye from {self.name}!")
                break
            response = self.generate_response(user_input)
            print(f"{self.name}: {response}")

    def integrate_custom_functionality(self, module_name, **kwargs):
        """
        Integrates custom functionality from user-defined modules.
        """
        try:
            module = __import__(module_name)
            if hasattr(module, 'run'):
                return module.run(**kwargs)
            else:
                return f"Module {module_name} does not have a 'run' method."
        except ImportError:
            return f"Module {module_name} not found."

    def custom_logic(self, task_type, **kwargs):
        """
        Handles specific tasks or logic for Rithm AI.
        """
        if task_type == "summarize":
            text = kwargs.get("text", "")
            return self.generate_response(f"Summarize the following text:\n{text}")
        elif task_type == "analyze_sentiment":
            text = kwargs.get("text", "")
            return self.generate_response(f"Analyze the sentiment of the following text:\n{text}")
        else:
            return f"Unknown task type: {task_type}"


# Example usage
if __name__ == "__main__":
    API_KEY = "your-openai-api-key-here"
    rithm = RithmAI(openai_api_key=API_KEY)

    # Main Chat Interface
    rithm.run_chat()

    # Example of custom functionality
    text_to_summarize = "Rithm AI is a powerful AI assistant that can handle multiple tasks."
    print("\nSummarizing text:")
    print(rithm.custom_logic(task_type="summarize", text=text_to_summarize))
