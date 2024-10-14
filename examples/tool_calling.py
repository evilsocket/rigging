import asyncio
from typing import Annotated

import requests

import rigging as rg


class WeatherTool(rg.Tool):
    name = "weather"
    description = "A tool to get the weather for a location"

    def get_for_city(self, city: Annotated[str, "The city name to get weather for"]) -> str:
        try:
            city = city.replace(" ", "+")
            return requests.get(f"http://wttr.in/{city}?format=2").text
        except:
            return "Failed to call the API"


async def main() -> None:
    chat = (
        await rg.get_generator("ollama/llama3.1,api_base=http://planetexpress:11434")
        .chat("What is the weather in London?")
        .using(WeatherTool(), force=True)
        .run()
    )

    print(chat.last.content)


if __name__ == "__main__":
    asyncio.run(main())
