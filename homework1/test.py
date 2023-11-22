import openai
response = openai.Completion.create(
    model="curie:ft-personal-2023-11-20-04-24-24",
    prompt="When do I need to start my air conditioner?"
    # additional parameters
    # temperature,
    # frequency_penalty,
    # presence_penalty
    # ..etc
)

print(response.choices[0].text)