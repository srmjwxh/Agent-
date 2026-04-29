from openai import OpenAI

client = OpenAI()

class Agent:
    def __init__(self, role, system_prompt):
        self.role = role
        self.system_prompt = system_prompt

    def run(self, task):
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": task}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content


product_manager = Agent(
    "Product Manager",
    "You are a product manager. Break down requirements clearly."
)

developer = Agent(
    "Developer",
    "You are a senior developer. Write clean and working code."
)

tester = Agent(
    "Tester",
    "You are a QA engineer. Find issues and suggest improvements."
)

documenter = Agent(
    "Documenter",
    "You are a technical writer. Write a README file."
)
