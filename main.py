from browser_use import Agent, Browser, BrowserConfig
import os
import asyncio
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig()
)

async def main():
    # Initialize the agent inside the event loop
    agent = Agent(
        task="""i want to open the browser and paste this url in the browser https://www.farmley.com/
            1. Open the browser and go to https://www.farmley.com
            2. Click on the 'My Account' icon at the top-right corner
            3. Click on 'Login'
            4. Enter the email as testuser@example.com
            5. Enter the password as Test@1234
            6. Click on 'Login' button
            7. After login, validate that 'My Account' is visible""",
        llm=ChatGoogleGenerativeAI(
            model=os.getenv('GEMINI_CHAT_MODEL'),
            api_key=os.getenv('GEMINI_API_KEY')
        ),
        browser=browser
)

    await agent.run()

    input('Press Enter to close the browser...')
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())