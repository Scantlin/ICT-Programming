from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.llms import OpenAI

# Define examples
examples = [
    {
        "input": "2+2",
        "output": "4"
    },
    {
        "input": "5*3",
        "output": "15"
    },
    {
        "input": "10/2",
        "output": "5"
    }
]

# Create example template
example_template = """
Input: {input}
Output: {output}
"""

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template=example_template
)

# Create few-shot prompt template
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="You are a math tutor. Solve the following problems:",
    suffix="Input: {input}\nOutput:",
    input_variables=["input"],
    example_separator="\n\n"
)

# Test it
formatted_prompt = few_shot_prompt.format(input="8-3")
print("Few-shot Prompt:")
print(formatted_prompt)

llm = OpenAI(temperature=0)
response = llm(formatted_prompt)
print("Response:", response)