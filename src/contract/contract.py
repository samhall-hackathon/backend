from pydantic_ai import Agent, RunContext

roulette_agent = Agent(  
    'gateway/openai:gpt-5',
    deps_type=int,
    output_type=bool,
    system_prompt=(
        'Use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),
)
