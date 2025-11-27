from pydantic_ai import Agent, BinaryContent
from src.contract.model import Contract, contract_prompt
from pathlib import Path
import logging

def parse_contract(file_content: bytes, file_content_type: str) -> Contract:
    """
    Receives a file in bytes and returns a Contract object.
    """
    agent = Agent(
        'google-gla:gemini-2.5-flash',
        output_type=[Contract, str], 
        system_prompt=contract_prompt
    )

    # Create the BinaryContent object
    binary_input = BinaryContent(
        data=file_content,
        media_type=file_content_type # Specify the correct MIME type
    )

    # Run the agent with both the text prompt and the file object
    try:
        result = agent.run_sync([
            binary_input
        ])
    except Exception as e:
        logging.error("could not parse contract: " + str(e))
   
    return result.output